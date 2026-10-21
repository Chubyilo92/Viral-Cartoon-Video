import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD, C
TITLE = "when you're new parents"
BODY_LINES = [
"When you're new parents, the exhaustion either breaks a couple or quietly rebuilds them.",
"Not because sleep doesn't matter. Because watching you love the baby made them love you more.",
"They take the 3am feed without being asked, so you can sleep one more hour.",
"They catch you crying over nothing... and just hold the baby, no questions, no fixing.",
"If you're surviving the hardest nights of your life together... send this to your co-parent.",
"But if the baby becomes the only thing you talk about... you lost each other somewhere in there.",
"Because new parents who still check in on each other... are raising two things at once.",
]
D = [
'''  room('#3d4b6c','#303b57','rgba(255,255,255,.05)');
  pup({kind:'boy',x:420,y:G+10,s:1.2,look:[.3,.3],brows:'sad',mouth:'flat',earLift:-.2});
  pup({kind:'girl',x:740,y:G+10,s:1.2,flip:-1,look:[-.3,.3],eyes:'happy',mouth:'smile',blush:.3});
  if(u>2)zzz(480,540,u,win(u,2,9)*.6);''',
'''  room('#f3cfa8','#d09d72');
  pup({kind:'boy',x:360,y:G+10,s:1.25,look:[.5,-.1],eyes:'happy',mouth:'smile',blush:.4});
  pup({kind:'girl',x:760,y:G+10,s:1.25,flip:-1,look:[-.5,-.1],eyes:'happy',mouth:'smile',blush:.5});
  if(u>1)floatHearts(560,800,1,u,3,130);''',
'''  room('#3d4b6c','#303b57','rgba(255,255,255,.05)');
  pup({kind:'girl',x:540,y:G+10,s:1.2,look:[0,.2],eyes:'closed',mouth:'smile'});
  pup({kind:'boy',x:880,y:1020,s:.55,look:[0,-.2],eyes:'closed',mouth:'flat',shadow:false});
  if(u>.6)zzz(900,920,u,win(u,.6,9)*.5);''',
'''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  pup({kind:'girl',x:380,y:G+10,s:1.25,look:[.3,.4],brows:'sad',mouth:'flat'});
  if(u>.6)raincloudSmall(380,610,win(u,.6,9)*.5);
  pup({kind:'boy',x:760,y:1020,s:.55,flip:-1,look:[0,-.2],eyes:'closed',mouth:'flat',shadow:false});''',
SHARE,
'''  room('#6f6a78','#5a5562','rgba(255,255,255,.05)');
  pup({kind:'boy',x:400,y:1010,s:.55,look:[0,-.2],eyes:'closed',mouth:'flat',shadow:false});
  pup({kind:'girl',x:740,y:G+10,s:1.2,flip:-1,look:[-.3,.4],brows:'sad',mouth:'flat'});
  if(u>.8)raincloudSmall(740,610,win(u,.8,9)*.6);''',
HUG,
]
SCENES = spec(BODY_LINES, D, [{'rebuilds them':'🤍'},{'more':'🥹'},{'hour':'🍼'},{'fixing':'🤍'},{'co-parent':'💌'},{'in there':'🚩'},{'at once':'🤍'}])
IG_LINE = "The 3am feed. The quiet holding. The checking in. Every new parent shows love their own way... Want to know yours? There's a sixty second test in our bio. Take it together."
IG_CAPS = C(IG_LINE, {'feed':'🍼','yours?':'🤍','bio':'🔗'})
IG_RESULT = "Acts of Service"
TT_LINE = TT_STD
