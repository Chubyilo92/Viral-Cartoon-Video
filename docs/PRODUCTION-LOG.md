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
| 2026-09-30 | 9. Overthinker | Love Language quiz (Words of Affirmation) | Follow counter (3/1,000) | Scheduled Thu 8 Oct 10:00 |
| 2026-09-30 | 10. Bad texter | Love Language quiz (Acts of Service) | Follow counter (3/1,000) | Scheduled Thu 8 Oct 18:00 |
| 2026-09-30 | 11. Quiet after a fight | Love Language quiz (Quality Time) | Follow counter (3/1,000) | Scheduled Fri 9 Oct 10:00 |
| 2026-09-30 | 12. Tired/hangry | Love Language quiz (Physical Touch) | Follow counter (3/1,000) | Scheduled Fri 9 Oct 18:00 |
| 2026-09-30 | 13. Long distance | Love Language quiz (Quality Time) | Follow counter (3/1,000) | Scheduled Sat 10 Oct 10:00 |
| 2026-09-30 | 14. First year living together | Love Language quiz (Acts of Service) | Follow counter (3/1,000) | Scheduled Sat 10 Oct 18:00 |
| 2026-09-30 | 15. Guarded heart | Love Language quiz (Physical Touch) | Follow counter (3/1,000) | Scheduled Sun 11 Oct 10:00 |
| 2026-10-01 | 16. When a girl loves you | Love Language quiz (Acts of Service) | Follow counter (3/1,000) | Scheduled Sun 11 Oct 18:00 (IG+FB Reel, TikTok) |
| 2026-10-01 | 17. When he says 'I'm fine' | Love Language quiz (Quality Time) | Follow counter (3/1,000) | Scheduled Mon 12 Oct 10:00 |
| 2026-10-01 | 18. When an introvert loves you | Love Language quiz (Quality Time) | Follow counter (3/1,000) | Scheduled Mon 12 Oct 18:00 |
| 2026-10-01 | 19. Tiny things | Love Language quiz (Acts of Service) | Follow counter (3/1,000) | Scheduled Tue 13 Oct 10:00 |
| 2026-10-01 | 20. Stubborn love | Love Language quiz (Acts of Service) | Follow counter (3/1,000) | Scheduled Tue 13 Oct 18:00 |
| 2026-10-01 | 21. Forgives easily (hook rewritten pre-build — see SCRIPTS.md) | Love Language quiz (Words of Affirmation) | Follow counter (3/1,000) | Scheduled Wed 14 Oct 10:00 |
| 2026-10-01 | 22. The planner | Love Language quiz (Acts of Service) | Follow counter (3/1,000) | Scheduled Wed 14 Oct 18:00 |

## Batch of 2026-10-01 — 10/10 scoring (downloads / engagement / conversion / relatability)

Metricool analytics for brand 7128333 were pulled first (`getAnalyticsDataByMetrics`,
TKEV02/06/01 evolution, 24 Sep - 1 Oct): ~150-320 views/day and 1-8
interactions/day, all from the two videos delivered directly to the user
before the Metricool scheduling pipeline existed — too thin to extract a
hook/pacing bar (no JJ post has gone through the actual posting pipeline yet;
the first is scheduled for 5 Oct). Scored against the `GROWTH-STRATEGY.md`
template and the established 10/10 rubric instead. TikTok follower count
checked via TKEV07: 3 (unchanged since 2026-09-30).

