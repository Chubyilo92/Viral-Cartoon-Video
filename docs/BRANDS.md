# Where this fits in the wider operation

This repo documents one content type (the JJ puppy cartoon videos) inside a
three-brand social media operation. Quick map so a fresh session knows where
else to look:

| Brand | What it is | Posts to | Media/asset repo |
|---|---|---|---|
| **CoupleIn** | The relationship app itself (coupleinapp.com) — carousels + daily quiz videos | Instagram, TikTok, Facebook, Threads, Pinterest | `Coupleinsocial` |
| **JJ** (`@jj_lovemonkey` on Instagram) | Cute two-puppy narrated relationship videos — **this repo** | Instagram, TikTok, Facebook | `JJCutecouple` |
| **Mike Gomorrah** (`@mikegomorrah` IG / `@fionaloveslove` TikTok) | Text-message/chat-drama video series, built from user-supplied screen recordings | Instagram, TikTok, Facebook | `Mikegomo`; pipeline docs in `Viral-Chat-Video` |

All scheduling for all three brands goes through Metricool.

**The JJ puppy account is a separate profile from the one hosting the
CoupleIn quiz content** — see `/docs/GROWTH-STRATEGY.md` for why that still
lets the Instagram ending work (the quiz lives on the coupleinapp.com
website, not on a specific Instagram profile).

Full per-account posting cadence, ad-concept libraries, and the carousel
production system live in the other repos/chat memory for those content
types — not duplicated here to avoid drift between copies. This repo owns
only the puppy-video build method, growth strategy and script library.
