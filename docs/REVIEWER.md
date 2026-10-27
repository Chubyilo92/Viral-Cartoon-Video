# Independent script review (mandatory before any JJ script is built)

Added 27 Oct 2026 after the 25 Oct batch shipped lines that made no sense ("When he finally meets
your parents, the nerves are the whole point") and the writer scored its own work 9.0. The writer is
never allowed to grade its own scripts again.

## How it works

1. The writer drafts scripts into a file (one `## slug` section each, numbered lines).
2. The writer spawns a **separate subagent** (Agent tool, general-purpose, opus) that has NOT seen the
   writer's notes or scores. It gets: the real winners/flops table from `WINNERS-BLUEPRINT.md` (script
   text + IG views), the known-bad examples below, and the draft file. Use the prompt in
   §"Reviewer prompt" verbatim, filling in the current data.
3. The reviewer paraphrases every line in plain words. Any line it can't paraphrase cleanly is FAIL and
   it writes the replacement. It scores each script and gives SHIP / SHIP WITH FIXES / CUT.
4. The writer applies the reviewer's line fixes word-for-word (or cuts the script). The writer may NOT
   overrule a FAIL or a CUT, and may NOT raise the reviewer's score. Reported scores = reviewer's scores.
5. Only scripts the reviewer marks SHIP / SHIP WITH FIXES and scores ≥40% "beats 1,000 IG views" get built.

## Known-bad examples (always include in the reviewer prompt)

- "When he finally meets your parents, the nerves are the whole point." (point of what?)
- "That's not moving in, that's just visiting longer." / "That's not distance, that's hesitation." /
  "That's not love, that's convenience" (said about someone who goes quiet when you're grieving).
  The "that's not X, that's Y" slot produces nonsense when filled mechanically. Only allowed when X and
  Y both literally describe the same behaviour (e.g. "that's not mystery, that's her not being sure").
- "When she's the one... you stop looking." (abstract, nothing to see, 117 views)
- Abstract thesis openers: "the exhaustion either breaks a couple or quietly rebuilds them".

## What the data actually says (27 Oct 2026, all JJ videos since 5 Oct)

- IG is bimodal: ~1,200 views or ~130, almost nothing between. 11 of ~45 hit the ~1,200 tier. Best ever
  1,754. Nothing has gone viral (10k+) yet.
- Near-identical clones split: "girl who's been hurt" 1,754 vs "girl who's been cheated on" 124;
  "a loyal man" 1,521 vs "a loyal woman" 125. Script text sets the floor; it does not decide the result.
  Never claim a script "will" hit. Honest ceiling for a strong script is ~35-50%.
- Measurable separator: winners average 10-22s watch time and 4-33 shares; flops 4-9s and 0-1 shares.
  So line 1-2 (stop + keep watching) and "would I send this to my partner" are what to optimise.
- Personality-trait hooks: 0 for ~20. Never use them.
- TikTok views are flat 225-250 per video regardless of content (≈700 early Oct): a distribution
  problem, not a content signal. Don't use TikTok views to judge scripts.

## Writing rules that come out of this

1. Line 1 names a big audience (a girl / a boy / a man / a woman) AND a specific behaviour people
   recognise from their own life, then flips it in the same or next sentence ("she'll ask the same
   question twice. Not because she thinks you're lying. It's because the last one did.").
2. Every beat is one picture you could draw, in plain words a 19-year-old reads once and gets.
3. The warning line must be a real turn that follows from the beats, readable alone.
4. No abstract thesis lines, no "that's not X, that's Y" fill-ins, no therapy words.
5. After 72h: ≥1,000 IG views → make 2 more in that exact shape. <200 → don't repeat that shape.

## Reviewer prompt

See the 27 Oct 2026 entry in PRODUCTION-LOG.md for the exact prompt used on the first reviewed batch
(copy it, update the winners/flops data with current numbers, point it at the new draft file).
