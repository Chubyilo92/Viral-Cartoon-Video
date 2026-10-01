# Build method: JJ puppy cartoon videos

How these are actually made, end to end, so a fresh Claude session (or a human) can
pick this up with zero prior context. Nothing here is AI video generation — the
whole thing is a hand-written HTML5 canvas renderer, driven frame-by-frame in
headless Chromium, plus a free local voice generator and an original synthesized
music bed. No credits, no subscriptions, no third-party assets.

## Why it's built this way

- No footage is ever supplied by the user — every frame is drawn by code.
- No paid tools (no vidIQ credits, no stock voice/music licenses). Everything
  in this pipeline is either free (Kokoro TTS, a local browser) or generated
  from scratch (the puppies, the music).
- Cost per new video is low: the expensive part (the character rig, the props,
  the renderer, the render pipeline) is built once and reused. A new video is
  mostly a new script and a new `SCENES` array.

## 1. The renderer (`/engine/puppy-engine.js`)

This is the shared engine every video's HTML file starts with. It's not a
standalone importable module — it's meant to be pasted at the top of a
self-contained `<script>` block in an `.html` file (see the two finished
videos under `/videos/` for the full pattern). It defines, in order:

- **Math/animation helpers**: `ease`, `back` (overshoot/pop-in), `P()` (a
  windowed ease between two times), `win()` (on/off ramp), a seeded `hash()`
  for consistent per-shape jitter (`seed()`/`SC`/`BOIL`) so linework looks
  hand-drawn but stays deterministic frame to frame.
- **Drawing primitives**: `ell()` (a wobbly, hand-drawn-style ellipse),
  `blob()` (a soft rounded polygon through jittered points), `line()`/`tube()`
  (a stroked or thick "arm/tail" path), `heart()`, `sparkle()`,
  `floatHearts()`.
- **The puppy rig** (`pup()`): a single parameterised function that draws
  *either* dog (`kind: 'boy'|'girl'`) in `sit` or `lie` pose, with props for
  expression (`eyes`, `mouth`, `brows`, `blush`, `tilt`, `wag`, `earLift`,
  `paw`, `breath`, `blink`, `shades`, `bandana`, `puff`, `squash`, `bob`,
  `hx`/`hy` head offset). Boy = tan fur + blue bandana; girl = cream fur +
  pink bow. This one function is what every scene in every video calls,
  usually twice (one per pup) with different prop values per frame.
- **Head/face detail** (`head()`): ears, eyes (open/wide/happy/closed/squint,
  plus an automatic periodic blink), brows, nose, mouth shapes (`w`, `open`,
  `smile`, `flat`, `pout`, `o`, `chomp`), blush.
