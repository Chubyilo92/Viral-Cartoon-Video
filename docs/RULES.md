# RULES — the only binding rulebook for JJ puppy videos (28 Oct 2026, updated 1 Nov and 6 Nov 2026)

**Precedence:** the scheduled task prompt → this file → everything else. Every other doc in this repo
(BUILD-METHOD, GROWTH-STRATEGY, SHORT-FORMAT, QA-CHECKLIST, PRODUCTION-LOG, SCRIPTS, VIRAL-BLUEPRINT,
DIALOGUE-AD-TEMPLATE) is background and history. Where it disagrees with this file, this file wins. If
you find a conflict, follow this file and note the conflict in your final report. **One named exception,
added 9 Nov 2026:** `docs/WINNERS-BLUEPRINT.md` is binding, not background, specifically for what counts
as "approved" in §4 — this file defers to it there on purpose, it is not a conflict to flag.

Why this exists: the pipeline kept failing in ways its own checks claimed to cover. 25 Oct: scripts that
made no sense, self-scored 9/10. 28 Oct: a video published MUTE (its music was a phone-recorded clip,
most likely a commercial song the platforms muted), and #fyp got into captions despite being banned.
Every check that relied on "remember to" failed at least once. So the rules below are enforced by code
wherever possible, and the code exits non-zero on failure. **Never schedule after a non-zero exit. Never
edit a threshold, approval or record to make something pass.**

## 1. Posting facts

- Metricool brand **7128333** ("JJ - Cute puppies"): Instagram @jj_lovemonkey + Facebook (one post),
  TikTok @jjthelovemonkey (separate post). Timezone Europe/London.
- Slots: **10:00 and 18:00 UK daily**. IG+FB post at :05, TikTok at :14. Filled up to 7 days ahead (§5b).
- A slot is FILLED if any non-draft JJ post that isn't an #ad post exists within ±30 minutes of 10:00
  or 18:00. Drafts don't count. Never stack a post into a filled slot. Probe getScheduledPosts one day
  per call.
- Compute the UTC offset with Python `zoneinfo.ZoneInfo('Europe/London')` for each date. Never
  hard-code it (BST ended 25 Oct 2026; it starts again on **28 Mar 2027**).
- Posts are created with **autoPublish true, draft false**. There is NO manual approval step, so the
  gates below are the only protection.
