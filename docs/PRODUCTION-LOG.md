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
| 2026-09-29 | 2. When she says 'I'm fine' | Love Language quiz (Quality Time) | Follow counter (3/1,000) | Scheduled Mon 5 Oct 10:00 (IG+FB Reel, TikTok) |
| 2026-09-29 | 1. When a boy loves you | Love Language quiz | Follow counter (3/1,000) | Scheduled Mon 5 Oct 18:00 |
| 2026-09-29 | 4. Trust (when a hurt girl loves you) | Love Language quiz | Follow counter (3/1,000) | Scheduled Tue 6 Oct 10:00 |
| 2026-09-29 | 5. Fidelity (a loyal man) | Love Language quiz | Follow counter (3/1,000) | Scheduled Tue 6 Oct 18:00 |
| 2026-09-29 | 6. Prioritisation | Love Language quiz | Follow counter (3/1,000) | Scheduled Wed 7 Oct 10:00 |
| 2026-09-29 | 8. Love languages | Love Language quiz | Follow counter (3/1,000) | Scheduled Wed 7 Oct 18:00 |

## Rotation order for future batches

Pull the next unused script from `docs/SCRIPTS.md` §"Drafted, not yet built"
in this order (skip any already logged above as built for the platform in
question): 4 (Trust), 5 (Fidelity), 6 (Prioritisation), 7 (Kids — needs a baby
puppy prop added to `engine/puppy-engine.js` first), 8 (Love languages).
Once all are used, start again with a boy/girl swap of #1 and #2, then a
relationship-stage variant (long distance, first year living together, etc.
— see the scaling list at the bottom of `docs/SCRIPTS.md`).

**Note (2026-09-28): at 14 videos/week, the 5 currently-drafted scripts
(4–8) only cover roughly one batch.** Once the drafted list runs dry mid-run,
each batch must write new scripts on the fly using the reusable template in
`docs/GROWTH-STRATEGY.md` §"Why this format at all" and the scaling/topic
list at the bottom of `docs/SCRIPTS.md`, then append them to `SCRIPTS.md`
before building, so the script library stays the source of truth rather than
scripts existing only inside a single batch run.

## Standing settings (current)

- **2 batches per week, 7 new videos per batch — 14 videos/week total**
  (updated 2026-09-28; was 6/week single batch before any batch had run).
  Batches run independently (each picks up wherever the rotation order left
  off, so a mid-week batch continues from the Sunday batch's last script,
  not from the top).
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
- **Publish mode (updated 2026-09-29): auto-publish** (`autoPublish:true`, `draft:false`) on Metricool JJ brand 7128333, tz Europe/London. **2 videos/day at 10:00 and 18:00** (TikTok best slots). Each video = one IG+Facebook Reel post (IG cut) + one TikTok post (TikTok cut), same time. **First JJ post: Mon 5 Oct 2026; never schedule earlier.** Each batch starts the day after the last already-scheduled JJ post (check Metricool first).
- **Pipeline**: all builds use `pipeline/` (see `pipeline/README.md`). Built: scripts 1, 2, 4, 5, 6, 8 (batch of 2026-09-29, scheduled 5-7 Oct). Still unbuilt: 7 (Kids, needs baby pup), then new scripts from the scaling list. Music = the 3 user-supplied sounds (rotated), not synthesized.
- TikTok follower count on 2026-09-29: 3.
- **Media hosting**: finished MP4s are pushed to the public `JJCutecouple`
  repo and referenced by their `raw.githubusercontent.com` URL as Metricool's
  media source (Metricool's post tools require a public media URL — there's
  no direct file-upload path from this pipeline).
