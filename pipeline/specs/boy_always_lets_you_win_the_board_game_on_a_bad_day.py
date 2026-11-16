import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD, C
from _r3props import R3_PROPS
from _gapfill1116 import GAPFILL_PROPS
TITLE = "when a boy lets you win"
PRELUDE = R3_PROPS + GAPFILL_PROPS
LINE_SPEED = {0: 0.82, 4: 0.8}  # voicecheck precheck: lines 1 and 5 ran fast (3.8 w/s) at default 0.9
BODY_LINES = [
"When a boy lets you win the board game on a bad day, he's not just bad at the game.",
"He'll throw away a winning hand of cards without making it obvious.",
"He \"forgets\" the rule that would've beaten you, only on your worst days.",
"He still argues every other day like his life depends on winning.",
"If he's let you win on the days you needed it... send this to him.",
"But the day he plays to win when you're already low... he's not being competitive. He's stopped noticing.",
"Because a boy who lets you win on a bad day... is paying more attention to you than to the game.",
]
D = [
'''  room('#f1d5b0','#caa070');
  boardGrid(540,G-40,.75);
  pawnProp(460,G-60,'#7fa6cf',1.1);pawnProp(640,G+20,'#ec7489',1.1);
  diceProp(540,G+120,.9,.2);
  pup({kind:'girl',x:280,y:G+10,s:1.1,look:[.4,-.1],eyes:'open',mouth:'flat',brows:'sad'});
  pup({kind:'boy',x:800,y:G+10,s:1.1,flip:-1,look:[-.4,-.1],eyes:'squint',mouth:'smile'});''',
'''  room('#e8d8c8','#c2a98f');
  pup({kind:'boy',x:700,y:G+10,s:1.2,flip:-1,look:[-.3,0],eyes:'squint',mouth:'flat',paw:{x:183,y:-108,k:1}});
  ctx.save();ctx.globalAlpha=win(u,.3,9);
  blob(rectPts(416,G-186,88,120,12),'#fffaf0');
  ctx.fillStyle='#e8484f';ctx.beginPath();ctx.ellipse(460,G-140,10,10,0,0,7);ctx.fill();
  heart(460,G-105,22,'#e8484f',1,0);
  ctx.restore();
  pup({kind:'girl',x:320,y:G+10,s:1.15,look:[.3,-.1],eyes:'open',mouth:'o'});''',
'''  room('#cfe3ec','#98b6c2');
  boardGrid(540,G-40,.75);
  pawnProp(460,G-60,'#7fa6cf',1.1);pawnProp(640,G+20,'#ec7489',1.1);
  labelCard(540,460,'"forgot" the rule 🤷',.85,1,22);
  pup({kind:'girl',x:280,y:G+10,s:1.1,look:[.4,-.1],eyes:'open',mouth:'flat',brows:'sad'});
  pup({kind:'boy',x:800,y:G+10,s:1.1,flip:-1,look:[-.4,-.1],eyes:'open',mouth:'flat'});''',
'''  room('#f6e4c8','#d4ad78');
  boardGrid(540,G-40,.75);
  pawnProp(460,G-60,'#7fa6cf',1.1);pawnProp(640,G+20,'#ec7489',1.1);
  pup({kind:'girl',x:280,y:G+10,s:1.15,look:[.4,-.1],eyes:'squint',mouth:'o'});
  pup({kind:'boy',x:800,y:G+10,s:1.15,flip:-1,look:[-.4,-.1],eyes:'wide',mouth:'open'});
  labelCard(540,460,'any other day 😤',.85,1,22);''',
SHARE,
'''  room('#6f6a78','#5a5562','rgba(255,255,255,.05)');
  boardGrid(540,G-40,.7);
  pawnProp(460,G-60,'#ec7489',1.0);pawnProp(640,G+20,'#7fa6cf',1.0);
  pup({kind:'girl',x:280,y:G+10,s:1.1,look:[.4,-.1],eyes:'open',mouth:'flat',brows:'sad'});
  pup({kind:'boy',x:800,y:G+10,s:1.1,flip:-1,look:[-.4,-.1],eyes:'happy',mouth:'smile',wag:.3});''',
HUG,
]
SCENES = spec(BODY_LINES, D, [{'the game':'🎲'},{'obvious':'🃏'},{'worst days':'🤷'},{'winning':'😤'},{'send this to him':'💌'},{'noticing':'💔'},{'the game':'🤍'}])
IG_LINE = "The hand of cards he quietly throws away. The rule he \"forgets\" on your worst days. The game he suddenly doesn't need to win. Everyone shows love their own way... Want to know yours? There's a sixty second test in our bio. Take it together."
IG_CAPS = C(IG_LINE, {'away.':'🃏','yours?':'🤍','bio':'🔗'})
IG_RESULT = "Acts of Service"
TT_LINE = TT_STD
