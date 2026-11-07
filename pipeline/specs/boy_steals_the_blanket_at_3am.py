import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD, C
from _r3props import R3_PROPS
TITLE = "when a boy steals the blanket at 3am"
PRELUDE = R3_PROPS
LINE_SPEED = {}
BODY_LINES = [
"3am. You're freezing. He's wrapped in the entire blanket like a burrito.",
"In the morning he swears he never moved, with the evidence still wrapped around his legs.",
"Same crime, every night. Neither of you can explain it.",
"Then, still mostly asleep, he unrolls himself and tucks it back around you without a word.",
"If you've ever woken up cold and caught him already fixing it... send this to him.",
"But the night he steals it and doesn't tuck you back in... he's not asleep. He's pretending.",
"Because a boy who gives the blanket back in his sleep... is looking after you even when he's unconscious.",
]
D = [
'''  bedNight();bedBack();
  blanket(640,1020,G-200,'#7fa6cf');
  pup({kind:'girl',x:360,y:G-90,s:1.15,look:[.3,0],brows:'sad',mouth:'flat'});
  pup({kind:'boy',x:820,y:G-110,s:1.2,flip:-1,eyes:'closed',mouth:'flat',tilt:-.1,bob:Math.sin(u*2)*3});''',
'''  room('#e8d8c8','#c2a98f');bedBack();
  blanket(640,1020,G-200,'#7fa6cf');
  pup({kind:'girl',x:360,y:G-90,s:1.2,eyes:'squint',mouth:'flat',look:[.3,0]});
  pup({kind:'boy',x:820,y:G-110,s:1.2,flip:-1,eyes:'wide',mouth:'o',look:[-.3,0]});
  if(u>.5){ctx.save();ctx.globalAlpha=win(u,.5,9);bubbleText(820,560,"I never moved!",1,.75);ctx.restore();}''',
'''  bedNight();bedBack();
  blanket(650,1010,G-200,'#7fa6cf');
  pup({kind:'girl',x:360,y:G-90,s:1.15,brows:'sad',mouth:'flat',look:[.2,0]});
  pup({kind:'boy',x:810,y:G-110,s:1.2,flip:-1,eyes:'closed',mouth:'flat',tilt:-.08});
  zzz(900,G-440,u,.6);''',
'''  bedNight();bedBack();
  blanket(360,1020,G-200,'#7fa6cf');
  pup({kind:'boy',x:790,y:G-110,s:1.2,flip:-1,eyes:'closed',mouth:'flat',tilt:-.1,paw:{x:-220,y:30,k:1}});
  pup({kind:'girl',x:360,y:G-90,s:1.15,eyes:'closed',mouth:'smile',blush:.2,tilt:.05});''',
SHARE,
'''  room('#4a4558','#3a3648','rgba(255,255,255,.05)');bedBack();
  blanket(640,1020,G-200,'#7fa6cf');
  pup({kind:'girl',x:360,y:G-90,s:1.15,brows:'sad',mouth:'flat',look:[.2,0]});
  pup({kind:'boy',x:820,y:G-110,s:1.2,flip:-1,eyes:'closed',mouth:'flat',tilt:-.1});
  if(u>1.2)raincloudSmall(360,G-470,win(u,1.2,9)*.6);''',
HUG,
]
SCENES = spec(BODY_LINES, D, [{'burrito':'🥶'},{'legs':'🙄'},{'explain it':'🌙'},{'a word':'🤍'},{'to him':'💌'},{'pretending':'🩶'},{'unconscious':'🤍'}])
IG_LINE = "The blanket burrito. The denial in the morning. The half-asleep tuck-in. Everyone shows love their own way... Want to know yours? There's a sixty second test in our bio. Take it together."
IG_CAPS = C(IG_LINE, {'burrito':'🥶','yours?':'🤍','bio':'🔗'})
IG_RESULT = "Physical Touch"
TT_LINE = TT_STD
