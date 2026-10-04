import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
import jjlib as J
from _kit import S, HUG, SHARE
TITLE = "when a hurt boy loves you"
BODY_LINES = [
"When a boy who's been hurt before loves you... he'll check his phone less, once he's sure you're not the one who disappears.",
"Not distrust of you — he was just braced for the old pattern to repeat.",
"He'll go quiet when you're five minutes late, then exhale the second you walk through the door.",
"He'll let you meet the people he protects, because that's the only \"I trust you\" he knows how to give.",
"If someone's slowly letting you prove the old pattern wrong... send this to him.",
"But if you use what he told you in confidence against him, even once... you become proof he was right to guard it.",
"Because when a hurt boy finally lets someone in... it's the bravest bet he's placed in years.",
]
SCENES = [
S(["when a boy","who's been hurt","before loves you 💔","he'll check","his phone less","once he's sure","you're not the one","who disappears"], '''  room('#f1d5b0','#caa070');
  phoneMock(360,780,.6,.05,()=>{ctx.fillStyle='#eef0f5';ctx.fillRect(-70,-290,140,280);});
  pup({kind:'boy',x:620,y:G+10,s:1.3,look:[-.2,0],eyes:'open',mouth:'flat',earLift:-.1,hy:4});'''),
S(["not distrust","of you 🤍","he was","just braced","for the old","pattern to repeat"], '''  room('#e3c9a0','#bf9670');
  pup({kind:'boy',x:540,y:G+10,s:1.32,look:[0,.1],brows:'sad',mouth:'flat',earLift:-.1});'''),
S(["he'll go quiet","when you're five","minutes late 🕐","then exhale","the second you","walk through the door"], '''  room('#f6d7c6','#d6a286');
  pup({kind:'boy',x:360,y:G+10,s:1.3,look:[.4,0],eyes:u<4?'open':'happy',mouth:u<4?'flat':'smile',earLift:u<4?-.15:.1,hy:u<4?4:0});
  pup({kind:'girl',x:820,y:u<4?G-20:G+10,s:1.1,flip:-1,look:[-.6,0],eyes:'happy',mouth:'smile',blush:.3,shadow:u>=4});'''),
S(["he'll let you","meet the people","he protects 🤍","because that's","the only","\"i trust you\"","he knows","how to give"], '''  room('#f1d5b0','#caa070');plant(970,G+6,.9);
  pup({kind:'boy',x:340,y:G+10,s:1.3,look:[.4,.1],eyes:'happy',mouth:'smile',tilt:.06,earLift:.1});
  pup({kind:'girl',x:640,y:G+10,s:1.3,flip:-1,look:[-.4,.1],eyes:'happy',mouth:'smile',blush:.4,tilt:-.06});
  pup({kind:'boy',x:880,y:G+40,s:.75,look:[-.5,.2],eyes:'happy',mouth:'smile',earLift:.1});'''),
S(["if someone's","slowly letting you","prove the old","pattern wrong 🤍","send this","to him 💌"], SHARE),
S(["but if you use","what he told you","in confidence 🌧️","against him","even once","you become proof","he was right","to guard it"], '''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  pup({kind:'boy',x:640,y:G+10,s:1.3,look:[.1,.3],brows:'sad',mouth:'flat',hy:4,earLift:-.2});
  if(u>1)raincloudSmall(640,720,win(u,1,7));'''),
S(["because when","a hurt boy","finally lets","someone in 🤍","it's the","bravest bet","he's placed","in years"], HUG),
]
IG_LINE = "The phone he checks less. The relief at the door. The people he finally let you meet... 60-second test in our bio."
IG_CAPS = ["the phone","he checks less 🤍","the relief","at the door","the people","he let you meet","want to know yours?","60-second test","in our bio 🔗","and see if","he knows yours 💌"]
IG_RESULT = "Physical Touch"
TT_LINE = "We're two little pups trying to find a thousand people who love like this... If this made you think of someone... follow us. We'll keep making them for you."
