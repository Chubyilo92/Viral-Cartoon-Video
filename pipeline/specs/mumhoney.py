import sys; sys.path[:0] = ['/home/claude/jj', '/home/claude/jj/specs']
from cast import P, S, RED, SAD, CALM, FLICK, PRELUDE, SHAKE
from dialogue import D, ENDCARD
from sting import sting, OUTRO_SECS

TITLE = "his mum came on our honeymoon"
MUSIC_N = 3
LOOP = "how did she find them? 👇"
G3, B3, M3 = (lambda m, t=False: P('girl', 220, 'r', m, t, s=1.1)), (lambda m, t=False: P('boy', 520, 'l', m, t, s=1.05)), (lambda m, t=False: P('mum', 850, 'l', m, t, s=1.05))
ROOM = "room('#e7b8a6','#b9876f',1180,'rgba(255,255,255,.08)');"
PRIV = "[['💗 our anniversary','🔒 only you two can see this']]"

LINES = [
 S('girl', "Your mum was on our HONEYMOON. In the next room.", RED,
   [P('girl', 320, 'r', 'angry', True, s=1.4, extra=SHAKE), P('boy', 780, 'l', 'sheepish', s=1.3)], '😡', LOOP),
 S('mum', "The walls were very thin, darling.", ROOM,
   [G3('shocked'), B3('sheepish'), P('mum', "lerp(1120,850,P(u,0,.6))", 'l', 'smug', True, s=1.05)], '🙂', LOOP),
 S('boy', "Mum! How did you even know where we were?", ROOM,
   [G3('angry'), P('boy', 520, 'r', 'shocked', True, s=1.05), M3('smug')], '😳', LOOP),
 S('mum', "Your calendar, sweetheart. You share it with me.", ROOM,
   [G3('shocked'), B3('sheepish'), M3('smug', True)], '📅', LOOP),
 S('girl', "You share your calendar with your MOTHER but not with ME?!", RED,
   [P('girl', 320, 'r', 'angry', True, s=1.4, extra=SHAKE), P('boy', 780, 'l', 'shocked', s=1.3)], '🤬', LOOP),
 S('boy', "She books my dentist!", RED,
   [P('girl', 320, 'r', 'angry', s=1.4), P('boy', 780, 'l', 'sheepish', True, s=1.3)], '🦷', LOOP,
   js="raincloudSmall(540,640,win(u,.3,9));"),
 S('mum', "And your first date. You're welcome.", ROOM,
   [G3('shocked'), B3('sheepish'), M3('smug', True)], '💅', 'wait for it 👀'),
 S('girl', "You're going to add me on CoupleIn, or we're done!", RED,
   [P('girl', 320, 'r', 'angry', True, s=1.4, extra=SHAKE), P('boy', 780, 'l', 'shocked', s=1.3)], '💔', 'last chance 💔'),
 S('boy', "Done. Our anniversary. Just us.", CALM,
   [P('girl', 230, 'r', 'angry', s=1.05), P('boy', 480, 'l', 'soft', True, s=1.0)], '🔒', 'last chance 💔', 'LATER',
   js="calPhone(830,1000,1.45,-.04,'our calendar',u>1?%s:[],u<=1);" % PRIV),
 S('girl', "...Thank you.", CALM,
   [P('girl', 230, 'r', 'happy', True, s=1.05), P('boy', 480, 'l', 'happy', s=1.0)], '🥹',
   js="calPhone(830,1000,1.45,-.04,'our calendar',%s,false);" % PRIV),
 S('boy', "And I put a fake dinner in my old calendar.", CALM,
   [P('girl', 330, 'r', 'shocked'), P('boy', 760, 'l', 'smug', True)], '😏'),
 S('girl', "...Where?", CALM, [P('girl', 330, 'r', 'shocked', True), P('boy', 760, 'l', 'smug')], '👀', 'plot twist 👀'),
 S('boy', "A Frankie and Benny's. In Leeds.", CALM,
   [P('girl', 330, 'r', 'happy'), P('boy', 760, 'l', 'smug', True)], '🍝',
   js="if(u>1.6)floatHearts(540,800,1.6,u,5,160);"),
 D('girl', "Some things are just for two. Link in bio!", ENDCARD('some things are just for two'), '🔗'),
]
q, a = sting('boy', 'Mum 💐', "I'm at the restaurant.", 'Where ARE you two? 😡', '10k')
LINES.append(q); END = a; END_TAIL = OUTRO_SECS
SFX = [(len(LINES) - 1, 'start', 'text')]