| # | Script | Downloads | Engagement | Conversion | Relatability | Avg | Notes |
|---|---|---|---|---|---|---|---|
| 16 | When a girl loves you | 9 | 9 | 9 | 9 | 9.0 | Mirrors #1's proven hook/structure for a new (male) audience |
| 17 | When he says I'm fine | 9 | 9 | 9 | 9 | 9.0 | Mirrors #2; everyday-stress angle, distinct from #11 |
| 18 | When an introvert loves you | 9 | 9 | 9 | 9 | 9.0 | |
| 19 | Tiny things | 9 | 9 | 9 | 10 | 9.25 | Most universal hook in the batch |
| 20 | Stubborn love | 9 | 9 | 9 | 9 | 9.0 | Comment-bait framing ("never said sorry, but—") |
| 21 | Forgives easily | 8 | 8 | 9 | 8.5 | 8.4 → 9.0 | **Weakest pre-build.** Hook was abstract ("when someone who forgives easily loves you...") and the share line had no urgency. Rewritten before building: opens on a sharper visual beat ("they cut you off mid-apology") and the share line now reads "send this to them, right now, before you forget." Re-scored 9/9/9/9 = 9.0 after rewrite; built from the rewritten version. |
| 22 | The planner | 9 | 9 | 9 | 9 | 9.0 | On-screen title pre-shortened per the title-length lesson below |

All 7 passed every mechanical check in `QA-CHECKLIST.md` on the first render
(no second pass needed): overlap gaps all ≥0.55s, durations 54.8-71.5s (all
within the 35-75s band — #21's IG cut at 71.5s is the longest in the batch,
still inside range), audio streams present and matched to video duration on
every file, and all 14 files 13.1-18.0MB (well under the 25MB cap, no
re-encode needed).

## Rotation order for future batches

Scripts 1, 2, 4, 5, 6, 8, 9-22 are now built. #7 (Kids) is still skipped — it
still needs a baby puppy prop added to `engine/puppy-engine.js`. The original
8-script seed list and its "Scaling beyond these 8" extension (16 topics) are
both now fully used. **Next batch**: invent fresh relationship-focused
topics per the standing approval in `docs/SCRIPTS.md` (10/10 bar, cut weak
ones) — see the "Scaling beyond these 22" candidate list at the bottom of
`SCRIPTS.md` (a competitive partner, someone who struggles to ask for help,
the "fixer" who can't just listen, opposites who balance each other, bad at
receiving compliments, or further gender/relationship-stage swaps), append
each script to `SCRIPTS.md` before building, and keep the 10/10 bar.

**Word-count lesson (2026-09-30): keep each script tight.** The renderer's
QA duration cap is 75s per cut. At Kokoro `am_michael` speed 0.9, roughly
0.39s of audio per word plus ~0.75s pad per scene. For 7 body lines + 1 end
line, that means body word count + end-line word count should stay under
~165 words total (body lines alone under ~145) to land the IG cut (the
longer of the two, because its end line is longest) comfortably under 75s.
Scripts 9 and 12–15 in this batch initially ran 76–90s and needed trimming
after the first render — write lean the first time instead of relying on a
second pass. **Confirmed again 2026-10-01**: all 7 new scripts (16-22) were
written to this budget and landed 54.8-71.5s on the first render with no
trimming needed.

**Title-length lesson (2026-10-01, carried over from script #22's first
draft): keep on-screen TITLEs under ~33 characters.** A longer title
overflows the caption pill at render width 1080px. Check this before the
first `preview.py` run, not after.

**Doc-vs-reality lesson (2026-10-01): a script isn't "Built" until the spec
file, the rendered/QA'd videos, and the Metricool post all exist.** An
earlier run on 2026-10-01 committed `SCRIPTS.md` text for #16-22 marked
"Built" and referencing spec file paths that didn't exist yet, then stopped
before writing `pipeline/specs/*.py` or rendering anything. A later run the
same day caught this by checking `pipeline/specs/` and the `JJCutecouple`
`videos/` listing against what `SCRIPTS.md` claimed, rather than trusting the
doc text alone. Future batches: verify the actual spec files and rendered
output exist (not just the docs) before assuming a script is built.

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
  since it goes stale). Still 3 as of the 2026-10-01 batch (checked via
  TKEV07 — no JJ posts have published yet; the first is 5 Oct).
