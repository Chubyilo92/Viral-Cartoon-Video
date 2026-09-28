# QA checklist — run before scheduling any video

Claude cannot watch or listen to a finished video. Every check here is
therefore mechanical/measurable, not subjective — that's deliberate: it's
what lets QA run unattended in a weekly batch without a human reviewing each
one. Run all of these on every video before it's pushed to Metricool. If any
check fails, fix the specific cause (almost always a timing/retiming issue —
see BUILD-METHOD.md's documented bug) and re-render; don't ship a video that
fails a check.

## 1. No overlapping voice lines

For every line `i`, confirm `scene_end[i] >= line_start[i] + line_duration[i]`
with a positive gap (this pipeline uses a 0.55s gap by design). Print a table
of `ends=` vs `next_starts=` for every line and eyeball that every gap is
positive — this is exactly the check that caught the retiming bug during
development. Never skip this; it silently breaks the video's most important
property (the voice actually matching what's on screen).

```python
import soundfile as sf, re
d = [float(x) for x in re.findall(r"\{d:([\d.]+),cap", open('anim.html').read())]
t = 0
for i in range(len(d)):
    a, sr = sf.read(f'tts/line{i}.wav'); dur = len(a) / sr
    start = t + 0.2; end = start + dur
    gap = t + d[i] - end
    assert gap > 0, f"line {i} overlaps the next scene by {-gap:.2f}s"
    t += d[i]
```

## 2. Total duration is sane

Between 35s and 75s. Shorter reads as unfinished; longer loses viewers before
the ending lands (the whole point of the ending is to convert, so it must be
reached).

## 3. Frame sampling renders cleanly

Render 4–6 sample frames spread across the video (start, each scene
boundary, the end card) and open them. Confirm: no visual glitches, the
correct caption text is on screen for that timestamp, the end-card ending
matches what was intended for that platform (quiz mockup for the IG cut,
follow-counter text for the TikTok cut — see §5, these are two separate
renders), and the puppies' expressions match the line being spoken (a sad
line shouldn't land on a smiling frame).

## 4. Audio actually muxed in

Check the final file's audio stream exists and roughly matches video
duration:

```bash
ffprobe -v error -show_entries stream=codec_type,duration -of default=noprint_wrappers=1 final.mp4
```

Confirm both a `video` and an `audio` stream are listed, and the audio
duration isn't wildly shorter than the video's (a silent/truncated mux is a
common and otherwise-invisible failure).

## 5. Two separate final renders, one per platform

Because the ending differs by platform (Instagram quiz card vs. TikTok
follow-counter card — see GROWTH-STRATEGY.md), each video needs **two**
distinct final exports sharing the same body but different end cards:
`*_instagram.mp4` and `*_tiktok.mp4`. Confirm both exist and are not
accidentally identical files before scheduling either.

## 6. File size and delivery

Keep each final export under ~25MB (re-encode at `-crf 23` if larger).
GitHub's push limit is much higher (100MB/file) so this cap is really about
keeping things fast to move around, not a hard platform limit.

## When a video fails

Remake it — don't schedule a video that fails any check above, and don't
silently drop it either. If a script fails QA twice in a row, stop trying a
third time in the same batch run; log it as failed in
`docs/PRODUCTION-LOG.md` with the reason, skip to the next script so the
batch still completes, and flag it in the end-of-batch summary so a human
sees it.
