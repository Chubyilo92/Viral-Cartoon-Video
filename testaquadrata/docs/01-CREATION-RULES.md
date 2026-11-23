# TestaQuadrata — Creation Rules (how an episode is made)

Source of truth for the course. Everything here was learned by shipping Episodes 1–3 (Parte 1–16).
Written so a new person (or a new Claude session) can make Episode 4+ cold. Edit rules that come *after* the
first render are in `02-POST-EDIT-RULES.md`.

## 0. What the product is
- Italian faceless zombie-survival series set in Rome, ~60 episodes planned. Hero = **Testa Quadrata (TS)**.
- No AI video. Every shot is a **still image** (Gemini) with push-ins/pans, overlays, counters and sound, drawn
  by a data-driven canvas renderer. The only "acting" is the human voice recording.
- Distribution: **full episode on YouTube**, the same episode **split into reels** for Instagram + TikTok.
  Reel numbers (Parte) continue across episodes: Ep1 = Parte 1–3, Ep2 = Parte 4–9, Ep3 = Parte 10–16.
- Next episode is released only when the channel reaches the agreed subscriber goal (Ep3 ends with a
  "TERZO EPISODIO A 50.000 ISCRITTI" style YouTube end card pointing at the subscribe button).
- Language of the product: **Italian**. Working language with the creator: **English only**.

## 1. Pipeline (per episode)
1. **Story/script (IT)**. Opens on fear, keeps the viewer on edge, explains any claim that isn't self-evident
   (e.g. *why* the power dies in 3 days). Teaches survival logic (water, food, time) — that is the addictive core.
   Every reel ends on a **massive cliffhanger**.
2. **Voice**. The creator records the narration himself (m4a). **His recording beats the script**: he may reword
   lines as a native speaker. Never time the edit to the script — time it to the audio.
3. **Transcribe** the voice with pause-segmentation (`sherpa-onnx whisper-medium`, Italian) → `asr.json`
   (utterances with start/end). This is the timing master.
4. **Images**. Generate every needed still in Gemini (see §3). Convert to 2752x1536 JPG, review each one by eye.
5. **Plan**. `mkplan.py` maps transcript times → shots, day cards, HUD counters → `plan.json`.
6. **Render**. `render.js` (Playwright + Chrome) draws `engine.html` frame by frame at 1920x1080, scales to 1280x720,
   30 fps, H.264 crf 18. ~120 shots for a 520 s episode.
7. **Mix**. `mix_epN.py`: voice master + beds + spot SFX + day sting (see §5). Mux with the silent video.
8. **QA loop** (see §8): rewatch, one correction pass, rewatch again, list only.
9. **Reels**. Cut the master at the pauses after each cliffhanger and wrap with `build_social.py`.
10. **Deliver**. Folders `PRONTI/Episodio N/{YouTube,Instagram,TikTok}`. Only deliver what is 100% checked.

## 2. The golden editing rules (set by the creator, apply to every episode)
1. **Edit in line with Episode 1** (same look, pacing, grade, card style).
2. **Written text appears only at the instant the voice reveals it — never before.** A word on a wall, a number
   on a counter, a name: it appears as the voice says it. Early text spoils the beat.
3. **Dynamic, not static.** If a passage would sit on one picture for long, make more images (different angles,
   close-ups of the object being described) and cut/push between them. Camera is never frozen.
4. **Scary sounds and effects at the right volume.** Loud hits only where *nobody is speaking*. Never cover
   the voice. Beds stay far under the voice.
5. **The voice is the master.** Never cut or retime the voice. Every shot starts on the sentence it illustrates.
6. **Images must match the actual story, not only the words.** Same recurring props, same characters, correct
   location, correct moment. (See §4 continuity.)
7. **Rewatch the full video yourself.** Do one correction pass. Rewatch again. In the second pass **only list
   what is still wrong — do not edit** — and give that list to the creator.
8. **Don't ask the creator to edit.** He gives the voice and the brief; the edit is delivered finished.

## 3. Image generation rules (Gemini hybrid method)
- Style block, always: *hand-drawn comic illustration, bold ink outlines, muted cinematic colours, no blood, no gore.*
- **Reusable empty backgrounds + character sheets**: generate each recurring location once as an empty set, and
  each recurring character as a reference sheet. Keep the sheets in the same Gemini chat and write
  *"exactly as in the <NAME> sheet above"*, pasting the exact text block from `code/characters/README_PERSONAGGI.md`.
