# Growth & conversion strategy: JJ puppy videos

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

## Delivery rules (apply to every video)

- **Voice**: warm, mature, calm male narrator (Kokoro `am_michael`, see
  BUILD-METHOD.md §4).
- **Only the captions-burned-in version is delivered** — no separate clean
  cut.
- **A soft original music bed plays under the voice at all times**
  (`/music/generate_music_bed.py`), never silence.
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
  session, scheduled as **Metricool drafts** (not auto-published) across the
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
