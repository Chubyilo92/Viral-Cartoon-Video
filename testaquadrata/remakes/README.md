# Testaquadrata – vertical remakes (Soldi, Calcio, Ultimo uomo, Rifugio)

Mobile-first 1080x1920 reels. Voice = creator's own recording (m4a), transcribed with `code/asr.py` (sherpa-onnx whisper-small, pause segmentation) for timing.

## TQ (fixed look, every video)
Square cream-white head, two black dot eyes, tiny line mouth, no hair/hat/scarf, red hoodie with small gold square on chest, dark jeans, white trainers. Sheet: `characters/TQ_sheet_red_hoodie.jpg`.
Rule: every other person also has a square cream head — never realistic human faces (Gemini slips on crowds/old men: always say "NO human face, his head must be a square block").

Recurring characters: `characters/` (madre di TQ, magazziniere, uomo della busta). Calcio father = square head, grey tufts, grey moustache, blue-white scarf.

## Image method (Gemini, free)
New chat → paste the TQ sheet → one prompt per shot with the shared prefix (see code/build_*.py shot lists). Runner downloads each image; 5-minute rule per image. Prompts: vertical 9:16, painterly cinematic, no text.

## Edit
`code/engine.py` renders shots (push-ins, crossfade 0.35 s, grain, vignette), burned captions timed to the voice, counters, iOS-style frosted notifications, vote end card. `code/mix.py` = voice master + ducked bed + SFX. Ending: vote card + "LA PARTE 2 ESCE A 300 COMMENTI" + "MANDALO NEL GRUPPO".
