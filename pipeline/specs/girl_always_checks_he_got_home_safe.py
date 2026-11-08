import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD, C
from _r3props import R3_PROPS
TITLE = "when a girl waits up for you"
PRELUDE = R3_PROPS
LINE_SPEED = {1: 0.85}
BODY_LINES = [
"She asks for one thing every single time you leave: text me when you're home.",
"You used to find it a bit much, a bit over the top.",
"Then one night you forgot, and found four missed calls and her still awake on the sofa, pretending she wasn't waiting.",
"She wasn't angry. She just couldn't sleep until she knew.",
"Send this to the one who always forgets to text.",
"And if you're the one always asking: you're not too much. You just love someone who forgets to text.",
"Send the text. Four seconds, and she finally goes to sleep.",
]
D = [
'''  room('#e8d8c8','#c2a98f');
  ctx.save();ctx.fillStyle='#caa070';ctx.fillRect(470,G-230,140,240);ctx.strokeStyle=INK;ctx.lineWidth=5;ctx.strokeRect(470,G-230,140,240);
  ctx.fillStyle='#8a6a4a';ctx.beginPath();ctx.arc(590,G-110,6,0,7);ctx.fill();ctx.restore();
  pup({kind:'girl',x:340,y:G+10,s:1.25,eyes:'happy',mouth:'smile',blush:.3,look:[.3,-.1]});
  pup({kind:'boy',x:760,y:G+10,s:1.2,eyes:'open',mouth:'smile',look:[-.3,-.1]});
  if(u>.4){ctx.save();ctx.globalAlpha=win(u,.4,9);bubbleText(450,580,"text me when you're home!",1,.6);ctx.restore();}''',
'''  room('#cfe3ec','#9fc0cc');
  pup({kind:'boy',x:540,y:G+10,s:1.3,eyes:'squint',mouth:'flat',look:[0,-.1]});
  if(u>.4){ctx.save();ctx.globalAlpha=win(u,.4,9);bubbleText(540,590,"a bit much...",1,.65);ctx.restore();}''',
'''  room('#33405e','#2a3550',1180,'rgba(255,255,255,.05)');
  blob(rectPts(220,G-170,420,180,30),'#c98fae');
  pup({kind:'girl',x:420,y:G-30,s:1.1,eyes:'open',mouth:'flat',look:[.3,-.1]});
  ctx.save();ctx.translate(560,600);ctx.globalAlpha=.85+Math.sin(u*6)*.15; blob(rectPts(-116,-40,232,80,16),'#fffaf0',{lw:4});
  ctx.fillStyle=INK;ctx.font='bold 26px Poppins';ctx.textAlign='center';ctx.fillText('4 missed calls 📱',0,8); ctx.restore();''',
'''  room('#2a3550','#20283f',1180,'rgba(255,255,255,.04)');
  pup({kind:'girl',x:540,y:G+10,s:1.6,eyes:'open',mouth:'flat',look:[0,-.05]});''',
SHARE,
'''  room('#f6e3d0','#d9b48f');
  pup({kind:'girl',x:540,y:G+10,s:1.3,eyes:'happy',mouth:'smile',blush:.3,look:[0,-.1]});
  if(u>.4){ctx.save();ctx.globalAlpha=win(u,.4,9);bubbleText(540,590,"you're not too much 🤍",1,.6);ctx.restore();}''',
'''  room('#33405e','#2a3550',1180,'rgba(255,255,255,.05)');
  blob(rectPts(220,G-170,420,180,30),'#c98fae');
  pup({kind:'girl',x:420,y:G-30,s:1.1,eyes:'closed',mouth:'smile',blush:.2,look:[0,0]});
  ctx.save();ctx.translate(600,600);ctx.globalAlpha=win(u,.1,9); blob(rectPts(-96,-36,192,72,14),'#fffaf0',{lw:4});
  ctx.fillStyle=INK;ctx.font='bold 24px Poppins';ctx.textAlign='center';ctx.fillText('sent ✓',0,8); ctx.restore();
  if(u>1.2)floatHearts(290,780,1.2,u,5,100);''',
]
SCENES = spec(BODY_LINES, D, [{'home':'📱'},{'the top':'🙄'},{'waiting':'📱'},{'knew':'🤍'},{'to text':'💌'},{'forgets to text':'🤍'},{'to sleep':'💤'}])
IG_LINE = "The text she asks for. The night you forgot. Why she really stays up. Everyone shows love their own way... Want to know yours? There's a sixty second test in our bio. Take it together."
IG_CAPS = C(IG_LINE, {'asks for':'📱','yours?':'🤍','bio':'🔗'})
IG_RESULT = "Acts of Service"
TT_LINE = TT_STD