- **Props/backgrounds**: `room()` (wall+floor+polka-dot pattern), `windowBox()`
  (a window with a custom sky-drawing callback), `plant()`, `frame()` (wall
  picture frame), `bowl()`, `mug()`, `flower()`, `cloud()` (also used as a
  small raincloud with falling-line rain), `note()` (musical note), `zzz()`
  (sleep Zs), `bubbleText()` (a speech-bubble pill), `phoneMock()` (a phone
  silhouette with a custom screen-drawing callback — used for both "watching
  a text" beats and the end-card quiz mockup).
- **Grain overlay**: a pre-rendered noise+vignette canvas composited with
  `multiply` blending on every frame, which is most of why this looks like a
  warm illustrated print rather than flat vector art.

## 2. A video file's structure

Each video is one self-contained `.html` file: the engine, then a
`SCENES` array, then shared timing/caption/render code at the bottom
(`title()`, `caption()`, `drawScene()`, `render(t, withCap)`), which exposes
`window.render`, `window.TOTAL`, `window.SCENES` for the headless renderer to
drive.

**A scene** is `{ d: <seconds>, cap: [<caption phrases>], draw(u) {...} }`
where `u` is seconds elapsed since that scene started. `draw(u)` calls
`room()`/`windowBox()`/etc. for the background, then `pup({...})` once or
twice with time-driven prop values (built from `P()`/`pop()`/`win()` against
`u`) to animate expressions and movement within the scene. Scenes cross-fade
into each other (0.3s) and each scene has a very slow zoom-in for a bit of
life.

**Captions** are auto-timed: word count per caption phrase determines its
share of the scene's duration, so longer phrases get more screen time
automatically. Each caption pops in with an overshoot animation and fades out
just before the next one.

**Critical: scene duration must equal the voice line's length**, not be
guessed. See the retiming step in §4 — this is where a real bug happened.

## 3. Rendering to video (`render.js` / `render2.js`)

Playwright drives headless Chromium against the `.html` file, calls
`window.render(t, withCap)` at 30fps for `t` from 0 to `window.TOTAL`,
grabs each frame as a JPEG data URL via `canvas.toDataURL()`, and pipes the
JPEG stream into `ffmpeg` (`-f image2pipe -c:v mjpeg`) to encode H.264. It
renders **two** frame streams per pass — `withCap=true` (captions burned in,
the only version now delivered — see §6) and `withCap=false` (clean, used
only if a variant needs different text later) — from the same Chromium
session, so it only launches the browser once.

Runtime: roughly 5 minutes of render time per ~50–60s video in this
environment. This costs no user-facing "usage" beyond that wall-clock wait —
it's the workspace's own compute, not model inference.

```bash
node render.js     # or render2.js — see each video's own copy
```

## 4. Voice (free, local, no credits)

TikTok/Instagram-style narrated relationship content lives and dies on
having *a* voice — but paid TTS (e.g. vidIQ's voiceover generator) costs
credits per character and was explicitly ruled out as unsustainable for
daily output.

**Fix: Kokoro TTS, running locally in the workspace, free and unlimited.**

```bash
pip install --break-system-packages kokoro-onnx soundfile
mkdir tts && cd tts
curl -sSL -o kokoro.onnx   https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx
curl -sSL -o voices.bin    https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin
```

Voice chosen: **`am_michael`** — warm, mature, calm male narrator, closest
match to the original viral video's tone. (Sampled `am_michael`, `am_adam`,
`am_onyx`, `bm_george`, `bm_lewis` before picking.) Spoken at `speed=0.9` so
it reads as reflective rather than rushed.

Each video's `tts/lines*.py` generates one `.wav` per script line (trimming
leading/trailing silence with an amplitude threshold), and writes a
`dur.json` with each line's real length in seconds.

### The retiming step — and the bug that happened here

A scene's `d` (duration) **must** be set to that line's real spoken length
plus a fixed pad (`+0.75s` worked well), not guessed from word count. The
first pass through this always assumes durations roughly, then gets
corrected once the real voice lengths are known:

```python
import json, re
vo = json.load(open('tts/dur.json'))       # real per-line durations, seconds
news = [round(v + 0.75, 2) for v in vo]
s = open('anim.html').read()
it = iter(news)
s2, n = re.subn(r"\{d:[\d.]+,cap:", lambda m: "{d:%s,cap:" % next(it), s)
assert n == len(news)
open('anim.html', 'w').write(s2)
```

**Bug that shipped once and was caught by the user, not by testing:** an
earlier version of this retiming did a naive `str.replace(f"{{d:{old},cap:")`
per scene. Whenever a scene's *original* duration happened to be a whole
number (`5`, `6`, `7`), Python's `float(x)` formatted it back as `"5.0"`,
which no longer matched the literal `"{d:5,cap:"` in the file — so the
replace silently no-op'd on exactly those scenes. Three scenes (including the
first two) kept their old, too-short durations while the full-length voice
line played underneath, so the next line started before the previous one
finished — audible mostly in the first ~30 seconds. **Lesson: always retime
by regex substitution in file order (`re.subn` with a positional callback,
asserting the replacement count), never by matching on the stringified old
value.** Always verify afterwards by recomputing each line's real start/end
against the scene boundaries (see the verification snippet used when this
was fixed — print each line's `ends=` vs the next line's `starts=` and
confirm a positive gap).

### Mixing multiple lines into one voice track

```python
import numpy as np, soundfile as sf, re
d = [float(x) for x in re.findall(r"\{d:([\d.]+),cap", open('anim.html').read())]
sr = 24000
out = np.zeros(int(sum(d) * sr) + 5 * sr)   # generous tail buffer
t = 0
for i, di in enumerate(d):
    a, _ = sf.read(f'tts/line{i}.wav')
    st = int((t + 0.2) * sr)                # 0.2s lead-in per scene
    end = min(st + len(a), len(out))
    out[st:end] += a[:end - st]
    t += di
sf.write('vo_raw.wav', out[:int(sum(d) * sr)], sr)
```

Then polish with ffmpeg (gentle compression, a touch of room echo, loudness
normalize to broadcast level):

