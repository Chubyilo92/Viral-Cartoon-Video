import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD, C
from _r3props import R3_PROPS
TITLE = "when a boy falls asleep on you"
PRELUDE = R3_PROPS
LINE_SPEED = {4: 0.8}  # voicecheck: line 5 pace 3.9 w/s at 0.9
TV = '''  blob(rectPts(740,G-540,280,180,16),'#1c2430',{lw:5});
  ctx.save();ctx.globalAlpha=.45+Math.sin(u*9)*.15;ctx.fillStyle='#8fd0ff';ctx.fillRect(752,G-526,256,152);ctx.restore();'''
BODY_LINES = [
"When a boy falls asleep on the sofa with you, he's not being boring.",
"He fights it for ten minutes, eyes closing mid-sentence, still trying to listen.",
"He's slept five hours a night all week, and this is the first time he's sat still.",
'He wakes up saying "I\'m watching, I\'m watching" with his eyes still shut.',
"If he's never once made it to the end of a film with you... send this to him.",
"But the night he sits at the other end of the sofa, wide awake on his phone... he's not less tired. He just can't switch off around you anymore.",
"Because a boy who falls asleep on you... finally feels safe enough to stop holding it together.",
]
D = [
'''  room('#4a3f4f','#3a3140','rgba(255,255,255,.05)');couch();
  ''' + TV + '''
  pup({kind:'girl',x:420,y:G-100,s:1.2,flip:1,look:[.3,-.1],eyes:'happy',mouth:'smile',blush:.3});
  pup({kind:'boy',x:620,y:G-100,s:1.22,flip:1,look:[.3,-.1],eyes:'squint',mouth:'flat',earLift:-.1,tilt:.08});''',
'''  room('#4a3f4f','#3a3140','rgba(255,255,255,.05)');couch();
  ''' + TV + '''
  const bk=(u*2.2)%2<1;
  pup({kind:'boy',x:620,y:G-100,s:1.22,flip:1,look:[.3,-.1],eyes:bk?'closed':'open',mouth:'flat',earLift:-.15,tilt:.14});
  pup({kind:'girl',x:420,y:G-100,s:1.2,flip:1,look:[.3,0],eyes:'open',mouth:'open',blush:.2});
  if(u>.6){ctx.save();ctx.globalAlpha=win(u,.6,9);bubbleText(300,560,"...and then she said-",1,.8);ctx.restore();}''',
'''  room('#3a3344','#2c2638','rgba(255,255,255,.05)');couch();
  ''' + TV + '''
  pup({kind:'boy',x:640,y:G-80,s:1.22,flip:1,look:[0,0],eyes:'closed',mouth:'flat',earLift:-.3,tilt:.22,bob:Math.sin(u*2)*4});
  pup({kind:'girl',x:420,y:G-100,s:1.2,flip:1,look:[.4,.1],eyes:'open',mouth:'smile',blush:.3});
  zzz(760,G-470,u);''',
'''  room('#3a3344','#2c2638','rgba(255,255,255,.05)');couch();
  ''' + TV + '''
  pup({kind:'boy',x:640,y:G-80,s:1.22,flip:1,look:[0,0],eyes:'closed',mouth:'open',earLift:-.3,tilt:.18});
  pup({kind:'girl',x:420,y:G-100,s:1.2,flip:1,look:[.4,0],eyes:'happy',mouth:'smile',blush:.5});
  if(u>.4){const k=pop(u,.4,.4);ctx.save();ctx.globalAlpha=win(u,.4,9);bubbleText(520,610,"I'm watching, I'm watching 😴",1,.72*k);ctx.restore();}''',
SHARE,
'''  room('#2b3144','#222838','rgba(255,255,255,.05)');couch();
  pup({kind:'boy',x:900,y:G-90,s:1.2,flip:-1,look:[-.3,-.2],eyes:'wide',mouth:'flat',earLift:-.2});
  bigPhone(900,G-280,.55,()=>{ctx.save();ctx.globalAlpha=.4+Math.sin(u*8)*.1;ctx.fillStyle='#8fd0ff';ctx.fillRect(-70,-130,140,170);ctx.restore();});
  pup({kind:'girl',x:300,y:G-100,s:1.2,flip:1,look:[.4,0],brows:'sad',mouth:'flat'});
  if(u>1.3)raincloudSmall(300,G-470,win(u,1.3,9)*.7);''',
HUG,
]
SCENES = spec(BODY_LINES, D, [None,{'listen':'😴'},{'sat still':'🛋️'},{'still shut':'😂'},{'with you':'💌'},{'anymore':'📱'},{'together':'🤍'}])
IG_LINE = "The fighting it for ten minutes. The still trying to listen. The finally sitting still. Everyone shows love their own way... Want to know yours? There's a sixty second test in our bio. Take it together."
IG_CAPS = C(IG_LINE, {'sofa':'🛋️','yours?':'🤍','bio':'🔗'})
IG_RESULT = "Physical Touch"
TT_LINE = TT_STD
