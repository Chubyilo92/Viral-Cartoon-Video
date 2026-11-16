import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD, C
from _kitchenprops import KITCHEN_PROPS
from _r3props import R3_PROPS
from _gapfill1116 import GAPFILL_PROPS
TITLE = "when a girl saves you a plate"
PRELUDE = KITCHEN_PROPS + R3_PROPS + GAPFILL_PROPS
LINE_SPEED = {1: 0.82}  # voicecheck precheck: line 2 ran fast (3.8 w/s) at default 0.9
BODY_LINES = [
"When a girl saves you a plate when you're running late, she's not just keeping leftovers.",
"She covers it in foil and leaves it on the stove, so it's still warm when you get in.",
"She waits to eat her own until you're home, even when you're an hour late.",
"She reheats it without being asked the second she hears your key in the door.",
"If you've never come home to a cold dinner... send this to her.",
"But the night you come home and the kitchen's already clean, nothing saved... she stopped waiting for you to be home.",
"Because a girl who saves you a plate... would rather eat late than eat without you.",
]
D = [
'''  room('#f1d9b8','#c9a06e');
  stove(800,G+60,1.0);
  foilPlate(800,G-20,1.0,1);
  pup({kind:'girl',x:460,y:G+10,s:1.2,look:[.3,-.1],eyes:'open',mouth:'flat'});
  labelCard(300,420,'7:40pm ⏰',.85,1,24);''',
'''  room('#f6e4c8','#d4ad78');
  stove(760,G+60,1.0);
  foilPlate(760,G-20,1.0,1);
  heatWave(720,G-100,u,2,.5);
  pup({kind:'girl',x:460,y:G+10,s:1.22,look:[.2,-.1],eyes:'happy',mouth:'smile',paw:{x:150,y:-190,k:.5}});''',
'''  room('#e7ccae','#bb9164');
  stove(760,G+60,.9);
  foilPlate(760,G-20,.9,1);
  pup({kind:'girl',x:460,y:G+10,s:1.2,look:[.2,-.2],eyes:'open',mouth:'flat',brows:'sad'});
  labelCard(820,460,'8:50pm ⏰',.85,1,24);''',
'''  room('#333c54','#28304a');
  doorFrame(820);
  pup({kind:'boy',x:860,y:G+10,s:1.1,flip:-1,look:[-.3,0],eyes:'open',mouth:'smile',shadow:false});
  stove(540,G+60,.9);
  potOnStove(540,G-20,.9,u);
  pup({kind:'girl',x:300,y:G+10,s:1.15,look:[.3,-.1],eyes:'happy',mouth:'smile',shadow:false});''',
SHARE,
'''  room('#6f6a78','#5a5562','rgba(255,255,255,.05)');
  stove(760,G+60,1.0);
  plateProp(500,G+70,.9,0);
  labelCard(500,420,'9:40pm ⏰',.85,1,24);
  pup({kind:'girl',x:320,y:G+10,s:1.15,look:[.2,0],eyes:'open',mouth:'flat'});''',
HUG,
]
SCENES = spec(BODY_LINES, D, [{'leftovers':'🍽️'},{'get in':'🧊'},{'hour late':'🕰️'},{'the door':'🔑'},{'send this to her':'💌'},{'be home':'💔'},{'without you':'🤍'}])
IG_LINE = "The plate covered in foil on the stove. The dinner she waits to eat until you're home. The one she warms the second she hears your key. Everyone shows love their own way... Want to know yours? There's a sixty second test in our bio. Take it together."
IG_CAPS = C(IG_LINE, {'stove.':'🍽️','yours?':'🤍','bio':'🔗'})
IG_RESULT = "Acts of Service"
TT_LINE = TT_STD
