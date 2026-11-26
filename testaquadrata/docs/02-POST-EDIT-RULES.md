# TestaQuadrata — Post-Edit Rules (fixing a finished video without breaking it)

These are the rules for everything that happens **after** the first full render: feedback rounds, "fix just
these two things", swapping a character everywhere, patching sound. They are the most valuable part of the
method because this is where most time and money is lost. Every rule below came from a real mistake.

## 1. The five laws of post-editing
1. **Fix only what was asked.** "Fix these two things without fixing anything else" means exactly two shots
   change; every other frame stays bit-identical. Keep a list of other issues you noticed and *report*, don't fix.
2. **Fix the master once, then derive everything else from it.** Fix the main YouTube video first, then reuse
   the *same fixed clips* in every derived file (reels, TikTok/IG versions, alternate cuts). Never fix each
   video one by one — that wastes hours and causes inconsistencies between versions.
3. **Re-render only the frames that change** (window re-render) and **splice** them in. Never re-render a
   full 9-minute video for a 2-second fix.
4. **Never delete a good file until the replacement is verified.** A cleanup step once deleted a full render
   after a failed splice. Write to a temp name ending `.mp4`, rename only on exit 0, delete old versions last.
5. **Look at the fixed frames before delivering.** Extract the frame(s) at the fixed second, view them, and
   also view one frame before and after the splice to confirm no flash, ghost or jump.