```bash
ffmpeg -i vo_raw.wav -af "highpass=f=70,acompressor=threshold=-20dB:ratio=3:attack=5:release=120,aecho=0.8:0.5:40:0.12,loudnorm=I=-14:TP=-1.5:LRA=7" -ar 44100 -ac 2 vo.wav
```

## 5. Music (free, original, no credits)

See `/music/generate_music_bed.py`. A warm chord pad (Cmaj7–Am7–Fmaj7–Gadd9)
plus a quiet music-box arpeggio, synthesized entirely from sine-wave
harmonics with simple ADSR envelopes — composed in code, so there's no
licensing question at all. Mixed in quietly (≈-6dB relative to voice) under
the narration:

```bash
ffmpeg -i voice.wav -i music_bed.wav -filter_complex \
 "[1:a]volume=0.5,atrim=0:<video_len>,asetpts=PTS-STARTPTS[m];
  [0:a][m]amix=inputs=2:duration=first:dropout_transition=0,loudnorm=I=-14:TP=-1.5:LRA=8[a]" \
 -map "[a]" -ar 44100 -ac 2 voice_with_music.wav
```

## 6. Final mux and delivery

```bash
ffmpeg -i captions_video.mp4 -i voice_with_music.wav -map 0:v -map 1:a \
  -c:v libx264 -crf 23 -preset slow -pix_fmt yuv420p -c:a aac -b:a 192k \
  -shortest -movflags +faststart final.mp4
```

**Delivery rule: only the captions-burned-in version is sent, no separate
clean version.** (Earlier videos included a clean cut too, in case captions
needed to be redone in CapCut — decided against continuing that once
captions became reliable and locked to the voice.)

## 7. Known constraints / gotchas

- Output width x height: 1080x1920 (9:16), 30fps, ~50–60s typical length.
- File size for delivery: keep the final mp4 under ~25MB where possible
  (re-encode with `-crf 23` if the first pass is bigger) — there's an upload
  ceiling on files sent back to the user.
- The Kokoro model files (`kokoro.onnx` ~325MB, `voices.bin` ~28MB) are
  **not** committed to this repo — too large, and they're a stable public
  download (see §4 URLs). Re-download them fresh in any new environment.
- Rendered video/audio outputs are not committed here either — this repo is
  the *method*, not a media archive. Finished videos are delivered directly
  to the user each time; brand-asset repos (see `/docs/BRANDS.md`) are for
  published media.

## 8. Dialogue videos — two puppy voices, no narrator (added 2026-10-01)

Format for CoupleIn story videos: the puppies *are* the characters and talk to
each other; there is no narrator. Built with `pipeline/dialogue.py <slug>`
(spec in `pipeline/specs/<slug>.py`; worked examples: `milk.py`, `argue.py`,
`brownies.py`).

- **Voices** (Kokoro, free/local, then pitched up with ffmpeg `rubberband`,
  `formant=shifted` so they sound small and cartoon-cute rather than just
  higher): boy pup = `am_puck`, speed 0.9, pitch ×1.36; girl pup =
  `af_heart`, speed 0.9, pitch ×1.24. Tune in `VOICES` at the top of
  `dialogue.py`.
- **Spec**: `TITLE`, `LINES = [D(who, text, sceneJS, emoji), ...]` — one
  spoken line per scene, `who` = `'boy'|'girl'` — plus `END` (end card, built
  with `ENDCARD(tagline, extraJS, speaker)`), optional `MUSIC_N`.
- **Captions** auto-chunk each line into ≤3-word / ≤15-char phrases and are
  tinted by speaker (boy light blue, girl pink) so viewers can follow who's
  talking with sound off.
- **Talking mouths**: call `SP(kind, u, {..., talk:1})` instead of `pup()` for
  the speaker — the mouth animates and the head bobs only while that line's
  audio is playing.
- Helpers in its PRELUDE: `chip(text)` (top label: DAY 2, ROUND 1…),
  `fridge`, `milk`, `cereal`, `brownies`, `cityOut` (street/office),
  `bag`, `appUI`/`pill` (CoupleIn phone screens), `ENDCARD`.
- Scene pad is 0.8s per line (snappier than narration's 0.75 + slower read).
- `python3 dialogue.py <slug> preview` renders one still per line to
  `work/<slug>/pv_*.png` for a layout check before the full render.
- Scene-space gotcha: the camera zooms 1.2× around (540,1180), so x < ~230 or
  x > ~850 at pup scale 1.3 gets cropped. Two pups + a phone need `s:1.1`.
- Output is one file per video (same creative for IG and TikTok, like ads).
