import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD, C
from _r3props import R3_PROPS
TITLE = "the charger she carries for you"
PRELUDE = R3_PROPS
LINE_SPEED = {4: 1.05}  # voicecheck: line 5 ended rising (+12.2%) at 0.9
BAG = '''  ctx.save();ctx.translate(x,y);
  blob(rectPts(-70,-140,140,140,20),'#c9703f',{lw:5});
  ctx.strokeStyle='#8a4a28';ctx.lineWidth=8;ctx.beginPath();ctx.moveTo(-50,-140);ctx.quadraticCurveTo(-50,-200,0,-200);ctx.quadraticCurveTo(50,-200,50,-140);ctx.stroke();
  ctx.restore();'''
CABLE = '''  ctx.save();ctx.translate(x,y);
  ctx.strokeStyle='#e8484f';ctx.lineWidth=9;ctx.lineCap='round';
  ctx.beginPath();ctx.moveTo(0,0);ctx.quadraticCurveTo(30,-40,10,-80);ctx.quadraticCurveTo(-10,-110,20,-140);ctx.stroke();
  blob(rectPts(6,-160,26,24,4),'#2b2830',{lw:3});
  ctx.restore();'''
BATTERY = '''  ctx.save();ctx.translate(x,y);
  blob(rectPts(-30,-16,60,32,6),'#fff',{lw:4});
  ctx.fillStyle='#e8484f';ctx.fillRect(-26,-12,6,24);
  ctx.fillStyle='#2b2830';ctx.fillRect(32,-8,8,16);
  ctx.restore();'''
FULL_BATTERY = '''  ctx.save();ctx.translate(x,y);
  blob(rectPts(-30,-16,60,32,6),'#fff',{lw:4});
  ctx.fillStyle='#4caf6e';ctx.fillRect(-26,-12,52,24);
  ctx.fillStyle='#2b2830';ctx.fillRect(32,-8,8,16);
  ctx.restore();'''
BODY_LINES = [
"When a girl carries a charger that doesn't fit her phone, she's not being forgetful.",
"It fits yours. She bought it just for you.",
"She'll dig through her whole bag at two percent battery and hand it over without a word.",
"She replaces it the second the cable frays, before you've even noticed it's wearing out.",
"If you've survived a night out because of the charger in her bag... send this to her.",
"But if you've never once said thank you for it... don't be surprised the night it isn't there.",
"Because a girl who carries your charger... is quietly making sure you never run out.",
]
D = [
'''  room('#f1d5b0','#caa070');
  ''' + BAG.replace('x,y', '560,G+10') + '''
  ''' + CABLE.replace('x,y', '560,G-130') + '''
  pup({kind:'girl',x:300,y:G+10,s:1.25,look:[.4,-.2],eyes:'open',mouth:'flat'});
  pup({kind:'boy',x:820,y:G+10,s:1.15,flip:-1,look:[-.4,-.2],eyes:'wide',mouth:'o'});''',
'''  room('#e8d8c8','#c2a98f');
  ''' + BAG.replace('x,y', '540,G+10') + '''
  ''' + CABLE.replace('x,y', '540,G-130') + '''
  pup({kind:'girl',x:300,y:G+10,s:1.25,look:[.5,-.3],eyes:'happy',mouth:'smile',blush:.3});''',
'''  room('#cfe3ec','#98b6c2');
  ''' + BAG.replace('x,y', '460,G+10') + '''
  ctx.save();ctx.strokeStyle='#e8484f';ctx.lineWidth=8;ctx.lineCap='round';
  ctx.beginPath();ctx.moveTo(500,G-110);ctx.quadraticCurveTo(650,G-170,780,G-90);ctx.stroke();
  ctx.restore();
  pup({kind:'girl',x:300,y:G+10,s:1.2,look:[.6,.2],eyes:'squint',mouth:'flat',tilt:.08});
  pup({kind:'boy',x:820,y:G+10,s:1.15,flip:-1,look:[-.4,-.1],eyes:'wide',mouth:'o',blush:.1});
  ''' + BATTERY.replace('x,y', '820,G-420') + '''''',
'''  room('#e3c9a0','#bf9670');
  ''' + BAG.replace('x,y', '780,G+10') + '''
  ''' + CABLE.replace('x,y', '780,G-20') + '''
  ctx.save();ctx.strokeStyle='#e8484f';ctx.lineWidth=9;ctx.lineCap='round';
  ctx.beginPath();ctx.moveTo(195,G-8);ctx.quadraticCurveTo(222,G-28,250,G-10);ctx.quadraticCurveTo(264,G+2,280,G-14);ctx.stroke();
  ctx.restore();
  blob(rectPts(172,G-24,24,22,4),'#2b2830',{lw:3});
  ctx.save();ctx.strokeStyle='#8a4a28';ctx.lineWidth=3;ctx.lineCap='round';
  ctx.beginPath();ctx.moveTo(280,G-14);ctx.lineTo(296,G-30);ctx.moveTo(280,G-14);ctx.lineTo(300,G-10);ctx.moveTo(280,G-14);ctx.lineTo(292,G+6);ctx.stroke();
  ctx.restore();
  pup({kind:'girl',x:540,y:G+10,s:1.2,look:[-.4,-.2],eyes:'open',mouth:'flat',tilt:.02});''',
SHARE,
'''  room('#333c54','#28304a','rgba(255,255,255,.05)');
  ctx.save();ctx.strokeStyle='#9aa8c2';ctx.lineWidth=6;ctx.globalAlpha=.8;ctx.setLineDash([12,10]);
  ctx.strokeRect(760,G-140,140,140);
  ctx.restore();
  ''' + BATTERY.replace('x,y', '300,G-420') + '''
  pup({kind:'boy',x:300,y:G+10,s:1.2,look:[.3,-.3],brows:'sad',mouth:'flat',shadow:false});''',
'''  room('#f1d5b0','#caa070');
  ''' + BAG.replace('x,y', '450,G+10') + '''
  ctx.save();ctx.strokeStyle='#e8484f';ctx.lineWidth=8;ctx.lineCap='round';
  ctx.beginPath();ctx.moveTo(480,G-130);ctx.quadraticCurveTo(620,G-180,780,G-100);ctx.stroke();
  ctx.restore();
  pup({kind:'girl',x:340,y:G+10,s:1.25,flip:1,look:[.4,-.1],eyes:'happy',mouth:'smile',blush:.3});
  pup({kind:'boy',x:780,y:G+10,s:1.2,flip:-1,look:[-.4,-.1],eyes:'happy',mouth:'smile',blush:.3});
  ''' + FULL_BATTERY.replace('x,y', '780,G-420') + '''
  if(u>.6)floatHearts(560,700,.6,u,3,130);''',
]
SCENES = spec(BODY_LINES, D, [{'forgetful':'🔌'},{'for you':'🤍'},{'without a word':'🔋'},{'wearing out':'🔌'},{'to her':'💌'},{'there':'🚩'},{'run out':'🤍'}])
IG_LINE = "The charger that only fits your phone. The bag she digs through at two percent. The cable she quietly replaces. Everyone shows love their own way... Want to know yours? There's a sixty second test in our bio. Take it together."
IG_CAPS = C(IG_LINE, {'charger':'🔌','yours?':'🤍','bio':'🔗'})
IG_RESULT = "Acts of Service"
TT_LINE = TT_STD
