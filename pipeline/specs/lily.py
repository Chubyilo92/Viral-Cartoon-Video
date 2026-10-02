import sys; sys.path[:0] = ['/home/claude/jj', '/home/claude/jj/specs']
from cast import P, S, RED, SAD, CALM, FLICK, PRELUDE, SHAKE
from dialogue import D, ENDCARD
from sting import sting, OUTRO_SECS

TITLE = "she thought he was cheating"
MUSIC_N = 1
CAFE = "room('#f3d4dc','#c99aa6',1180,'rgba(255,255,255,.15)');"
LOOP = "who is Lily? 👇"
CAL = lambda rows, empty='false': "calPhone(830,1000,1.45,-.04,'Thursdays',%s,%s);" % (rows, empty)
LILY = "[['💃 Lily · 7pm','first dance lessons']]"

LINES = [
 S('girl', "He's been seeing a woman called Lily. Every Thursday. For SIX months.", CAFE,
   [P('girl', 330, 'r', 'sad', True), P('friend', 760, 'l', 'shocked')], '😭', LOOP),
 S('friend', "Take the car. Take the dog. And key the car first.", CAFE,
   [P('girl', 330, 'r', 'shocked'), P('friend', 760, 'l', 'angry', True, extra=SHAKE)], '🔑', LOOP),
 S('girl', "I'm doing it tonight.", CAFE,
   [P('girl', 330, 'r', 'angry', True), P('friend', 760, 'l', 'smug')], '😤', LOOP),
 S('girl', "Who the hell is LILY?!", RED,
   [P('girl', 320, 'r', 'angry', True, s=1.4, extra=SHAKE), P('boy', 780, 'l', 'shocked', s=1.3)], '😡', LOOP, 'THAT NIGHT'),
 S('boy', "You went through my PHONE?!", RED,
   [P('girl', 320, 'r', 'shocked', s=1.3), P('boy', 780, 'l', 'angry', True, s=1.4, extra=SHAKE)], '🤬', LOOP),
 S('girl', "Thursdays. Seven o'clock. Lily, with a heart. Six months!", RED,
   [P('girl', 320, 'r', 'angry', True, s=1.4), P('boy', 780, 'l', 'sad', s=1.3)], '💔', LOOP,
   js="raincloudSmall(540,640,win(u,.3,9));"),
 S('boy', "You're unbelievable.", RED,
   [P('girl', 320, 'r', 'angry', s=1.4), P('boy', 780, 'l', 'angry', True, s=1.3)], '🙄', 'wait for it 👀',
   js="raincloudSmall(540,640,1);raincloudSmall(400,580,win(u,.3,9));"),
 S('girl', "If it's nothing, put every Thursday in our CoupleIn calendar. Every single one.", SAD,
   [P('girl', 330, 'r', 'angry', True), P('boy', 760, 'l', 'sad')], '📅', 'last chance 💔'),
 S('boy', "Fine. Every Thursday.", CALM,
   [P('girl', 230, 'r', 'angry', s=1.05), P('boy', 480, 'l', 'flat', True, s=1.0)], '📲', 'last chance 💔',
   js="calPhone(830,1000,1.45,-.04,'Thursdays',u>1.2?%s:[],u<=1.2);" % LILY),
 S('girl', "...Dance lessons?", CALM,
   [P('girl', 230, 'r', 'shocked', True, s=1.05), P('boy', 480, 'l', 'sad', s=1.0)], '😳', 'plot twist 👀',
   js=CAL(LILY)),
 S('boy', "For OUR wedding. Lily's my teacher. She's seventy-four.", CALM,
   [P('girl', 230, 'r', 'sheepish', s=1.05), P('boy', 480, 'l', 'smug', True, s=1.0)], '💃',
   js=CAL(LILY) + "bigEmoji('👵',360,700,120,pop(u,1.8,.4));"),
 S('girl', "...I told Sophie to key your car.", CALM,
   [P('girl', 330, 'r', 'sheepish', True), P('boy', 760, 'l', 'shocked')], '🙈'),
 S('boy', "...Sophie keyed my car.", CALM,
   [P('girl', 330, 'r', 'shocked'), P('boy', 760, 'l', 'sad', True)], '🚗',
   js="bigEmoji('🔑',540,760,110,pop(u,.6,.4));"),
 D('girl', "Secrets start fights. One shared calendar ends them. Link in bio!", ENDCARD('no more secret Thursdays'), '🔗'),
]
q, a = sting('boy', 'Lily 💃', 'Same time Thursday,', 'handsome? 😘', '1k')
LINES.append(q); END = a; END_TAIL = OUTRO_SECS
SFX = [(len(LINES) - 1, 'start', 'text')]