- **Publish mode (updated 2026-09-29): auto-publish** (`autoPublish:true`, `draft:false`) on Metricool JJ brand 7128333, tz Europe/London. **2 videos/day at 10:00 and 18:00** (TikTok best slots). Each video = one IG+Facebook Reel post (IG cut) + one TikTok post (TikTok cut), same time. **First JJ post: Mon 5 Oct 2026; never schedule earlier.** Each batch starts the day after the last already-scheduled JJ post (check Metricool first — probe day by day, 1-3 days per `getScheduledPosts` call, to avoid oversized responses).
- **Pipeline**: all builds use `pipeline/` (see `pipeline/README.md`). Built: scripts 1, 2, 4, 5, 6, 8 (batch of 2026-09-29, scheduled 5-7 Oct); scripts 9-15 (batch of 2026-09-30, scheduled 8-11 Oct); scripts 16-22 (batch of 2026-10-01, scheduled 11-14 Oct). Still unbuilt: 7 (Kids, needs baby pup prop). Next batch pulls further topics from the "Scaling beyond these 22" list / invents new ones. Music = the 3 user-supplied sounds (rotated), not synthesized.
- TikTok follower count on 2026-10-01: 3 (checked via Metricool analytics, metric TKEV07 — unchanged since 2026-09-30; no JJ posts have gone live yet to move it).
- **Last scheduled JJ day as of the 2026-10-01 batch: Wed 14 Oct 2026 (10:00 and 18:00 — both slots filled).** Next batch starts Thu 15 Oct 2026, 10:00.
- **Media hosting**: finished MP4s are pushed to the public `JJCutecouple`
  repo and referenced by their `raw.githubusercontent.com` URL as Metricool's
  media source (Metricool's post tools require a public media URL — there's
  no direct file-upload path from this pipeline).

## Ads / promos (outside the regular weekly rotation)

One-off direct-response ads for CoupleIn itself, narrated by the puppies but
built and scheduled outside the normal script rotation/cadence above — don't
count these toward the "7 videos" batch math or the script numbering in
`docs/SCRIPTS.md`.

| Date | What | Platform | Status |
|---|---|---|---|
| 2026-09-30 | "The fight you keep having" — painkiller angle selling CoupleIn's 5-minute fight fix feature, mocked-up phone UI (no real screenshots — coupleinapp.com is blocked by this session's network policy), custom download-CTA end card instead of the usual quiz/follow-counter ending, custom cover image | IG+FB Reel + TikTok (same creative both cuts — no platform-specific ending needed for a direct-response ad) | Scheduled as a 3rd post on 6 Oct 2026, 20:00 Europe/London (that day already had 2 organic posts at 10:00/18:00) |
| 2026-10-01 | "We almost broke up over this" - last biscuit (Resolve; VIRAL-BLUEPRINT original, `biscuit2.py`), two-voice dialogue, app unnamed in story | IG+FB Reel + TikTok (same file) | Scheduled Tue 20 Oct 2026 20:00 Europe/London (auto-publish) |
| 2026-10-01 | "We almost broke up over this" - kindness machine (browny points, `kindness.py`) | IG+FB Reel + TikTok (same file) | Scheduled Wed 21 Oct 2026 20:00 Europe/London (auto-publish) |

**Build tool**: `pipeline/build_ad.py <slug>` (not `make_video.py` — ads need
a custom end card/CTA rather than the quiz or follow-counter ending, so they
skip `J.end_ig`/`J.end_tt` entirely). Spec needs `TITLE`, `BODY_LINES`,
`SCENES`, `END_LINE` (CTA voice line), `END_SCENE_JS` (built via `_kit.S`
like any other scene), optional `PRELUDE`/`MUSIC_N`. Produces
`<slug>-instagram.mp4` and `<slug>-tiktok.mp4` as identical files. See
`pipeline/specs/ad_couplein_fightfix.py` for a worked example, including the
`adTag()`/`appBadge()` PRELUDE helpers for an on-screen "Ad" disclosure tag
and app-store-style badges.
