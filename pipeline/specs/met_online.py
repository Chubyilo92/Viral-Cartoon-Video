import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD, C
TITLE = "when you met online"
BODY_LINES = [
"When you met online, the first thing people ask is if it's even real.",
"Not because meeting online is strange now. Because everyone's still hoping it's real.",
"You talked for three weeks before you ever saw each other's face on camera.",
"They still have the first message you sent... saved, screenshotted, read more than once.",
"If your love started with a message and still feels real... send this to them.",
"But if you're hiding how you met, like it's something to be embarrassed about... that's not love, that's shame.",
"Because love that started with a message... counts exactly the same as love that didn't.",
]
D = [
'''  room('#cfe3ec','#98b6c2');
  phoneMock(700,1010,.5,.08,()=>{ctx.fillStyle='#eef0f5';ctx.fillRect(-70,-290,140,280);ctx.fillStyle='#ec7489';ctx.beginPath();ctx.roundRect(-60,-250,110,40,14);ctx.fill();ctx.fillStyle='#fff';ctx.font='bold 14px Poppins';ctx.textAlign='left';ctx.fillText('is this even real? 🤔',-52,-224);});
  pup({kind:'girl',x:360,y:G+10,s:1.25,look:[.4,.1],eyes:'open',mouth:'smile',blush:.3});''',
'''  room('#e3c9a0','#bf9670');
  pup({kind:'boy',x:380,y:G+10,s:1.25,look:[.4,0],eyes:'happy',mouth:'smile'});
  pup({kind:'girl',x:760,y:G+10,s:1.25,flip:-1,look:[-.4,0],eyes:'happy',mouth:'smile',blush:.4});
  if(u>.9)floatHearts(560,800,.9,u,3,130);''',
'''  room('#3d4b6c','#303b57','rgba(255,255,255,.05)');
  phoneMock(420,1000,.52,-.06,()=>{ctx.fillStyle='#2b2830';ctx.fillRect(-70,-290,140,280);ctx.fillStyle='#8fd0f0';ctx.font='bold 14px Poppins';ctx.textAlign='center';ctx.fillText('day 21 🎥',0,-150);});
  pup({kind:'girl',x:740,y:G+10,s:1.2,flip:-1,look:[-.4,.1],eyes:'happy',mouth:'smile',blush:.5});''',
'''  room('#f6d7c6','#d6a286');
  phoneMock(560,1000,.6,0,()=>{ctx.fillStyle='#eef0f5';ctx.fillRect(-70,-290,140,280);ctx.fillStyle='#3b2a20';ctx.font='13px Poppins';ctx.textAlign='left';ctx.fillText('hey! loved your',-58,-230);ctx.fillText('profile, this is',-58,-210);ctx.fillText('so random but...',-58,-190);});
  pup({kind:'girl',x:300,y:G+10,s:1.25,look:[.5,-.2],eyes:'happy',mouth:'smile',blush:.5});
  pup({kind:'boy',x:820,y:G+10,s:1.2,flip:-1,look:[-.5,-.2],eyes:'open',mouth:'smile'});''',
SHARE,
'''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  pup({kind:'girl',x:420,y:G+10,s:1.25,look:[.3,.4],brows:'sad',mouth:'flat',earLift:-.3});
  pup({kind:'boy',x:800,y:G+10,s:1.2,flip:-1,look:[-.3,.4],brows:'sad',mouth:'flat'});
  if(u>.8)raincloudSmall(610,610,win(u,.8,9)*.5);''',
HUG,
]
SCENES = spec(BODY_LINES, D, [{'real':'🤔'},{'real':'🤍'},{'camera':'🎥'},{'once':'💌'},{'them':'💌'},{'shame':'🚩'},{"didn't":'🤍'}])
IG_LINE = "The first message. The three weeks of talking. The saved screenshot. Every love story starts its own way... Want to know yours? There's a sixty second test in our bio. Take it together."
IG_CAPS = C(IG_LINE, {'message':'💌','yours?':'🤍','bio':'🔗'})
IG_RESULT = "Words of Affirmation"
TT_LINE = TT_STD
