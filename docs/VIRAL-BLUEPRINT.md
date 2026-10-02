# Viral blueprint — JJ puppy marketing videos

**Status: the standard for every puppy video that markets CoupleIn.** Built from
"the last biscuit" (`pipeline/specs/biscuit2.py`, rendered 2026-10-01), the
video the user rated *really good* after five earlier versions were rejected as
"good on paper, not viral". Read this before writing any new marketing script.

## The core rule

A script that is well structured is **not** a 10/10. Virality needs the
**unexpected**: a hook that shocks, a middle that keeps re-hooking, and a twist
nobody predicts. Score every script on real viral potential (likes, comments,
shares, downloads), not on structure. Report the score every time.

## Format

- **Dialogue, no narrator.** The two pups *are* the couple and talk to each
  other. Boy = `am_puck` ×1.36 pitch, girl = `af_heart` ×1.24 (see `voices/`).
- One spoken line per scene, short lines (≈1.5–3s each), captions tinted by
  speaker (boy blue, girl pink), mouths animate only on the speaker.
- Target 40–50s. Hard ceiling 55s. Cut soft lines before cutting the fight.
- Built with `pipeline/dialogue.py <slug>` — see BUILD-METHOD.md §8.

## Act 1 — The nasty hook (0–15s)

- **The first line lands at 0.2s and it is brutal.** No set-up, no title card
  pause. Real things couples say in their worst fights:
  - "I can't stand you anymore!"
  - "Good! Because I can't stand your mom!"
  - "Don't you DARE talk about my mom!"
  - "You know what? Maybe we need a break."
  - "Fine. You were never good enough for me anyway."
  - "Then I'm done." (he walks out of frame)
- **Every insult is answered with something just as bad** — both sides escalate,
  so the viewer can't pick a side (that's what drives comments).
