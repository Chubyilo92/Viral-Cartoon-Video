import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD, C
from _r3props import R3_PROPS
TITLE = "when a girl overpacks for every trip"
PRELUDE = R3_PROPS
LINE_SPEED = {}
SUITCASE = '''  ctx.save();ctx.translate(x,y);
  blob(rectPts(-110,-230,220,230,22),'#ec9a6e',{lw:5});
  blob(rectPts(-40,-270,80,50,14),'#ec9a6e',{lw:5});
  line([[-110,-115],[110,-115]],{c:'#c9703f',lw:5});
  blob(rectPts(-20,-150,40,30,8),'#c9703f',{lw:3.5});
  ctx.restore();'''
BODY_LINES = [
'When a girl packs five "just in case" outfits for a two-day trip, she\'s not being extra.',
"Half that suitcase is your charger, your paracetamol and the socks you forgot.",
"She packs a tiny first-aid kit that's bailed you out more times than either of you can count.",
'She still swears she "barely packed anything" while the zipper strains to close.',
"If she's the reason you've never once been without a charger on holiday... send this to her.",
"But the trip she packs light and there's nothing of yours in her bag... she's not travelling lighter. She's stopped planning for you.",
"Because a girl who overpacks for every trip... is packing for two.",
]
D = [
'''  room('#cfe3ec','#98b6c2');
  ''' + SUITCASE.replace('x,y', '575,G+10') + '''
  pup({kind:'girl',x:300,y:G+10,s:1.25,look:[.4,-.2],eyes:'open',mouth:'flat',tilt:-.04});
  pup({kind:'boy',x:820,y:G+10,s:1.1,flip:-1,look:[-.4,-.2],eyes:'wide',mouth:'o'});''',
'''  room('#e8d8c8','#c2a98f');
  ''' + SUITCASE.replace('x,y', '560,G+10') + '''
  pup({kind:'girl',x:340,y:G+10,s:1.25,look:[.5,-.3],eyes:'squint',mouth:'open',blush:.3});
  if(u>.5){const k=pop(u,.5,.4);ctx.save();ctx.globalAlpha=win(u,.5,9);bubbleText(560,650,"your charger 🔌",1,.8*k);ctx.restore();}''',
'''  room('#f1d5b0','#caa070');
  ''' + SUITCASE.replace('x,y', '560,G+10') + '''
  ctx.save();ctx.translate(500,G-180);ctx.scale(.5,.5);
  blob(rectPts(-34,-30,68,56,10),'#fff',{lw:4});
  ctx.fillStyle='#ec7489';ctx.fillRect(-22,-5,44,10);ctx.fillRect(-5,-22,10,44);ctx.restore();
  pup({kind:'girl',x:330,y:G+10,s:1.25,look:[.5,-.2],eyes:'happy',mouth:'smile',blush:.3});''',
'''  room('#e3c9a0','#bf9670');
  ''' + SUITCASE.replace('x,y', '560,G+10') + '''
  ctx.save();ctx.strokeStyle='#fff';ctx.globalAlpha=.5+Math.sin(u*14)*.3;ctx.lineWidth=3;
  for(let i=0;i<3;i++){ctx.beginPath();ctx.moveTo(560-40+i*40,G-220);ctx.lineTo(560-20+i*40,G-250);ctx.stroke();}ctx.restore();
  pup({kind:'girl',x:730,y:G+10,s:1.2,look:[-.3,-.4],eyes:'squint',mouth:'o',blush:.3});
  if(u>.5){ctx.save();ctx.globalAlpha=win(u,.5,9);bubbleText(470,610,"barely packed anything 😇",1,.72);ctx.restore();}''',
SHARE,
'''  room('#6f6a78','#5a5562','rgba(255,255,255,.05)');
  ''' + SUITCASE.replace('x,y', '560,G+10') + '''
  pup({kind:'girl',x:730,y:G+10,s:1.2,look:[-.3,-.1],eyes:'open',mouth:'flat'});
  pup({kind:'boy',x:280,y:G+10,s:1.15,flip:-1,brows:'sad',look:[.3,-.1],mouth:'flat'});
  if(u>1.2)raincloudSmall(280,G-430,win(u,1.2,9)*.6);''',
HUG,
]
SCENES = spec(BODY_LINES, D, [{'extra':'🧳'},{'forgot':'🔌'},{'can count':'🩹'},{'close':'😇'},{'to her':'💌'},{'for you':'💔'},{'for two':'🤍'}])
IG_LINE = "The five outfits. The tiny first-aid kit. The zipper that barely closes. Everyone shows love their own way... Want to know yours? There's a sixty second test in our bio. Take it together."
IG_CAPS = C(IG_LINE, {'suitcase':'🧳','yours?':'🤍','bio':'🔗'})
IG_RESULT = "Acts of Service"
TT_LINE = TT_STD
