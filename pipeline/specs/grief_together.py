import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD, C
TITLE = "when you lose someone together"
BODY_LINES = [
"When you lose someone together, the silence after is where you find out who they really are.",
"Not because they have the right words. Because they stop needing any.",
"They sit with you on the floor for an hour and never once check their phone.",
"They bring food you didn't ask for and leave before you have to say thank you.",
"If someone sat through your worst week without flinching... send this to the one who stayed.",
"But if grief makes them disappear because they don't know what to say... that's not love, that's convenience.",
"Because showing up for someone's worst week... isn't about fixing it, it's about not leaving.",
]
D = [
'''  room('#6f6a78','#5a5562','rgba(255,255,255,.05)');
  flower(760,G+10,.9);
  pup({kind:'girl',x:380,y:G+20,s:1.2,look:[.3,.3],brows:'sad',mouth:'flat'});''',
'''  room('#8fb6c9','#6f98ac');
  pup({kind:'boy',x:380,y:G+10,s:1.2,look:[.3,.1],eyes:'open',mouth:'flat'});
  pup({kind:'girl',x:740,y:G+10,s:1.2,flip:-1,look:[-.3,.1],eyes:'open',mouth:'flat'});''',
'''  room('#cfe3ec','#98b6c2');
  pup({kind:'boy',x:420,y:G+40,s:1.15,look:[.2,.3],eyes:'open',mouth:'flat'});
  pup({kind:'girl',x:700,y:G+40,s:1.15,flip:-1,look:[-.2,.3],brows:'sad',mouth:'flat'});''',
'''  room('#f3cfa8','#d09d72');
  bowl(720,G-10,true);
  pup({kind:'boy',x:380,y:G+10,s:1.2,look:[.4,0],eyes:'open',mouth:'flat'});
  if(u>.8){ctx.save();ctx.globalAlpha=win(u,.8,8);bubbleText(380,680,"didn't know what you needed, so... soup",1,.8);ctx.restore();}''',
SHARE,
'''  room('#6f6a78','#5a5562','rgba(255,255,255,.05)');
  pup({kind:'girl',x:380,y:G+10,s:1.2,look:[.4,.3],brows:'sad',mouth:'flat'});
  pup({kind:'boy',x:760,y:G+10,s:1.2,flip:-1,look:[-.4,.3],brows:'sad',mouth:'flat'});
  if(u>.8){ctx.save();ctx.globalAlpha=win(u,.8,8);bubbleText(560,680,"...I'll check in later, okay?",1,.8);ctx.restore();}
  if(u>1.6)raincloudSmall(540,580,win(u,1.6,9)*.6);''',
HUG,
]
SCENES = spec(BODY_LINES, D, [{'really are':'🤍'},{'any':'🤍'},{'phone':'🤍'},{'thank you':'🍲'},{'who stayed':'💌'},{'convenience':'🚩'},{'not leaving':'🤍'}])
IG_LINE = "The hour on the floor. The food you didn't ask for. The not-leaving when it's hardest to stay. Everyone shows up for grief their own way... Want to know yours? There's a sixty second test in our bio. Take it together."
IG_CAPS = C(IG_LINE, {'floor':'🤍','yours?':'🤍','bio':'🔗'})
IG_RESULT = "Quality Time"
TT_LINE = TT_STD
