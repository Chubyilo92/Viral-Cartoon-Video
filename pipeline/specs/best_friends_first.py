import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD, C
TITLE = "when you were best friends first"
BODY_LINES = [
"When you were best friends first, falling in love felt like losing your safest person.",
"Not because the friendship was at risk. Because you were terrified to ruin the one sure thing.",
"They knew your worst stories first... and still chose to date you after hearing them.",
"You argue less like strangers now, and more like people who already know how to make up.",
"If your best friend became your person... send this to them.",
"But if you're still 'just friends' after years of this... that's not friendship, that's fear in a nice outfit.",
"Because love that started as friendship... isn't the backup plan, it's the strongest kind there is.",
]
D = [
'''  room('#e3c9a0','#bf9670');
  pup({kind:'boy',x:380,y:G+10,s:1.25,look:[.4,.2],eyes:'open',mouth:'flat',brows:'sad'});
  pup({kind:'girl',x:760,y:G+10,s:1.2,flip:-1,look:[-.4,.2],eyes:'open',mouth:'flat'});''',
'''  room('#cfe3ec','#98b6c2');
  pup({kind:'boy',x:360,y:G+10,s:1.25,look:[.4,.1],eyes:'open',mouth:'flat'});
  pup({kind:'girl',x:760,y:G+10,s:1.25,flip:-1,look:[-.4,.1],eyes:'open',mouth:'flat'});
  if(u>1)raincloudSmall(560,600,win(u,1,9)*.4);''',
'''  room('#f6d7c6','#d6a286');
  pup({kind:'girl',x:380,y:G+10,s:1.3,look:[.4,0],eyes:'happy',mouth:'smile',blush:.5});
  pup({kind:'boy',x:760,y:G+10,s:1.25,flip:-1,look:[-.4,0],eyes:'happy',mouth:'smile'});
  if(u>1.1)sparkle(570,700,42*pop(u,1.1,.4),win(u,1.1,8));''',
'''  room('#d9e2c8','#a9b38f');
  pup({kind:'boy',x:400,y:G+10,s:1.25,look:[.3,.2],eyes:'open',mouth:'smile'});
  pup({kind:'girl',x:740,y:G+10,s:1.25,flip:-1,look:[-.3,.2],eyes:'happy',mouth:'smile',blush:.4,wag:.3});
  if(u>.9){ctx.save();ctx.globalAlpha=win(u,.9,8);bubbleText(570,680,"okay fine, you win 🙄🤍",1,.85);ctx.restore();}''',
SHARE,
'''  room('#6f6a78','#5a5562','rgba(255,255,255,.05)');
  pup({kind:'boy',x:380,y:G+10,s:1.2,look:[.4,.3],brows:'sad',mouth:'flat'});
  pup({kind:'girl',x:760,y:G+10,s:1.2,flip:-1,look:[-.4,.3],brows:'sad',mouth:'flat'});
  shadesProp(760,970,.6);''',
HUG,
]
SCENES = spec(BODY_LINES, D, [{'safest person':'🤍'},{'thing':'🤍'},{'them':'🥹'},{'make up':'🤍'},{'them':'💌'},{'nice outfit':'🚩'},{'kind there is':'🤍'}])
IG_LINE = "The worst stories. The arguments that end fast. The friendship underneath it all. Everyone falls in love their own way... Want to know yours? There's a sixty second test in our bio. Take it together."
IG_CAPS = C(IG_LINE, {'stories':'🤍','yours?':'🤍','bio':'🔗'})
IG_RESULT = "Quality Time"
TT_LINE = TT_STD
