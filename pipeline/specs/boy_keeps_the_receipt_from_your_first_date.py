import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD, C
from _r3props import R3_PROPS
TITLE = "the receipt he still keeps"
PRELUDE = R3_PROPS
LINE_SPEED = {}
WALLET = '''  ctx.save();ctx.translate(x,y);
  blob(rectPts(-62,-52,124,104,10),'#6b4a35',{lw:5});
  ctx.strokeStyle='#4a3022';ctx.lineWidth=3;ctx.beginPath();ctx.moveTo(0,-52);ctx.lineTo(0,52);ctx.stroke();
  blob(rectPts(-48,-40,40,30,4),'#8a6246',{lw:2.5});
  ctx.restore();'''
RECEIPT = '''  ctx.save();ctx.translate(x,y);ctx.rotate(.05);
  blob(rectPts(-26,-66,52,132,4),'#fffaf0',{lw:3.5});
  ctx.strokeStyle='#e8e0d0';ctx.lineWidth=2.5;
  for(let i=0;i<5;i++){ctx.beginPath();ctx.moveTo(-16,-46+i*20);ctx.lineTo(16,-46+i*20);ctx.stroke();}
  ctx.restore();'''
FOLDED = '''  ctx.save();ctx.translate(x,y);ctx.rotate(-.08);
  blob(rectPts(-15,-22,30,44,3),'#fffaf0',{lw:3});
  ctx.strokeStyle='#e8e0d0';ctx.lineWidth=2;
  ctx.beginPath();ctx.moveTo(-9,-7);ctx.lineTo(9,-7);ctx.moveTo(-9,3);ctx.lineTo(9,3);ctx.stroke();
  ctx.restore();'''
BIN = '''  ctx.save();ctx.translate(x,y);
  ctx.fillStyle='#9a9a9a';ctx.strokeStyle='#6a6a6a';ctx.lineWidth=5;ctx.lineJoin='round';
  ctx.beginPath();ctx.moveTo(-34,16);ctx.lineTo(-54,-110);ctx.lineTo(54,-110);ctx.lineTo(34,16);ctx.closePath();
  ctx.fill();ctx.stroke();
  ctx.strokeStyle='#7f7f7f';ctx.lineWidth=2.5;
  ctx.beginPath();ctx.moveTo(-26,6);ctx.lineTo(-38,-102);ctx.moveTo(0,10);ctx.lineTo(0,-106);ctx.moveTo(26,6);ctx.lineTo(38,-102);ctx.stroke();
  ctx.strokeStyle='#5a5a5a';ctx.lineWidth=9;ctx.lineCap='round';
  ctx.beginPath();ctx.moveTo(-60,-110);ctx.lineTo(60,-110);ctx.stroke();
  blob([[-34,-128],[-14,-144],[4,-130],[-8,-112],[-30,-114]],'#fffaf0',{lw:3,j:3});
  ctx.strokeStyle='#d8cdb8';ctx.lineWidth=1.5;
  ctx.beginPath();ctx.moveTo(-26,-134);ctx.lineTo(-14,-120);ctx.moveTo(-10,-130);ctx.lineTo(-20,-118);ctx.stroke();
  blob([[16,-144],[38,-134],[40,-116],[20,-108],[6,-122]],'#fffaf0',{lw:3,j:3});
  ctx.strokeStyle='#d8cdb8';ctx.lineWidth=1.5;
  ctx.beginPath();ctx.moveTo(24,-138);ctx.lineTo(34,-122);ctx.moveTo(14,-124);ctx.lineTo(30,-114);ctx.stroke();
  blob([[64,30],[84,22],[88,42],[68,52],[54,40]],'#fffaf0',{lw:3,j:3});
  ctx.strokeStyle='#d8cdb8';ctx.lineWidth=1.5;
  ctx.beginPath();ctx.moveTo(60,38);ctx.lineTo(76,24);ctx.moveTo(72,46);ctx.lineTo(62,30);ctx.stroke();
  ctx.restore();'''
