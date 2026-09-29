# JJ video pipeline (free: Kokoro TTS + canvas renderer + user's 3 music beds)

Setup in a fresh session (workspace `/home/claude/jj` is assumed by the scripts):
```
pip install --break-system-packages kokoro-onnx soundfile numpy playwright pillow
mkdir -p /tmp/kk && cd /tmp/kk
curl -sSL -o kokoro.onnx https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx
curl -sSL -o voices.bin  https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin
mkdir -p /home/claude/jj && cp -r <repo>/pipeline/* /home/claude/jj/ && mkdir -p /home/claude/jj/out /home/claude/jj/work
cd /home/claude/jj/music && for i in 1 2 3; do ffmpeg -y -i sound$i.m4a -ar 44100 -ac 2 sound$i.wav; done
```
Also clone this repo to `/home/claude/viral-cartoon-video` (jjlib reads scenes from `videos/*/anim*.html`).

- New video = one file `specs/<slug>.py` (TITLE, BODY_LINES, SCENES = list of scene JS strings via `_kit.S`, IG_LINE, IG_CAPS, IG_RESULT, TT_LINE).
- `python3 preview.py <slug>` -> frames per scene in `work/<slug>/pv_*.png` (check layout before the long render).
- `TT_COUNT=<real follower count> python3 make_video.py <slug> both` -> `out/<slug>-instagram.mp4`, `out/<slug>-tiktok.mp4`, plus QA JSON and `*_f0..5.png` sample frames. ~2.5-4 min per cut.
- Music: rotates the 3 user-supplied sounds by slug hash (`MUSIC_N` in a spec overrides), looped/faded under the voice.
- Files must be < 25MB (crf 24 is enough; re-encode at crf 27 if not).
- Caption text: use straight quotes, not curly.
