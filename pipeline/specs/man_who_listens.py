import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD, C
TITLE = "a man who really listens"
BODY_LINES = [
"A man who really listens remembers the name of the girl at work you can't stand.",
"He asks if she's still being weird with you, a week later.",
"He asks how the dentist went, three days later.",
"He puts his phone face down the second you start a story.",
"If he listens like this... send this to the girl who deserves it.",
"But if you have to tell every story twice... he's not tired. He's not interested.",
"Because a man who listens remembers things you forgot you told him.",
]
D = [
'''  room('#e3c9a0','#bf9670');
  pup({kind:'girl',x:380,y:G+10,s:1.3,look:[.4,.1],brows:'sad',mouth:'flat'});
  pup({kind:'boy',x:760,y:G+10,s:1.25,flip:-1,look:[-.4,.1],eyes:'open',mouth:'flat'});
  if(u>.6){ctx.save();ctx.globalAlpha=win(u,.6,9);bubbleText(360,680,"...and Karen did it again 🙄",1,.8);ctx.restore();}''',
'''  room('#e8d8c8','#c2a98f');
  pup({kind:'girl',x:400,y:G+10,s:1.3,look:[.3,.1],eyes:'open',mouth:'flat'});
  pup({kind:'boy',x:770,y:G+10,s:1.25,flip:-1,look:[-.3,.1],eyes:'open',mouth:'smile',tilt:.05});
  if(u>.6){ctx.save();ctx.globalAlpha=win(u,.6,9);bubbleText(640,680,"is Karen still being weird? 🤍",1,.75);ctx.restore();}''',
'''  room('#cfe3ec','#98b6c2');
  windowBox(680,330,300,240,(w,h)=>{ctx.fillStyle='#8fd0f0';ctx.fillRect(0,0,w,h);});
  pup({kind:'girl',x:400,y:G+10,s:1.3,look:[.3,.1],eyes:'open',mouth:'flat'});
  pup({kind:'boy',x:770,y:G+10,s:1.25,flip:-1,look:[-.3,.1],eyes:'open',mouth:'smile',tilt:.05});
  if(u>.6){ctx.save();ctx.globalAlpha=win(u,.6,9);bubbleText(640,660,"how'd the dentist go? 🦷",1,.75);ctx.restore();}''',
'''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  pup({kind:'girl',x:400,y:G+10,s:1.3,look:[.3,.1],eyes:'happy',mouth:'smile',blush:.3});
  pup({kind:'boy',x:770,y:G+10,s:1.25,flip:-1,look:[-.3,.1],eyes:'open',mouth:'smile'});
  phoneMock(770,G-130,.3,.5,()=>{ctx.fillStyle='#2b2830';ctx.fillRect(-70,-290,140,280);});''',
SHARE,
'''  room('#4a3f4f','#3a3140','rgba(255,255,255,.05)');
  pup({kind:'girl',x:380,y:G+10,s:1.3,look:[.4,.3],brows:'sad',mouth:'flat',earLift:-.3});
  pup({kind:'boy',x:760,y:G+10,s:1.25,flip:-1,look:[-.6,0],eyes:'open',mouth:'flat'});
  phoneMock(lerp(640,760,P(u,.4,2)),G-320,.42,-.08,()=>{ctx.fillStyle='#dfe4ee';ctx.fillRect(-70,-290,140,280);ctx.fillStyle='#ec7489';ctx.fillRect(-60,-260,120,26);});
  if(u>1.6)raincloudSmall(380,640,win(u,1.6,9)*.7);''',
HUG,
]
SCENES = spec(BODY_LINES, D, [{'listens':'🤍'},{"weird":'🤍'},{'dentist':'🦷'},{'story':'📵'},{'deserves':'💌'},{'interested':'🚩'},{'forgot':'🤍'}])
IG_LINE = "The name he remembers. The question a week later. The phone face down. Everyone shows love their own way... Want to know yours? There's a sixty second test in our bio. Take it together."
IG_CAPS = C(IG_LINE, {'remembers':'🤍','yours?':'🤍','bio':'🔗'})
IG_RESULT = "Quality Time"
TT_LINE = TT_STD
