import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD, C
TITLE = "when you're back together"
BODY_LINES = [
"When you're back together after a real break, everyone suddenly has an opinion about it.",
"Not because they know the whole story. Because they only saw the ending, not the reason.",
"You two actually talked this time... about the thing that broke it the first time.",
"They show up different now... texting less about nothing, showing up more for everything.",
"If you two actually talked this time instead of just missing each other... send this to them.",
"But if you're back together and nothing actually changed... you didn't get back together, you just paused the ending.",
"Because a second chance that's actually different... isn't going backward, it's finally moving forward.",
]
D = [
'''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  pup({kind:'boy',x:380,y:G+10,s:1.25,look:[.4,.3],eyes:'open',mouth:'flat'});
  pup({kind:'girl',x:760,y:G+10,s:1.2,flip:-1,look:[-.4,.3],eyes:'open',mouth:'flat'});
  if(u>.8){ctx.save();ctx.globalAlpha=win(u,.8,8);bubbleText(560,680,"wait, really? 👀",1,.8);ctx.restore();}''',
'''  room('#d9e2c8','#a9b38f');
  pup({kind:'girl',x:360,y:G+10,s:1.2,look:[.4,.2],brows:'sad',mouth:'flat'});
  pup({kind:'boy',x:760,y:G+10,s:1.2,flip:-1,look:[-.4,.2],brows:'sad',mouth:'flat'});''',
'''  room('#e3c9a0','#bf9670');
  pup({kind:'boy',x:380,y:G+10,s:1.25,look:[.4,.1],eyes:'open',mouth:'flat'});
  pup({kind:'girl',x:740,y:G+10,s:1.25,flip:-1,look:[-.4,.1],eyes:'open',mouth:'flat'});
  if(u>1.4){ctx.save();ctx.globalAlpha=win(u,1.4,8);bubbleText(560,680,"that's what actually happened 🤍",1,.8);ctx.restore();}''',
'''  room('#f6d7c6','#d6a286');
  phoneMock(300,1000,.42,-.08,()=>{ctx.fillStyle='#eef0f5';ctx.fillRect(-70,-290,140,280);});
  pup({kind:'boy',x:560,y:G+10,s:1.25,look:[.3,-.1],eyes:'happy',mouth:'smile',blush:.3});
  pup({kind:'girl',x:840,y:G+10,s:1.2,flip:-1,look:[-.4,-.1],eyes:'happy',mouth:'smile',blush:.5,wag:.3});
  if(u>1.2)floatHearts(700,800,1.2,u,3,130);''',
SHARE,
'''  room('#6f6a78','#5a5562','rgba(255,255,255,.05)');
  pup({kind:'boy',x:380,y:G+10,s:1.2,look:[.3,.4],brows:'sad',mouth:'flat'});
  pup({kind:'girl',x:760,y:G+10,s:1.2,flip:-1,look:[-.3,.4],brows:'sad',mouth:'flat'});
  if(u>.8)raincloudSmall(560,610,win(u,.8,9)*.6);''',
HUG,
]
SCENES = spec(BODY_LINES, D, [{'about it':'👀'},{'reason':'🤍'},{'first time':'🤍'},{'everything':'🤍'},{'them':'💌'},{'ending':'🚩'},{'forward':'🤍'}])
IG_LINE = "The real talk. The showing up different. The second chance that stuck. Everyone gets a fresh start their own way... Want to know yours? There's a sixty second test in our bio. Take it together."
IG_CAPS = C(IG_LINE, {'talk':'🤍','yours?':'🤍','bio':'🔗'})
IG_RESULT = "Quality Time"
TT_LINE = TT_STD
