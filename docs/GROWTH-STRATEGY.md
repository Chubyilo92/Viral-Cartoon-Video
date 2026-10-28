# Growth & conversion strategy: JJ puppy videos

> **28 Oct 2026: background/history only.** The binding rules are in `docs/RULES.md`. Where this file disagrees with RULES.md, RULES.md wins. (Known stale here: anything saying the music is the user's clips, that posts are drafts the owner approves, that the writer scores its own scripts, or that topics can be invented freely.)


The videos must drive conversions, not just views. This is the rulebook for
every script written for this series — read it before writing a new one.

## Why this format at all

Modeled on a viral TikTok template ("when a girl loves you..."), which works
because it takes behaviors a viewer might feel judged for (clinginess,
jealousy, nagging, overthinking) and reframes each one as proof of love. That
reframe is what makes people send it to their partner. The reusable template:

> When [a girl / a boy / your partner] loves you, [behaviour].
> [Behaviour that looks bad], but not because [bad reading]. It's because
> [loving reading]. (×3–4 beats)
> But if they [opposite sign]… maybe [warning].
> Because when [they] truly love, [closing line].

The puppies swap in for the human couple in the original — same structure,
original wording and visuals, cuter and safer to run at volume.

## What's actually driving reach (real data, checked 2026-10-11)

Checked via `getAnalyticsDataByMetrics` (Instagram Reels connector:
comments/interactions/likes/reach/saved/shares/views/avgWatchTime/
reelsViewRate/reposts; TikTok posts connector: views/likes/comments/shares)
for every organic post live so far, 5–10 Oct 2026 — the only real
performance data this series has. Small sample (11 IG Reels, 1 week), so
treat this as a direction to lean into, not a locked law, and re-check it
once more weeks of data exist.

**The anomaly the user asked about**: "A loyal man" (script #5, Fidelity) —
1,481 IG views / 1,335 reach, 33 shares, 31 saves, **5 reposts**, 150
interactions (11.2% of reach — by far the highest interaction rate of any
post). Its near-twin, "When a hurt girl loves you" (script #4, Trust) —
1,753 views / 1,593 reach (the single highest reach of the batch), but a
lower interaction rate (6.3% of reach) and no reposts. Both posted the same
day, Tue 6 Oct (10:00 and 18:00) — every other day's posts, before and
since, have stayed under 900 reach, so there's a real possibility this was
partly a one-time new-account distribution boost (IG testing a brand-new
profile's reach early on) rather than something repeatable by content
choice alone. That confound can't be fully separated out from a week of
data.

What *does* hold up independent of that one day, ranked across all 11 real
posts: the next-best performers, in order, are "quiet after a fight" (#11,
conflict/vulnerability) and "the first year living together" (#14,
emotionally real rather than cute) — while the weakest are "bad texter"
(#10), "long distance" (#13) and "priority" (#6) — lighter, quirkier,
lower-stakes topics. This confirms, with real numbers now, the direction
flagged qualitatively in `PRODUCTION-LOG.md`'s 2026-10-07 batch note:
**vulnerability and specificity beat purely sweet/quirky framing.**

One sharper, more specific pattern sits inside that: the two best-of-all
topics (trust-after-being-hurt, fidelity/not-being-treated-as-an-option)
aren't just "vulnerable" in general — they're both **reassurance against a
named relational fear** (will I be believed, will I be cheated on/treated
as replaceable), the kind of topic a viewer sends to their actual partner
as a direct, personal affirmation ("you do this for me") rather than just
a relatable feeling. "A loyal man"'s unusually high share/save/repost rate
in particular lines up with its caption's explicit personal send-line
("Send this to the girl who deserves it") — though that alone isn't a
clean signal: "When she says 'I'm fine'" also has a personal send-line
("send this to the one who keeps asking") and still underperformed, likely
because it was the account's very first-ever post, before any distribution
history existed. So caption wording is a secondary lever at best, not the
main driver.

**Integrating this into topic selection**: when picking or inventing the
next batch's topics (see the candidate list at the bottom of
`SCRIPTS.md`), weight "does this resolve a specific, named relational fear
the viewer could send straight to their partner as reassurance" above
generic vulnerability and well above a cute/quirky behavioral trait —
fidelity/trust/abandonment-coded topics first, "how they show care in a
specific situation" topics (protector, workaholic, peacemaker, steady one,
etc.) next, pure habit/quirk topics (bad texter, overthinker, priority,
long distance) last unless the drafted-list well runs dry. Keep writing
the mid-video share line as a specific, personal send-to-someone line (per
the rule below) — it's necessary even if this data can't yet prove it's
sufficient on its own.

**Also worth tracking, not yet acted on**: pull shares/saves/reposts
specifically in every future batch's analytics check, not just reach/views
— "A loyal man" shows a video can have *less* reach than another and still
be the stronger pick by that measure, and reposts/shares are the most
likely lever IG's own algorithm rewards with more organic reach. If a
future batch's reach stays flat below ~900 for several weeks running (i.e.
the 6 Oct spike really was a one-off new-account boost, not a repeatable
content effect), that's worth surfacing to the user as a separate question
about paid boosting or posting-cadence changes, not something script
rewrites alone can fix.

## Delivery rules (apply to every video)

- **Voice**: warm, mature, calm male narrator (Kokoro `am_michael`, see
  BUILD-METHOD.md §4).
- **Only the captions-burned-in version is delivered** — no separate clean
  cut.
- **A soft original music bed plays under the voice at all times** — generated by
  `pipeline/original_music.py`, never silence, never a user-supplied or downloaded track (those get
  muted by the platforms — see BUILD-METHOD §5, 28 Oct correction).
- **He supplies no assets at all** for this series — scripts, visuals, voice
  and music are all produced end to end; the only footage he supplies
  anywhere in the wider operation is app-screen recordings for the separate
  Mike Gomorrah series (see `/docs/BRANDS.md`).

## The mid-video share line

Placed right after the video's warmest beat, just before the closing
warning/payoff — the moment the viewer feels "that's us."

- **For sweet/warm topics**: prompt a *send*, not a *tag* — sending feels like
  a small romantic gesture and converts better than "tag your partner."
  - _"If you've found someone like this… send it to them. Don't say
    anything. Just send it."_
  - _"If he does this… tag him. Let him know it doesn't go unnoticed."_
- **For conflict/vulnerable topics** (trust, "I'm fine", going quiet): let the
  sender explain themselves without a real conversation —
  _"If you're the one who goes quiet… send this to the one who keeps
  asking."_
- **Never** put a share line on a video whose mood doesn't support it —
  skip it rather than force one.

## The ending — platform-specific, and it must be a kept promise

A generic "check us out" ending does not convert. The ending must promise
something specific and then the profile must actually deliver it.

### Instagram: quiz ending

The puppy account's Instagram bio links to CoupleIn's real quizzes, so the
promise resolves immediately:

- Love Language quiz: `https://www.coupleinapp.com/quiz/love-language`
- Attachment Style quiz: `https://www.coupleinapp.com/quiz/attachment-style`

Rules for picking which quiz:
- Sweet / love-language-flavoured videos → Love Language quiz.
- Trust / overthinking / jealousy videos → Attachment Style quiz.
- Conflict-resolution videos → the 5-minute-fight-fix feature page instead
  of a quiz (`https://www.coupleinapp.com/solve-fights-in-5-minutes`).

**Current standing simplification (from 2026-09-28 batch onward): use the
Love Language quiz on every Instagram video regardless of topic**, to keep
the weekly batch simple while the pipeline is new. Revert to the per-topic
rule above whenever asked.

End-card pattern (visual: the two pups looking at a phone showing a mock quiz
result screen):

> "[Callback to 2–3 specific moments just shown]… Every [boy/girl] shows
> love in his/her own way. Want to know which one? There's a 60-second test
> in our bio. Take it together… and see if he/she knows yours."

Example used on "When a boy loves you": _"The last bite. The tea. Sitting
close when it's hard. Every boy shows love in his own way… Want to know his?
There's a 60-second test in our bio. Take it together… and see if he knows
yours."_

**Important**: the puppy account and the quiz-hosting/CoupleIn account are
*different profiles*. That's fine — the quiz lives on the *website*
(coupleinapp.com), so any profile's bio can link to it. Never send viewers
from the puppy video to "our other account" directly — that's a second hop
and kills conversion. A cross-link between the two profiles, if wanted,
belongs in bio text or a pinned comment, never the voiceover/end-card.

### TikTok: follow ending (goal: reach 1,000 followers)

TikTok's bio link doesn't unlock until 1,000 followers, so the TikTok ending
asks for a follow instead of a click — but never as a bare "help me get to
1k," which reads as begging.

**Active as of the 2026-09-28 batch: ending #1 below, on every TikTok video.**
Starting counter: 4 followers (set 2026-09-28). **Update the on-screen count
every batch** to the real current TikTok follower number — check it via
Metricool analytics each run rather than trusting a stale value here or in
`PRODUCTION-LOG.md`.

**1. The puppies ask, with a live follower counter on screen** (the one in
active use — a visible near-complete goal pulls people to finish it):
> "We're two little pups trying to find a thousand people who love like
> this… If this made you think of someone… follow us. We'll keep making them
> for you."
> On-screen counter text: "🐾 [current count] / 1,000" — update the number
> each batch from the real count.

**2. Follow-for-next-part** (best posted in boy/girl script pairs — e.g. "when
a boy loves you" followed next day by "when a girl loves you"):
> "Tomorrow… when a girl loves you. Follow so you don't miss it."

Two more endings discussed but not chosen for regular rotation:
- Honest creator voice ("I make these every day, on my own… a follow helps
  me keep going") — sincere, but use sparingly (~1 in 4) or it wears out.
- Identity framing ("Follow if you love like this… and you're done
  pretending you're fine") — ties the follow to the viewer's self-image;
  second clause changes per video topic.

## Posting

- Target cadence once fully ramped: 2/day on each of Instagram and TikTok.
- **Current standing process (updated 2026-09-28): two batches per week, 7
  new videos each — 14 videos/week total**, each built and QA'd in one
  session, scheduled with **autoPublish true** (NOT drafts — corrected 28 Oct 2026; there is no manual approval step, which is why `pipeline/preflight.py` must pass) across the
  coming days on the JJ account (Metricool
  brand id `7128333`, IG `@jj_lovemonkey`, TikTok `@jjthelovemonkey`). The
  user taps publish per post in Metricool — Claude's job is to make sure only
  videos that pass `docs/QA-CHECKLIST.md` ever reach that stage, so the
  user's review is a glance, not a line-by-line check.
- Puppy videos post on a separate profile from the CoupleIn quiz-content
  profile (see `/docs/BRANDS.md` for the full account map).
- See `/docs/PRODUCTION-LOG.md` for what's been made, the script rotation
  order, and the current standing settings (batch size, endings, publish
  mode) — check it before every batch run since these can change.

## Quality bar

Every script and video is checked against a 10/10 bar before delivery: does
it look/sound as strong as the best videos in this genre, scored on how well
it would actually download, engage, convert and feel relatable — not just
against this series' own earlier posts. Weak ideas get cut rather than
shipped.
