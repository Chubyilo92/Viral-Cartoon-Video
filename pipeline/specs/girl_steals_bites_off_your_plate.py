import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD, C
from _r3props import R3_PROPS
TITLE = "when a girl steals bites off your plate"
PRELUDE = R3_PROPS
LINE_SPEED = {2: 0.8}  # voicecheck: line 3 pace 3.7 w/s at 0.9
BODY_LINES = [
'When a girl says she\'s "not hungry" and then eats half your chips, she\'s not stealing your food.',
"She'd never touch her friends' food. Only yours.",
'She "just wants a bite," and the bite turns into a third of the meal.',
"She still insists she wasn't that hungry, with your fork in her hand.",
"If you've started ordering extra chips just for her... send this to her.",
"But the day she orders her own and doesn't touch yours... she's not finally full. She's keeping her distance.",
"Because a girl who eats off your plate... feels close enough to you to stop pretending she's not hungry.",
]
D = [
'''  room('#e8d8c8','#c2a98f');
  friesBag(820,G+10,1.1,1,0);
  pup({kind:'girl',x:360,y:G+10,s:1.25,look:[.4,-.2],eyes:'open',mouth:'flat',tilt:-.04});
  pup({kind:'boy',x:650,y:G+10,s:1.2,flip:-1,look:[-.3,-.2],eyes:'wide',mouth:'o'});
  if(u>.5){const k=pop(u,.5,.4);ctx.save();ctx.globalAlpha=win(u,.5,9);bubbleText(300,620,"not hungry 🙅",1,.85*k);ctx.restore();}''',
'''  room('#e3c9a0','#bf9670');
  friesBag(820,G+10,1.1,.4,0);
  pup({kind:'girl',x:420,y:G+10,s:1.25,look:[.4,-.2],eyes:'happy',mouth:'open',blush:.3});
  pup({kind:'boy',x:280,y:G+10,s:1.2,look:[.6,.1],eyes:'open',mouth:'smile'});''',
'''  room('#f1d5b0','#caa070');
  const n=Math.max(0,1-(u*.28));
  friesBag(820,G+10,1.15,n,0);
  pup({kind:'girl',x:420,y:G+10,s:1.3,look:[.4,-.3],eyes:'squint',mouth:'open',blush:.4,tilt:-.06});
  if(u>.5){const k=pop(u,.5,.4);ctx.save();ctx.globalAlpha=win(u,.5,9);bubbleText(340,610,"just one bite 😇",1,.85*k);ctx.restore();}''',
'''  room('#cfe3ec','#98b6c2');
  friesBag(820,G+10,1.1,.1,0);
  pup({kind:'girl',x:420,y:G+10,s:1.3,look:[.4,-.1],eyes:'happy',mouth:'smile',blush:.4});
  pup({kind:'boy',x:260,y:G+10,s:1.2,look:[.6,0],brows:'sad',mouth:'flat'});
  if(u>.8){ctx.save();ctx.globalAlpha=win(u,.8,9);bubbleText(340,610,"I wasn't even hungry 😌",1,.75);ctx.restore();}''',
SHARE,
'''  room('#6f6a78','#5a5562','rgba(255,255,255,.05)');
  friesBag(300,G+10,1.05,.9,0);friesBag(760,G+10,1.05,1,0);
  pup({kind:'girl',x:300,y:G+10,s:1.2,look:[.3,-.1],eyes:'open',mouth:'flat'});
  pup({kind:'boy',x:760,y:G+10,s:1.2,flip:-1,brows:'sad',look:[-.3,-.1],mouth:'flat'});
  if(u>1.2)raincloudSmall(300,G-440,win(u,1.2,9)*.6);''',
HUG,
]
SCENES = spec(BODY_LINES, D, [{'not hungry':'🙅'},{'only yours':'🍟'},{'the meal':'😇'},{'in her hand':'🍴'},{'to her':'💌'},{'distance':'💔'},{'not hungry':'🤍'}])
IG_LINE = "The not hungry. The just one bite. The whole plate gone. Everyone shows love their own way... Want to know yours? There's a sixty second test in our bio. Take it together."
IG_CAPS = C(IG_LINE, {'bite':'🍟','yours?':'🤍','bio':'🔗'})
IG_RESULT = "Quality Time"
TT_LINE = TT_STD
