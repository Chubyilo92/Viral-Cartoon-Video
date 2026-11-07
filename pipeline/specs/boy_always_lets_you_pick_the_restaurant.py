import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD, C
from _r3props import R3_PROPS
TITLE = "when a boy says wherever you want"
PRELUDE = R3_PROPS
LINE_SPEED = {}
TOAST = '''  ctx.save();ctx.translate(x,y);
  blob(rectPts(-40,-70,80,70,10),'#e8b97a');
  blob(rectPts(-34,-62,68,54,8),'#f3d6a0',{stroke:false});
  ctx.restore();'''
BODY_LINES = [
"Ask him where he wants to eat. You already know the answer: \"wherever you want.\"",
"And he has opinions. You've heard him rant to his mates about one bad burger for twenty minutes.",
"He just won't risk picking somewhere you don't like. Not even when you beg him to choose.",
"He'll scroll through five apps pretending to help decide, then land right back on \"wherever you want.\"",
"If you've never once heard him actually name a restaurant first... send this to him.",
"But if you keep saying \"I don't mind, you choose\" right back at him... you're the reason you're both eating toast at 9pm.",
"Because he'd rather eat somewhere he hates than watch you sit through a dinner you didn't pick.",
]
D = [
'''  room('#e3c9a0','#bf9670');
  pup({kind:'girl',x:330,y:G+10,s:1.25,look:[.4,-.1],eyes:'open',mouth:'open'});
  pup({kind:'boy',x:760,y:G+10,s:1.22,flip:-1,eyes:'squint',mouth:'smile',look:[-.3,0]});
  if(u>.5){ctx.save();ctx.globalAlpha=win(u,.5,9);bubbleText(760,650,"wherever you want 🤷",1,.78);ctx.restore();}''',
'''  room('#f1d5b0','#caa070');
  pup({kind:'boy',x:540,y:G+10,s:1.3,mouth:'open',eyes:'wide',look:[0,-.1]});
  if(u>.5){ctx.save();ctx.globalAlpha=win(u,.5,9);bubbleText(540,650,"worst burger of my life",1,.78);ctx.restore();}''',
'''  room('#cfe3ec','#98b6c2');
  pup({kind:'girl',x:330,y:G+10,s:1.25,eyes:'open',mouth:'open',look:[.4,-.1]});
  pup({kind:'boy',x:760,y:G+10,s:1.2,flip:-1,eyes:'squint',mouth:'flat'});
  if(u>.5){ctx.save();ctx.globalAlpha=win(u,.5,9);bubbleText(330,650,"just pick something!!",1,.78);ctx.restore();}''',
'''  room('#e8d8c8','#c2a98f');
  bigPhone(560,780,1.0,()=>{chatBub(-90,-200,180,70,false);chatBub(-90,-100,180,70,false);});
  pup({kind:'boy',x:280,y:G+10,s:1.2,eyes:'squint',mouth:'flat',look:[.4,-.1]});
  if(u>.9){ctx.save();ctx.globalAlpha=win(u,.9,9);bubbleText(280,650,"wherever you want",1,.72);ctx.restore();}''',
SHARE,
'''  room('#e9ceb8','#c39a76',1180,'rgba(255,255,255,.1)');
  ''' + TOAST.replace('x,y', '460,G+10') + '''
  ''' + TOAST.replace('x,y', '620,G+10') + '''
  pup({kind:'girl',x:330,y:G+10,s:1.2,eyes:'squint',mouth:'flat',look:[.3,0]});
  pup({kind:'boy',x:820,y:G+10,s:1.15,flip:-1,eyes:'squint',mouth:'flat',look:[-.3,0]});''',
HUG,
]
SCENES = spec(BODY_LINES, D, [{'want':'🤷'},{'minutes':'🍔'},{'choose':'🙃'},{'want':'📱'},{'to him':'💌'},{'9pm':'🍞'},{'pick':'🤍'}])
IG_LINE = "The wherever-you-want. The five apps. The toast at 9pm. Everyone shows love their own way... Want to know yours? There's a sixty second test in our bio. Take it together."
IG_CAPS = C(IG_LINE, {'apps':'📱','yours?':'🤍','bio':'🔗'})
IG_RESULT = "Acts of Service"
TT_LINE = TT_STD
