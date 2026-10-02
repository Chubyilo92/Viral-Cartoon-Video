import sys; sys.path[:0] = ['/home/claude/jj', '/home/claude/jj/specs']
from cast import P, S, RED, SAD, CALM, FLICK, PRELUDE, SHAKE
from dialogue import D, ENDCARD
from sting import sting, OUTRO_SECS

TITLE = "he hired my EX to plan our wedding"
MUSIC_N = 1
LOOP = "wait for the cake 👇"
G3, B3, X3 = (lambda m, t=False, e='': P('girl', 220, 'r', m, t, s=1.1, extra=e)), (lambda m, t=False, e='': P('boy', 520, 'l', m, t, s=1.05, extra=e)), (lambda m, t=False, e='': P('ex', 850, 'l', m, t, s=1.05, extra=e))
CAKE = "cake(370,G+40,.7);"
RES = lambda a, d='[]', n='': "stepsPhone(820,1010,1.35,'Resolve',['🗣️  her turn','👂  his turn','🤝  the fix'],%s,%s,%s);" % (a, d, repr(n))
G2, B2 = (lambda m, t=False, e='': P('girl', 230, 'r', m, t, s=1.05, extra=e)), (lambda m, t=False, e='': P('boy', 480, 'l', m, t, s=1.0, extra=e))

LINES = [
 S('girl', "You hired my EX to plan our WEDDING?!", RED + CAKE,
   [G3('angry', True, SHAKE), B3('shocked'), X3('sheepish')], '😡', LOOP),
 S('boy', "He had five stars!", RED + CAKE, [G3('angry'), B3('angry', True, SHAKE), X3('smug')], '⭐', LOOP),
 S('ex', "Four point nine. One bad review. Hers.", RED + CAKE, [G3('angry'), B3('shocked'), X3('smug', True)], '🙃', LOOP),
 S('girl', "Did you not read his NAME?", RED + CAKE, [G3('angry', True, SHAKE), B3('sad'), X3('flat')], '🤬', LOOP,
   js="raincloudSmall(380,600,win(u,.3,9));"),
 S('boy', "You never told me his name! You just call him 'the mistake'!", RED + CAKE,
   [G3('shocked'), B3('angry', True, SHAKE), X3('shocked')], '💢', LOOP, js="raincloudSmall(380,600,1);"),
 S('ex', "...Still?", RED + CAKE, [G3('smug'), B3('flat'), X3('sad', True)], '🥲', 'wait for it 👀', js="raincloudSmall(380,600,1);"),
 S('girl', "Get the app. Now. Or there's no wedding to plan.", SAD,
   [P('girl', 330, 'r', 'angry', True), P('boy', 760, 'l', 'sad')], '📱', 'last chance 💔'),
 S('boy', "Follow the screen. You first.", CALM, [G2('soft'), B2('soft', True)], None, 'last chance 💔', js=RES(0)),
 S('girl', "I don't want my ex choosing the cake on the best day of my life.", CALM,
   [G2('sad', True), B2('soft')], '🎂', 'last chance 💔', js=RES(0)),
 S('boy', "What I heard is... you want a different cake.", CALM, [G2('shocked'), B2('soft', True)], '🍰', 'last chance 💔', js=RES(1, '[0]')),
 S('girl', "NO!", CALM + FLICK, [G2('angry', True, SHAKE), B2('shocked')], '😤', 'last chance 💔', js=RES(1, '[0]', '❌ try again')),
 S('boy', "...You want our day to be only ours.", CALM, [G2('soft'), B2('soft', True)], '🥺', 'it worked 💗', js=RES(2, '[0,1]', '✅ heard')),
 S('boy', "You're fired.", CALM + CAKE, [G3('happy'), P('boy', 520, 'r', 'smug', True, s=1.05), X3('shocked')], '👋', js=RES(2, '[0,1]', '🤝 the fix') if False else ''),
 S('ex', "Fair. But she hates lemon. You ordered lemon.", CALM + CAKE, [G3('shocked'), B3('shocked'), X3('smug', True)], '🍋', 'plot twist 👀'),
 S('boy', "...You hate lemon?", CALM, [P('girl', 330, 'r', 'sheepish'), P('boy', 760, 'l', 'shocked', True)], '😳', 'plot twist 👀'),
 S('girl', "I've eaten your lemon cake every birthday. For three years.", CALM,
   [P('girl', 330, 'r', 'sheepish', True), P('boy', 760, 'l', 'sad')], '🍋', js="bigEmoji('🍋',540,740,110,pop(u,1.5,.4));"),
 D('boy', "Fix it before the wedding, not after. Link in bio!", ENDCARD('fix it before the wedding', speaker='boy'), '🔗'),
]
q, a = sting('girl', 'the mistake 🚩', "He doesn't even know your", 'favourite cake. I do. 🍰', '20k')
LINES.append(q); END = a; END_TAIL = OUTRO_SECS
SFX = [(len(LINES) - 1, 'start', 'text')]
