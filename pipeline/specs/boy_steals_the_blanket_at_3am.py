import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD, C
from _r3props import R3_PROPS
TITLE = "when a boy steals the blanket"
PRELUDE = R3_PROPS
LINE_SPEED = {}
BODY_LINES = [
"3am. You're freezing. He's wrapped in the entire blanket like a burrito.",
"In the morning he swears he never moved, with the evidence still wrapped around his legs.",
"Same crime, every night. Neither of you can explain it.",
"Then, still mostly asleep, he unrolls himself and tucks it back around you without a word.",
"If you've ever woken up cold and caught him already fixing it... send this to him.",
"But the night he steals it and doesn't tuck you back in... he's not asleep. He's pretending.",
"Because a boy who gives the blanket back in his sleep... is looking after you even when he's unconscious.",
]
D = [
'''  bedNight();bedBack();
  pup({kind:'girl',x:340,y:G-90,s:1.15,look:[.3,0],brows:'sad',mouth:'flat'});
  for(const sd of[-1,1])snowflake(340+sd*110,G-330,10,.8);
  pup({kind:'boy',x:740,y:G-110,s:1.2,flip:-1,eyes:'closed',mouth:'flat',tilt:-.1,bob:Math.sin(u*2)*3});
  blob([[600,G-10],[582,G-150],[612,G-260],[700,G-300],[800,G-280],[872,G-180],[882,G-40],[840,G-10]],'#7fa6cf',{lw:5});
  ctx.save();ctx.globalAlpha=.3;
  line([[630,G-220],[650,G-30]],{c:'#ffffff',lw:7});
  line([[760,G-270],[800,G-30]],{c:'#ffffff',lw:7});
  ctx.restore();
  ctx.save();ctx.strokeStyle='#5a85b0';ctx.lineWidth=6;ctx.lineCap='round';
  ctx.beginPath();ctx.moveTo(614,G-250);ctx.quadraticCurveTo(700,G-220,770,G-250);ctx.quadraticCurveTo(840,G-280,862,G-180);ctx.stroke();
  ctx.restore();''',
'''  room('#e8d8c8','#c2a98f');bedBack();
  blanket(640,940,G-200,'#7fa6cf');
  pup({kind:'girl',x:340,y:G-90,s:1.2,eyes:'squint',mouth:'flat',look:[.3,0]});
  pup({kind:'boy',x:740,y:G-110,s:1.2,flip:-1,eyes:'wide',mouth:'o',look:[-.3,0]});
  if(u>.5){ctx.save();ctx.globalAlpha=win(u,.5,9);bubbleText(740,560,"I never moved!",1,.75);ctx.restore();}''',
'''  bedNight();bedBack();
  blanket(650,930,G-200,'#7fa6cf');
  pup({kind:'girl',x:340,y:G-90,s:1.15,brows:'sad',mouth:'flat',look:[.2,0]});
  pup({kind:'boy',x:730,y:G-110,s:1.2,flip:-1,eyes:'closed',mouth:'flat',tilt:-.08});
  zzz(820,G-440,u,.6);''',
'''  bedNight();bedBack();
  blanket(280,940,G-220,'#7fa6cf');
  pup({kind:'girl',x:340,y:G-90,s:1.15,eyes:'closed',mouth:'smile',blush:.2,tilt:.05});
  pup({kind:'boy',x:710,y:G-110,s:1.2,flip:-1,eyes:'closed',mouth:'flat',tilt:-.1});''',
'''  bedNight();bedBack();
  blanket(320,900,G-210,'#7fa6cf');
  pup({kind:'girl',x:340,y:G-90,s:1.15,eyes:'wide',mouth:'o',look:[.3,-.1]});
  pup({kind:'boy',x:720,y:G-110,s:1.2,flip:-1,eyes:'open',mouth:'flat',tilt:-.15,look:[-.2,-.2]});
  ctx.save();ctx.globalAlpha=.35+Math.sin(u*5)*.15;ctx.strokeStyle='#fffaf0';ctx.lineWidth=5;ctx.lineCap='round';
  ctx.beginPath();ctx.moveTo(560,G-200);ctx.lineTo(600,G-160);ctx.stroke();
  ctx.beginPath();ctx.moveTo(580,G-190);ctx.lineTo(620,G-150);ctx.stroke();
  ctx.restore();
  if(u>.5){ctx.save();ctx.globalAlpha=win(u,.5,9);bubbleText(540,560,"send this to him 💌",1,.62);ctx.restore();}''',
'''  room('#4a4558','#3a3648','rgba(255,255,255,.05)');bedBack();
  blanket(640,940,G-200,'#7fa6cf');
  pup({kind:'girl',x:340,y:G-90,s:1.15,brows:'sad',mouth:'flat',look:[.2,0]});
  pup({kind:'boy',x:740,y:G-110,s:1.2,flip:-1,eyes:'closed',mouth:'smile',tilt:-.1});
  ctx.save();ctx.translate(560,G-460);ctx.globalAlpha=.85+Math.sin(u*6)*.15;
  blob(rectPts(-30,-26,60,52,16),'#fffaf0',{lw:3.5});
  ctx.font='40px Poppins';ctx.textAlign='center';ctx.fillText('👁️',0,14);
  ctx.restore();
  if(u>1.2)raincloudSmall(340,G-540,win(u,1.2,9)*.6);''',
'''  bedNight();bedBack();
  blanket(300,900,G-240,'#7fa6cf');
  pup({kind:'girl',x:360,y:G-90,s:1.2,flip:-1,eyes:'happy',mouth:'smile',blush:.4,tilt:-.06,look:[.2,-.1]});
  pup({kind:'boy',x:680,y:G-110,s:1.2,eyes:'closed',mouth:'smile',tilt:.08,blush:.2});
  if(u>1.2)floatHearts(500,G-420,1.2,u,5,140);''',
]
SCENES = spec(BODY_LINES, D, [{'burrito':'🥶'},{'legs':'🙄'},{'explain it':'🌙'},{'a word':'🤍'},{'to him':'💌'},{'pretending':'🩶'},{'unconscious':'🤍'}])
IG_LINE = "The blanket burrito. The denial in the morning. The half-asleep tuck-in. Everyone shows love their own way... Want to know yours? There's a sixty second test in our bio. Take it together."
IG_CAPS = C(IG_LINE, {'burrito':'🥶','yours?':'🤍','bio':'🔗'})
IG_RESULT = "Physical Touch"
TT_LINE = TT_STD
