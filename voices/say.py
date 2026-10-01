#!/usr/bin/env python3
"""Generate one line in a JJ pup voice.
Usage: python3 voices/say.py boy|girl "Babe... did you get the milk?" out.wav
Needs: pip install kokoro-onnx soundfile numpy; Kokoro model files in /tmp/kk (see pipeline/README.md); ffmpeg with rubberband."""
import json, os, subprocess, sys
import numpy as np, soundfile as sf
from kokoro_onnx import Kokoro
who, text, out = sys.argv[1], sys.argv[2], sys.argv[3]
v = json.load(open(os.path.join(os.path.dirname(__file__), 'voices.json')))[who]
a, sr = Kokoro('/tmp/kk/kokoro.onnx', '/tmp/kk/voices.bin').create(text, voice=v['kokoro_voice'], speed=v['speed'], lang='en-us')
sf.write(out + '.raw.wav', a, sr)
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', out + '.raw.wav', '-af',
                f"rubberband=pitch={v['pitch']}:formant={v['formant']}:pitchq=quality", '-ar', str(sr), '-ac', '1', out], check=True)
os.remove(out + '.raw.wav')
a, _ = sf.read(out); idx = np.where(np.abs(a) > 0.01)[0]; sf.write(out, a[max(0, idx[0]-400):idx[-1]+2400], sr)
print(out)
