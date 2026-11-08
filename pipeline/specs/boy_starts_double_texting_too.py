import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD, C
from _r3props import R3_PROPS
TITLE = "when a boy double-texts back"
PRELUDE = R3_PROPS
LINE_SPEED = {}
BODY_LINES = [
"He used to roll his eyes every time you double-texted. Now he's the one sending three in a row.",
"He used to call it \"needy\" to his mates, every single time.",
"He still hasn't told them he does it himself now, every time you go quiet for too long.",
"He waits exactly four minutes before he caves and sends the second one.",
"If you're the one who's caught him mid-send, deleting it, then sending it anyway... send this to him.",
"But the day you go quiet and he doesn't send the second one... he's not finally playing it cool. He's stopped noticing you've gone quiet.",
"Because a boy who finally double-texts back... just learned the thing he used to tease you for.",
]
D = [
'''  room('#e3c9a0','#bf9670');
  bigPhone(700,780,1.0,()=>{chatBub(-100,-200,170,92,false);chatBub(-100,-96,190,72,false);});
  pup({kind:'boy',x:330,y:G+10,s:1.25,eyes:'squint',mouth:'flat',look:[.4,-.1]});''',
'''  room('#e8d8c8','#c2a98f');
  pup({kind:'boy',x:540,y:G+10,s:1.3,mouth:'open',eyes:'open',look:[0,-.1]});
  if(u>.5){ctx.save();ctx.globalAlpha=win(u,.5,9);bubbleText(540,650,"so needy, man 🙄",1,.85);ctx.restore();}
  ctx.save();ctx.translate(820,560);
  blob(rectPts(-104,-38,208,76,14),'#fffaf0',{lw:4});
  ctx.fillStyle=INK;ctx.font='bold 24px Poppins';ctx.textAlign='center';ctx.fillText('🙄 his mates',0,10);
  ctx.restore();''',
'''  room('#cfe3ec','#98b6c2');
  bigPhone(620,780,1.0,()=>{chatBub(-100,-210,170,80,true);chatBub(-100,-110,150,60,true);chatBub(-100,-28,130,60,true);});
  pup({kind:'boy',x:280,y:G+10,s:1.2,mouth:'flat',look:[.5,-.1]});''',
'''  room('#f1d5b0','#caa070');
  pup({kind:'boy',x:320,y:G+10,s:1.3,eyes:'wide',mouth:'flat',look:[.3,-.2]});
  bigPhone(780,780,.9,()=>{chatBub(-80,-180,160,70,true);});
  ctx.save();ctx.translate(380,560);
  blob(rectPts(-100,-40,200,80,16),'#fffaf0',{lw:4});
  ctx.save();ctx.translate(-44,2);ctx.strokeStyle=INK;ctx.lineWidth=5;ctx.lineCap='round';
  ctx.beginPath();ctx.arc(0,0,22,0,7);ctx.stroke();
  ctx.beginPath();ctx.moveTo(0,0);ctx.lineTo(0,-14);ctx.stroke();
  ctx.beginPath();ctx.moveTo(0,0);ctx.lineTo(12,6);ctx.stroke();
  ctx.restore();
  ctx.fillStyle=INK;ctx.font='bold 30px Poppins';ctx.textAlign='center';ctx.fillText('4 min',26,12);
  ctx.restore();''',
'''  room('#dfe6d0','#b9c49f');
  bigPhone(680,780,1.1,()=>{chatBub(-100,-180,180,70,true);
    ctx.save();ctx.strokeStyle='#c0392b';ctx.lineWidth=10;ctx.lineCap='round';
    ctx.beginPath();ctx.moveTo(-100,-180);ctx.lineTo(80,-110);ctx.stroke();
    ctx.beginPath();ctx.moveTo(-100,-110);ctx.lineTo(80,-180);ctx.stroke();ctx.restore();});
  pup({kind:'boy',x:300,y:G+10,s:1.2,eyes:'wide',mouth:'o',brows:'sad',look:[.4,-.1],blush:.3});''',
'''  room('#6f6a78','#5a5562','rgba(255,255,255,.05)');
  pup({kind:'boy',x:800,y:G+10,s:1.15,flip:-1,eyes:'open',mouth:'flat',look:[-.3,.3]});
  bigPhone(560,800,.75,()=>{});
  pup({kind:'girl',x:300,y:G+10,s:1.15,mouth:'flat',look:[.2,0]});
  if(u>1.2)raincloudSmall(300,G-430,win(u,1.2,9)*.6);''',
HUG,
]
SCENES = spec(BODY_LINES, D, [{'row':'📱'},{'mates':'🙄'},{'long':'📱'},{'second one':'⏱️'},{'to him':'💌'},{'quiet':'🩶'},{'tease you for':'🤍'}])
IG_LINE = "The eye-roll that turned into the second text. The four-minute wait. The one he finally learned. Everyone shows love their own way... Want to know yours? There's a sixty second test in our bio. Take it together."
IG_CAPS = C(IG_LINE, {'roll':'📱','yours?':'🤍','bio':'🔗'})
IG_RESULT = "Words of Affirmation"
TT_LINE = TT_STD
