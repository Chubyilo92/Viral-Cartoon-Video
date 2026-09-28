import soundfile as sf, numpy as np, json
from kokoro_onnx import Kokoro
k=Kokoro('kokoro.onnx','voices.bin')
L=["When a boy loves you... he won't always say it out loud.",
"He'll show it in small ways. He saves you the last bite... even when he's hungry.",
"He might tease you all day. Not to annoy you. It's because your smile is his favourite thing to see.",
"He might act tough... around everyone else.",
"But with you, he's soft. Because you're the one place he doesn't have to be strong.",
"He might go quiet when something's wrong. Not because he's pulling away. He just needs you close... not a hundred questions.",
"He remembers the little things. How you take your tea. The song you hum. The bad day you mentioned once.",
"But if you always have to ask... if he only shows up when it's easy... maybe he's not the one.",
"Because when a boy truly loves you... you'll never have to wonder."]
d=[]
for i,t in enumerate(L):
    a,sr=k.create(t,voice='am_michael',speed=0.9,lang='en-us')
    # trim silence
    idx=np.where(np.abs(a)>0.01)[0]; a=a[max(0,idx[0]-400):idx[-1]+2400]
    sf.write(f'line{i}.wav',a,sr); d.append(round(len(a)/sr,2))
json.dump(d,open('dur.json','w')); print(d, sr)
