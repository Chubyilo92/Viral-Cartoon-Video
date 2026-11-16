import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD, C
from _r3props import R3_PROPS
from _gapfill1116 import GAPFILL_PROPS
TITLE = "when a boy warms up the car"
PRELUDE = R3_PROPS + GAPFILL_PROPS
LINE_SPEED = {6: 0.82}  # voicecheck precheck: line 7 ended rising +17.2% at default 0.9
BODY_LINES = [
"When a boy warms up the car before you get in, he's not just avoiding the cold himself.",
"He goes out five minutes early and scrapes the ice off your side first.",
"He turns your seat heater on before his own.",
"He does it on mornings he's not even driving anywhere with you.",
"If you've never once got into a cold car... send this to him.",
"But the morning you walk out to ice on your side of the windscreen... he hasn't forgotten. He's stopped thinking of you first.",
"Because a boy who warms your seat before his own... has already put you first today.",
]
D = [
'''  room('#cfe3ec','#98b6c2');
  carFront(560,G+120,1.0);
  heatWave(475,G-18,u,3);heatWave(655,G-18,u,3);
  pup({kind:'boy',x:950,y:G+10,s:1.1,flip:-1,eyes:'happy',mouth:'smile',look:[-.3,0]});''',
'''  room('#e8d8c8','#c2a98f');
  carFront(560,G+120,1.0);
  frostGlass(475,G+60,150,96,1);
  scraperProp(475,G+8,-.3,1.0);
  pup({kind:'boy',x:620,y:G+10,s:1.15,flip:-1,eyes:'squint',mouth:'flat',paw:{x:110,y:-15,k:1}});''',
'''  room('#f1d5b0','#caa070');
  blob(rectPts(220,G-40,620,110,16),'#8a8f98');
  blob(rectPts(260,G-10,250,70,10),'#caa06e');blob(rectPts(570,G-10,250,70,10),'#94a0a8');
  heatWave(380,G-10,u,2);
  labelCard(380,G-120,'her seat: warm 🔥',.85,1,22);
  labelCard(690,G-120,'his seat: cold',.85,1,22);''',
'''  room('#e3c9a0','#bf9670');
  carFront(560,G+120,1.0);
  heatWave(475,G-18,u,3);heatWave(655,G-18,u,3);
  pup({kind:'boy',x:950,y:G+10,s:1.1,flip:-1,eyes:'open',mouth:'flat',look:[-.3,0]});
  labelCard(540,430,"not driving together today",.72,1,21);''',
SHARE,
'''  room('#6f6a78','#5a5562','rgba(255,255,255,.05)');
  carFront(560,G+120,1.0);
  frostGlass(475,G+60,150,96,1);
  pup({kind:'girl',x:800,y:G+10,s:1.1,flip:-1,eyes:'open',mouth:'flat',brows:'sad',look:[-.3,0]});''',
HUG,
]
SCENES = spec(BODY_LINES, D, [{'himself':'🚗'},{'your side first':'🧊'},{'his own':'🔥'},{'with you':'🤍'},{'send this to him':'💌'},{'first':'💔'},{'put you first':'🤍'}])
IG_LINE = "The ice scraped off first. The seat heater on before his own. The five minutes he leaves early so you don't feel the cold. Everyone shows love their own way... Want to know yours? There's a sixty second test in our bio. Take it together."
IG_CAPS = C(IG_LINE, {'first.':'🧊','yours?':'🤍','bio':'🔗'})
IG_RESULT = "Acts of Service"
TT_LINE = TT_STD
