# Independent script review (mandatory before any JJ script is built)

The writer never grades its own scripts. A separate, fresh subagent reviews every draft against
`docs/WINNERS-BLUEPRINT.md` — the only definition of what a script should be — and nothing else decides
approval.

## How it works

1. The writer drafts scripts into a file (one `## slug` section each, numbered lines), each one written
   to match the template in `docs/WINNERS-BLUEPRINT.md`.
2. The writer spawns a **separate subagent** (Agent tool, general-purpose, opus) that has NOT seen the
   writer's notes. It gets the current top-5 table and full scripts from `WINNERS-BLUEPRINT.md`, pulled
   fresh from Metricool if that file is more than a few days old, and the draft file. Use the prompt in
   "Reviewer prompt" below verbatim, filling in the current data.
3. The reviewer paraphrases every line in plain words. Any line it can't paraphrase cleanly is FAIL and
   it writes the replacement. For each script it names the ONE top-5 script this draft is closest to and
   says plainly whether it MATCHES, BEATS, or FALLS SHORT of it, structurally, line for line — then
   gives SHIP / SHIP WITH FIXES / CUT.
4. The writer applies the reviewer's line fixes word-for-word (or cuts the script). The writer may NOT
   overrule a FAIL or a CUT, and may NOT change the reviewer's benchmark verdict.
5. Only scripts the reviewer marks SHIP / SHIP WITH FIXES **and** MATCHES or BEATS a named top-5 script
   are recorded as approved in `docs/approvals.json`. There is no numeric score to meet — the benchmark
   comparison in step 3 is the whole decision. Save the reviewer's raw answer to `reviews/<date>.md`.

## Reviewer prompt (template — fill the {braces}, send to a general-purpose subagent, model opus)

```
You are an independent, harsh script reviewer. Judgment only: do not edit files. You did not write
these scripts and you have no stake in them passing.

CONTEXT: A small Instagram/TikTok account posts ~50-second narrated cartoon videos of two puppies, a
calm male narrator reading a short script with captions on screen.

THE FLOOR: a script passes only if you can name which ONE of the 5 real scripts below it most
resembles and say honestly whether it MATCHES, BEATS, or FALLS SHORT of it — structurally, line for
line (same kind of hook, same kind of concrete beats, a "But..." turn as real as theirs, a
"Because..." closer as quotable as theirs). There is no numeric score. Only MATCHES or BEATS can carry
a SHIP or SHIP WITH FIXES verdict.

THE 5 REAL SCRIPTS THIS ACCOUNT HAS ACTUALLY HAD WORK (paste the full "The current top 5" section of
docs/WINNERS-BLUEPRINT.md here verbatim — all 5 full scripts and their real share numbers; re-pull from
Metricool first if that file is more than a few days old):
{paste WINNERS-BLUEPRINT.md's top-5 table and full scripts here}

TASK: review the scripts in {draft file path}. For EACH:
1. Line check: paraphrase every line in a few plain words. If a line is unclear, a riddle, a
   contradiction, or needs context to make sense, mark it FAIL and write a replacement.
2. Hook check: does line 1 name a broad, general subject and state one specific, concrete behaviour,
   the way all 5 real scripts do?
3. Beat check: are the middle lines concrete, physical, one-picture actions, all illustrating the SAME
   behaviour — not a chain of different claims?
4. Send check: is there a direct "If [condition]... send this to [a specific person]" line, the way 4
   of the 5 real scripts have one?
5. Turn check: does the turn line start with "But" and land as a real consequence (addressed to the
   viewer, or naming a specific future moment), not a restatement of the beats?
6. Closer check: does the last line start with "Because" and compress the whole trait into one short,
   standalone, quotable sentence?
7. Risk check: anything that could read as endorsing controlling or toxic behaviour, regardless of how
   it benchmarks structurally.
8. Benchmark verdict: name the ONE real script this is closest to. Say MATCHES / BEATS / FALLS SHORT OF
   it, and exactly why.
9. Verdict: SHIP / SHIP WITH FIXES (exact replacement lines) / CUT.
Finish with a ranking, the weakest named, and whether any script is clearly better than the current top
5. Use a compact table with the benchmark column from #7.
```
