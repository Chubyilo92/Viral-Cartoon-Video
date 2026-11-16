import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD, C
from _kitchenprops import KITCHEN_PROPS
from _r3props import R3_PROPS
from _gapfill1116 import GAPFILL_PROPS
TITLE = "when his phone stays face down"
PRELUDE = KITCHEN_PROPS + R3_PROPS + GAPFILL_PROPS
LINE_SPEED = {}
BODY_LINES = [
"When a boy puts his phone face down and leaves it there for your whole dinner, he's not just being polite.",
"He'll let it buzz through a whole string of messages without even turning it over.",
"He mutes it before you've even sat down, every single time.",
"He lets a call ring out and doesn't check who it was until the bill comes.",
"If you've never had a dinner interrupted by his phone... send this to him.",
"But if you're the one scrolling while he talks... don't be surprised the night his phone stays face up.",
"Because a boy who leaves his phone face down... is choosing to be nowhere else but here with you.",
]
D = [
'''  room('#f1d5b0','#caa070');
  plateProp(360,G+80,.9,1);plateProp(740,G+80,.9,1);
  phoneFaceDown(550,G+40,.9,0);
  pup({kind:'boy',x:740,y:G+10,s:1.15,flip:-1,look:[-.3,-.1],eyes:'open',mouth:'smile'});
  pup({kind:'girl',x:360,y:G+10,s:1.15,look:[.3,-.1],eyes:'happy',mouth:'smile'});''',
'''  room('#e8d8c8','#c2a98f');
  plateProp(360,G+80,.9,1);plateProp(740,G+80,.9,1);
  phoneFaceDown(650,G+40,1.0,1);
  pup({kind:'boy',x:740,y:G+10,s:1.15,flip:-1,look:[-.4,0],eyes:'squint',mouth:'smile'});
  pup({kind:'girl',x:360,y:G+10,s:1.15,look:[.3,-.1],eyes:'open',mouth:'smile'});''',
'''  room('#cfe3ec','#98b6c2');
  phoneFaceDown(560,G-60,1.1,0);
  labelCard(560,430,'🔇 muted',.85,1,24);
  pup({kind:'boy',x:760,y:G+10,s:1.1,flip:-1,look:[-.3,0],eyes:'open',mouth:'flat',paw:{x:-170,y:-200,k:.6}});
  pup({kind:'girl',x:330,y:G+10,s:1.15,look:[.5,0],eyes:'happy',mouth:'smile'});''',
'''  room('#f6e4c8','#d4ad78');
  plateProp(360,G+80,.9,1);plateProp(740,G+80,.9,1);
  phoneFaceDown(650,G+40,1.0,1);
  labelCard(820,380,'the bill 🧾',.8,1,22);
  pup({kind:'boy',x:740,y:G+10,s:1.15,flip:-1,look:[-.3,-.1],eyes:'open',mouth:'smile'});
  pup({kind:'girl',x:360,y:G+10,s:1.15,look:[.3,-.1],eyes:'happy',mouth:'smile'});''',
SHARE,
'''  room('#6f6a78','#5a5562','rgba(255,255,255,.05)');
  plateProp(360,G+80,.85,1);plateProp(740,G+80,.85,1);
  bigPhone(300,G-20,.4,()=>{});
  labelCard(690,460,'his, face up tonight 📱',.68,1,19);
  pup({kind:'girl',x:360,y:G+10,s:1.1,look:[.1,.5],eyes:'squint',mouth:'flat'});
  pup({kind:'boy',x:740,y:G+10,s:1.1,flip:-1,look:[-.2,0],eyes:'open',mouth:'flat',brows:'sad'});
  blob(rectPts(705,G+50,70,116,10),'#3a3a3f');
  blob(rectPts(712,G+57,56,102,6),'#8fc8f0');''',
HUG,
]
SCENES = spec(BODY_LINES, D, [{'being polite':'📵'},{'turning it over':'📳'},{'single time':'🔇'},{'bill comes':'🧾'},{'send this to him':'💌'},{'face up':'💔'},{'here with you':'🤍'}])
IG_LINE = "The phone face down through the whole dinner. The buzz he lets ring out. The bill that comes before he even checks who called. Everyone shows love their own way... Want to know yours? There's a sixty second test in our bio. Take it together."
IG_CAPS = C(IG_LINE, {'dinner.':'📵','yours?':'🤍','bio':'🔗'})
IG_RESULT = "Quality Time"
TT_LINE = TT_STD
