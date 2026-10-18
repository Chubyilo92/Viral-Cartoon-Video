import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD, C
TITLE = "when she's the one"
BODY_LINES = [
"When she's the one... you stop looking. Not because you can't. Because there's no one else you want to see.",
"Something good happens... and she's the first person you want to tell.",
"Her bad days start feeling like your problem too. And you don't mind one bit.",
"Every future you picture... she's already in it.",
"If she's the one for you... send this to her.",
"But if you're still keeping your options open... she's not the one. And you already know it.",
"Because when she's the one... nobody else even feels like an option.",
]
D = [
'''  room('#d9b9c9','#a98496','rgba(255,255,255,.1)');
  pup({kind:'girl',x:180,y:G+10,s:.75,flip:1,look:[.6,0],eyes:'happy',mouth:'smile',blush:.5});
  pup({kind:'girl',x:900,y:G+10,s:.75,flip:-1,look:[-.6,0],eyes:'happy',mouth:'smile',blush:.5});
  pup({kind:'girl',x:640,y:G+10,s:1.3,flip:-1,look:[-.5,0],eyes:'happy',mouth:'smile',blush:.5,tilt:-.05});
  pup({kind:'boy',x:400,y:G+10,s:1.35,look:[.6,0],eyes:'happy',mouth:'smile',blush:.4,tilt:.05});
  if(u>2)floatHearts(520,820,2,u,4,140);''',
'''  room('#cfe3ec','#98b6c2');
  const j=P(u,.4,1.2);
  pup({kind:'boy',x:440,y:G+10,s:1.4,bob:-Math.abs(Math.sin(u*7))*14*j,look:[.4,-.2],eyes:'happy',mouth:'smile',wag:.6});
  phoneMock(720,980,.5,.1,()=>{ctx.fillStyle='#fbdfe4';ctx.fillRect(-70,-290,140,280);heart(0,-180,40,'#ec7489');ctx.fillStyle='#3a2a2a';ctx.font='bold 16px Poppins';ctx.textAlign='center';ctx.fillText('calling her 📞',0,-110);});
  sparkle(440,660,50*pop(u,.4,.4),win(u,.4,5));''',
'''  room('#e9ceb8','#c39a76',1180,'rgba(255,255,255,.2)');
  const w=P(u,1.6,3.0);
  pup({kind:'girl',x:340,y:G+10,s:1.3,look:[.3,.3],brows:w<1?'sad':undefined,eyes:w>=1?'happy':'open',mouth:w>=1?'smile':'flat'});
  if(w<1)raincloudSmall(340,700,1-w);
  pup({kind:'boy',x:lerp(900,640,w),y:G+10,s:1.3,flip:-1,look:[-.5,0],eyes:'happy',mouth:'smile'});
  mug(lerp(860,520,w),1090,.9);''',
'''  room('#f1d5b0','#caa070');
  pup({kind:'boy',x:300,y:G+10,s:1.3,look:[.3,-.5],eyes:'closed',mouth:'smile',blush:.3,tilt:.05});
  const k=pop(u,.6,.6);
  ctx.save();ctx.translate(680,560);ctx.scale(k,k);cloud(0,0,1.6,'#fffaf0');
  blob(rectPts(-90,-30,180,110,8),'#f3b9a0',{lw:4});ctx.beginPath();ctx.moveTo(-110,-30);ctx.lineTo(0,-110);ctx.lineTo(110,-30);ctx.closePath();ctx.fillStyle='#c46b5a';ctx.fill();ctx.stroke();
  heart(-30,30,26,'#ec7489');heart(30,30,26,'#ec7489');ctx.restore();''',
SHARE,
'''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  pup({kind:'boy',x:340,y:G+10,s:1.3,look:[.5,.5],eyes:'open',mouth:'flat'});
  phoneMock(560,1010,.42,.1,()=>{ctx.fillStyle='#dfe4ee';ctx.fillRect(-70,-290,140,280);const o=(u*60)%140;ctx.fillStyle='#f0a0b4';ctx.fillRect(-60+o-70,-250,110,150);});
  pup({kind:'girl',x:820,y:G+10,s:1.2,flip:-1,look:[-.6,.2],brows:'sad',mouth:'flat',earLift:-.3});
  if(u>1)raincloudSmall(820,720,win(u,1,9)*.7);''',
HUG,
]
SCENES = spec(BODY_LINES, D, [{'see':'🤍'},{'tell':'📞'},{'mind':'☕'},{'in it':'🏡'},{'her':'💌'},{'know it':'🚩'},{'option':'🤍'}])
IG_LINE = "The first call. The bad days. The future. Everyone shows love their own way... Want to know how she feels it? There's a sixty second test in our bio. Take it together."
IG_CAPS = C(IG_LINE, {'call':'📞','feels it?':'🤍','bio':'🔗'})
IG_RESULT = "Quality Time"
TT_LINE = TT_STD
LINE_SPEED = {4: 0.74}
