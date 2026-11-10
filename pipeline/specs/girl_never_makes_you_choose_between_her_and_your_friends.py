import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD, C
from _r3props import R3_PROPS
TITLE = "when a girl never makes you choose"
PRELUDE = R3_PROPS
LINE_SPEED = {4: 0.8}
# PRESSURE_PHONE is the deliberate mirror of line 4's calm "no new texts" phone: a different,
# controlling partner's phone (never the bow-wearing girl from panels 1-5/7), so the dark turn in
# line 6 reads as "a different, worse partner" rather than the same couple souring.
PRESSURE_PHONE = '''  ctx.save();ctx.translate(x,y);
  blob(rectPts(-112,-232,224,464,30),'#2b2830',{lw:6});
  blob(rectPts(-96,-206,192,412,16),'#f4f1ec',{lw:0,stroke:false});
  ctx.fillStyle='#e8484f';ctx.beginPath();ctx.roundRect(-88,-172,176,52,14);ctx.fill();
  ctx.fillStyle='#fffaf0';ctx.font='bold 19px Poppins';ctx.textAlign='center';ctx.textBaseline='middle';
  ctx.fillText('where are you?',0,-146);
  ctx.fillStyle='#e8484f';ctx.beginPath();ctx.roundRect(-88,-100,176,52,14);ctx.fill();
  ctx.fillStyle='#fffaf0';ctx.fillText("it's me or them",0,-74);
  ctx.fillStyle='#e8484f';ctx.beginPath();ctx.arc(96,-210,30,0,7);ctx.fill();
  ctx.strokeStyle=INK;ctx.lineWidth=3;ctx.beginPath();ctx.arc(96,-210,30,0,7);ctx.stroke();
  ctx.fillStyle='#fffaf0';ctx.font='bold 26px Poppins';ctx.fillText('12',96,-209);
  ctx.restore();'''
BODY_LINES = [
"When a girl never makes you choose between her and your friends, she's not just being easygoing.",
"She asks about them by name and actually means it.",
"She tells you to go, even when she'd rather you stayed.",
"She sends you out the door with \"have fun\"... and not one text asking when you'll be back.",
"If she's ever told you to go have fun with your friends and meant it... send this to her.",
"But if you ever feel like you have to pick a side... that's not love. That's control.",
"Because a girl who never makes you choose... knows you'll always come home.",
]
D = [
'''  room('#e8d8c8','#c2a98f');
  pup({kind:'girl',x:340,y:G+10,s:1.2,eyes:'happy',mouth:'smile',blush:.2,look:[.3,-.1]});
  pup({kind:'boy',x:760,y:G+10,s:1.22,flip:-1,eyes:'open',mouth:'smile',look:[-.3,-.1]});''',
'''  room('#cfe3ec','#98b6c2');
  pup({kind:'girl',x:330,y:G+10,s:1.25,eyes:'happy',mouth:'smile',blush:.2,look:[.3,-.1]});
  pup({kind:'boy',x:760,y:G+10,s:1.2,flip:-1,eyes:'open',mouth:'smile',look:[-.3,-.1]});
  if(u>.4){ctx.save();ctx.globalAlpha=win(u,.4,9);bubbleText(540,560,"how's Marcus doing?",1,.6);ctx.restore();}''',
'''  room('#f1d5b0','#caa070');
  pup({kind:'boy',x:760,y:G+10,s:1.2,flip:-1,eyes:'happy',mouth:'smile',look:[-.3,-.1]});
  pup({kind:'girl',x:340,y:G+10,s:1.2,eyes:'open',mouth:'smile',blush:.2,look:[.3,-.1]});
  if(u>.4){ctx.save();ctx.globalAlpha=win(u,.4,9);bubbleText(540,560,"go, have fun!",1,.62);ctx.restore();}''',
'''  room('#394867','#2c3652');
  bigPhone(700,780,1.0,()=>{ctx.fillStyle='#8a8f9a';ctx.font='bold 26px Poppins';ctx.textAlign='center';ctx.fillText('no new texts',0,0);});
  pup({kind:'girl',x:340,y:G+10,s:1.15,eyes:'happy',mouth:'smile',blush:.2,look:[.3,-.1]});''',
SHARE,
'''  room('#333c54','#28304a','rgba(255,255,255,.05)');
  pup({kind:'boy',x:330,y:G+10,s:1.2,look:[.3,-.1],brows:'sad',mouth:'flat',shadow:false});
  ''' + PRESSURE_PHONE.replace('x,y', '740,G-280') + '''''',
'''  room('#f1d5b0','#caa070');
  pup({kind:'girl',x:380,y:G+10,s:1.2,look:[.3,-.3],eyes:'happy',mouth:'smile',blush:.3});
  pup({kind:'boy',x:680,y:G+10,s:1.2,flip:-1,look:[-.3,-.3],eyes:'happy',mouth:'smile',blush:.3});
  sparkle(540,G-440,24,win(u,.2,3.8));
  heart(500,G-400,20,'#ec7489',1,-.1);
  if(u>.6)floatHearts(530,700,.6,u,3,130);''',
]
SCENES = spec(BODY_LINES, D, [{'easygoing':'🤍'},{'means it':'🗨️'},{'stayed':'👋'},{'be back':'📱'},{'to her':'💌'},{'control':'🚩'},{'come home':'🤍'}])
IG_LINE = "The friend's name she actually remembers. The \"go have fun\" she means every time. The text she never sends asking when you'll be back. Everyone shows love their own way... Want to know yours? There's a sixty second test in our bio. Take it together."
IG_CAPS = C(IG_LINE, {'remembers':'🤍','yours?':'🤍','bio':'🔗'})
IG_RESULT = "Trust"
TT_LINE = TT_STD
