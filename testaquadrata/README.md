# TestaQuadrata — method package (for the course)

Italian faceless zombie series (Rome). Still images + human voice + a data-driven canvas renderer. No AI video.

Read in this order:
1. `docs/01-CREATION-RULES.md` — pipeline, golden editing rules, image/character rules, continuity, sound, reels, QA loop.
2. `docs/02-POST-EDIT-RULES.md` — everything that happens after the first render: the five laws, window re-render + splice, swapping a character across a finished episode, fix recipes, final checklist, real feedback examples.
3. `docs/03-COURSE-NOTES.md` — what to teach, in what order, and the mistakes that cost the most time.

Code (reference implementations used for Ep1–Ep3):
- `code/engine/` — `engine.html` (canvas renderer), `render.js` (Playwright frame renderer), `mkplan.py` (Ep3 shot plan = worked example), `prep_ov3.py` (clean plate + word-reveal layers), `splice_clips.py` (window splice), `patch_head_swap.py` (character swap by tracking).
- `code/audio/` — `mix_ep3.py` (mix example), `sfxlib.py` (synthesised SFX), `day_sting.wav`.
- `code/social/build_social.py` — reel wrapper.
- `code/characters/README_PERSONAGGI.md` — exact Gemini prompt text per character.
- `samples/` — reference stills.

Paths inside the scripts point at the original working machine (`/home/claude/tq/...`); adjust when reusing.
Finished videos and full-size images are not stored here.
