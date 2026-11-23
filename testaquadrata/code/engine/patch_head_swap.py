# patch a time window [t0,t1) of src -> clip (video only). Handles crossfades by patching both layers.
import cv2,numpy as np,subprocess,sys
src,t0,t1,dst=sys.argv[1],float(sys.argv[2]),float(sys.argv[3]),sys.argv[4]
ND='/home/claude/tq/characters/new/'
P=[]
for n in ['van10','vanman']:
    o=cv2.imread(f'/home/claude/tq/reel/img/{n}.jpg');b=cv2.imread(ND+f'{n}_box.jpg')
    d=(np.abs(o.astype(int)-b.astype(int)).sum(2)>30).astype(np.uint8)*255
    a=cv2.GaussianBlur(cv2.dilate(d,np.ones((9,9),np.uint8)),(9,9),0)
    P.append(dict(o=o.astype(np.float32),b=b.astype(np.float32),a=a))
orb=cv2.ORB_create(3000,fastThreshold=12);bf=cv2.BFMatcher(cv2.NORM_HAMMING)
for p in P: p['k'],p['d']=orb.detectAndCompute(cv2.cvtColor(p['o'].astype(np.uint8),cv2.COLOR_BGR2GRAY),None)
cap=cv2.VideoCapture(src);fps=cap.get(cv2.CAP_PROP_FPS);W=int(cap.get(3));H=int(cap.get(4))
f0,f1=int(round(t0*fps)),int(round(t1*fps));cap.set(cv2.CAP_PROP_POS_FRAMES,f0)
frames=[];est={}
for f in range(f0,f1):
    ok,fr=cap.read()
    if not ok:break
    frames.append(fr);g=cv2.cvtColor(fr,cv2.COLOR_BGR2GRAY);k,d=orb.detectAndCompute(g,None)
    if d is None:continue
    for i,p in enumerate(P):
        m=bf.knnMatch(p['d'],d,k=2);good=[x[0] for x in m if len(x)==2 and x[0].distance<0.75*x[1].distance]
        if len(good)<25:continue
        sp=np.float32([p['k'][x.queryIdx].pt for x in good]);dp=np.float32([k[x.trainIdx].pt for x in good])
        M,inl=cv2.estimateAffinePartial2D(sp,dp,method=cv2.RANSAC,ransacReprojThreshold=2.5)
        if M is not None and inl.sum()>=40 and (f-f0 not in est or est[f-f0][2]<inl.sum()): est[f-f0]=(i,M,int(inl.sum()))
n=len(frames);print('frames',n,'matched',len(est),file=sys.stderr)
# per-frame scale -> detect segments of smooth motion; a jump in params = new shot
keys=sorted(est);segs=[]
for j in keys:
    i,M,_=est[j];s=np.hypot(M[0,0],M[0,1])
    if segs and j-segs[-1]['last']<=2 and segs[-1]['i']==i:
        q=segs[-1];pM=est[q['last']][1];ps=np.hypot(pM[0,0],pM[0,1])
        if abs(s/ps-1)<0.03 and np.abs(M[:,2]-pM[:,2]).max()<25*(j-q['last']):
            q['f'].append(j);q['last']=j;continue
    segs.append(dict(i=i,f=[j],last=j))
segs=[s for s in segs if len(s['f'])>=6]
# fit smooth (quadratic) param curves per segment, extendable a few frames for dissolves
for s in segs:
    xs=np.array(s['f']);Ps=np.array([est[x][1].flatten() for x in xs]);deg=2 if len(xs)>8 else 1
    s['fit']=[np.polyfit(xs,Ps[:,c],deg) for c in range(6)];s['a'],s['b']=xs[0],xs[-1]
    print('seg',P[s['i']] is P[0] and 'van10' or 'vanman',round((f0+xs[0])/fps,2),round((f0+xs[-1])/fps,2),file=sys.stderr)
def Mat(s,x):
    near=[y for y in range(x-3,x+4) if y in est and s['a']<=y<=s['b'] and est[y][0]==s['i']]
    if near: return np.mean([est[y][1] for y in near],axis=0)
    return np.array([np.polyval(c,x) for c in s['fit']]).reshape(2,3)
# layer weights: inside seg ->1; in a gap between seg A and B (<=20 frames) -> linear dissolve
lay=[[] for _ in range(n)]
for k,s in enumerate(segs):
    for x in range(s['a'],s['b']+1): lay[x].append((s,1.0))
for A,B in zip(segs,segs[1:]):
    g0,g1=A['b'],B['a']
    if 1<g1-g0<=24:
        for x in range(g0+1,g1):
            w=(x-g0)/(g1-g0);lay[x]+= [(A,1-w),(B,w)]
ff=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','rawvideo','-pix_fmt','bgr24','-s',f'{W}x{H}','-r',str(fps),'-i','-','-c:v','libx264','-preset','veryfast','-crf','14','-pix_fmt','yuv420p',dst],stdin=subprocess.PIPE)
for x,fr in enumerate(frames):
    out=fr.astype(np.float32)
    for s,w in lay[x]:
        p=P[s['i']];M=Mat(s,x)
        wo=cv2.warpAffine(p['o'],M,(W,H),flags=cv2.INTER_AREA)
        wb=cv2.warpAffine(p['b'],M,(W,H),flags=cv2.INTER_AREA)
        wa=cv2.warpAffine(p['a'],M,(W,H)).astype(np.float32)/255
        if wa.max()<=0:continue
        ratio=np.clip(cv2.GaussianBlur(fr.astype(np.float32)+1,(0,0),18)/cv2.GaussianBlur(wo+1,(0,0),18),0,1.6)
        A=(wa*w)[...,None];out=out*(1-A)+np.clip(wb*ratio,0,255)*A
    ff.stdin.write(np.clip(out,0,255).astype(np.uint8).tobytes())
ff.stdin.close();ff.wait();print('done',file=sys.stderr)
