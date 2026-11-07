import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD, C
TITLE = "when a boy hijacks the car playlist"
PRELUDE = ''
LINE_SPEED = {1: 1.15}
RADIO = '''  ctx.save();ctx.translate(x,y);
  blob(rectPts(-120,-50,240,120,18),'#333a48');
  blob(rectPts(-86,-28,172,60,9),'#8fd0ff',{stroke:false});
  ctx.fillStyle=INK;ctx.font='bold 38px Poppins';ctx.textAlign='center';ctx.fillText('ICON',0,16);
  ell(-62,56,13,13,'#5a6274');ell(0,56,13,13,'#5a6274');ell(62,56,13,13,'#5a6274');
  ctx.restore();'''
BODY_LINES = [
"He skips your song three seconds in. Then puts on the same five songs he always plays.",
"He'll let your playlist run the second you've had a bad day, no questions asked.",
"He still has the one song you hate saved at the top, just to watch you groan.",
"He turns it right down the second you start talking, without being asked.",
"If you're the one who always loses the aux and somehow doesn't mind... send this to him.",
"But the day he stops touching the aux at all... he's not finally respecting your taste. He's stopped trying to share his with you.",
"Because a boy who hijacks the car playlist... just wants you to hear what he's hearing.",
]
D = [
'''  room('#cfe3ec','#98b6c2');
  pup({kind:'boy',x:360,y:G+10,s:1.25,look:[.4,-.1],eyes:'open',mouth:'o',paw:{x:180,y:-150,k:1}});
  pup({kind:'girl',x:760,y:G+10,s:1.2,flip:-1,look:[-.3,0],brows:'sad',mouth:'flat'});
  ''' + RADIO.replace('x,y', '540,G-90').replace('ICON', '⏭') + '''
  note(560,610,1.15,1);''',
'''  room('#e8d8c8','#c2a98f');
  pup({kind:'girl',x:330,y:G+10,s:1.25,look:[.3,-.1],brows:'sad',mouth:'flat'});
  pup({kind:'boy',x:760,y:G+10,s:1.22,flip:-1,eyes:'happy',mouth:'smile',tilt:.05,look:[-.3,-.1]});
  ''' + RADIO.replace('x,y', '540,G-90').replace('ICON', '▶') + '''
  note(330,600,1,1);''',
'''  room('#f1d5b0','#caa070');
  pup({kind:'boy',x:760,y:G+10,s:1.22,flip:-1,eyes:'squint',mouth:'smile'});
  pup({kind:'girl',x:330,y:G+10,s:1.25,eyes:'squint',mouth:'flat'});
  ''' + RADIO.replace('x,y', '540,G-90').replace('ICON', '🔁') + '''
  if(u>.5){const k=pop(u,.5,.4);ctx.save();ctx.globalAlpha=win(u,.5,9);bubbleText(330,650,"not this one again 😩",1,.8*k);ctx.restore();}''',
'''  room('#cfe3ec','#98b6c2');
  pup({kind:'girl',x:330,y:G+10,s:1.25,look:[.3,0],eyes:'open',mouth:'open'});
  pup({kind:'boy',x:760,y:G+10,s:1.22,flip:-1,look:[-.4,.1],eyes:'open',mouth:'flat',paw:{x:30,y:-40,k:1}});
  ''' + RADIO.replace('x,y', '540,G-90').replace('ICON', '🔉') + '''
  note(760,760,.7,win(u,0,4));''',
SHARE,
'''  room('#6f6a78','#5a5562','rgba(255,255,255,.05)');
  pup({kind:'boy',x:760,y:G+10,s:1.15,flip:-1,brows:'sad',mouth:'flat',look:[-.2,0]});
  pup({kind:'girl',x:330,y:G+10,s:1.2,mouth:'flat',look:[.2,0]});
  ctx.save();ctx.globalAlpha=.55;''' + RADIO.replace('x,y', '540,G-90').replace('ICON', '⏻') + '''ctx.restore();
  if(u>1.2)raincloudSmall(330,G-430,win(u,1.2,9)*.6);''',
HUG,
]
SCENES = spec(BODY_LINES, D, [{'plays':'🎵'},{'questions asked':'🤍'},{'groan':'😩'},{'asked':'🔉'},{'send this to him':'💌'},{'with you':'💔'},{'hearing':'🤍'}])
IG_LINE = "The skipped songs. The one he saved to annoy you. The volume he turns down mid-sentence. Everyone shows love their own way... Want to know yours? There's a sixty second test in our bio. Take it together."
IG_CAPS = C(IG_LINE, {'skipped':'🎵','yours?':'🤍','bio':'🔗'})
IG_RESULT = "Quality Time"
TT_LINE = TT_STD