## 2. Window re-render + splice (the standard fix)
1. Find the shot in `plan.json` that covers the fix (note `t` and the next shot's `t`; crossfades are 0.35 s).
2. Change the plan (new image name, new camera, new overlay). Add the new image to `img_all/` (2752x1536 JPG).
3. Render only the frame range: `node render.js <startFrame> <endFrame> clip.mp4` — extend ±0.35 s (≈ 11 frames) each side so the
   crossfades into/out of the shot are re-rendered too.
4. Splice: `python splice_clips.py base.mp4 out.mp4 '[["clip.mp4", startFrame]]'`. It splits the base into
   pieces, joins with the concat demuxer (re-encode to the same crf/fps), and maps the original audio as `1:a?`
   (optional map — the silent base has no audio and an unconditional map crashed once).
5. If the **audio** also changed, remix only the audio (`mix_epN.py`) and re-mux with `-c:v copy`. Never re-encode video for an audio fix.
6. Regenerate the reels from the fixed master (`build_social.py` takes reel numbers as arguments, so only the affected reels are rebuilt).

## 3. Swapping a character/prop across an already-finished episode (Ep1 van-man swap)
Problem: Ep1 used a round-headed van man; the creator preferred the boxed, masked design and wanted it in Ep1.
- **First attempt failed**: fading the new head in at every cut showed the *old* face for a few frames at the
  end of the video ("flashes into the old image") — and the same bug would repeat in every derived video.
- **Method that worked** (`code/engine/patch_head_swap.py`): detect the old image in each frame with ORB features + RANSAC partial-affine
  per frame; group frames into smooth-motion runs, fit quadratic parameter curves per run (extend a few frames for
  dissolves); build a mask from the difference between the old and new still; **replace** pixels (`out*(1-A) + new*A`),
  never cross-fade; nearest-frame average where tracking is missing.
- **Fix the master once, reuse the clips**: the same fixed clips (by frame number) were spliced into the main video and into Reel 2.
  Then check *every other place* the old image appears (end cards, call-back shots, reels).
- Also fix ghosts: an end text ("CONTINUA…") showed a ghost of the head; restore the original frames there.
- Save cut-out heads (`head_vanman.png`, `head_socio.png`) and a character sheet so Gemini reproduces the design in future episodes.

## 4. Typical fix recipes (what to do for each kind of complaint)
| Complaint | Fix |
|---|---|
| Wrong/misspelled text on a wall | New blank plate + handwriting/word reveal overlay; reveal only on the spoken line |
| Text appears too early | Move `hand`/`ov` `t0` to the utterance start from `asr.json`; the image underneath must be the *clean* plate |
| Wrong location (Lucia's house instead of Giulia) | New image (photo of TS+Giulia), `swap`/new shot on the word, repeat on the echo line |
| Same prop must be same prop (the 3rd-floor door) | One base image of that door; draw chalk with `chalk={mode:'draw'}` then `{mode:'smudge'}` (wiped) over the *same* image |
| Floating hand / phone with no body | Remove the shot or replace with an image where a visible character holds it |
| A hand is on the wrong person (checking *him* instead of *her* pulse) | Fix the image only: mirror/regenerate the second hand so the hand lies on the correct person; change nothing else (Ep3 `e3_hands_gap` → mirrored second hand; original kept as `_orig`) |
| Object on the face that shouldn't be there (a watch on his face in the pulse shot) | Regenerate/clean the still (`e3_pulse_v3`), update the two shots that use it (`t=180.0` and `t=443.8`), re-render only those windows |
| Giulia passes a zombie / Antonelli in lift cage | New still using the character sheet; replace that window only |
| Loud noise at a timestamp | Move or duck that SFX in `mix_epN.py`; re-measure that second; remix audio only |
| Background too strong / too weak | Raise/lower `BED` in the mix by the stated % (e.g. ×1.13 on backgrounds), **excluding the day sting**; re-measure speech windows (≥15 dB under voice) |
| Chain / prop that does not belong | Remove the element from the image or replace the image; re-check every shot that reuses it |
| YouTube ending | Render a dedicated end card (8 s: "TERZO EPISODIO A 50.000 ISCRITTI" + arrow + circle pointing at the subscribe button) and append; reels use the "EPISODIO INTERO SU YOUTUBE" card instead |
| Fallback image used | Generate the real image, add to `img_all/`, re-render that window |

## 5. Rules for rendering fixes
- Keep **one encoder setting** for everything (30 fps, H.264, crf 17–18, yuv420p). Mixed settings make concat visible.
- Render server: the local `http.server` for `engine.html` can die — if window renders fail, restart it before anything else.
- Disk is finite: delete only your own temp files; keep the last good master and the final deliverables.
- Large Desktop saves time out: commit 1–4 files per call.
- Gemini images arrive as `.tmp` then `.jfif`; stage them, convert with PIL to 2752x1536 JPG, review each one visually before using.

## 6. After the fix — checklist (must all be yes)
- [ ] Only the requested shots changed (diff a few untouched frames: identical).
- [ ] The fixed frame was extracted and looked at.
- [ ] No flash/ghost at the splice boundaries (view frames at start−1, start, end, end+1).
- [ ] Audio untouched unless the fix was audio; if audio changed, speech windows re-measured.
- [ ] Master fixed first; all derived files (reels, social, alternates) rebuilt from it.
- [ ] Old files not deleted until the new ones were checked.
- [ ] The deliverable was saved to `PRONTI` in the right episode/platform folder.
- [ ] Remaining known issues were *listed*, not silently fixed.

## 7. Creator-feedback log (Ep2/Ep3) — kept as worked examples for the course
Ep2: animate the wall name writing; sister photo on "tua sorella" and "evviva"; lower the loud noise at 45 s; stop
showing Lucia's house when Giulia is mentioned; background too strong at ~2:00/3:00/7:00; chalk circle on the hands door
(drawn then wiped); olive oil at 5:10; the circle door at 5:22/5:27; NON SCENDERE only at 5:48; chain removed at 7:36;
real portone at 7:47; no body-less phone; Antonelli's context; last minute remade to follow the story; Giulia passes a
zombie; Ep1 phone message call-back; check all background noise; rewatch with the story in mind.
Ep3: two fixes only — (1) at 0:32 / 3:02 the two hands must check *her* pulse, not his; (2) remove the watch from his face in the pulse picture.
Second-pass list left unfixed by the creator's choice: lock-in fallback image, wedge on the front door instead of the bathroom door, `e1_door_sit` continuity mismatch, static shutters, Giulia on the stairs before she decides, a calm ending, a night image used on a day scene, Ostia bite only implied.

## 8. Reel captions (burned-in subtitles) — approved 26 Nov 2026
Every Instagram and TikTok reel carries burned-in captions. Rules, approved by the creator after three rounds:
1. **Never ahead of the voice.** A caption word may appear only when that word is spoken. Time captions against the
   CLEAN voice track (episode `voice16.wav` / Ep1 `reel2/voice_full.wav`), never the mixed reel audio: the day sting and
   music at the start of a reel fooled the detector and put the first 10 s of captions up to 1 s early.
   - Find the reel inside the clean voice by cross-correlation (offset + corr > 0.9).
   - Words come from Whisper on pause-split chunks; word times are spread by syllables inside voiced sub-intervals.
   - Then three snaps: any word with no voice in the 150 ms after it → moved to the voice onset; any word after
     punctuation → moved to the next voiced onset (unless it already sits on one); unmatched words → next onset.
   - Final check: zero words shown with no voice in the following 150 ms.
2. **Text = what was actually said**, not the script. Script spelling is used only where the spoken word matches;
   recognition errors are fixed by hand and doubtful words listed for the creator to check by ear.
3. **Look:** Poppins Bold 58 px on a 1080×1920 frame (22% smaller than the 74 px draft), white, black outline, all caps,
   max 3 words / 18 characters per chunk; the word being spoken turns gold (#F2C14E, the title underline colour).
4. **Position:** centred ~85 px UNDER the picture (y = 1350), clear of the image and above the app's caption/buttons area.
5. **Don't collide with the follow card.** Instagram's "SEGUICI per la Parte N" card + arrow sit under the picture for
   4–5 s → during that window captions move to the strip above the picture (y = 612). TikTok's card sits above the
   picture → captions stay under it. Detect the card window from the uncaptioned reel by frame brightness.
6. Work in batches of 3 reels, closest publish date first. Keep originals; captioned copies go to
   `TESTAQUADRATA PRONTI\Sottotitolati`.
