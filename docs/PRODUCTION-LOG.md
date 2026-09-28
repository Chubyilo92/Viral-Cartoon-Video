# Production log

Tracks what's been made and scheduled, so the weekly batch task knows what to
build next without a human in the loop. Update this file at the end of every
batch run — it's the only state a fresh session needs to avoid repeating a
script or an ending.

## Format

One row per video: date built, script (from `docs/SCRIPTS.md`), platform +
ending used, Metricool post status.

## Log

| Date | Script | IG ending | TikTok ending | Status |
|---|---|---|---|---|
| 2026-09-26 | 1. When a boy loves you | Love Language quiz | — (built before TikTok ending existed) | Delivered to user directly, not scheduled |
| 2026-09-27 | 2. When she says 'I'm fine' | Love Language quiz (per batch default; topic would normally suggest Attachment Style) | — (built before TikTok ending existed) | Delivered to user directly, not scheduled |

## Rotation order for future batches

Pull the next unused script from `docs/SCRIPTS.md` §"Drafted, not yet built"
in this order (skip any already logged above as built for the platform in
question): 4 (Trust), 5 (Fidelity), 6 (Prioritisation), 7 (Kids — needs a baby
puppy prop added to `engine/puppy-engine.js` first), 8 (Love languages).
Once all are used, start again with a boy/girl swap of #1 and #2, then a
relationship-stage variant (long distance, first year living together, etc.
— see the scaling list at the bottom of `docs/SCRIPTS.md`).

## Standing settings (current)

- **6 new videos per weekly batch.**
- **Instagram ending**: Love Language quiz, on every video, regardless of
  topic (simplification for the initial batches — the per-topic
  Attachment-Style override in `docs/GROWTH-STRATEGY.md` can be reinstated
  later).
- **TikTok ending**: the follow-ask with a live counter — "We're two little
  pups trying to find a thousand people who love like this… If this made you
  think of someone… follow us. We'll keep making them for you." + on-screen
  "🐾 [count] / 1,000". **Update `[count]` each batch to the real current
  TikTok follower count** (starting count: 4, set 2026-09-28 — check the real
  number each run via Metricool analytics rather than trusting this file,
  since it goes stale).
- **Publish mode: scheduled as Metricool drafts, not auto-published.** The
  user reviews/taps publish in the Metricool app; Claude's job is to make
  sure only videos that pass QA reach that stage at all — see
  `docs/QA-CHECKLIST.md`.
- **Media hosting**: finished MP4s are pushed to the public `JJCutecouple`
  repo and referenced by their `raw.githubusercontent.com` URL as Metricool's
  media source (Metricool's post tools require a public media URL — there's
  no direct file-upload path from this pipeline).
