#!/usr/bin/env python3
"""Final-file gate (added 6 Nov 2026): checks the FINISHED mp4, not the per-line wavs.

  python3 watchcheck.py <slug> <mp4>

1. Vocal delivery in the final mix: speech recognition on the whole file; every BODY_LINE must have
   >= 45% of its words recognised (catches a line drowned by music, cut off, or garbled).
2. Edge clipping: samples a frame every 0.5 s and fails if the caption cream fill (#fffaf0-ish) or
   label/bubble text touches the left/right 6 px of the frame (6 Nov: "barely packed anything" and
   long caption chunks ran off the edge and no gate caught it).
3. Writes work/<slug>/watch_sheet.png: one frame per scene (middle of each line) in order, for the
   fresh structure reviewer (RULES.md §5 step 3b). Code cannot judge whether the story makes sense;
   that reviewer does.

Exit 1 on any failure. Writes work/<slug>/watchcheck.json."""
import sys, os, re, json, subprocess, importlib, tempfile
import numpy as np, soundfile as sf, librosa
from PIL import Image
sys.path.insert(0, '/home/claude/jj'); sys.path.insert(0, '/home/claude/jj/specs')
from pocketsphinx import Decoder

slug, mp4 = sys.argv[1], sys.argv[2]
spec = importlib.import_module(slug)
W = f'/home/claude/jj/work/{slug}'; os.makedirs(W, exist_ok=True)
fails = []

def words(t): return re.findall(r"[a-z']+", t.lower())

# 1. ASR on the final mix
tmp = tempfile.mktemp(suffix='.wav')
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', mp4, '-ac', '1', '-ar', '16000', tmp], check=True)
a, sr = sf.read(tmp); a = a.astype(np.float32)
d = Decoder(); d.start_utt(); d.process_raw((np.clip(a, -1, 1) * 32767).astype(np.int16).tobytes(), full_utt=True); d.end_utt()
hyp = set(d.hyp().hypstr.split()) if d.hyp() else set()
lines = []
for i, l in enumerate(spec.BODY_LINES):
    ws = set(words(l)); m = round(100 * len(ws & hyp) / max(1, len(ws)))
    lines.append({'line': i + 1, 'match': m})
    if m < 45: fails.append(f'L{i+1} only {m}% of words recognised in the final mix')
dur = len(a) / sr

# 2. edge clipping + 3. scene sheet
def frame(t):
    f = tempfile.mktemp(suffix='.png')
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', f'{t:.2f}', '-i', mp4, '-frames:v', '1', f], check=True)
    return Image.open(f).convert('RGB')

edge_hits = []
for t in np.arange(0.3, dur - 0.2, 0.5):
    im = np.asarray(frame(t)).astype(int)
    h, w, _ = im.shape
    for side, sl in (('left', im[:, :6]), ('right', im[:, w - 6:])):
        band = sl[int(h * .08):int(h * .92)]
        cream = (band[..., 0] > 240) & (band[..., 1] > 235) & (band[..., 2] > 215)
        ink = (band.sum(-1) < 120)
        if cream.sum() > 40 and ink.sum() > 20:
            edge_hits.append(f'{t:.1f}s {side}')
if edge_hits: fails.append('text touching frame edge at ' + ', '.join(edge_hits[:8]))

n = len(spec.BODY_LINES)
# Use REAL per-scene boundaries (from the cached TTS durations make_video.py wrote), not a
# uniform-duration guess: lines vary a lot in length (4.2s-8.1s here), so a uniform split drifts
# out of alignment with the actual scene it's meant to sample as it goes (discovered 7 Nov 2026:
# a uniform-split sheet showed line 5's frame under line 4's position and so on).
PAD = 0.75
cut = 'ig' if 'instagram' in os.path.basename(mp4) else 'tt'
b_meta = json.load(open(f'{W}/b_meta.json'))
body_dur = [round(d + PAD, 2) for d in b_meta['durs']]
end_meta = json.load(open(f'{W}/{cut}_meta.json'))
end_pad = PAD + (0.6 if cut == 'ig' else 0.9)
end_dur = round(end_meta['durs'][0] + end_pad, 2)
all_dur = body_dur + [end_dur]
if abs(sum(all_dur) - dur) > 1.0:
    # fallback to the old uniform guess if the cached durations don't match this mp4's actual length
    ts = [dur * (i + .5) / (n + 1.2) for i in range(n)] + [dur - 1.5]
else:
    starts = np.cumsum([0] + all_dur[:-1])
    ts = [round(starts[i] + all_dur[i] / 2, 2) for i in range(n)] + [round(starts[n] + all_dur[n] / 2, 2)]
ims = [frame(t).resize((270, 480)) for t in ts]
sheet = Image.new('RGB', (270 * len(ims), 480), 'white')
for k, im in enumerate(ims): sheet.paste(im, (270 * k, 0))
sheet.save(f'{W}/watch_sheet.png')

json.dump({'slug': slug, 'mp4': mp4, 'lines': lines, 'edge_hits': edge_hits, 'fails': fails,
           'sheet': f'{W}/watch_sheet.png'}, open(f'{W}/watchcheck.json', 'w'), indent=1)
for r in lines: print(f"L{r['line']} word match {r['match']}%")
print('sheet:', f'{W}/watch_sheet.png')
if fails:
    print('WATCHCHECK FAILED:\n  ' + '\n  '.join(fails)); sys.exit(1)
print('WATCHCHECK PASSED (now send watch_sheet.png + BODY_LINES to a fresh structure reviewer)')
