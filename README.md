# Viral Cartoon Video — JJ puppy video pipeline

The complete, reproducible method for the JJ two-puppy narrated relationship
video series: a hand-written canvas renderer (no AI video generation), a free
local voice, and an original synthesized music bed. Built so a brand-new
Claude session — or a human — can pick this up cold, with no memory of any
prior conversation.

**Making a marketing video with the puppies? Start with [`docs/DIALOGUE-AD-TEMPLATE.md`](docs/DIALOGUE-AD-TEMPLATE.md)** — the reusable template (what makes a 10, what flexes, how to adapt). Code: `pipeline/adkit.py` + `pipeline/specs/_template_ad.py`. Rule history: `docs/VIRAL-BLUEPRINT.md`.

**Start here, in order:**

1. [`docs/BUILD-METHOD.md`](docs/BUILD-METHOD.md) — how the renderer works,
   how to render a video, how the voice and music are generated, and a
   documented bug/fix worth not repeating.
2. [`docs/GROWTH-STRATEGY.md`](docs/GROWTH-STRATEGY.md) — the mid-video share
   line, the platform-specific endings (Instagram quiz vs. TikTok follow
   ask), and delivery rules.
3. [`docs/SCRIPTS.md`](docs/SCRIPTS.md) — the script library: 2 finished,
   6 drafted and ready to build, plus scaling ideas.
4. [`docs/BRANDS.md`](docs/BRANDS.md) — where this fits among the other
   social accounts/repos.
5. [`docs/PRODUCTION-LOG.md`](docs/PRODUCTION-LOG.md) — what's been made,
   what's next in rotation, and the current standing batch settings. **Read
   this first if you're running a batch** — it's the state file.
6. [`docs/QA-CHECKLIST.md`](docs/QA-CHECKLIST.md) — mechanical checks to run
   on every video before it's scheduled, since Claude can't watch/listen to
   verify a video by eye or ear.

## Repo layout

```
engine/
  puppy-engine.js         the shared drawing engine (rig, props, backgrounds)
music/
  generate_music_bed.py   synthesizes the original background music, from scratch
videos/
  when-a-boy-loves-you/   finished video #1 — source + render script + voice lines
  when-she-says-im-fine/  finished video #2 — source + render script + voice lines
docs/
  BUILD-METHOD.md
  GROWTH-STRATEGY.md
  SCRIPTS.md
  BRANDS.md
```

Each video folder is self-contained: the `.html` file has the engine pasted
in plus that video's own `SCENES`, the `render*.js` drives headless Chromium
to encode it, and `tts/` has the per-line voice-generation script and the
resulting line durations. Rendered video/audio files themselves are **not**
stored here (see BUILD-METHOD.md §7) — this repo is the method, not a media
archive.

## Quickest path to a new video

1. Write a script (or take one from `docs/SCRIPTS.md`) and check it against
   `docs/GROWTH-STRATEGY.md` (share line, platform ending).
2. Copy an existing video folder as a starting point.
3. Write new `SCENES` reusing `pup()` and the existing props; add new props
   to `engine/puppy-engine.js` only if genuinely new.
4. Generate voice lines (`tts/lines.py` pattern), get real durations, retime
   scenes by **regex substitution in file order** (see the documented bug —
   never match-and-replace on the stringified old duration).
5. Render both frame streams, mix in the voice + music bed, mux, verify by
   sampling frames and checking line-to-line audio gaps.
6. Deliver only the captions-burned-in version.
