import subprocess,sys,json,os
src,dst,spec=sys.argv[1],sys.argv[2],json.loads(sys.argv[3])  # spec: [[clip,startframe],...]
N=int(subprocess.check_output(['ffprobe','-v','error','-count_packets','-select_streams','v','-show_entries','stream=nb_read_packets','-of','csv=p=0',src]).decode().strip().split(',')[0])
L=lambda c:int(subprocess.check_output(['ffprobe','-v','error','-count_packets','-select_streams','v','-show_entries','stream=nb_read_packets','-of','csv=p=0',c]).decode().strip().split(',')[0])
os.makedirs('/tmp/sp3',exist_ok=True);parts=[];cur=0
for k,(c,s) in enumerate(spec):
    if s>cur: parts.append(('b',cur,s))
    n=L(c);parts.append(('c',c,n));cur=s+n
if cur<N: parts.append(('b',cur,N))
names=[]
for i,p in enumerate(parts):
    o=f'/tmp/sp3/p{i}.mp4'
    if p[0]=='b': subprocess.run(['ffmpeg','-y','-loglevel','error','-i',src,'-vf',f'trim=start_frame={p[1]}:end_frame={p[2]},setpts=PTS-STARTPTS','-an','-c:v','libx264','-preset','veryfast','-crf','17','-pix_fmt','yuv420p','-r','30',o],check=True)
    else: subprocess.run(['ffmpeg','-y','-loglevel','error','-i',p[1],'-c:v','libx264','-preset','veryfast','-crf','17','-pix_fmt','yuv420p','-r','30',o],check=True)
    names.append(o)
open('/tmp/sp3/l.txt','w').write(''.join(f"file '{n}'\n" for n in names))
subprocess.run(['ffmpeg','-y','-loglevel','error','-f','concat','-safe','0','-i','/tmp/sp3/l.txt','-i',src,'-map','0:v','-map','1:a?','-c','copy','-movflags','+faststart',dst],check=True)
print(N,L(dst),parts)
