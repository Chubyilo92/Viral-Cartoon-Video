import sys; sys.path[:0] = ['/home/claude/jj', '/home/claude/jj/specs']
from cast import P, S, RED, SAD, CALM, FLICK, PRELUDE, SHAKE
from dialogue import D, ENDCARD
from sting import sting, OUTRO_SECS

TITLE = "we almost broke up over a FISH"
MUSIC_N = 2
LOOP = "wait till you hear the fish's name 👇"
TANK = "tank(540,G+10,.95);"
RES = lambda a, d='[]', n='': "stepsPhone(820,1010,1.35,'Resolve',['🗣️  her turn','👂  his turn','🤝  the fix'],%s,%s,%s);" % (a, d, repr(n))
G2, B2 = (lambda m, t=False, e='': P('girl', 230, 'r', m, t, s=1.05, extra=e)), (lambda m, t=False, e='': P('boy', 480, 'l', m, t, s=1.0, extra=e))

LINES = [
 S('girl', "You named our goldfish after your EX?!", RED + TANK,
   [P('girl', 300, 'r', 'angry', True, s=1.35, extra=SHAKE), P('boy', 800, 'l', 'shocked', s=1.25)], '😡', LOOP),
 S('boy', "You named your PLANTS after yours!", RED + TANK,
   [P('girl', 300, 'r', 'shocked', s=1.35), P('boy', 800, 'l', 'angry', True, s=1.3, extra=SHAKE)], '🪴', LOOP),
 S('girl', "They're DEAD. That's the point!", RED + TANK,
   [P('girl', 300, 'r', 'angry', True, s=1.35), P('boy', 800, 'l', 'shocked', s=1.25)], '💀', LOOP,
   js="raincloudSmall(540,600,win(u,.3,9));"),
 S('boy', "Well, Tiffany's thriving!", RED + TANK,
   [P('girl', 300, 'r', 'angry', s=1.35), P('boy', 800, 'l', 'smug', True, s=1.25)], '🐠', LOOP,
   js="raincloudSmall(540,600,1);"),
 S('girl', "Then go and live in the tank with her.", RED + TANK,
   [P('girl', 300, 'r', 'angry', True, s=1.35), P('boy', "lerp(800,1120,P(u,CURLEAD+CURVO-.2,CURLEAD+CURVO+.6))", 'r', 'angry', s=1.25)], '🚪', 'wait for it 👀',
   js="raincloudSmall(540,600,1);raincloudSmall(400,560,1);"),
 S('girl', "Get the app. Let's try again. If this doesn't work, the fish goes.", SAD + TANK,
   [P('girl', 300, 'r', 'soft', True), P('boy', "lerp(1120,780,P(u,0,1))", 'l', 'sad')], '📱', 'last try 💔', 'LATER'),
 S('boy', "Follow the screen. You first.", CALM, [G2('soft'), B2('soft', True)], None, 'last try 💔', js=RES(0)),
 S('girl', "I say your ex's name out loud. Twice a day. Every feeding.", CALM,
   [G2('sad', True), B2('shocked')], '🐠', 'last try 💔', js=RES(0, n='🐠 Tiffany')),
 S('boy', "What I heard is... you want to feed her once a day.", CALM,
   [G2('shocked'), B2('soft', True)], '🤔', 'last try 💔', js=RES(1, '[0]')),
 S('girl', "That is NOT what I said!", CALM + FLICK,
   [G2('angry', True, SHAKE), B2('shocked')], '😤', 'last try 💔', js=RES(1, '[0]', '❌ try again')),
 S('boy', "...You feel like she lives with us.", CALM,
   [G2('soft'), B2('soft', True)], '🥺', 'it worked 💗', js=RES(2, '[0,1]', '✅ heard')),
 S('boy', "We'll rename her. You pick.", CALM,
   [G2('happy'), B2('happy', True)], '✏️', js=RES(2, '[0,1]', '🤝 the fix') + "bigEmoji('🐠',360,700,110,1);"),
 S('girl', "...Kevin.", CALM, [P('girl', 330, 'r', 'smug', True), P('boy', 760, 'l', 'flat')], '🐠', js=TANK),
 S('boy', "KEVIN? Like your ex Kevin?!", CALM + FLICK, [P('girl', 330, 'r', 'smug'), P('boy', 760, 'l', 'shocked', True, extra=SHAKE)], '😳', 'plot twist 👀', js=TANK),
 S('girl', "...It suits her.", CALM, [P('girl', 330, 'r', 'smug', True), P('boy', 760, 'l', 'sad')], '🙂', js=TANK),
 D('boy', "Every couple has a Tiffany. This is how we deal with ours. Link in bio!", ENDCARD('every couple has a Tiffany', speaker='boy'), '🔗'),
]
q, a = sting('girl', 'Kevin 🐟', 'Did you just name a', 'fish after me? ❤️', '5k')
LINES.append(q); END = a; END_TAIL = OUTRO_SECS
SFX = [(len(LINES) - 1, 'start', 'text')]
