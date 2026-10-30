# RULES — the only binding rulebook for JJ puppy videos (28 Oct 2026)

**Precedence:** the scheduled task prompt → this file → everything else. Every other doc in this repo
(BUILD-METHOD, GROWTH-STRATEGY, WINNERS-BLUEPRINT, SHORT-FORMAT, QA-CHECKLIST, PRODUCTION-LOG, SCRIPTS,
VIRAL-BLUEPRINT, DIALOGUE-AD-TEMPLATE) is background and history. Where it disagrees with this file,
this file wins. If you find a conflict, follow this file and note the conflict in your final report.

Why this exists: the pipeline kept failing in ways its own checks claimed to cover. 25 Oct: scripts that
made no sense, self-scored 9/10. 28 Oct: a video published MUTE (its music was a phone-recorded clip,
most likely a commercial song the platforms muted), and #fyp got into captions despite being banned.
Every check that relied on "remember to" failed at least once. So the rules below are enforced by code
wherever possible, and the code exits non-zero on failure. **Never schedule after a non-zero exit. Never
edit a threshold, approval or record to make something pass.**

## 1. Posting facts

- Metricool brand **7128333** ("JJ - Cute puppies"): Instagram @jj_lovemonkey + Facebook (one post),
  TikTok @jjthelovemonkey (separate post). Timezone Europe/London.
- Slots: **10:00 and 18:00 UK daily**. IG+FB post at :05, TikTok at :14.
- A slot is FILLED if any non-draft JJ post that isn't an #ad post exists within ±30 minutes of 10:00
  or 18:00. Drafts don't count. Never stack a post into a filled slot. Probe getScheduledPosts one day
  per call.
- Compute the UTC offset with Python `zoneinfo.ZoneInfo('Europe/London')` for each date. Never
  hard-code it (BST ended 25 Oct 2026; it starts again on **28 Mar 2027**).
- Posts are created with **autoPublish true, draft false**. There is NO manual approval step, so the
  gates below are the only protection.
- Never delete posts. Never re-enable drafts, including the 25 Oct batch (#67-71) and the 18 Oct trait
  videos. Ads are paused: no #ad videos. Never use vidIQ at all (Chuby, 30 Oct: no connecting it, no credits).

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

## 4. Scripts: written by one agent, judged by another

1. Write drafts per docs/REVIEWER.md "Writing rules".
2. Spawn a separate reviewer subagent with the prompt template in docs/REVIEWER.md, filled with fresh
   Metricool numbers. Save its full raw answer verbatim to `reviews/<YYYY-MM-DD>.md` and commit it.
3. Apply its line fixes word for word. You may not overrule a FAIL or a CUT, or change its scores.
4. Record every reviewed script in `docs/approvals.json` (`python3 approval.py hash <slug>` gives the
   sha256 once the spec exists). Use the REVIEWER's numbers. Status is "approved" only if the reviewer
   said SHIP or SHIP WITH FIXES **and** the average of **Reach, Engagement and Relatability** is ≥ **7.0**
   **and** P(beats 1,000 IG views) ≥ **35%**. Otherwise "hold" or "cut".
   - 30 Oct 2026, Chuby: the page's goal right now is **growing the audience, not converting**. So
     Conversion is no longer scored or averaged. (It was usually the lowest score and was dragging
     scripts under the bar.) The P(1k) floor went from 40% to 35% so the channel doesn't go silent.
   - The floor went from Chuby's earlier 8.5 to 7.0 on 30 Oct. The independent reviewer marks far harder
     than the old self-scores: nothing it has scored has reached 8.5, and the 1,000+ view winners would
     likely score 7-8 under it.
   - A script can be held for a stated non-score reason (e.g. brand risk), even if it passes the numbers.
5. `make_video.py` and `make_short.py` refuse to build (exit) unless the spec's exact text matches an
   approved entry. Editing a line after review changes the hash, so it has to be reviewed again.
6. Ship fewer videos rather than weaker ones. An empty slot is better than a bad post.

## 5. Build → gate → schedule (in this order, no skipping)

1. Build. The builder writes `<file>.qa.json` and `<file>.music.json`.
2. Long format: `python3 voicecheck.py <slug>` must exit 0. It writes `<slug>.voicecheck.json`.
3. Look at the frames: `work/<slug>/sheet.png` for shorts, `work/<slug>/*_f0..5.png` for long. Check
   for clipped puppies, text over faces, and props that don't match the line. Code can't enforce this,
   so name the frames you looked at in the log entry.
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
