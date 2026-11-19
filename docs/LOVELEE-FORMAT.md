# LOVELEE FORMAT — CoupleIn app account quiz reels (from 19 Nov 2026)

For the **CoupleIn** Instagram + TikTok account (not JJ). A direct-sale format: the video ends on an App
Store card for CoupleIn, and it mainly pushes **Bond** (the daily question feature).
Source: https://www.instagram.com/lovelee_app/reels/ (294 reels scanned 19 Nov 2026, 40 over 20k views;
the 30 animated ones were remade — phone-demo videos and real-person "face + text" videos are ignored,
per Chuby).

## Rules (Chuby, 19 Nov 2026)

- Copy the background design and everything else from their animated videos, using the round JJ pups.
- Remake every animated reel over 20k views; exact source length (most are 18.219 s), exact hashtags.
- Silent video; the source's song is added in the app (most are lovelee's "original audio" → open the
  source reel → Use audio).
- Questions are new, Bond-style (first person, things the partner can actually answer).

## Template (all 30 sources use it)

`title 0–2.7 s` → `N question cards, 2.6 s each` (N = 5, or 8 for "rate me") → `end card to the exact length`.

Looks:
- **flat** — one pastel colour per card with a radial light in the middle; small label ("pick one. no
  "both"." / "questions for him"); progress hearts; big bold white Inter text with a soft shadow;
  optional answer pills (a/b) or A–D rows; both pups at the bottom with a reaction (sweat drop, !, ?,
  hearts, notes, popcorn, phone). `solo=True` = the girl alone holding her phone ("nosy" videos).
  End: pink card "find more questions for you two on CoupleIn / free on the app store" + App Store card.
- **beach** — sky, clouds, palms, sand, sea foam; wooden sign ("gf quiz"); white speech bubble in
  Pixelify Sans; A–D rows, a/b pills, or the 1–10 heart grid (`kind='rate'`). End: night sky + moon,
  "search CoupleIn on the app store for more questions", App Store card, and three real Bond screens
  (cropped from Missionandbond `images/bond-screens.png`, in `pipeline/assets/`).

The App Store card is drawn to look like the real one (search field typing "couplein", icon, name,
subtitle "Two selfies. One reveal.", blue GET). The app icon is the official CoupleIn logo hearts on a white tile (`pipeline/assets/couplein_icon.png`, made from Chuby's `couplein_logo.png`, 19 Nov 2026).

## Build

`python3 make_quiz.py <slug> [preview]` → `out/couplein/<slug>.mp4`. All 30 videos are data in
`pipeline/specs/lovelee_data.py` (source reel, views, exact length, song, hashtags, caption, questions).
Needs fonts Inter + Pixelify Sans (`fonts/`), and the shared chibi JJ rig in `specs/_dk.py`.
To make more: rescan lovelee_app for new animated reels over 20k, add a dict per video, render.

## Caption

`<their caption, lovelee swapped for CoupleIn>` + blank line + `more questions for you two on CoupleIn,
free on the app store 💕` + blank line + `<source hashtags>`. All 30 are in the Claude Sheet
"JJ week 1 – Dinkly remakes posting sheet", tab "CoupleIn quiz reels".
