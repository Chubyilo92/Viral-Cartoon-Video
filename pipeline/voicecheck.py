#!/usr/bin/env python3
"""Post-render voice check for a JJ spec: does each narrated line (a) say the words we wrote,
(b) pause where the script breaks, (c) end with falling intonation on statements, and
(d) stay at a natural pace. Usage: python3 voicecheck.py <slug>  (after make_video.py)."""
import sys, re, json, importlib
import numpy as np, soundfile as sf, librosa
sys.path.insert(0, '/home/claude/jj'); sys.path.insert(0, '/home/claude/jj/specs')
from pocketsphinx import Decoder

slug = sys.argv[1]
spec = importlib.import_module(slug)
W = f'/home/claude/jj/work/{slug}'
dec = Decoder()
NUM = {'sixty': '60'}


def words(t):
    t = t.lower().replace('"', '').replace("'", "'")
    return re.findall(r"[a-z']+", t)


def recog(a, sr):
    y = librosa.resample(a.astype(np.float32), orig_sr=sr, target_sr=16000)
    pcm = (np.clip(y, -1, 1) * 32767).astype(np.int16).tobytes()
    dec.start_utt(); dec.process_raw(pcm, full_utt=True); dec.end_utt()
    h = dec.hyp()
    return h.hypstr.split() if h else []


def check(text, wav):
    a, sr = sf.read(wav)
    dur = len(a) / sr
    wl = words(text)
    rate = len(wl) / dur
    # pauses: frames below threshold for >= .22s inside the line
    hop = int(sr * .01)
    rms = librosa.feature.rms(y=a.astype(np.float32), frame_length=hop * 3, hop_length=hop)[0]
    thr = max(rms.max() * .04, 1e-4)
    sil = rms < thr
    pauses, run = 0, 0
    for s in sil[10:-10]:
        if s: run += 1
        else:
            if run >= 22: pauses += 1
            run = 0
    breaks = len(re.findall(r'\.\.\.|[.?!](?=\s)|,|;', text.strip()))
    # end intonation of the final clause
    f0, vf, _ = librosa.pyin(a.astype(np.float32), fmin=60, fmax=300, sr=sr, frame_length=1024, hop_length=256)
    v = f0[~np.isnan(f0)]
    trend = None
    if len(v) > 20:
        tail = v[-max(6, len(v) // 8):]
        body = np.median(v)
        trend = round(float(np.median(tail) / body - 1) * 100, 1)
    question = text.strip().endswith('?')
    hyp = recog(a, sr)
    hits = sum(1 for w in set(wl) if w in hyp)
    recall = round(hits / max(1, len(set(wl))) * 100)
    flags = []
    if not (1.8 <= rate <= 3.6): flags.append(f'pace {rate:.1f} w/s')
    if trend is not None and not question and trend > 12: flags.append(f'ends rising +{trend}% (sounds like a question)')
    if trend is not None and question and trend < -10: flags.append('question ends falling')
    if pauses + 1 < breaks // 2: flags.append(f'few pauses ({pauses} vs {breaks} breaks: may sound rushed)')
    if recall < 45: flags.append(f'low word match {recall}% (possible mispronunciation)')
    return dict(text=text, dur=round(dur, 1), rate=round(rate, 2), pauses=pauses, breaks=breaks,
                end_trend_pct=trend, word_match=recall, flags=flags)


rows = [check(t, f'{W}/b{i}.wav') for i, t in enumerate(spec.BODY_LINES)]
import os
for t, f in ((spec.IG_LINE, f'{W}/ig0.wav'), (spec.TT_LINE, f'{W}/tt0.wav')):
    if os.path.exists(f): rows.append(check(t, f))
json.dump(rows, open(f'{W}/voicecheck.json', 'w'), indent=1)
for r in rows:
    print(('FLAG ' if r['flags'] else 'ok   ') + f"{r['dur']:>5}s {r['rate']:.1f}w/s end{r['end_trend_pct']}% match{r['word_match']}% | {r['text'][:70]}" + ('  <-- ' + '; '.join(r['flags']) if r['flags'] else ''))
# 28 Oct 2026: a FLAG used to print and exit 0, so "fix every FLAG" depended on the model choosing to.
# Now the result is written next to the videos (preflight.py requires it for long format) and any
# FLAG exits 1.
nflags = sum(1 for r in rows if r['flags'])
json.dump({'slug': slug, 'flags_total': nflags, 'rows': rows},
          open(f"/home/claude/jj/out/{slug.replace('_', '-')}.voicecheck.json", 'w'), indent=1)
if nflags:
    print(f'VOICECHECK FAILED: {nflags} flagged line(s). Fix them (LINE_SPEED / reword) and re-render.')
    sys.exit(1)
print('VOICECHECK PASSED')
