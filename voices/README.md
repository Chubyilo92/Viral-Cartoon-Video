# JJ puppy voices

The two character voices for the JJ dialogue videos (no narrator).

| Pup | Kokoro voice | Speed | Pitch (rubberband, formant shifted) | Sample |
|---|---|---|---|---|
| Boy (blue bandana) | `am_puck` | 0.9 | ×1.36 | `sample-boy.mp3` |
| Girl (pink bow) | `af_heart` | 0.9 | ×1.24 | `sample-girl.mp3` |

- Settings live in `voices.json`; `pipeline/dialogue.py` uses the same values — change both together.
- One-off line: `python3 voices/say.py boy|girl "text" out.wav`
- Free and local: no vidIQ / paid TTS credits.
