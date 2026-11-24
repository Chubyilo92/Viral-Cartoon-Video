import sys, json, numpy as np, subprocess, sherpa_onnx
M='/tmp/asr/sherpa-onnx-whisper-small/'
rec = sherpa_onnx.OfflineRecognizer.from_whisper(encoder=M+'small-encoder.int8.onnx', decoder=M+'small-decoder.int8.onnx', tokens=M+'small-tokens.txt', language='it', task='transcribe', num_threads=4)
src, out = sys.argv[1], sys.argv[2]
pcm = subprocess.run(['ffmpeg','-v','error','-i',src,'-ac','1','-ar','16000','-f','f32le','-'],capture_output=True).stdout
a = np.frombuffer(pcm, np.float32); sr=16000
# pause segmentation
win=int(0.03*sr); e=np.array([np.sqrt(np.mean(a[i:i+win]**2)) for i in range(0,len(a)-win,win)])
thr=max(0.008, np.percentile(e,20)*2.5); speech=e>thr
segs=[]; start=None; sil=0
for i,s in enumerate(speech):
    if s:
        if start is None: start=i
        sil=0
    elif start is not None:
        sil+=1
        if sil*0.03>=0.45:
            segs.append((start,i-sil+1)); start=None; sil=0
if start is not None: segs.append((start,len(speech)))
res=[]
for s,t in segs:
    if (t-s)*0.03<0.25: continue
    b=a[max(0,int((s*0.03-0.15)*sr)):int((t*0.03+0.15)*sr)]
    st=rec.create_stream(); st.accept_waveform(sr,b); rec.decode_stream(st)
    res.append({'start':round(s*0.03,2),'end':round(t*0.03,2),'text':st.result.text.strip()})
json.dump(res,open(out,'w'),ensure_ascii=False,indent=1)
for r in res: print(f"{r['start']:6.2f}-{r['end']:6.2f} {r['text']}")
