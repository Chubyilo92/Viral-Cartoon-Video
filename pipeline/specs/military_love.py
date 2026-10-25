import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD, C
TITLE = "when you love someone who serves"
BODY_LINES = [
"When you love someone who serves, the goodbyes don't get easier, you get better at them.",
"Not because distance stops hurting. Because it was never going to be why you stopped.",
"You keep a countdown on your phone that only one person asks about.",
"They call the second they land, before they grab their bag.",
"If you've loved someone through deployment and still run to the door every time... send this to the one counting down with you.",
"But if you can't trust them the second they're out of sight... that's not love, that's a leash.",
"Because loving someone who serves... isn't about missing them less, it's about waiting well.",
]
D = [
'''  room('#3d4b6c','#303b57','rgba(255,255,255,.05)');
  pup({kind:'girl',x:380,y:G+10,s:1.2,look:[.3,.2],brows:'sad',mouth:'flat'});
  pup({kind:'boy',x:740,y:G+10,s:1.2,flip:-1,look:[-.3,.2],brows:'sad',mouth:'flat'});''',
'''  room('#8fb6c9','#6f98ac');
  pup({kind:'girl',x:400,y:G+10,s:1.2,look:[.3,0],eyes:'open',mouth:'flat'});
  pup({kind:'boy',x:740,y:G+10,s:1.2,flip:-1,look:[-.3,0],eyes:'open',mouth:'flat'});''',
'''  room('#6f6a78','#5a5562','rgba(255,255,255,.05)');
  phoneMock(540,900,.7,0,()=>{ctx.fillStyle='#fde9b0';ctx.fillRect(-70,-280,140,270);ctx.font='bold 46px Poppins';ctx.textAlign='center';ctx.fillStyle='#3d2b1f';ctx.fillText('42',0,-150);ctx.font='16px Poppins';ctx.fillText('days left',0,-110);});''',
'''  room('#cfe3ec','#98b6c2');
  windowBox(760,320,290,230,(w,h)=>{ctx.fillStyle='#8fd0f0';ctx.fillRect(0,0,w,h);});
  pup({kind:'girl',x:380,y:G+10,s:1.3,look:[.4,0],eyes:'happy',mouth:'smile',blush:.5,wag:.5});
  if(u>.7)floatHearts(540,790,.7,u,4,150);''',
SHARE,
'''  room('#6f6a78','#5a5562','rgba(255,255,255,.05)');
  pup({kind:'girl',x:380,y:G+10,s:1.25,look:[.4,.3],brows:'sad',mouth:'flat'});
  pup({kind:'boy',x:760,y:G+10,s:1.2,flip:-1,look:[-.4,.3],brows:'sad',mouth:'flat'});
  if(u>.8){ctx.save();ctx.globalAlpha=win(u,.8,8);bubbleText(560,680,"...who were you texting?",1,.8);ctx.restore();}
  if(u>1.6)raincloudSmall(540,580,win(u,1.6,9)*.6);''',
HUG,
]
SCENES = spec(BODY_LINES, D, [{'better at them':'🤍'},{'you stopped':'🤍'},{'asks about':'📅'},{'their bag':'🤍'},{'with you':'💌'},{'a leash':'🚩'},{'waiting well':'🤍'}])
IG_LINE = "The countdown. The call the second they land. The goodbyes that never get easy. Everyone waits their own way... Want to know yours? There's a sixty second test in our bio. Take it together."
IG_CAPS = C(IG_LINE, {'countdown':'📅','yours?':'🤍','bio':'🔗'})
IG_RESULT = "Physical Touch"
TT_LINE = TT_STD
