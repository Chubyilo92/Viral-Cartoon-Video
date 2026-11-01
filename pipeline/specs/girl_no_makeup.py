import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD, C
from _r3props import R3_PROPS
TITLE = "when she stops wearing makeup"
PRELUDE = R3_PROPS
BODY_LINES = [
"When a girl stops wearing makeup around you, she hasn't stopped trying.",
"She used to fix her hair before she opened the door. Now she answers it in pyjamas with spot cream on her chin.",
"She lets you see her at 7am, before coffee, before anything.",
"She falls asleep next to you with a face mask still on.",
"If she's stopped hiding anything from you... send this to her.",
"But if you ever make a joke about how she looks without it... watch how fast the makeup goes back on.",
"Because a girl who stops dressing up for you... feels at home with you.",
]
D = [
'''  room('#f3cfa8','#d09d72');
  pup({kind:'girl',x:380,y:G+10,s:1.3,look:[.4,.1],eyes:'happy',mouth:'smile',blush:.2});
  pup({kind:'boy',x:770,y:G+10,s:1.25,flip:-1,look:[-.4,.1],eyes:'happy',mouth:'smile',blush:.5});
  if(u>1)floatHearts(770,800,1,u,3,120);''',
'''  room('#e8d8c8','#c2a98f');
  doorFrame(170);
  pup({kind:'girl',x:285,y:G+10,s:1.15,look:[.6,.1],eyes:'open',mouth:'smile'});
  pjTop(285,1.15);chinSpot(285,G+10,1.15);
  pup({kind:'boy',x:740,y:G+10,s:1.25,flip:-1,look:[-.6,.1],eyes:'happy',mouth:'smile',blush:.5});
  if(u>1.4)floatHearts(740,800,1.4,u,3,110);''',
'''  room('#f6d7c6','#d6a286');
  windowBox(680,330,300,240,()=>{const g=ctx.createLinearGradient(0,0,0,240);g.addColorStop(0,'#ffd59e');g.addColorStop(1,'#ffb07a');ctx.fillStyle=g;ctx.fillRect(0,0,300,240);ctx.fillStyle='#fff3c4';ctx.beginPath();ctx.arc(150,190,40,0,7);ctx.fill();});
  pup({kind:'girl',x:370,y:G+10,s:1.3,look:[.3,.1],eyes:'squint',mouth:'flat'});
  pjTop(370,1.3);
  pup({kind:'boy',x:780,y:G+10,s:1.22,flip:-1,look:[-.4,.1],eyes:'happy',mouth:'smile',blush:.4});
  mug(575,G+4,1);''',
'''  bedNight();bedBack();
  pup({kind:'girl',x:420,y:G-100,s:1.1,flip:1,look:[0,0],eyes:'closed',mouth:'flat',tilt:.06,shadow:false});
  faceMask(420+0,G-100,1.1);
  pup({kind:'boy',x:680,y:G-100,s:1.1,flip:-1,look:[-.4,.1],eyes:'happy',mouth:'smile',blush:.4,shadow:false});
  blanket(150,935,G-190);zzz(460,G-500,u);''',
SHARE,
'''  room('#4a3f4f','#3a3140','rgba(255,255,255,.05)');
  pup({kind:'boy',x:760,y:G+10,s:1.25,flip:-1,look:[-.4,.1],eyes:'squint',mouth:'open'});
  pup({kind:'girl',x:350,y:G+10,s:1.3,look:[.4,.3],brows:'sad',mouth:'flat',earLift:-.3});
  if(u>.4){ctx.save();ctx.globalAlpha=win(u,.4,9);bubbleText(690,640,"lol what's on your face 😂",1,.7);ctx.restore();}
  if(u>1.8)raincloudSmall(350,620,win(u,1.8,9)*.7);''',
HUG,
]
SCENES = spec(BODY_LINES, D, [{'trying':'🤍'},{'chin':'🩷'},{'anything':'☀️'},{'still on':'🧖‍♀️'},{'to her':'💌'},{'back on':'🚩'},{'at home':'🏡'}])
IG_LINE = "The pyjamas. The early morning face. The mask she fell asleep in. Everyone shows love their own way... Want to know yours? There's a sixty second test in our bio. Take it together."
IG_CAPS = C(IG_LINE, {'pyjamas':'🩷','yours?':'🤍','bio':'🔗'})
IG_RESULT = "Quality Time"
TT_LINE = TT_STD
