import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD, C
from _r3props import R3_PROPS
TITLE = "when a boy copies her goodbye"
PRELUDE = R3_PROPS
LINE_SPEED = {1: 0.85}
BODY_LINES = [
"She always hangs up the same odd way: \"bye, bye, bye, love you, bye.\"",
"He used to mock her for it, relentlessly.",
"Lately he's started doing the exact same multi-bye thing, without noticing.",
"She noticed straight away. She's saying nothing. She's waiting.",
"If you've caught yourself doing your partner's weird goodbye without meaning to... send this to them.",
"But the day he hangs up on his boss with \"bye, bye, bye, love you, bye\"... she is never, ever letting him live that down.",
"Because a boy who picks up her weirdest habit without noticing... has had her rubbing off on him longer than he'd ever admit.",
]
D = [
'''  room('#e3c9a0','#bf9670');
  bigPhone(620,780,1.0,()=>{});
  pup({kind:'girl',x:340,y:G+10,s:1.25,eyes:'happy',mouth:'smile',blush:.3,look:[.3,-.1]});
  if(u>.5){ctx.save();ctx.globalAlpha=win(u,.5,9);bubbleText(340,650,"bye bye bye love you bye",1,.56);ctx.restore();}''',
'''  room('#f1d5b0','#caa070');
  pup({kind:'boy',x:620,y:G+10,s:1.25,eyes:'squint',mouth:'open',look:[-.2,-.1]});
  if(u>.5){ctx.save();ctx.globalAlpha=win(u,.5,9);bubbleText(620,560,"who even talks like that?! 😂",1,.6);ctx.restore();}''',
'''  room('#cfe3ec','#98b6c2');
  bigPhone(620,780,1.0,()=>{});
  pup({kind:'boy',x:340,y:G+10,s:1.25,eyes:'open',mouth:'smile',look:[.3,-.1]});
  if(u>.5){ctx.save();ctx.globalAlpha=win(u,.5,9);bubbleText(340,650,"bye bye bye love you bye",1,.56);ctx.restore();}''',
'''  room('#e8d8c8','#c2a98f');
  pup({kind:'girl',x:700,y:G+10,s:1.25,flip:-1,eyes:'squint',mouth:'flat',look:[-.3,0]});
  pup({kind:'boy',x:320,y:G+10,s:1.2,eyes:'open',mouth:'flat',look:[.4,-.1]});''',
SHARE,
'''  room('#f6d7c6','#d6a286');
  bigPhone(620,780,1.0,()=>{});
  pup({kind:'boy',x:340,y:G+10,s:1.25,eyes:'wide',mouth:'o',look:[.3,-.1]});
  pup({kind:'girl',x:820,y:G+10,s:1.2,flip:-1,eyes:'happy',mouth:'smile',blush:.4,look:[-.4,0]});
  if(u>.7){ctx.save();ctx.globalAlpha=win(u,.7,9);bubbleText(340,560,"bye bye bye... love you... sir",1,.52);ctx.restore();}''',
HUG,
]
SCENES = spec(BODY_LINES, D, [{'bye':'📱'},{'relentlessly':'😂'},{'noticing':'📱'},{'waiting':'👀'},{'to them':'💌'},{'that down':'😂'},{'ever admit':'🤍'}])
IG_LINE = "Her weird goodbye. The mocking. The day it became his too. Everyone shows love their own way... Want to know yours? There's a sixty second test in our bio. Take it together."
IG_CAPS = C(IG_LINE, {'goodbye':'📱','yours?':'🤍','bio':'🔗'})
IG_RESULT = "Words of Affirmation"
TT_LINE = TT_STD
