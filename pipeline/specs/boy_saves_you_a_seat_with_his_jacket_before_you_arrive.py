import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD, C
from _r3props import R3_PROPS
from _gapfill1116 import GAPFILL_PROPS
TITLE = "when a boy saves you a seat"
PRELUDE = R3_PROPS + GAPFILL_PROPS
LINE_SPEED = {4: 0.82}  # voicecheck precheck: line 5 ran fast (3.7 w/s) at default 0.9
BODY_LINES = [
"When a boy saves you a seat with his jacket before you even arrive, he's not just holding a spot.",
"He'll tell three different people \"sorry, it's taken\" before you walk in.",
"He keeps one hand on the jacket every time someone walks past.",
"He does it at the pub, at his cousin's wedding, anywhere there's a chair to lose.",
"If you've never once had to look for a seat when he's there... send this to him.",
"But the night he sits down first and doesn't save you one... he didn't forget. He's stopped making room for you.",
"Because a boy who saves you a seat before you arrive... is always making space for you, even when you're not there yet.",
]
D = [
'''  room('#f1d5b0','#caa070');
  chairJacket(760,G+140,1.0,1);
  pup({kind:'boy',x:380,y:G+10,s:1.25,look:[.4,-.1],eyes:'open',mouth:'smile'});''',
'''  room('#e8d8c8','#c2a98f');
  chairJacket(800,G+140,.9,1);
  pup({kind:'boy',x:420,y:G+10,s:1.2,look:[.4,-.1],eyes:'squint',mouth:'o',paw:{x:160,y:-150,k:1}});
  if(u>.4){ctx.save();ctx.globalAlpha=win(u,.4,9);bubbleText(420,560,"sorry, it's taken!",1,.62);ctx.restore();}''',
'''  room('#cfe3ec','#98b6c2');
  chairJacket(700,G+140,1.05,1);
  pup({kind:'boy',x:400,y:G+10,s:1.25,look:[.5,0],eyes:'open',mouth:'flat',paw:{x:260,y:-30,k:1}});''',
'''  room('#f6e4c8','#d4ad78');
  chairJacket(760,G+140,.95,1);
  pup({kind:'boy',x:380,y:G+10,s:1.2,look:[.4,-.1],eyes:'happy',mouth:'smile'});
  labelCard(820,460,'the pub 🍺',.9,1,22);
  labelCard(330,460,"cousin's wedding 💍",.78,1,22);''',
SHARE,
'''  room('#6f6a78','#5a5562','rgba(255,255,255,.05)');
  pup({kind:'boy',x:700,y:G+10,s:1.2,flip:-1,eyes:'happy',mouth:'smile',look:[-.2,0]});
  pup({kind:'girl',x:340,y:G+10,s:1.2,eyes:'open',mouth:'flat',brows:'sad',look:[.3,0]});
  chairJacket(760,G+140,.8,0);''',
HUG,
]
SCENES = spec(BODY_LINES, D, [{'holding a spot':'🪑'},{"it's taken":'🙅'},{'walks past':'🧥'},{'chair to lose':'🥂'},{'send this to him':'💌'},{'for you':'💔'},{'there yet':'🤍'}])
IG_LINE = "The jacket on the chair. The \"sorry, it's taken.\" The seat that's always already yours. Everyone shows love their own way... Want to know yours? There's a sixty second test in our bio. Take it together."
IG_CAPS = C(IG_LINE, {'chair.':'🪑','yours?':'🤍','bio':'🔗'})
IG_RESULT = "Acts of Service"
TT_LINE = TT_STD
