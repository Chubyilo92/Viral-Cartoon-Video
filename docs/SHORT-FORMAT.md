# SHORT FORMAT — JJ share-first test (set 26 Oct 2026)

**Status: TEST.** Three videos are scheduled. If the test passes (criteria below), this becomes the
**default JJ organic format** and the long narrated format (WINNERS-BLUEPRINT.md) becomes the exception.
Until the verdict, keep running the long format in every slot that isn't a test slot.

## Why this exists (the diagnosis)

JJ's problem is **followers, not views**. Through 25 Oct the Instagram account had ~25,000 reel views
in three weeks and **9 followers** (about 0.3 follows per 1,000 views). For an account this size, 1,000+
views per winner is not bad — people watch, then don't follow, share or save much.

Compared with breakout cartoon-couple reels found on vidIQ in Oct 2026, JJ differs on almost every element:

| Element | Breakouts | JJ long format |
|---|---|---|
| Length | 20–24s | 48–70s (avg watch ~10s, so most never reach the share line or ending) |
| Ending | ends on the emotional/comic peak, no ask | 15s quiz pitch / follow counter (reads as an ad, kills rewatch) |
| Voice | first-person, sendable *as the viewer's own message* ("thank you for the way you love me") or "this is us" | third-person advice ("a loyal man…"), often turns into a red flag that can feel accusing to the partner who receives it |
| Twist | a beat you don't see coming (cinder block, kicked out of bed, role reversal) | sincere throughout |
| Audio | music only (or SFX) | narrator over music |
| Text | one persistent hook line + short beat text | captions chunked from the narration |

References (all 5–45x their account median): @dinklygame "thank you for loving me" (5M, 24s, love-note
slideshow); @capiandcoco "POV: we never go to bed angry" (1.4M, 20s, wordless bed vignette);
@the.benny.bella "Driving home, not knowing which version of your princess…" (593K on 5.6K followers,
22s, one persistent hook + rapid vignettes); @ailove.art "When a man truly loves you…" (1.6M).

## The format rules

1. **18–22 seconds.** 5–6 beats of ~3s. Nothing over 24s.
2. **No narrator.** One of Chuby's three music beds only (`MUSIC_N`), faded out at the end.
3. **One persistent hook line at the top for the whole video** — it must make sense on its own and
   state the premise ("when he asks if I want anything 🍟", "we never go to bed angry 🐾").
4. **One short plain sentence per beat** at the bottom (≤ 2 lines). Read-aloud test still applies.
5. **Sendable as the viewer's own message** — first person ("I", "you", "me") or "this is us".
   The person who receives it must feel *loved or laughed with*, never accused. No red-flag turn.
6. **A twist beat** in the last third (unexpected but obvious in hindsight). No twist = not a 10.
7. **End on the peak.** No quiz, no follow counter, no end card. The last frame is the payoff.
8. **One ask per post, in the caption only — the follow positioning line** (below). The quiz link
   lives in the bio, not in posts.
9. Captions sit in the Reels safe zone (hook at y≈300, beat text at y≈1440 on 1080×1920).

### The follow positioning line (caption)
> Your feed is full of reasons to doubt them. This page is the reminder of why you stayed 🤍 Follow if you want more of that.

TikTok short version: "Follow for the reminders of why you stayed 🤍". The idea: most couple content
online is red flags/cheating/suspicion that divides couples; JJ is the page that keeps you together.
Don't use generic "follow for more". Use the same line on all three test posts so it is testable.

## Build

`pipeline/make_short.py` + `pipeline/specs/_short.py` (props: fries, cookie, popcorn, bed/blanket,
snowflakes, big rain cloud). Spec = `HOOK`, `BEATS=[(caption, draw_js, seconds)]`, optional `MUSIC_N`.

```
python3 make_short.py <slug> preview   # contact sheet: work/<slug>/sheet.png — LOOK at it
python3 make_short.py <slug>           # out/<slug>.mp4 (one cut for IG, FB and TikTok)
```
Needs the same setup as pipeline/README.md minus Kokoro (no voice). Check every frame on the sheet:
both faces visible, props match the line, nothing hidden behind the caption.

## The test (scheduled 26 Oct 2026, brand 7128333)

| Slot | Video | Mechanism tested | Score at build |
|---|---|---|---|
| Wed 28 Oct 10:05 IG/FB, 10:14 TT | `short_fries` — "when he asks if I want anything" → "the 'one'" → he pulls out a second bag he got for her | relatable comedy + green-flag twist | 9/10 |
| Wed 28 Oct 18:05 IG/FB, 18:14 TT | `short_ps` — "I don't say it enough… so the puppies will" → 4 love-note beats → "p.s. I ate your fries" | love note the viewer sends as their own + joke twist | 9/10 |
| Sat 31 Oct 10:05 IG/FB, 10:14 TT | `short_bed` — "we never go to bed angry" → 3 failed attempts → he gives up → *she* cuddles him | wordless "this is us" + role-reversal twist | 8.5/10 |

Media: github.com/Chubyilo92/JJCutecouple/tree/main/videos/short-format. The long-format posts that
were in the Wednesday slots (grief_together, closes_distance) moved to Fri 30 Oct, same times.

## Pass / fail (judge 72h after each post; pull IGRE + IGEV via Metricool)

Baselines are JJ's own long-format winners (5–24 Oct).

| Metric | Long-format baseline | Pass mark |
|---|---|---|
| IG avg watch time (IGRE24) | ~10s of ~55s (~18%) | ≥ 9s of ~19s (≥ 45%) |
| Shares ÷ views (IGRE21/IGRE23) | 0.4–2.3% on winners, ~0% on the rest | ≥ 2% |
| Saves ÷ views (IGRE12/IGRE23) | 0.5–1% | ≥ 1% |
| Follows per 1,000 views (IGEV43 on the day vs reel views) | ~0.3 | ≥ 3 |
| Views | ~120 or ~1,200 (bimodal) | ≥ 1,000 on 2 of 3 |
| TikTok shares (TKPO10) | 0–3 | ≥ 5 |

**Verdict:** if 2 of 3 videos pass the watch-time and share marks AND follows per 1,000 views
clearly beats ~0.3, the short format becomes the default for JJ (two posts a day, 10:00/18:00, same as
now). If watch time passes but follows don't, keep the format and test a different follow line. If
neither passes, go back to the long winners format and record why here.

Whichever mechanism wins (comedy+green flag / love note / wordless rule) gets made in gender-flipped
and situation variants first, before inventing new mechanisms — same rule as WINNERS-BLUEPRINT.md.

## Results
(fill in after 31 Oct + 72h)
