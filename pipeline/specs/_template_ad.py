"""TEMPLATE - JJ puppy dialogue ad. Copy to specs/<slug>.py, fill the beats, then:
     python3 dialogue.py <slug> preview   -> work/<slug>/pv_*.png  (check every frame)
     python3 dialogue.py <slug>           -> out/<slug>.mp4 + QA
Rules + line banks: docs/DIALOGUE-AD-TEMPLATE.md. The beat list below is the worked example ("the last biscuit").
Change the WORDS and the FEATURE every time; keep the SHAPE (hook -> walkout -> stakes -> app with a fail ->
small cause -> human fix -> twist -> end card -> sting -> big like-goal outro)."""
import sys; sys.path[:0] = ['/home/claude/jj', '/home/claude/jj/specs']
from adkit import build, beat as b

APP = dict(head='Resolve', steps=['🗣️  her turn', '👂  his turn', '🤝  the fix'])   # the feature's screen
STING = dict(owner='girl', sender='Ex 🚩', l1='I got your favourite', l2='biscuits 🍪😉', goal='1k')
MUSIC_N = 2

BEATS = [
    # ACT 1 - nasty hook from 0.2s; every insult answered by one just as bad
    b('girl', "I can't stand you anymore!", 'fight', emoji='😡'),
    b('boy',  "Good! Because I can't stand your mom!", 'fight', emoji='🤬'),
    b('girl', "Don't you DARE talk about my mom!", 'fight', emoji='💢'),
    b('boy',  "You know what? Maybe we need a break.", 'fight', other='sad', emoji='💔'),
    b('girl', "Fine. You were never good enough for me anyway.", 'fight', mood='smug'),
    b('boy',  "Then I'm done.", 'walkout', emoji='🚪'),
    # ACT 2 - regret + come back + stakes (vary the wording every video)
    b('girl', "...Why did I say that?", 'alone', emoji='🥺'),
    b('boy',  "Babe, get the app. Let's try again.", 'return', mood='soft', other='sad', emoji='📱'),
    b('girl', "Fine. If it doesn't help... we break up.", 'stakes', mood='soft', other='shocked'),
    # ACT 3 - the feature on screen at every step; it fails once; the small cause comes out
    b('boy',  "Let's follow the instructions on screen. You go first.", 'app', mood='soft', app=dict(active=0)),
    b('girl', "You ate the last biscuit. And you didn't even ask.", 'reveal', mood='sad', prop='🍪', app=dict(active=0, note='🍪 the last biscuit'), emoji='🍪'),
    b('boy',  "What I heard is... you hate me.", 'app', mood='soft', other='shocked', app=dict(active=1, done=[0]), emoji='😬'),
    b('girl', "That is NOT what I said!", 'fail', app=dict(active=1, done=[0], note='❌ try again'), emoji='😤'),
    b('boy',  "Sorry. I took the last one... and you felt forgotten.", 'app', mood='soft', app=dict(active=1, done=[0]), emoji='🥺'),
    b('girl', "...Yeah. That's exactly it.", 'app', mood='happy', other='happy', label='it worked 💗', app=dict(active=2, done=[0, 1], note='✅ heard'), sparkle=1),
    # ACT 4 - concrete human fix + laugh twist (never salesy)
    b('boy',  "Next time, I promise not to eat the last biscuit.", 'solution', mood='happy', other='happy', prop='🍪', app=dict(active=2, done=[0, 1], note='🤝 the fix'), emoji='🍪'),
    b('girl', "...You had a spare packet this whole time?!", 'hug', app=dict(active=-1, done=[0, 1, 2], note='💗 resolved'), emoji='😂'),
]

TITLE, LINES, END, SFX, END_TAIL, PRELUDE = build(
    "we almost broke up over this", BEATS, app=APP, sting=STING,
    endline="Every couple fights over something stupid. This is how we fix ours. Link in bio!",
    tagline='fix the small stuff')
