import subprocess,sys
M='../EP2_master.mp4'
B=[0,74.9,164.8,263.9,333.9,427.4,522.2]
PAD=3.2
def run(r,k):
    n=r+4; a,b=B[r],B[r+1]; L=b-a; T=L+PAD; f0=round(L*0.45,2); f1=f0+4.5; e0=L+0.15
    if k=='ig': ax="-9*abs(sin(2*PI*t*1.6))"; ay="11*abs(sin(2*PI*t*1.6))"
    else: ax="5*abs(sin(2*PI*t*1.6))"; ay="14*abs(sin(2*PI*t*1.6))"
    fc=(f"[0:v]trim={a}:{b},setpts=PTS-STARTPTS[cv];[0:a]atrim={a}:{b},asetpts=PTS-STARTPTS,afade=t=in:d=0.15[ca];"
        f"[cv]tpad=stop_mode=clone:stop_duration={PAD},scale=1080:608,pad=1080:1920:0:656:black,setsar=1[bg];"
        f"[bg][1:v]overlay=0:0[v1];[v1][2:v]overlay=0:0:enable='between(t,{f0},{f1})'[v2];"
        f"[v2][3:v]overlay=x='{ax}':y='{ay}':enable='between(t,{f0},{f1})'[v3];[v3][4:v]overlay=0:0:enable='gte(t,{e0})'[v];"
        f"[ca]afade=t=out:st={L-0.35}:d=0.35,apad=pad_dur={PAD}[a]")
    out=f'TESTAQUADRATA_Parte{n}_{"Instagram" if k=="ig" else "TikTok"}.mp4'
    cmd=['ffmpeg','-y','-loglevel','error','-i',M,'-loop','1','-i',f'title_{n}.png','-loop','1','-i',f'follow_{k}_{n}.png','-loop','1','-i',f'arrow_{k}.png','-loop','1','-i','end_yt.png',
         '-filter_complex',fc,'-map','[v]','-map','[a]','-t',f'{T:.3f}','-r','30','-c:v','libx264','-preset','veryfast','-crf','20','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-movflags','+faststart',out]
    subprocess.run(cmd,check=True); print('done',out,round(T,2),flush=True)
for r in range(6):
    for k in ('ig','tt'): run(r,k)
