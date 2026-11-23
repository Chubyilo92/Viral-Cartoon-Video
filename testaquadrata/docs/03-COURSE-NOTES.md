# Course notes — how to teach the TestaQuadrata method

## Module order
1. The format: why still images + voice work; fear-first scripts; survival logic as the hook; cliffhanger per reel.
2. Characters & sets in Gemini: reference sheets, "exactly as in the sheet above", reusable empty backgrounds, fallback images.
3. Voice-led editing: transcribe the creator's recording, time every shot to utterances, text appears only when spoken.
4. The renderer: plan.json fields, camera moves, overlays, HUD counters, day cards.
5. Sound design: beds, spot SFX, ducking, measuring (≥15 dB under speech), day sting.
6. Reels: cut at cliffhanger pauses, follow prompt at 45 %, end card.
7. QA loop and **post-edit** (the module that saves the most money): fix master once, window re-render, splice, derive the rest.
8. Delivery and branding: neutral umbrella brand, platform-safe content, naming across episodes.

## Mistakes that cost the most (teach these explicitly)
- Editing to the script instead of the recorded voice.
- Revealing text before the voice says it.
- Cross-fading a replacement (old face flashes) instead of replacing pixels; fixing videos one by one instead of master-first.
- Static images held too long; images that match the words but not the story (wrong door, wrong person, body-less hands).
- Loud effects over speech; judging levels by ear instead of measuring.
- Deleting a good render before the splice is verified; running out of disk.
- Claiming "ready" without viewing the fixed frames.
- Gemini: unverified spelling on walls, character drift without the sheet, stalls without retry/fallback.

## Why this is cheap
No video model. Cost = Gemini images (≈120 per episode) + one human voice recording + local rendering.
