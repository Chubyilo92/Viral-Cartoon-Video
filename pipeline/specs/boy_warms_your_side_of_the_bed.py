import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD, C
from _short import SHORT_PROPS
TITLE = "when a boy warms your side first"
PRELUDE = SHORT_PROPS
BODY_LINES = [
"When a boy gets into your side of the bed first, he's not stealing it.",
"He climbs in on your side first, just to take the cold off it before you get there.",
"On winter nights he'll lie there on your cold sheets till he hears the bathroom tap turn off.",
"He never once mentions it. He just moves over when you walk in.",
"If you've climbed into a bed that was already warm... send this to him.",
"But the night you get in and his side is warm and yours is cold... he hasn't forgotten. He's stopped waiting for you.",
"Because a boy who warms your side first... would rather be cold than let you be.",
]
D = [
'''  bedNight();bedBack();
  pup({kind:'boy',x:380,y:G-100,s:1.15,flip:1,look:[.2,-.1],eyes:'closed',mouth:'smile',tilt:.05,blush:.3,shadow:false});
  blanket(150,540,G-150);''',
'''  room('#f1d5b0','#caa070');bedBack();
  pup({kind:'boy',x:360,y:G-60,s:1.15,flip:1,look:[.3,-.2],eyes:'open',mouth:'flat',shadow:false});
  for(let i=0;i<3;i++)snowflake(230+i*70,G-170,15-i*2,.85);''',
'''  bedNight();bedBack();
  pup({kind:'boy',x:380,y:G-100,s:1.15,flip:1,look:[.65,-.05],eyes:'open',mouth:'flat',earLift:.35,tilt:.02,shadow:false});
  blanket(150,540,G-150);
  blob(rectPts(650,430,110,185,16),'#445577',{lw:4});
  ell(705,570,34,15,'#dce9f2',{lw:3});
  tube([[705,570],[705,525],[687,500],[667,495]],14,'#bcd8ea');
  const flow=win(u,.3,4.2);
  if(flow>.02){ctx.save();ctx.globalAlpha=flow;tube([[667,502],[667,558]],6,'#8fc8f0');ctx.restore();}''',
'''  room('#3a4560','#2a3550','rgba(255,255,255,.05)');bedBack();
  const k=P(u,.3,1.5),k2=P(u,.4,1.6);
  pup({kind:'boy',x:lerp(380,720,k),y:G-100,s:1.15,flip:1,look:[.2,-.1],eyes:'open',mouth:'smile',tilt:.04,shadow:false});
  pup({kind:'girl',x:lerp(220,380,k2),y:G-100,s:1.15,flip:-1,look:[.4,0],eyes:'happy',mouth:'smile',shadow:false});
  blanket(150,780,G-150);''',
SHARE,
'''  room('#333c54','#28304a','rgba(255,255,255,.05)');bedBack();
  pup({kind:'boy',x:720,y:G-100,s:1.15,flip:-1,look:[-.2,-.1],eyes:'closed',mouth:'flat',tilt:-.04,shadow:false});
  blanket(620,865,G-150);
  pup({kind:'girl',x:360,y:G-90,s:1.15,flip:1,look:[.3,0],eyes:'open',mouth:'flat',tilt:-.03,shadow:false});
  for(let i=0;i<3;i++){snowflake(200+i*80,G-230,16-i*2,.9);}
  ell(380,G-30,170,16,'#ffffff18',{stroke:false});''',
'''  bedNight();bedBack();
  pup({kind:'girl',x:360,y:G-100,s:1.15,flip:1,look:[.3,-.05],eyes:'closed',mouth:'smile',tilt:.04,blush:.3,shadow:false});
  blanket(150,540,G-150);
  pup({kind:'boy',x:700,y:G-80,s:1.15,flip:-1,look:[-.3,-.05],eyes:'happy',mouth:'smile',tilt:-.04,blush:.2,shadow:false});
  for(let i=0;i<2;i++)snowflake(630+i*70,G-200,14-i*2,.8);
  if(u>.6)floatHearts(540,700,.6,u,3,140);''',
]
SCENES = spec(BODY_LINES, D, [{'stealing it':'🛏️'},{'before you':'🥶'},{'tap turn off':'🚿'},{'walk in':'🤍'},{'send this':'💌'},{'stopped waiting':'🚩'},{'let you be':'🤍'}])
IG_LINE = "The side he warms before you get there. The move-over he never mentions. The side that stays warm. Everyone shows love their own way... Want to know yours? There's a sixty second test in our bio. Take it together."
IG_CAPS = C(IG_LINE, {'warms':'🛏️','yours?':'🤍','bio':'🔗'})
IG_RESULT = "Physical Touch"
TT_LINE = TT_STD
