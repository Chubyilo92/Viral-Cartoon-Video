import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD, C
from _r3props import R3_PROPS
from _gapfill1116 import GAPFILL_PROPS
TITLE = "when a boy takes the road side"
PRELUDE = R3_PROPS + GAPFILL_PROPS
LINE_SPEED = {3: 0.82}  # voicecheck precheck: line 4 ran fast (3.9 w/s) at default 0.9
BODY_LINES = [
"When a boy walks on the road side of the pavement without being asked, he's not just being polite.",
"He switches sides without a word the second a car comes close.",
"He does it on an empty street at midnight, with no car in sight.",
"He'll step around you to get back on that side if you swap on him.",
"If he's always somehow on the traffic side... send this to him.",
"But the day he lets you walk on the road side... he's not being lazy. He's stopped putting himself in the way.",
"Because a boy who walks on the road side... is standing between you and the world without making it a thing.",
]
D = [
'''  room('#cfe3ec','#9fa9a6');
  curbRoad(1620);
  pup({kind:'girl',x:420,y:G+10,s:1.2,look:[.3,-.1],eyes:'happy',mouth:'smile'});
  pup({kind:'boy',x:660,y:G+10,s:1.22,look:[.2,-.1],eyes:'open',mouth:'flat'});
  labelCard(420,460,'curb side 🏠',.68,1,19);
  labelCard(660,560,'road side 🚗',.68,1,19);''',
'''  room('#cfe3ec','#9fa9a6');
  curbRoad(1620);
  carPass(900-((u*260)%1400),1600,1.0,1);
  pup({kind:'girl',x:420,y:G+10,s:1.2,look:[.2,-.1],eyes:'open',mouth:'o'});
  pup({kind:'boy',x:660,y:G+10,s:1.22,look:[.2,-.1],eyes:'squint',mouth:'flat'});
  labelCard(420,460,'curb side 🏠',.68,1,19);
  labelCard(660,560,'road side 🚗',.68,1,19);''',
'''  room('#303b57','#262c42');
  curbRoad(1620);
  sparkle(900,220,16,.8);sparkle(200,300,12,.7);sparkle(650,160,14,.75);
  pup({kind:'girl',x:420,y:G+10,s:1.2,look:[.3,-.1],eyes:'happy',mouth:'smile',shadow:false});
  pup({kind:'boy',x:660,y:G+10,s:1.22,look:[.2,-.1],eyes:'open',mouth:'flat',shadow:false});
  labelCard(420,460,'curb side 🏠',.68,1,19);
  labelCard(660,560,'road side 🚗',.68,1,19);''',
'''  room('#e8d8c8','#9fa9a6');
  curbRoad(1620);
  pup({kind:'girl',x:660,y:G+10,s:1.2,flip:-1,look:[-.2,-.1],eyes:'wide',mouth:'o'});
  pup({kind:'boy',x:420,y:G+10,s:1.22,flip:-1,look:[-.2,-.1],eyes:'squint',mouth:'flat'});
  line([[560,G-120],[500,G-70],[560,G-20]],{lw:6,c:INK});
  labelCard(660,560,'she swapped onto the road side 🚗',.6,1,17);
  labelCard(420,460,'he steps back around 🔄',.6,1,17);''',
SHARE,
'''  room('#6f6a78','#5a5562','rgba(255,255,255,.05)');
  curbRoad(1620);
  carPass(780,1600,1.0,1);
  pup({kind:'girl',x:700,y:G+10,s:1.2,look:[.1,-.1],eyes:'open',mouth:'flat',brows:'sad'});
  pup({kind:'boy',x:380,y:G+10,s:1.2,flip:-1,look:[-.3,0],eyes:'open',mouth:'flat'});
  labelCard(700,560,'road side 🚗',.6,1,17);
  labelCard(380,460,'curb side 🏠',.6,1,17);''',
HUG,
]
SCENES = spec(BODY_LINES, D, [{'being polite':'🚶'},{'comes close':'🚗'},{'no car in sight':'🌙'},{'swap on him':'🔄'},{'send this to him':'💌'},{'in the way':'💔'},{'a thing':'🤍'}])
IG_LINE = "The side he always takes without a word. The empty street he still does it on. The one he's quietly standing on. Everyone shows love their own way... Want to know yours? There's a sixty second test in our bio. Take it together."
IG_CAPS = C(IG_LINE, {'word.':'🚶','yours?':'🤍','bio':'🔗'})
IG_RESULT = "Acts of Service"
TT_LINE = TT_STD
