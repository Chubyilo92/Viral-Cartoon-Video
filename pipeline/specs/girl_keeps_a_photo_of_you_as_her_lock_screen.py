import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD, C
from _r3props import R3_PROPS
TITLE = "the photo she never changes"
PRELUDE = R3_PROPS
PHOTO_DRAW = '''()=>{
    const g=ctx.createLinearGradient(0,-222,0,222);g.addColorStop(0,'#ffd59e');g.addColorStop(1,'#f3b07a');
    ctx.fillStyle=g;ctx.fillRect(-112,-222,224,444);
    pup({kind:'boy',x:6,y:150,s:.5,flip:1,eyes:'happy',mouth:'open',tilt:.22,look:[.7,.3],blush:.2,shadow:false});
    ctx.fillStyle='#ffffff';ctx.font='bold 32px Poppins';ctx.textAlign='center';ctx.fillText('9:41',0,-160);
  }'''
BLANK_DRAW = '''()=>{
    const g=ctx.createLinearGradient(0,-222,0,222);g.addColorStop(0,'#9fb3c8');g.addColorStop(1,'#7490ac');
    ctx.fillStyle=g;ctx.fillRect(-112,-222,224,444);
    ctx.fillStyle='#ffffff';ctx.font='bold 32px Poppins';ctx.textAlign='center';ctx.fillText('9:41',0,-160);
  }'''
BODY_LINES = [
"When a girl never changes her lock screen from a photo of you, she's not being lazy.",
"It's the one where you're laughing at something stupid, not even looking at the camera.",
"She'll update everything else on her phone... except that one photo.",
"Her friends tease her about it. She changes the subject, never the photo.",
"If you're still her lock screen, two years in... send this to her.",
"But the day she changes it and doesn't tell you... she's not bored of the photo. She's getting used to not seeing you.",
"Because a girl who keeps you as her lock screen... wants you to be the first thing she sees.",
]
D = [
'''  room('#f1d5b0','#caa070');
  bigPhone(700,780,1,''' + PHOTO_DRAW + ''');
  pup({kind:'girl',x:300,y:G+10,s:1.25,eyes:'happy',mouth:'smile',blush:.2,look:[.4,-.2]});''',
'''  room('#e8d8c8','#c2a98f');
  bigPhone(540,790,1.3,''' + PHOTO_DRAW + ''');''',
'''  room('#cfe3ec','#98b6c2');
  bigPhone(700,780,1,''' + PHOTO_DRAW + ''');
  pup({kind:'girl',x:300,y:G+10,s:1.25,eyes:'squint',mouth:'smile',look:[.4,-.1]});
  sparkle(880,480,30,win(u,.3,9));''',
'''  room('#f6d7c6','#d6a286');
  pup({kind:'girl',x:780,y:G+10,s:1.2,flip:-1,eyes:'squint',mouth:'open',look:[-.3,-.1]});
  shadesProp(780,924,1.1);
  pup({kind:'girl',x:320,y:G+10,s:1.25,eyes:'open',mouth:'flat',look:[.5,.2]});
  bigPhone(490,940,.5,''' + PHOTO_DRAW + ''');
  if(u>.5){ctx.save();ctx.globalAlpha=win(u,.5,9);bubbleText(780,540,"still him?? 👀",1,.68);ctx.restore();}''',
SHARE,
'''  room('#333c54','#28304a','rgba(255,255,255,.05)');
  bigPhone(700,780,1,''' + BLANK_DRAW + ''');
  pup({kind:'girl',x:300,y:G+10,s:1.2,eyes:'open',mouth:'flat',look:[.3,.1],tilt:-.03,shadow:false});''',
'''  room('#f1d5b0','#caa070');
  bigPhone(700,780,1,''' + PHOTO_DRAW + ''');
  pup({kind:'girl',x:300,y:G+10,s:1.25,eyes:'happy',mouth:'smile',blush:.3,look:[.4,-.1]});
  if(u>.6)floatHearts(700,650,.6,u,3,110);''',
]
SCENES = spec(BODY_LINES, D, [{'not being lazy':'📱'},{'the camera':'😂'},{'that one photo':'🔒'},{'the photo':'👀'},{'send this':'💌'},{'seeing you':'🚩'},{'she sees':'🤍'}])
IG_LINE = "The photo she never changes. The friends who tease her about it. The lock screen that's stayed you for two years. Everyone shows love their own way... Want to know yours? There's a sixty second test in our bio. Take it together."
IG_CAPS = C(IG_LINE, {'changes':'📱','yours?':'🤍','bio':'🔗'})
IG_RESULT = "Quality Time"
TT_LINE = TT_STD