- Never delete posts. Never re-enable drafts, including the 25 Oct batch (#67-71) and the 18 Oct trait
  videos. Ads are paused: no #ad videos.
- **vidIQ (2 Nov 2026, Chuby: "you can use it for inspiration for what works, but you must pass it by me
  first"):** vidIQ may be used for inspiration and research only (niche outliers, what 10K-100K videos do).
  **Every use needs Chuby's OK first**: say which call you want to make, why, and what it costs in
  credits, then wait for his yes. Never call vidIQ without that approval, including "free" or
  balance-check calls.
  - **Scheduled/unattended runs never call vidIQ**, because nobody is there to approve it. If vidIQ data
    would help, put the proposed call(s), the reason and the credit cost in the run's push notification
    for Chuby to approve next time he's in a session.
  - This replaces the 30 Oct total ban and the 1 Nov "use whenever connected" wording.

## 2. Formats

- **Long** (narrated, 35-75 s, two cuts: `-instagram` with the quiz end card, `-tiktok` with the follow
  counter). Built with `make_video.py`. This is the default.
- **Short** (music only, 15-25 s): **STOPPED 30 Oct 2026.** Chuby objected that the videos had no
  spoken words, and the no-narrator test had never been put to him. Every JJ video is narrated. Don't
  build or schedule music-only videos unless he asks for them again.
- Captions: max 5 hashtags, never #fyp #foryou #foryoupage #viral #trending #explore.
  - Long IG/FB caption mentions the 60-sec love-language test in the bio.
  - Long TikTok caption: no links, no "bio".
  - Short (all platforms): the follow positioning line from SHORT-FORMAT.md, no quiz mention.

## 3. Music

Only `pipeline/original_music.py` beds (synthesized in code). The phone-recorded clips were deleted on
28 Oct. Never add user-supplied, downloaded or "trending" audio files. Every builder writes
`<file>.music.json`, and preflight fails if it's missing or doesn't point at an `original*.wav`.

## 4. Scripts: written by one agent, judged by another (rebuilt from a clean slate, 9 Nov 2026)

**9 Nov 2026, Chuby: stop patching the approval rules — rebuild them from nothing but what the 5 real
best-performing scripts actually are.** Every rule in this section is either (a) something directly
true of all 5 scripts in `docs/WINNERS-BLUEPRINT.md`, cited there line by line, or (b) a bare mechanical
safeguard (fresh reviewer, hash lock, phonemizer check) that has nothing to do with judging content.
Nothing else survives — no invented scoring rubric, no twist-family taxonomy, no accumulated "lessons"
from past batches. If `docs/WINNERS-BLUEPRINT.md` and this section ever disagree on what a script should
contain, WINNERS-BLUEPRINT.md is correct and this section is stale; fix this section to match it.

1. Read `docs/WINNERS-BLUEPRINT.md` in full before writing anything. It is the only definition of what a
   script should be.
2. Write ~10 BRAND-NEW drafts, each matching the template in WINNERS-BLUEPRINT.md. Vary which real
   behaviour/trait each draft is about — don't write 10 drafts that are the same trait reworded.
3. Spawn a separate reviewer subagent (never the writer grading itself — this is the one process rule
   with its own incident history: the 25 Oct batch shipped nonsense lines after self-scoring 9/10) with
   the prompt template in `docs/REVIEWER.md`, filled with the current top-5 table from
   `docs/WINNERS-BLUEPRINT.md` pulled fresh. Each round uses a FRESH reviewer that has not seen earlier
   rounds. Save its full raw answer verbatim to `reviews/<YYYY-MM-DD>.md` and commit it.
4. Apply its line fixes word for word. You may not overrule a FAIL or a CUT.
5. **The floor:** a script is "approved" only if the reviewer names a specific one of the 5 real
   scripts in WINNERS-BLUEPRINT.md and says this draft matches or beats it, line-structure for
   line-structure (same kind of hook, same kind of concrete beats, a "But..." turn as real as theirs, a
   "Because..." closer as quotable as theirs). No number replaces this judgment — there is no rubric to
   fill in, no score to average. If the reviewer can't honestly make that comparison, it's "hold" or
   "cut." A script can still be held for a stated non-score reason (e.g. brand risk) even if it matches.
6. `make_video.py` and `make_short.py` refuse to build (exit) unless the spec's exact text matches an
   approved entry in `docs/approvals.json`. Editing a line after review changes the hash, so it has to
   be reviewed again.
7. **Read-aloud check BEFORE review:** run every line through Kokoro's phonemizer
   (`Kokoro(...).tokenizer.phonemize(line,'en-us')`). No emoji in BODY_LINES (Kokoro reads the emoji's
   name), no distinctions that exist only in spelling ("ok" vs "okay" sound identical). If a reviewed
   line fails this, send that line back to the same reviewer for a replacement; never edit it yourself.
8. Ship fewer videos rather than weaker ones. An empty slot is never the finished state of a run — it's
   a reason to write another round, not a result to report. The floor in step 5 never moves to force a
   fill. If slots are still empty after a round, immediately write a new round of ~10 BRAND-NEW scripts
   (not resubmissions — a "hold" script is reused only if substantively rewritten, never resent as-is)
   and send them to a fresh reviewer. Do this up to 3 rounds per run, in the same run, before stopping —
   write round 2, then round 3, and only then report whatever is still open.
9. Scheduling spacing: don't schedule two approved scripts about the same specific behaviour within 7
   days of each other — check this by reading them, not by a label. Never push an approved video more
   than 7 days out to satisfy this; if it can't fit, it goes to the backlog (approved, unscheduled) for
   the next run to use first.

## 5. Build → gate → schedule (in this order, no skipping)

1. Build. The builder writes `<file>.qa.json` and `<file>.music.json`.
2. Long format: `python3 voicecheck.py <slug>` must exit 0. It writes `<slug>.voicecheck.json`.
   Save a render: before the full build, TTS each BODY_LINE alone and run voicecheck's `check()` on it
   (exec voicecheck.py up to `rows = [`). Set LINE_SPEED for any flagged line up front (1 Nov: 4 of 5
   scripts had one flagged line; fixes were 0.8-1.05). IG_LINE/TT_LINE must not contain abbreviations with
   full stops ("a.m."): the caption splitter breaks them into "the seven a" / "m".
3. Look at the frames: `work/<slug>/sheet.png` for shorts, `work/<slug>/*_f0..5.png` for long. Check
   for clipped puppies, text over faces, and props that don't match the line. Code can't enforce this,
   so name the frames you looked at in the log entry.
3a. **Final-file gate (6 Nov 2026):** `python3 watchcheck.py <slug> out/<file>.mp4` for EACH cut must
   exit 0. It runs speech recognition on the finished mix (every line ≥ 45% words recognised: catches a
   line drowned by music or garbled) and fails if caption/label text touches the frame edge. Added after
   three of the 4 Nov videos shipped with a label off the left edge, a puppy cut off at the right edge, and a
   blue block over the girl's face that read as a face mask — all passed every earlier gate.
3b. **Structure review (6 Nov 2026):** send `work/<slug>/watch_sheet.png` (one frame per line, in order)
   plus the BODY_LINES to a FRESH reviewer subagent that has not seen the script before. It must answer
   PASS/FAIL to each: (1) watched in order with sound, does the story make sense without the script?
   (2) does every scene's picture match its line (props make sense: a sink for washing up, not a block
   on the face)? (3) is anything over a face or cut off? (4) does line 6 land as a turn and line 7 pay it
   off? (5) does the narration sound natural (from voicecheck.json: no rising statement endings, pace
   1.8-3.6 w/s)? Any FAIL → fix the scene code (layout/props never need re-approval) and rebuild, or, if
   the TEXT is the problem, send the line back to a reviewer. Save its answer to reviews/<date>.md.
   Captions now auto-shrink to fit (caption() in the anim html), so long chunks can't run off the edge.
4. `python3 preflight.py --file <mp4> --platform instagram|tiktok --format long|short --slug <slug>
   --caption-file <txt>` must exit 0. Run it once per post.
5. Push the mp4 to JJCutecouple. Run preflight again with `--url <commit-pinned raw URL>`. That run
   downloads the file, checks it's byte-identical to the one that passed, and writes `<file>.pass.json`.
6. createScheduledPost with exactly that URL and exactly the caption file's text.
7. Read the post back (getScheduledPosts for that day) and check: caption identical to the caption
   file, no banned tags, right providers, right time, draft false, one media item. If anything is off,
   fix it with updateScheduledPost, or draft the post and report it.
8. Log every scheduled post in PRODUCTION-LOG.md with slug, slot, file sha256 (from .pass.json) and
   the reviewer's scores.

Anything made outside the scheduled task (tests, one-offs, manual fixes) goes through the same steps
1-8. No exceptions.

## 5b. Gap filling — the channel must not go silent (6 Nov 2026, Chuby)

- The batch task runs **every day at 06:12 UK** and looks **7 days ahead** (today's 10:00 included).
  If every slot in that window is filled, it stops after the check (cheap). Otherwise it fills them.
- Order of supply: (1) approved-but-unscheduled backlog, (2) new rounds of ~10 drafts, up to 3 rounds —
  **use all 3 in the same run if that's what it takes; do not stop at round 1 and report empty slots as
  the outcome (8 Nov 2026, Chuby).**
- **If a video fails any gate** (voicecheck, watchcheck, structure review, preflight) and can't be fixed
  in the run, it is NOT scheduled, and its slot counts as still empty: the run immediately writes a
  replacement in the next round. Only after 3 rounds have genuinely been tried in one run does a
  leftover gap wait for the next day's run — that fallback is not a substitute for trying rounds 2 and 3
  today.
- Approved scripts that don't fit the 7-day window go to the backlog (status "approved", unscheduled),
  so the next run starts with stock instead of from zero.
- Never fill a gap by lowering a floor, skipping a gate or re-using a script that failed.

## 6. What can't be checked from here (say so, don't pretend)

- **The copy Metricool hosts.** Metricool re-hosts every file at static.metricool.com, which this
  environment's network blocks, so nothing can confirm the hosted copy is identical to ours. The
  protection is step 5 (the file we hand over is verified).
- **Platform muting after publish.** A muted reel still shows as PUBLISHED. The only protection is
  original music (section 3).
- **Whether a video will go viral.** Near-identical videos on this account have landed at 124 and
  1,754 views. Scores are probabilities. Never promise results.

## 7. Reporting

One push notification per run with: posts scheduled (slot + slug), scripts cut or held and why, the
REVIEWER's score table (not yours), lines the reviewer rewrote, voicecheck/preflight failures and fixes,
any rule conflicts you found, the TikTok follower count, and the last batch's real numbers (IG views,
average watch time, shares). Say plainly if nothing could be shipped.
