import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD, C
from _r3props import R3_PROPS
TITLE = "when a boy downplays the price"
PRELUDE = R3_PROPS
LINE_SPEED = {}
GIFT = '''  ctx.save();ctx.translate(x,y);
  blob(rectPts(-54,-64,108,64,12),'#ec9a6e');
  ctx.save();ctx.strokeStyle='#c9703f';ctx.lineWidth=10;ctx.beginPath();ctx.moveTo(0,-64);ctx.lineTo(0,0);ctx.stroke();
  ctx.beginPath();ctx.moveTo(-54,-32);ctx.lineTo(54,-32);ctx.stroke();ctx.restore();
  blob([[-20,-78],[0,-60],[20,-78],[10,-66],[0,-70],[-10,-66]],'#c9703f',{lw:3.5});
  ctx.restore();'''
TAG = '''  ctx.save();ctx.translate(x,y);ctx.rotate(-.1);
  blob([[-30,-18],[30,-18],[36,0],[30,18],[-30,18]],'#fffaf0',{lw:4});
  ctx.fillStyle=INK;ctx.font='bold 20px Poppins';ctx.textAlign='center';ctx.fillText('£?!',0,6);
  ctx.restore();'''
BODY_LINES = [
"He says \"it wasn't that expensive\" about everything he buys you.",
"Then you find the price tag he forgot to peel off.",
"He said it about a coffee this morning. Nobody asked. It was a coffee.",
"He changes the subject fast whenever you try to actually check the receipt.",
"If he's ever lied to your face about the price of a candle... send this to him.",
"But if you keep insisting on paying him back anyway, down to the penny... you're the reason he's started buying things while you're in the bathroom.",
"Because a boy who says \"it wasn't that expensive\"... just doesn't want a gift to feel like a transaction.",
]
D = [
'''  room('#f1d5b0','#caa070');
  ''' + GIFT.replace('x,y', '620,G+10') + '''
  pup({kind:'boy',x:800,y:G+10,s:1.2,flip:-1,eyes:'squint',mouth:'smile',look:[-.3,-.1]});
  pup({kind:'girl',x:340,y:G+10,s:1.25,eyes:'happy',mouth:'smile',blush:.3,look:[.3,-.1]});
  if(u>.5){ctx.save();ctx.globalAlpha=win(u,.5,9);bubbleText(800,560,"wasn't that expensive",1,.68);ctx.restore();}''',
'''  room('#e8d8c8','#c2a98f');
  ''' + TAG.replace('x,y', '560,G-200') + '''
  pup({kind:'girl',x:360,y:G+10,s:1.25,eyes:'wide',mouth:'o',look:[.3,-.2]});
  pup({kind:'boy',x:800,y:G+10,s:1.2,flip:-1,eyes:'squint',mouth:'flat',look:[-.4,0]});''',
'''  room('#cfe3ec','#98b6c2');
  mug(700,G-10,1);
  pup({kind:'boy',x:400,y:G+10,s:1.25,eyes:'open',mouth:'open',look:[.3,-.1]});
  if(u>.5){ctx.save();ctx.globalAlpha=win(u,.5,9);bubbleText(400,560,"wasn't that expensive",1,.68);ctx.restore();}''',
'''  room('#e3c9a0','#bf9670');
  ''' + TAG.replace('x,y', '620,G-180') + '''
  pup({kind:'girl',x:340,y:G+10,s:1.25,eyes:'squint',mouth:'flat',look:[.4,-.1]});
  pup({kind:'boy',x:800,y:G+10,s:1.2,flip:-1,eyes:'wide',mouth:'o',look:[-.4,.2]});''',
SHARE,
'''  room('#f6d7c6','#d6a286');
  doorFrame(800);
  pup({kind:'boy',x:460,y:G+10,s:1.2,eyes:'squint',mouth:'smile',look:[.2,-.1]});
  ''' + GIFT.replace('x,y', '620,G+10') + '''
  if(u>.5){ctx.save();ctx.globalAlpha=win(u,.5,9);bubbleText(460,560,"quick, before she's back",1,.62);ctx.restore();}''',
HUG,
]
SCENES = spec(BODY_LINES, D, [{'buys you':'🎁'},{'peel off':'🏷️'},{'coffee':'☕'},{'receipt':'🧾'},{'to him':'💌'},{'bathroom':'🤭'},{'transaction':'🤍'}])
IG_LINE = "The price tag he forgot to peel off. The coffee nobody asked about. The receipt he changes the subject about. Everyone shows love their own way... Want to know yours? There's a sixty second test in our bio. Take it together."
IG_CAPS = C(IG_LINE, {'tag':'🏷️','yours?':'🤍','bio':'🔗'})
IG_RESULT = "Receiving Gifts"
TT_LINE = TT_STD
