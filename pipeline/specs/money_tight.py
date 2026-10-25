import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD, C
TITLE = "when money's tight and you stay anyway"
BODY_LINES = [
"When money's tight and you stay anyway, that's the relationship being tested.",
"Not because love pays the bills. Because it decides who you face them with.",
"You recheck the bill twice, not to be cheap, just to make it stretch another day.",
"They skip their own haircut so your car payment clears on time.",
"If you've been broke together and never made each other feel poor... send this to the one who stayed.",
"But if money stress turns into keeping score of who paid last... that's not a partnership, that's a tab.",
"Because staying through the tight months... isn't about the money, it's about who you become without it.",
]
D = [
'''  room('#e3c9a0','#bf9670');
  pup({kind:'boy',x:380,y:G+10,s:1.2,look:[.3,.2],eyes:'open',mouth:'flat'});
  pup({kind:'girl',x:740,y:G+10,s:1.2,flip:-1,look:[-.3,.2],eyes:'open',mouth:'smile',blush:.3});''',
'''  room('#d9e2c8','#a9b38f');
  pup({kind:'boy',x:400,y:G+10,s:1.2,look:[.3,0],eyes:'open',mouth:'smile'});
  pup({kind:'girl',x:740,y:G+10,s:1.2,flip:-1,look:[-.3,0],eyes:'happy',mouth:'smile',blush:.4});''',
'''  room('#cfe3ec','#98b6c2');
  pup({kind:'girl',x:420,y:G+20,s:1.2,look:[.3,.3],eyes:'open',mouth:'flat'});
  pup({kind:'boy',x:740,y:G+20,s:1.15,flip:-1,look:[-.3,.3],eyes:'open',mouth:'flat'});
  if(u>.7){ctx.save();ctx.globalAlpha=win(u,.7,8);bubbleText(540,680,"okay, we're fine for this week",1,.8);ctx.restore();}''',
'''  room('#f6d7c6','#d6a286');
  pup({kind:'boy',x:380,y:G+10,s:1.25,look:[.3,0],eyes:'happy',mouth:'smile'});
  pup({kind:'girl',x:740,y:G+10,s:1.2,flip:-1,look:[-.3,0],eyes:'happy',mouth:'smile',blush:.4,wag:.3});
  if(u>1)sparkle(570,700,38*pop(u,1,.4),win(u,1,8));''',
SHARE,
'''  room('#6f6a78','#5a5562','rgba(255,255,255,.05)');
  pup({kind:'boy',x:380,y:G+10,s:1.25,look:[.4,.3],brows:'sad',mouth:'flat'});
  pup({kind:'girl',x:760,y:G+10,s:1.2,flip:-1,look:[-.4,.3],brows:'sad',mouth:'flat'});
  if(u>.8){ctx.save();ctx.globalAlpha=win(u,.8,8);bubbleText(560,680,"...you owe me from last time",1,.8);ctx.restore();}
  if(u>1.6)raincloudSmall(540,580,win(u,1.6,9)*.6);''',
HUG,
]
SCENES = spec(BODY_LINES, D, [{'being tested':'🤍'},{'face them with':'🤍'},{'another day':'🧾'},{'on time':'💇'},{'who stayed':'💌'},{'a tab':'🚩'},{'without it':'🤍'}])
IG_LINE = "The rechecked bill. The skipped haircut. The months that tested everything. Everyone handles being broke their own way... Want to know yours? There's a sixty second test in our bio. Take it together."
IG_CAPS = C(IG_LINE, {'bill':'🧾','yours?':'🤍','bio':'🔗'})
IG_RESULT = "Acts of Service"
TT_LINE = TT_STD
