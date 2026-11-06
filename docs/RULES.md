# RULES — the only binding rulebook for JJ puppy videos (28 Oct 2026, updated 1 Nov and 6 Nov 2026)

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

## 4. Scripts: written by one agent, judged by another

1. Write ~10 BRAND-NEW drafts per docs/REVIEWER.md "Writing rules" and the lessons in §4a below.
2. Spawn a separate reviewer subagent with the prompt template in docs/REVIEWER.md, filled with fresh
   Metricool numbers. Each round uses a FRESH reviewer that has not seen earlier rounds. Save its full raw answer verbatim to `reviews/<YYYY-MM-DD>.md` and commit it.
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
7. **Rounds (changed 1 Nov 2026, Chuby: "apply it automatically next time"):** if slots are still empty after
   a round, write a new round of ~10 BRAND-NEW scripts (not resubmissions) and send them to a fresh reviewer.
   Up to **3 rounds per run**. The floor never moves. On 1 Nov rounds 1-2 produced nothing (best 6.7) and
   round 3, written to the lessons below, produced 5 approvals (7.3-8.3).

### 4a. Script lessons (1 Nov 2026 — what separated round 3 from rounds 1-2)

- The behaviour must LOOK bad first (annoying, needy, cold, messy-in-a-bad-way), then be reframed as love.
  Sweet behaviours that already look good (fixing a chair, carrying a bag, keeping a ticket stub) flop and
  the reviewer scores them 4-6.
- Don't use one skeleton for every script. Vary the beats (not "She'll / She'll / She'll").
- Line 6 must be a real turn, never a restatement ("turns the light off… she's stopped waiting up" = FAIL).
  The strongest warnings turn on the VIEWER's behaviour ("if you keep saying 'I'm fine'…").
- **Twist variety (changed 6 Nov 2026, Chuby).** The old 7-day spacing pushed 4 approved videos weeks
  out (14 Nov-5 Dec) and left the week of 3-8 Nov with 7 empty slots, because all 5 approvals of 4 Nov
  shared one twist. New rule, enforced at WRITING time, not scheduling time:
  - Every round of ~10 drafts spans **at least 4 twist families, max 3 drafts per family**. Families:
    (a) withdrawal warning — "the day she stops X… she's not Y, she's Z";
    (b) only-with-you — she does it with you and never with anyone else, and why;
    (c) hidden reason — the annoying thing is secretly protecting/helping you;
    (d) viewer-turn — line 6 flips onto the viewer ("if you keep saying 'I'm fine'…");
    (e) mirror — he/she has quietly started doing it too, and what that means.
    Label each draft's family in the reviewer submission and in approvals.json (`"twist": "a"`).
  - Scheduling: same family **max once per calendar day and at least 48 h apart**. Never push an approved
    video more than 7 days out for spacing; if it can't fit within 7 days, it goes in the backlog
    (approved, unscheduled) for the next run to use first.
- **Read-aloud check BEFORE review:** run every line through Kokoro's phonemizer
  (`Kokoro(...).tokenizer.phonemize(line,'en-us')`). No emoji in BODY_LINES (Kokoro reads the emoji's name),
  no distinctions that exist only in spelling ("ok" vs "okay" sound identical). If a reviewed line fails
  this, send that line back to the same reviewer for a replacement and a re-score; never edit it yourself.

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
- Order of supply: (1) approved-but-unscheduled backlog, (2) new rounds of ~10 drafts, up to 3 rounds.
- **If a video fails any gate** (voicecheck, watchcheck, structure review, preflight) and can't be fixed
  in the run, it is NOT scheduled, and its slot counts as still empty: the run immediately writes a
  replacement in the next round. Whatever is still empty after the run is retried by the next day's
  run, so a gap gets at least one new attempt every day.
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
