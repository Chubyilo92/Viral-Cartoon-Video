import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD, C
TITLE = "when you're married to the right person"
BODY_LINES = [
"When you're married to the right person, the butterflies turn into something steadier.",
"Not because the spark is gone. Because you stopped needing it to prove anything.",
"They still reach for your hand... at the stove, in the car, during the boring parts.",
"They choose you again, on the Tuesdays no one's watching, long after the vows.",
"If your marriage still reaches for your hand after all this time... send this to the one who still chooses you.",
"But if 'I do' slowly became 'I guess so'... that's not marriage, that's just habit now.",
"Because a marriage that still reaches for your hand... isn't routine, it's still a choice.",
]
D = [
'''  room('#e9ceb8','#c39a76',1180,'rgba(255,255,255,.2)');
  pup({kind:'boy',x:380,y:G+10,s:1.3,look:[.4,0],eyes:'happy',mouth:'smile',tilt:.06});
  pup({kind:'girl',x:700,y:G+10,s:1.3,flip:-1,look:[-.4,0],eyes:'happy',mouth:'smile',blush:.4,tilt:-.06});
  if(u>1.4)floatHearts(540,790,1.4,u,3,130);''',
'''  room('#f3cfa8','#d09d72');
  mug(700,G-40,1.1);
  pup({kind:'girl',x:380,y:G+10,s:1.25,look:[.4,-.1],eyes:'open',mouth:'smile',blush:.3});
  pup({kind:'boy',x:780,y:G+10,s:1.2,flip:-1,look:[-.5,-.1],eyes:'happy',mouth:'smile'});''',
'''  room('#8fb6c9','#6f98ac');
  pup({kind:'boy',x:360,y:G+10,s:1.25,look:[.3,.4],eyes:'open',mouth:'smile',paw:{x:120,y:-70,k:P(u,.6,1.4)}});
  pup({kind:'girl',x:700,y:G+10,s:1.25,flip:-1,look:[-.3,.4],eyes:'happy',mouth:'smile',blush:.5,paw:{x:-120,y:-70,k:P(u,.6,1.4)}});''',
'''  room('#e3c9a0','#bf9670');
  pup({kind:'boy',x:400,y:G+10,s:1.25,look:[.4,0],eyes:'happy',mouth:'smile'});
  pup({kind:'girl',x:740,y:G+10,s:1.25,flip:-1,look:[-.4,0],eyes:'happy',mouth:'smile',blush:.5,wag:.3});
  if(u>1)sparkle(570,700,40*pop(u,1,.4),win(u,1,8));''',
SHARE,
'''  room('#6f6a78','#5a5562','rgba(255,255,255,.05)');
  pup({kind:'boy',x:360,y:G+10,s:1.25,look:[.4,.3],brows:'sad',mouth:'flat'});
  pup({kind:'girl',x:760,y:G+10,s:1.2,flip:-1,look:[-.4,.3],brows:'sad',mouth:'flat'});
  if(u>.8){ctx.save();ctx.globalAlpha=win(u,.8,8);bubbleText(560,680,"...I guess so",1,.8);ctx.restore();}''',
HUG,
]
SCENES = spec(BODY_LINES, D, [{'steadier':'🤍'},{'anything':'🤍'},{'hand':'🤍'},{'vows':'💍'},{'chooses you':'💌'},{'habit now':'🚩'},{'a choice':'🤍'}])
IG_LINE = "The hand at the stove. The Tuesdays. The vows that still hold. Every marriage shows love its own way... Want to know yours? There's a sixty second test in our bio. Take it together."
IG_CAPS = C(IG_LINE, {'stove':'🤍','yours?':'🤍','bio':'🔗'})
IG_RESULT = "Physical Touch"
TT_LINE = TT_STD
