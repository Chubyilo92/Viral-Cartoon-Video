import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD, C
TITLE = "when you're engaged to the right person"
BODY_LINES = [
"When you're engaged to the right person, wedding stress doesn't scare either of you.",
"Not because the planning is easy. Because you already know you'll end up married anyway.",
"They fight for your favorite song at the venue... over the one everyone else wants.",
"They call you their fiance to strangers, every time, like it's still new.",
"If you found someone who fights for you, not just the wedding... send this to your person.",
"But if planning it turns you into two people negotiating instead of two people in love... that's a warning, not a wedding.",
"Because the right engagement... isn't about the wedding day, it's every day before it.",
]
D = [
'''  room('#f6d7c6','#d6a286');
  const r=P(u,.3,1.2);
  pup({kind:'girl',x:lerp(640,580,r),y:G+10,s:1.35,flip:-1,look:[-.3,0],eyes:'happy',mouth:'smile',blush:.6,tilt:-.06});
  pup({kind:'boy',x:360,y:G+10,s:1.35,look:[.5,0],eyes:'happy',mouth:'smile',blush:.3,tilt:.05});
  sparkle(500,700,44*pop(u,1.0,.4),win(u,1.0,8));
  if(u>1.6)floatHearts(500,820,1.6,u,3,130);''',
'''  room('#e3c9a0','#bf9670');
  pup({kind:'boy',x:760,y:G+10,s:1.25,flip:-1,look:[-.6,0],eyes:'open',mouth:'smile'});
  pup({kind:'girl',x:320,y:G+10,s:1.25,look:[.6,0],eyes:'happy',mouth:'smile',blush:.4});
  if(u>.8)floatHearts(540,820,.8,u,4,150);''',
'''  room('#d9e2c8','#a9b38f');
  pup({kind:'boy',x:340,y:G+10,s:1.25,look:[.4,.2],eyes:'open',mouth:'smile'});
  pup({kind:'girl',x:740,y:G+10,s:1.25,flip:-1,look:[-.4,.2],eyes:'open',mouth:'flat'});
  if(u>.7){ctx.save();ctx.globalAlpha=win(u,.7,8);bubbleText(340,680,"THIS song, not that one 🎵",1,.85);ctx.restore();}''',
'''  room('#cfe3ec','#98b6c2');
  pup({kind:'girl',x:360,y:G+10,s:1.3,look:[.4,.2],eyes:'happy',mouth:'smile',blush:.5,wag:.3});
  pup({kind:'boy',x:740,y:G+10,s:1.25,flip:-1,look:[-.4,.2],eyes:'happy',mouth:'smile'});
  if(u>.9){ctx.save();ctx.globalAlpha=win(u,.9,8);bubbleText(360,680,"this is my fiance 🥹",1,.85);ctx.restore();}''',
SHARE,
'''  room('#6f6a78','#5a5562','rgba(255,255,255,.05)');
  pup({kind:'boy',x:340,y:G+10,s:1.25,look:[.4,.4],brows:'sad',mouth:'flat'});
  pup({kind:'girl',x:740,y:G+10,s:1.2,flip:-1,look:[-.4,.4],brows:'sad',mouth:'flat'});
  if(u>.8){ctx.save();ctx.globalAlpha=win(u,.8,8);bubbleText(540,680,"round tables or long? 😤",1,.8);ctx.restore();}
  if(u>1.6)raincloudSmall(540,580,win(u,1.6,9)*.6);''',
HUG,
]
SCENES = spec(BODY_LINES, D, [{'either of you':'🤍'},{'anyway':'💍'},{'wants':'🎵'},{'new':'🥹'},{'person':'💌'},{'wedding':'🚩'},{'before it':'🤍'}])
IG_LINE = "The song. The fiance word. The seating chart fight. Everyone gets through it their own way... Want to know yours? There's a sixty second test in our bio. Take it together."
IG_CAPS = C(IG_LINE, {'song':'🎵','yours?':'🤍','bio':'🔗'})
IG_RESULT = "Acts of Service"
TT_LINE = TT_STD
