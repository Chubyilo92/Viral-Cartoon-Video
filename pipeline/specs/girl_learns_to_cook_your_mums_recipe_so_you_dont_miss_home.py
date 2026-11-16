import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD, C
from _kitchenprops import KITCHEN_PROPS
from _r3props import R3_PROPS
from _gapfill1116 import GAPFILL_PROPS
TITLE = "when a girl learns mum's recipe"
PRELUDE = KITCHEN_PROPS + R3_PROPS + GAPFILL_PROPS
LINE_SPEED = {5: 0.8}  # voicecheck precheck: line 6 ran fast (3.7 w/s) at default 0.9
BODY_LINES = [
"When a girl learns to cook your mum's recipe, she's not just being a good cook.",
"She calls your mum for the measurements that were never written down.",
"She gets the spice wrong four times before she gets it right.",
"She makes it on the nights you're missing home the most.",
"If she's learned to cook the thing that tastes like home... send this to her.",
"But if you never once tell her it tastes right... she'll stop trying to get it right for you.",
"Because a girl who learns to cook your mum's recipe... is building you a second home.",
]
D = [
'''  room('#f1d9b8','#c9a06e');
  stove(800,G+60,1.0);
  potOnStove(800,G-20,1.0,u);
  recipeCard(300,G-180,.55,1);
  pup({kind:'girl',x:540,y:G+10,s:1.2,look:[.2,-.1],eyes:'open',mouth:'smile',paw:{x:-140,y:-190,k:.6}});''',
'''  room('#f6e4c8','#d4ad78');
  pup({kind:'girl',x:580,y:G+10,s:1.3,look:[.1,-.1],eyes:'open',mouth:'o'});
  bigPhone(300,780,.85,()=>{chatBub(-90,-200,170,80,false);});
  if(u>.5){ctx.save();ctx.globalAlpha=win(u,.5,9);bubbleText(640,560,"how much sugar?",1,.62);ctx.restore();}''',
'''  room('#e7ccae','#bb9164');
  stove(760,G+60,1.0);
  potOnStove(760,G-20,1.0,u);
  pup({kind:'girl',x:460,y:G+10,s:1.22,look:[.3,-.1],eyes:'squint',mouth:'o',paw:{x:140,y:-190,k:.5}});
  labelCard(300,460,'try #4',.85,1,24);''',
'''  room('#333c54','#28304a');
  windowBox(650,340,220,260,()=>{ctx.fillStyle='#1c2340';ctx.fillRect(650,340,220,260);ctx.fillStyle='#fff3c4';ctx.beginPath();ctx.arc(800,520,26,0,7);ctx.fill();});
  pup({kind:'boy',x:420,y:G+10,s:1.22,look:[.3,-.1],eyes:'open',mouth:'flat',brows:'sad',shadow:false});
  stove(650,G+60,.85);potOnStove(650,G-20,.85,u);
  pup({kind:'girl',x:800,y:G+10,s:1.15,flip:-1,look:[-.3,-.1],eyes:'happy',mouth:'smile',shadow:false,paw:{x:-130,y:-170,k:.5}});''',
SHARE,
'''  room('#6f6a78','#5a5562','rgba(255,255,255,.05)');
  stove(700,G+60,.9);
  pup({kind:'girl',x:480,y:G+10,s:1.2,look:[.2,-.1],eyes:'open',mouth:'flat',brows:'sad',paw:{x:140,y:-190,k:.5}});''',
HUG,
]
SCENES = spec(BODY_LINES, D, [{'good cook':'🍳'},{'written down':'📞'},{'right':'🧂'},{'the most':'🏠'},{'send this to her':'💌'},{'for you':'💔'},{'second home':'🤍'}])
IG_LINE = "The phone call to your mum for the recipe. The fourth try to get it right. The dinner that tastes like home on the nights you need it most. Everyone shows love their own way... Want to know yours? There's a sixty second test in our bio. Take it together."
IG_CAPS = C(IG_LINE, {'mum':'📞','yours?':'🤍','bio':'🔗'})
IG_RESULT = "Acts of Service"
TT_LINE = TT_STD
