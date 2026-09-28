import soundfile as sf, numpy as np, json
from kokoro_onnx import Kokoro
k=Kokoro('kokoro.onnx','voices.bin')
L=[
"When she says... \"I'm fine\"... she's not always fine. She's waiting to see if you'll notice.",
"She might go quiet after a long day. Not to punish you. She's just tired of explaining the same hurt twice.",
"She might bring up something small from last week. It's not about the dishes. It's about feeling heard.",
"She doesn't need you to fix it. She needs you to put the phone down... and ask, what's really wrong.",
"If you're the one who goes quiet... send this to the one who keeps asking.",
"But if you only listen when it's easy... one day, she'll stop telling you.",
"Because the girl who still tells you what's wrong... is the girl who still wants to make it work.",
"Overthinking isn't random. It's usually your attachment style. Find yours in sixty seconds... link in our bio."
]
d=[]
for i,t in enumerate(L):
    a,sr=k.create(t,voice='am_michael',speed=0.9,lang='en-us')
    idx=np.where(np.abs(a)>0.01)[0]; a=a[max(0,idx[0]-400):idx[-1]+2400]
    sf.write(f'v2_line{i}.wav',a,sr); d.append(round(len(a)/sr,2))
json.dump(d,open('v2_dur.json','w')); print(d, sr)
