#!/usr/bin/env python3
"""Pre-render per-line TTS + voicecheck pass (RULES.md step 2): TTS each BODY_LINE alone with the
spec's current LINE_SPEED, run the same check() voicecheck.py uses, report flags. Writes to a
throwaway dir, not the real work/<slug>, and does not require approval.check(). Usage:
python3 prevoice.py <slug>"""
import sys, os, re, json, importlib, shutil
import numpy as np, soundfile as sf, librosa
sys.path.insert(0, '/home/claude/jj'); sys.path.insert(0, '/home/claude/jj/specs')
from pocketsphinx import Decoder
import jjlib as J

slug = sys.argv[1]
spec = importlib.import_module(slug)
J.LINE_SPEED = getattr(spec, 'LINE_SPEED', {})
tmp = f'/home/claude/jj/work/{slug}_prevoice'
shutil.rmtree(tmp, ignore_errors=True)
os.makedirs(tmp, exist_ok=True)
durs, sr0 = J.tts_lines(spec.BODY_LINES, tmp, 'b')

dec = Decoder()

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

rows = []
for i, t in enumerate(spec.BODY_LINES):
    r = check(t, f'{tmp}/b{i}.wav')
    rows.append(r)
    print(('FLAG ' if r['flags'] else 'ok   ') + f"L{i} {r['dur']:>5}s {r['rate']:.1f}w/s end{r['end_trend_pct']}% match{r['word_match']}% | {r['text'][:60]}" + ('  <-- ' + '; '.join(r['flags']) if r['flags'] else ''))
nflags = sum(1 for r in rows if r['flags'])
print(f'--- {nflags} flagged line(s) ---')
shutil.rmtree(tmp, ignore_errors=True)
sys.exit(1 if nflags else 0)
