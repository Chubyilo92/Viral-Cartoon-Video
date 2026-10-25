import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD, C
TITLE = "when you move into your first place together"
BODY_LINES = [
"When you move into your first place together, the mess means more than the furniture.",
"Not because boxes are fun. Because home is finally a person, not an address.",
"You eat pizza on the floor because the table hasn't arrived, and neither of you minds.",
"They hang your photo first, before anything else goes on the wall.",
"If your first place was more love than furniture... send this to the one who built it with you.",
"But if 'our place' still feels like their place... that's not moving in, that's just visiting longer.",
"Because the first home you build together... isn't about the address, it's about who's inside it.",
]
D = [
'''  room('#f6d7c6','#d6a286');
  pup({kind:'boy',x:380,y:G+10,s:1.25,look:[.3,.1],eyes:'open',mouth:'smile'});
  pup({kind:'girl',x:740,y:G+10,s:1.2,flip:-1,look:[-.3,.1],eyes:'happy',mouth:'smile',blush:.3,wag:.3});''',
'''  room('#8fb6c9','#6f98ac');
  windowBox(760,320,290,230,(w,h)=>{ctx.fillStyle='#fde9b0';ctx.fillRect(0,0,w,h);});
  pup({kind:'boy',x:360,y:G+10,s:1.25,look:[.3,0],eyes:'happy',mouth:'smile'});
  pup({kind:'girl',x:700,y:G+10,s:1.2,flip:-1,look:[-.3,0],eyes:'happy',mouth:'smile',blush:.4});''',
'''  room('#d9e2c8','#a9b38f');
  pup({kind:'girl',x:400,y:G+30,s:1.2,look:[.3,.2],eyes:'happy',mouth:'smile',blush:.4});
  pup({kind:'boy',x:700,y:G+30,s:1.2,flip:-1,look:[-.3,.2],eyes:'happy',mouth:'smile'});
  if(u>.7){ctx.save();ctx.globalAlpha=win(u,.7,8);bubbleText(540,680,"best table we never bought",1,.8);ctx.restore();}''',
'''  room('#e3c9a0','#bf9670');
  pup({kind:'boy',x:400,y:G+10,s:1.25,look:[.4,0],eyes:'happy',mouth:'smile'});
  pup({kind:'girl',x:740,y:G+10,s:1.25,flip:-1,look:[-.4,0],eyes:'happy',mouth:'smile',blush:.5,wag:.3});
  if(u>1)sparkle(570,700,40*pop(u,1,.4),win(u,1,8));''',
SHARE,
'''  room('#6f6a78','#5a5562','rgba(255,255,255,.05)');
  pup({kind:'boy',x:380,y:G+10,s:1.25,look:[.4,.3],brows:'sad',mouth:'flat'});
  pup({kind:'girl',x:760,y:G+10,s:1.2,flip:-1,look:[-.4,.3],brows:'sad',mouth:'flat'});
  if(u>.8){ctx.save();ctx.globalAlpha=win(u,.8,8);bubbleText(560,680,"...it's still just your place",1,.8);ctx.restore();}
  if(u>1.6)raincloudSmall(540,580,win(u,1.6,9)*.6);''',
HUG,
]
SCENES = spec(BODY_LINES, D, [{'furniture':'🤍'},{'an address':'🏠'},{'minds':'🍕'},{'the wall':'🖼️'},{'with you':'💌'},{'visiting longer':'🚩'},{'inside it':'🤍'}])
IG_LINE = "The pizza on the floor. The photo on the wall first. The first place that's truly yours. Everyone makes a house a home their own way... Want to know yours? There's a sixty second test in our bio. Take it together."
IG_CAPS = C(IG_LINE, {'floor':'🍕','yours?':'🤍','bio':'🔗'})
IG_RESULT = "Quality Time"
TT_LINE = TT_STD