BODY_LINES = [
"When a boy still has the receipt from your first date, he's not just bad at throwing things away.",
"It's folded small, in the same pocket of the same wallet, years later.",
"The ink's almost faded to nothing. He can still tell you what you both ordered.",
"He's thrown away receipts from every other night since... just not that one.",
"If he still has something from your very first date... send this to him.",
"But if you ever laugh at him for keeping it... watch how fast he stops keeping anything.",
"Because a boy who keeps that one receipt... is still holding onto the night everything started.",
]
D = [
'''  room('#f1d5b0','#caa070');
  ''' + WALLET.replace('x,y', '640,G-10') + '''
  ''' + RECEIPT.replace('x,y', '640,G-130') + '''
  pup({kind:'girl',x:300,y:G+10,s:1.25,look:[.5,-.3],eyes:'wide',mouth:'o'});
  pup({kind:'boy',x:780,y:G+10,s:1.2,flip:-1,look:[-.3,-.1],eyes:'open',mouth:'flat'});''',
'''  room('#e8d8c8','#c2a98f');
  ''' + WALLET.replace('x,y', '340,G-20') + '''
  ''' + FOLDED.replace('x,y', '340,G-60') + '''
  pup({kind:'boy',x:680,y:G+10,s:1.3,flip:-1,look:[-.4,-.2],eyes:'open',mouth:'flat',tilt:.03});''',
'''  room('#cfe3ec','#98b6c2');
  ''' + RECEIPT.replace('x,y', '560,G-120') + '''
  pup({kind:'boy',x:700,y:G+10,s:1.2,flip:-1,look:[-.2,-.1],eyes:'squint',mouth:'open'});
  pup({kind:'girl',x:280,y:G+10,s:1.2,look:[.4,-.1],eyes:'happy',mouth:'smile',blush:.2});
  if(u>.5){ctx.save();ctx.globalAlpha=win(u,.5,9);bubbleText(700,560,"fries and a milkshake",1,.6);ctx.restore();}''',
'''  room('#e3c9a0','#bf9670');
  ''' + BIN.replace('x,y', '300,G+10') + '''
  pup({kind:'boy',x:780,y:G+10,s:1.2,flip:-1,look:[-.4,-.1],eyes:'open',mouth:'flat'});
  ''' + FOLDED.replace('x,y', '730,G-110') + '''''',
SHARE,
'''  room('#333c54','#28304a','rgba(255,255,255,.05)');
  pup({kind:'boy',x:560,y:G+10,s:1.2,look:[0,-.1],brows:'sad',mouth:'flat',shadow:false});''',
'''  room('#f1d5b0','#caa070');
  pup({kind:'girl',x:380,y:G+10,s:1.2,look:[.3,-.3],eyes:'happy',mouth:'smile',blush:.3});
  pup({kind:'boy',x:680,y:G+10,s:1.2,flip:-1,look:[-.3,-.3],eyes:'happy',mouth:'smile',blush:.3});
  ''' + RECEIPT.replace('x,y', '530,G-440') + '''
  sparkle(552,G-491,22,win(u,.2,3.8));
  heart(500,G-400,20,'#ec7489',1,-.1);
  if(u>.6)floatHearts(530,700,.6,u,3,130);''',
]
SCENES = spec(BODY_LINES, D, [{'throwing things away':'👛'},{'years later':'🧾'},{'both ordered':'🍟'},{'just not that one':'🗑️'},{'to him':'💌'},{'keeping anything':'🚩'},{'everything started':'🤍'}])
IG_LINE = "The receipt folded small in the same pocket. The order he still remembers by heart. The one he never throws away. Everyone shows love their own way... Want to know yours? There's a sixty second test in our bio. Take it together."
IG_CAPS = C(IG_LINE, {'receipt':'🧾','yours?':'🤍','bio':'🔗'})
IG_RESULT = "Receiving Gifts"
TT_LINE = TT_STD