- Characters (never drift):
  - **TS**: perfectly square cream-white head, two dot eyes, red-and-gold striped knitted scarf, thin stick limbs. No ponytail.
  - **Giulia** (TS's sister, alive): same style as TS + small black ponytail on a top corner, faded teal scarf, torn beach clothes, pink phone/case. Must look like TS.
  - **Van man / furgonista**: boxed square head, white surgical mask, blue cap, brown work gloves, grey zip jacket. Partner ("il socio") taller/thinner, charcoal jacket. (The boxed, masked design replaced an earlier round-headed one — keep it everywhere.)
  - **The dead**: sickly grey-green square heads, hollow eye sockets, torn grey clothes. **No blood.**
  - **Antonelli** (dead, caged in the old lift cage on TS's landing): elderly, dirty white shirt, brass key on a paper tag.
  - **Lucia** (alive, window across the piazza): grey bun, floral dress, waves a white cloth.
- **Brand is a neutral umbrella**: Testaquadrata will cover many series. Zombie art lives on the zombie account
  only; the general YouTube banner/avatar stays neutral (a normal, non-suffering TS).
- Social-platform safety: no overly realistic blood. Replace anything risky with something that gives the same effect.
- **Spell-check every wall/banner/sheet image by eye** (Gemini misspells). If text is wrong, regenerate or use a
  clean plate + animated overlay (§4 *Written reveals*).
- The hero's name when written (wall etc.) is **"TestaQ"**.
- Gemini ops notes: PRO plan has a rolling window plus a weekly limit; when it stalls, stop, reload, redefine helpers, retry; when the limit hits, resume at reset. Keep a fallback image per shot in `mkplan.py` (`FB` map) so a failed image never blocks a render — then list every fallback in the QA list.

## 4. Story-continuity rules (learned from Ep2 feedback — each one was a real complaint)
- **Show what the sentence is about.** "Tua sorella" → show **Giulia** (an old photo of TS with her), never Lucia's house. Repeat the photo on "È viva".
- **Recurring props are the same object every time.** The 3rd-floor door: hands under it → chalk circle drawn on it → circle wiped. Never substitute another door.
- **Antonelli is in the old lift cage on TS's landing**, never a random cage.
- **The portone** (street door of the palazzo) is the big ground-floor door seen from street/lobby — never a flat door.
- **No body-less props.** No floating hand holding a phone, no arm without a person. If a hand is shown it belongs to a visible person. (A hand "checking her pulse" must be on the right person — see post-edit rules.)
- **Reuse earlier-episode assets for call-backs** (Giulia's Ep1 phone message at the end of Ep2).
- **Written reveals**: text a character writes (spray on a wall, bedsheet, chalk) is *animated on* as the voice
  says it (handwriting reveal), and the final reveal word only lands on the climactic line (NON SCENDERE appears
  exactly when spoken, not minutes earlier). The cleanest method: generate/inpaint a **blank plate** (wall with no
  letters) and reveal the word onto it with a per-letter mask overlay (`prep_ov3.py`). Ghost letters in a "clean" plate
  mean you must regenerate the blank wall.
- **Counters**: any time the narration counts rations, food, water or time (e.g. the 72 hours), show an on-screen HUD counter *exactly when the voice says the number*; the number animates (`count`), unit set by `unit`, red for danger.
- **Day cards**: a dark `#16171d` card with big white "GIORNO n", gold underline, appears exactly when the voice says "giorno N" and the creator's own **day sting** sound plays at card start. Every new day in every story gets it.

## 5. Sound rules
- Voice = master track. Everything else is ducked **12 dB** under speech (day sting 20 dB).
- Beds per location at about **−46 dB** (room tone, cicadas, landing electrical hum, rain, night). **No wind hiss.**
- Spot SFX at −20…−44 dB with a room reverb matching the shot (`verb(x, room, wet)`). Cliffhanger = `sub_drop`; tension = riser; hits = boom/thud; use heartbeat/clock ticks for countdowns.
- **Loud only in gaps with no speech.** Verify by measurement: in every 1 s window of speech, effects ≥ 15 dB under the voice.
- Silence is a tool: drop the beds before a reveal and let a heartbeat carry it.
- Background bed level was raised **+13 %** after feedback ("background too strong" in some places, "too weak" in others → *measure*, don't guess). The **day-count sting is excluded** from any background raise — it is already loud.
- Final bus: `tanh` soft clip, then `loudnorm I=-16`.
- Loud noise cut at specific timestamps (e.g. a harsh noise at 45 s) — always ducked or moved into a speech gap.

## 6. Look
- Subtle film grain, soft vignette, gentle push-ins/pans only. No cuts shorter than ~2 s unless a beat needs it.
- Palette: warm gold day, deep blue night. Shake only on hits/thunder. Pulse/flash grades on bites and cliffhangers.
- Reused images keep consistent camera logic; never two consecutive shots on the same image unless the camera moves to a new target.
- Shots crossfade 0.35 s into each other.
- Shot fields in `plan.json`: `img`, `z` (zoom from→to), `c` (camera centre from→to), `ov` (reveal layers), `hand` (handwriting), `swap` (image crossfade within a shot, e.g. clean wall → wall with name), `chalk`, `phone`, `punch`, `shake`, `flash`, `pulse`, `dim`, `g` (grade), `flick`, `fadein`.

## 7. Social/reel format
- 1080x1920 at 30 fps, 16:9 video centred, title block "TESTAQUADRATA / PARTE n" on top.
- "SEGUICI per la Parte n+1" prompt at **45 %** of the reel for 4.5 s, bouncing arrow (IG bottom-left, TikTok top-right).
- 3.2 s end hold: **"EPISODIO INTERO SU YOUTUBE / LINK IN BIO"**.
- Cut each reel at the pause after its cliffhanger line; the next reel starts on the next day card.
- Instagram and TikTok files are identical apart from the follow-arrow position.
- The creator defines the reel boundaries by the last spoken line of each reel (Ep3 example: P10 ends "E' davanti alla tua porta e parla"; P15 starts by repeating the last line of P14). Always honour his list; if the last reel's audio runs past the line he named, include the whole audio and flag it.

## 8. QA loop (mandatory)
1. Render. 2. Rewatch **the full video** against the script and this document. 3. One correction pass.
4. Rewatch again and produce a **list of problems only** (no editing). 5. The creator picks which to fix.
Typical second-pass items: fallback images, a prop on the wrong door, static shutters, a character moving before the voice says so, a night image on a day scene, an event only implied that the voice states outright.
Never claim "100 % ready" without having measured sound levels and looked at frames at every shot start.

## 9. Delivery
- Desktop `TESTAQUADRATA/PRONTI/Episodio N/{YouTube, Instagram, TikTok}` — only finished, checked files.
- Large files: commit 1–4 per call (big batches time out).
- Images live separately in `Immagini/Episodio N`.
