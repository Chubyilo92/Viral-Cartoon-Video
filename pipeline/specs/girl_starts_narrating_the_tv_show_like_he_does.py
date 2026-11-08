import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD, C, S
from _r3props import R3_PROPS
TITLE = "when a girl narrates the tv too"
PRELUDE = R3_PROPS
BODY_LINES = [
"He talks to the television like the characters can hear him, every single episode, out loud.",
"You used to find it genuinely irritating.",
"Last week you caught yourself yelling \"don't go in there\" at the screen before he'd even opened his mouth.",
"He didn't say anything. He just smiled and kept watching.",
"If you've ever picked up your partner's most annoying habit without even noticing, send this to them.",
"Careful. It starts with the TV. Next it's his sayings, his snacks, and his side of the sofa.",
"Enjoy it. You're basically the same weirdo now.",
]
D = [
'''  room('#e3c9a0','#bf9670');
  ctx.save();ctx.translate(820,G-150);
  ctx.fillStyle='#2b2830';ctx.beginPath();ctx.roundRect(-90,-110,180,130,14);ctx.fill();
  ctx.fillStyle='#8fc8f0';ctx.beginPath();ctx.roundRect(-74,-96,148,100,8);ctx.fill();
  ctx.fillStyle='#2b2830';ctx.fillRect(-14,20,28,18);ctx.fillRect(-40,38,80,8);
  ctx.restore();
  pup({kind:'boy',x:620,y:G+10,s:1.25,eyes:'wide',mouth:'open',look:[.3,-.1]});
  pup({kind:'girl',x:360,y:G+10,s:1.2,eyes:'squint',mouth:'flat',look:[.3,-.1]});
  if(u>.4){ctx.save();ctx.globalAlpha=win(u,.4,9);bubbleText(620,590,"don't you dare open that door!!",1,.52);ctx.restore();}''',
'''  room('#cfe3ec','#9fc0cc');
  pup({kind:'girl',x:540,y:G+10,s:1.3,eyes:'squint',mouth:'flat',look:[0,-.1]});
  if(u>.4){ctx.save();ctx.globalAlpha=win(u,.4,9);bubbleText(540,590,"so annoying...",1,.65);ctx.restore();}''',
'''  room('#f1d5b0','#caa070');
  ctx.save();ctx.translate(820,G-150);
  ctx.fillStyle='#2b2830';ctx.beginPath();ctx.roundRect(-90,-110,180,130,14);ctx.fill();
  ctx.fillStyle='#8fc8f0';ctx.beginPath();ctx.roundRect(-74,-96,148,100,8);ctx.fill();
  ctx.fillStyle='#2b2830';ctx.fillRect(-14,20,28,18);ctx.fillRect(-40,38,80,8);
  ctx.restore();
  pup({kind:'girl',x:360,y:G+10,s:1.25,eyes:'wide',mouth:'open',look:[.3,-.1]});
  pup({kind:'boy',x:620,y:G+10,s:1.2,eyes:'open',mouth:'flat',look:[.3,-.1]});
  if(u>.4){ctx.save();ctx.globalAlpha=win(u,.4,9);bubbleText(360,590,"don't go in there!!",1,.6);ctx.restore();}''',
'''  room('#f1d5b0','#caa070');
  pup({kind:'girl',x:340,y:G+10,s:1.2,eyes:'open',mouth:'o',look:[.3,-.1]});
  pup({kind:'boy',x:700,y:G+10,s:1.25,eyes:'happy',mouth:'smile',look:[-.3,-.1],tilt:.08});''',
SHARE,
'''  room('#e8d8c8','#c2a98f');
  pup({kind:'boy',x:620,y:G+10,s:1.2,eyes:'happy',mouth:'smile',look:[-.3,-.1]});
  pup({kind:'girl',x:340,y:G+10,s:1.2,eyes:'squint',mouth:'smile',blush:.2,look:[.3,-.1]});
  ctx.save();ctx.translate(540,600);ctx.globalAlpha=win(u,.1,9); blob(rectPts(-180,-40,360,80,16),'#fffaf0',{lw:4});
  ctx.fillStyle=INK;ctx.font='bold 20px Poppins';ctx.textAlign='center';ctx.fillText('sayings • snacks • the sofa',0,8); ctx.restore();''',
HUG,
]
EMOJI = [{'out loud':'📺'},{'irritating':'😑'},{'mouth':'😱'},{'watching':'😌'},{'to them':'💌'},{'the sofa':'🚨'},{'now':'🤡'}]
# Line 3 (index 2): C()'s default tokenizer splits the quoted phrase across a caption-chunk boundary
# ("'don't go" / "in there' at"), which reads as a stray apostrophe on screen (6-Nov-caption
# auto-shrink doesn't fix a *split*, only overflow). Fixed per fresh structure-reviewer note
# (2026-11-08): keep the quoted phrase as one caption chunk. Narration text/approval hash unchanged.
CAP3 = ['last week', 'you caught', 'yourself yelling', "'don't go in there'", 'at the screen', "before he'd", 'even opened', 'his mouth 😱']
SCENES = (spec(BODY_LINES[:2], D[:2], EMOJI[:2])
          + [S(CAP3, D[2])]
          + spec(BODY_LINES[3:], D[3:], EMOJI[3:]))
IG_LINE = "The habit you used to roll your eyes at. The night you caught yourself doing it too. Everyone shows love their own way... Want to know yours? There's a sixty second test in our bio. Take it together."
IG_CAPS = C(IG_LINE, {'eyes at':'📺','yours?':'🤍','bio':'🔗'})
IG_RESULT = "Quality Time"
TT_LINE = TT_STD