- Hit the emotional triggers: mothers/family, "a break", worth ("never good
  enough"), leaving.
- Visuals: red-tinted room, screen shake on the speaker, rainclouds stacking up
  one per line, pups at larger scale (1.3–1.4) and angry brows.
- Title pill is a curiosity hook, not a description: **"we almost broke up over
  this"**.

## The open loop (runs under Act 1)

- A label under the captions from the very first second: **"it started over
  something stupid 👇"**. The viewer now needs to know *what* — they stay for
  the answer. The answer is held back until Act 3.
- As someone storms out, swap it for a re-hook: **"wait for it 👀"**.

## Act 2 — The break and the stakes (15–30s)

- **Time cut + mood shift**: "1 HOUR LATER", dark blue room, one pup alone,
  one beat of regret ("…Why did I say that?").
- The other comes back, softer: **"Babe… remember why we got the app?"**
- **Never name the app in the dialogue or on in-story phone screens.** It's
  "the app". This keeps it feeling like a real couple, not an ad. The phone UI
  shows only a heart + the feature name ("Resolve").
- **Put the relationship on the line**: "For moments like this. **If it doesn't
  help… we break up.**" Then a persistent **"last try 💔"** label stays on
  screen until it's resolved. Live stakes = the viewer has to see the outcome.

## Act 3 — The feature, with a failure (30–45s)

- Show the actual mechanic in one line ("You talk, I repeat it back.") with a
  phone mock of the feature, plus top chips for each step ("🗣️ SHE SPEAKS",
  "👂 HE REPEATS").
- **Pay off the open loop**: the real cause comes out and it's tiny and
  relatable — "You ate the last biscuit. And you didn't even ask." Show the
  object big on screen with the label "the something stupid".
- **The first attempt fails**: he repeats it back wrong ("What I heard is… you
  hate me."), she snaps ("That is NOT what I said!"), the red flashes back —
  a mid-video jolt that nearly re-ignites the fight. This proves *why* the
  feature matters instead of claiming it.
- Second try works and names the real feeling underneath ("…and you felt
  forgotten."), label flips to **"it worked 💗"**.

## Act 4 — Solution + twist (45–50s)

- **A concrete, cute solution** from the one who messed up: "Next time, I
  promise not to eat the last biscuit" — and he pulls out a brand-new packet.
- **End on a laugh twist**: "…You had a spare packet this whole time?!" →
  hug, hearts.

## End card

- This is the only place the brand appears: "CoupleIn · link in bio" pill +
  phone with the app logo and "start free".
- Spoken line generalises the story to the viewer: "Every couple fights over
  something stupid. This is how we fix ours. Link in bio!"

- **Ending line must match the feature's message**, not one generic line for every video:
  fights (Resolve) → "Every couple fights over something stupid. This is how we fix ours.";
  browny points / gestures → "A relationship full of kindness will overcome the small fights. This is how we turn ours into a kindness machine."

## Adapting the blueprint to a different feature

Acts 1–2 (nasty hook, open loop, walk-out, "remember why we got the app?",
live stakes) stay the same for every feature. Acts 3–4 must be rebuilt around
**what that feature actually does** — don't reuse fight/Resolve language
("ROUND 2", "repeat it back", "it worked") on a non-Resolve video.

| | Resolve (conflict) | Browny points / gestures (kindness) |
|---|---|---|
| Real problem | not hearing each other | effort nobody sees / feeling unappreciated |
| Feature fails once | wrong repeat-back ("you hate me") | his points read **0** — "you never log anything!" |
| Feature works | right repeat-back names the feeling | he logs what he already does and the points climb on screen |
| Mid-twist | — | the hidden kindness is revealed ("YOU make my tea? I thought it just appeared") |
| Something stupid | last biscuit | she made herself a tea and not him |
| Solution | promise + spare packet | spend the points on a gesture ("warm brownies, baked by you") |
| Twist | "you had a spare packet this whole time?!" | "I made them before the fight… I was going to throw them at you." (one speaker, one line) |
| Loop close | — | he logs HER gesture: "+10 points… for not throwing them" — kindness flows both ways |
| Labels | "last try 💔" → "it worked 💗" | "nice things = points 💗", "last try 💔" → "kindness unlocked 💗" |
| Ending line | "Every couple fights over something stupid. This is how we fix ours." | "A relationship full of kindness will overcome the small fights. This is how we turn ours into a kindness machine." |

**Shared calendar + notifications (forgetting)** — real problem: important dates live in one
person's head. Forgotten thing: the anniversary ("he forgot something HUGE 👇"). Feature check: the
day is empty ("nothing today"). Twist: *she* was the one meant to put every important date in so he'd
get notified — "So… why are you mad at ME?" ("plot twist 👀"), she admits it. Solution: she adds it
("every year · notify him") and his phone pings instantly → he takes her out. Laugh button: a second
ping — his mum's birthday is tomorrow. Ending: "Love shouldn't depend on one person's memory. Put it
in once, and you both get reminded." Spec: `anniversary.py`.

**Shared calendar, variant 2 — double-booking** (`doublebook.py`): avoids the "why can't he just
remember?" objection the anniversary one invites. Hook: "This is why I never wanted to marry a short
guy!" / "I'm not short. You're just freakishly tall!" Cause: he booked a work meeting over the dinner
she set up with the neighbours. Check: "Check the app. If it's not there, I'll apologise." — it is.
It isn't there — only his work meeting is ("plot twist 👀"). She realises and apologises:
"…I was so sure I put it in." / "I'm sorry, babe. I shouldn't have called you short." / "And?" /
"…And you're the perfect height." Ending is one plain line: "This is what CoupleIn is for."
(v1 had a "his meeting is WITH Tom the neighbour" twist and a feature-pitch ending — the user
rejected both as too salesy. Keep twists human and the closing line short.)

**Framework, not wording.** Never reuse the same transition line across videos. "Babe… remember why
we got the app?" was one way in; others: "Okay. Let's just check the app." / "Check the app. If it's
not there, I'll apologise." / "Fine. It's in there. Then you're apologising." The stakes label can
change too ("last try 💔", "who's apologising? 👀").

**Post-end-card sting (anniversary v3):** after the end card, one more beat — her phone lights up with
a text from her ex ("Happy anniversary baby. I miss you 🥺"), he asks "Babe… who was that?", she says
"…No one." with "10k likes for part 2 👀" on screen. It pays off the opening "my ex was better" line and
ends on a cliffhanger built for comments, likes and a sequel. Use this kind of sting when the opening
fight mentions an ex or a third person.

**Standard ending for every dialogue ad (from 2026-10-02):** after the end card, a text lands on one
pup's phone from someone who threatens the couple (an ex, his mum…), the other asks "Babe… who was
that?", the owner says "…No one.", and a like goal for part 2 sits on screen ("1k / 5k / 10k likes for
part 2 👀"). Built with `pipeline/specs/sting.py` → `sting(owner, sender, line1, line2, goal)`.

Twist lines stay with one speaker — don't split a punchline across both pups.

## Checklist before building any new one

1. Is the first line shocking enough to stop a scroll on its own?
2. Does each insult get an equally bad reply?
3. Is there an open-loop label from second 1, answered later?
4. Is there a re-hook at the walk-out / time cut?
5. Are the stakes explicit and on screen ("if it doesn't help, we break up")?
6. Is the app unnamed everywhere except the end card?
7. Does the feature fail once before it works?
8. Is the real cause small, specific and relatable?
9. Is the solution concrete, and does the final line land a laugh/twist?
10. Under 55s? Score it honestly (viral potential) and report the score.

## Swappable parts for new videos

Keep the four-act skeleton; change the trigger and the feature:
- **Cause** ("the something stupid"): last biscuit, left the toilet seat up,
  liked his ex's photo, forgot the milk, took the good side of the bed.
- **Feature**: Resolve repeat-back (fights), shared calendar reminders
  (forgetting), browny points → gestures (feeling unappreciated), Grow
  together (repeated behaviour).
- **Solution prop**: new packet, a reminder set on the phone, a gesture
  redeemed, a calendar event added.

## Built from this blueprint

| Date | Video | Spec | Cause / fail / twist |
|---|---|---|---|
| 2026-10-01 | the last biscuit (the original) | `biscuit2.py` | last biscuit / "you hate me" / spare packet |
| 2026-10-01 | browny points (first test - superseded) | `brownies_bp.py` | she made tea for herself, not him (he makes hers daily) / his points read ZERO / she'd already baked the brownies - to throw at him |
| 2026-10-01 | kindness machine (browny points, feature-adapted) | `kindness.py` | tea for herself not him / his points read 0 / brownies were baked to throw at him / +10 for not throwing |
| 2026-10-02 | forgot the anniversary (shared calendar + notifications) | `anniversary.py` | anniversary / calendar day empty / she never added it - "why are you mad at ME?" / mum's birthday is tomorrow |
| 2026-10-02 | double-booked (shared calendar) | `doublebook.py` | short-guy insult / dinner vs work meeting / app proves her right / meeting is WITH the neighbour / Tom's paying |
