import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD, C
TITLE = "a man who's sure about you"
BODY_LINES = [
"A man who's sure about you doesn't keep you guessing. You always know where you stand.",
"He introduces you to his mum early. Not to rush it. Because he's not hiding you.",
"He makes plans for next summer... and you're already in them.",
"He texts back. Not every second. Just enough that you never sit there wondering.",
"If he's sure like this... send this to the girl who's tired of guessing.",
"But if it's been months and you still don't know what you are... that's your answer.",
"Because a man who's sure about you never makes you ask.",
]
D = [
'''  room('#f6d7c6','#d6a286');
  const h=P(u,.6,1.6);
  pup({kind:'girl',x:lerp(640,600,h),y:G+10,s:1.35,flip:-1,look:[-.4,0],eyes:'happy',mouth:'smile',blush:.5,tilt:-.06});
  pup({kind:'boy',x:380,y:G+10,s:1.35,look:[.5,0],eyes:'happy',mouth:'smile',blush:.3,tilt:.05,paw:{x:140,y:-80,k:h}});
  sparkle(500,700,46*pop(u,1.6,.4),win(u,1.6,6));
  if(u>2)floatHearts(500,820,2,u,4,140);''',
'''  room('#e3c9a0','#bf9670');plant(980,G+6,.9);
  pup({kind:'girl',x:770,y:G+10,s:1.4,flip:-1,look:[-.6,0],eyes:'happy',mouth:'smile',blush:.6,tilt:-.05});
  pup({kind:'boy',x:200,y:G+10,s:1.15,look:[.6,0],eyes:'happy',mouth:'smile',wag:.3});
  pup({kind:'girl',x:460,y:G+10,s:1.1,look:[.6,0],eyes:'open',mouth:'smile',blush:.6,tilt:.04});
  if(u>1.2){const k=pop(u,1.2,.4);ctx.save();ctx.globalAlpha=win(u,1.2,8);bubbleText(700,660,"so THIS is her! 🥹",1,.85*k);ctx.restore();}''',
'''  room('#cfe3ec','#98b6c2');
  windowBox(560,330,340,270,(w,h)=>{ctx.fillStyle='#8fd0f0';ctx.fillRect(0,0,w,h);ell(w*.7,h*.3,40,40,'#ffd75e',{lw:3});});
  pup({kind:'boy',x:320,y:G+10,s:1.3,look:[.4,-.3],eyes:'happy',mouth:'smile',tilt:.05});
  pup({kind:'girl',x:660,y:G+10,s:1.25,flip:-1,look:[-.4,0],eyes:'happy',mouth:'smile',blush:.5});
  if(u>.8){const k=pop(u,.8,.4);ctx.save();ctx.globalAlpha=win(u,.8,8);bubbleText(330,700,"us, next summer ☀️✈️",1,.85*k);ctx.restore();}''',
'''  room('#e9ceb8','#c39a76',1180,'rgba(255,255,255,.2)');
  const r=P(u,1.6,2.2);
  pup({kind:'girl',x:420,y:G+10,s:1.4,look:[.4,.4],eyes:r>0?'happy':'open',mouth:r>0?'smile':'flat',blush:.5*r});
  phoneMock(700,1000,.5,.08,()=>{ctx.fillStyle='#f5f2ee';ctx.fillRect(-70,-290,140,280);if(u>1.6){ctx.fillStyle='#ec7489';ctx.beginPath();ctx.roundRect(-60,-250,110,40,14);ctx.fill();ctx.fillStyle='#fff';ctx.font='bold 15px Poppins';ctx.textAlign='left';ctx.fillText('home safe? 🤍',-52,-224);}});
  if(u>2.4)floatHearts(440,820,2.4,u,3,120);''',
SHARE,
'''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  pup({kind:'girl',x:400,y:G+10,s:1.3,look:[.4,.5],brows:'sad',mouth:'flat',earLift:-.3});
  phoneMock(680,1020,.45,.06,()=>{ctx.fillStyle='#dfe4ee';ctx.fillRect(-70,-290,140,280);ctx.fillStyle='#9fb4d8';ctx.beginPath();ctx.roundRect(-60,-250,90,34,12);ctx.fill();});
  if(u>.8){ctx.save();ctx.globalAlpha=win(u,.8,8);bubbleText(400,690,"so... what are we? 🤷‍♀️",1,.85);ctx.restore();}
  if(u>1.5)raincloudSmall(400,560,win(u,1.5,9)*.6);''',
HUG,
]
SCENES = spec(BODY_LINES, D, [{'stand':'🤍'},{'mum':'🥹'},{'summer':'☀️'},{'wondering':'📱'},{'guessing':'💌'},{'answer':'🚩'},{'ask':'🤍'}])
IG_LINE = "Meeting his mum. Next summer. Home safe. Every man shows love his own way... Want to know his? There's a sixty second test in our bio. Take it together."
IG_CAPS = C(IG_LINE, {'mum':'🥹','his?':'🤍','bio':'🔗'})
IG_RESULT = "Quality Time"
TT_LINE = TT_STD
