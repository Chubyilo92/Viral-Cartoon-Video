import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD, C
from _r3props import R3_PROPS
TITLE = "when a girl calls you for no reason"
PRELUDE = R3_PROPS
LINE_SPEED = {0: 0.85, 1: 0.8}  # voicecheck: line 1 pace 3.6 w/s, line 2 pace 3.8 w/s at 0.9
BODY_LINES = [
"When a girl calls you in the middle of the afternoon for no reason at all, she's not checking up on you.",
'She just wants to tell you about a dog she saw on the walk home.',
"She stays on the call in silence while she does the washing up, just so the kitchen isn't quiet.",
"She hangs up the second you sound busy, before you've even said that you are.",
"If you've heard about more random dogs on the phone than you've ever met in real life... send this to her.",
"But the week she stops calling for no reason at all... she's not finally respecting your time. She's stopped wanting to share the small stuff with you.",
"Because a girl who calls you for nothing... just wants you there for everything, even the boring parts.",
]
D = [
'''  room('#cfe3ec','#98b6c2');
  pup({kind:'girl',x:340,y:G+10,s:1.25,look:[.4,-.2],eyes:'happy',mouth:'open',blush:.3});
  bigPhone(760,760,.9,()=>{ctx.font='bold 26px Poppins';ctx.fillStyle=INK;ctx.textAlign='center';ctx.fillText('Calling...',0,0);});''',
'''  room('#e8d8c8','#c2a98f');
  pup({kind:'girl',x:360,y:G+10,s:1.3,look:[.3,-.2],eyes:'happy',mouth:'open',blush:.4,tilt:-.06});
  if(u>.4){const k=pop(u,.4,.4);ctx.save();ctx.globalAlpha=win(u,.4,9);bubbleText(420,610,"there was a dog 🐶",1,.85*k);ctx.restore();}''',
'''  room('#f1d5b0','#caa070');
  pup({kind:'girl',x:620,y:G+10,s:1.25,flip:-1,look:[-.2,.1],eyes:'squint',mouth:'flat',earLift:.1});
  ctx.save();ctx.translate(620,G-260);ctx.rotate(Math.sin(u*2)*.06);
  blob(rectPts(-55,-10,110,55,10),'#cfe3ec',{lw:4});ctx.restore();
  bigPhone(300,780,.7,()=>{ctx.font='bold 22px Poppins';ctx.fillStyle='#7a726c';ctx.textAlign='center';ctx.fillText('04:12',0,0);});''',
'''  room('#e3c9a0','#bf9670');
  pup({kind:'girl',x:360,y:G+10,s:1.25,look:[.3,-.1],brows:'sad',mouth:'flat'});
  bigPhone(760,760,.9,()=>{ctx.font='bold 26px Poppins';ctx.fillStyle='#9a928c';ctx.textAlign='center';ctx.fillText('Call ended',0,0);});''',
SHARE,
'''  room('#6f6a78','#5a5562','rgba(255,255,255,.05)');
  pup({kind:'girl',x:650,y:G+10,s:1.2,flip:-1,look:[-.3,-.1],brows:'sad',mouth:'flat'});
  bigPhone(300,780,.7,()=>{ctx.font='bold 22px Poppins';ctx.fillStyle='#9a928c';ctx.textAlign='center';ctx.fillText('no new',0,-16);ctx.fillText('calls',0,16);});
  if(u>1.2)raincloudSmall(650,G-440,win(u,1.2,9)*.6);''',
HUG,
]
SCENES = spec(BODY_LINES, D, [{'no reason':'📞'},{'walk home':'🐶'},{"isn't quiet":'🧽'},{'that you are':'📴'},{'to her':'💌'},{'with you':'💔'},{'boring parts':'🤍'}])
IG_LINE = "The random dog. The staying on the line while she washes up. The hanging up when you're busy. Everyone shows love their own way... Want to know yours? There's a sixty second test in our bio. Take it together."
IG_CAPS = C(IG_LINE, {'dog':'🐶','yours?':'🤍','bio':'🔗'})
IG_RESULT = "Words of Affirmation"
TT_LINE = TT_STD
