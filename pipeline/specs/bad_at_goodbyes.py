import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
import jjlib as J
from _kit import S, HUG, SHARE
TITLE = "when they're bad at goodbyes"
BODY_LINES = [
"When someone bad at goodbyes loves you... they'll hug you one beat too long at the door, like letting go first makes it more real.",
"Not clingy — just someone who's learned that \"see you later\" still needs a moment before it's true.",
"They'll text \"landed safe?\" before you've even left the jet bridge, thinking about you the whole flight.",
"They'll walk you to the car in the cold, every single time, just to get three more minutes.",
"If someone makes every goodbye last a little longer than it needs to... send this to them before you go.",
"But if goodbyes turn into guilt trips about leaving at all... that's not missing you, that's control dressed up as missing you.",
"Because someone who hates goodbyes but never once asks you to stay... loves you enough to let you go anyway.",
]
SCENES = [
S(["when someone bad","at goodbyes loves you 🚪","they'll hug you","one beat too long","at the door","like letting go","makes it more real"], '''  room('#f1d5b0','#caa070');
  pup({kind:'girl',x:560,y:G+10,s:1.3,flip:-1,look:[-.2,.1],eyes:'happy',mouth:'smile',blush:.4,paw:{x:60,y:-180,k:1}});
  pup({kind:'boy',x:440,y:G+10,s:1.3,look:[.2,.1],eyes:'happy',mouth:'smile',blush:.3,earLift:.1});'''),
S(["not clingy 🤍","just someone","who's learned","that 'see you","later' still needs","a moment","before it's true"], '''  room('#e3c9a0','#bf9670');
  pup({kind:'girl',x:540,y:G+10,s:1.3,flip:-1,look:[0,.1],brows:'sad',mouth:'flat',hy:4});'''),
S(["they'll text","'landed safe?' ✈️","before you've even","left the jet bridge","thinking about you","the whole flight"], '''  room('#3d4b6c','#303b57','rgba(255,255,255,.05)');
  phoneMock(540,780,.62,0,()=>{ctx.fillStyle='#eef0f5';ctx.fillRect(-70,-290,140,280);ctx.font='13px Poppins';ctx.fillStyle=INK;ctx.textAlign='center';ctx.fillText('landed safe? 🤍',0,-150);});'''),
S(["they'll walk you","to the car","in the cold 🥶","every single time","just to get","three more minutes"], '''  room('#aeb9c9','#8a97aa');
  pup({kind:'boy',x:420,y:G+10,s:1.26,look:[.2,0],mouth:'flat',earLift:.05});
  pup({kind:'girl',x:680,y:G+10,s:1.24,flip:-1,eyes:'happy',mouth:'smile',blush:.3});'''),
S(["if someone makes","every goodbye last","a little longer 🤍","than it needs to","send this to them","before you go 💌"], SHARE),
S(["but if goodbyes","turn into","guilt trips 🌧️","about leaving","at all","that's control","dressed up","as missing you"], '''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  pup({kind:'boy',x:640,y:G+10,s:1.3,look:[-.1,.2],brows:'sad',mouth:'flat',hy:4});
  if(u>1)raincloudSmall(640,720,win(u,1,7));'''),
S(["because someone","who hates goodbyes","but never asks","you to stay 🤍","loves you enough","to let you","go anyway"], HUG),
]
IG_LINE = "The too-long hug at the door. 'Landed safe?' before you've even left the gate... want to know how they love? 60-second test in our bio."
IG_CAPS = ["the hug","one beat too long 🤍","'landed safe?'","before you've left ✈️","want to know yours?","60-second test","in our bio 🔗","and see if they","know yours 💌"]
IG_RESULT = "Physical Touch"
TT_LINE = "We're two little pups trying to find a thousand people who love like this... If this made you think of someone... follow us. We'll keep making them for you."
