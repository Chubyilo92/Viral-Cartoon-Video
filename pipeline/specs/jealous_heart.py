import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
import jjlib as J
from _kit import S, HUG, SHARE
TITLE = "when a jealous heart loves you"
BODY_LINES = [
"When a jealous heart loves you... they'll go quiet for a second when someone flirts with you.",
"Not because they don't trust you — it's because they can't stand the thought of losing this.",
"They'll ask who texted back, then laugh it off before it turns into a thing.",
"They'll hold your hand a little tighter in a crowded room, not to control you, just to feel close.",
"If someone gets quiet because they're scared of losing you, not because they don't trust you... send this to them.",
"But if quiet turns into checking your phone, or counting who you talked to... that's not love anymore, that's control.",
"Because a little jealousy means they see what they have... but the moment it takes your freedom, it stops being love.",
]
SCENES = [
S(["when a jealous","heart loves you 🤍","they'll go quiet","for a second","when someone","flirts with you 😶"], '''  room('#f1d5b0','#caa070');
  pup({kind:'girl',x:700,y:G+10,s:1.2,look:[-.3,0],eyes:'happy',mouth:'smile',blush:.4});
  if(u>.5&&u<4.5){ctx.save();ctx.globalAlpha=win(u,.5,4.5);bubbleText(840,700,"nice collar 😏",1,.7);ctx.restore();}
  pup({kind:'boy',x:360,y:G+10,s:1.28,look:[.2,0],mouth:'flat',brows:'sad',earLift:-.1,hy:4});'''),
S(["not because","they don't trust you 🤍","it's because","they can't stand","the thought","of losing this"], '''  room('#e3c9a0','#bf9670');
  pup({kind:'boy',x:540,y:G+10,s:1.34,look:[0,.1],brows:'sad',mouth:'flat',hy:5});'''),
S(["they'll ask","who texted back 📱","then laugh","it off","before it turns","into a thing 😅"], '''  room('#f6d7c6','#d6a286');
  phoneMock(730,780,.62,-.04,()=>{ctx.fillStyle='#eef0f5';ctx.fillRect(-70,-290,140,280);ctx.font='15px Poppins';ctx.fillStyle=INK;ctx.textAlign='center';ctx.fillText('who was that? 😅',0,-150);});
  pup({kind:'girl',x:340,y:G+10,s:1.26,flip:-1,look:[.3,0],eyes:'happy',mouth:'smile',blush:.3});'''),
S(["they'll hold","your hand a","little tighter 🤍","in a crowded room","not to control you","just to feel close"], '''  room('#f1d5b0','#caa070');
  ell(540,G+16,320,30,'#00000010',{stroke:false});
  pup({kind:'girl',x:440,y:G+10,s:1.3,flip:-1,eyes:'happy',mouth:'smile',blush:.4,tilt:-.05,paw:{x:80,y:-150,k:.9}});
  pup({kind:'boy',x:660,y:G+10,s:1.3,eyes:'happy',mouth:'smile',blush:.3,tilt:.05,paw:{x:-80,y:-150,k:.9}});
  if(u>1.6)floatHearts(540,760,1.6,u,3,140);'''),
S(["if someone","gets quiet 🤍","because they're","scared of losing you","not because","they don't trust you","send this","to them 💌"], SHARE),
S(["but if quiet","turns into checking","your phone 🌧️","or counting","who you talked to","that's not love","anymore, that's control"], '''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  pup({kind:'boy',x:640,y:G+10,s:1.3,look:[-.1,.2],brows:'sad',mouth:'flat',hy:4});
  phoneMock(420,800,.48,.06,()=>{ctx.fillStyle='#2b2830';ctx.fillRect(-70,-290,140,280);});
  if(u>1)raincloudSmall(640,720,win(u,1,7));'''),
S(["because a little","jealousy means","they see what","they have 🤍","but the moment","it takes your freedom","it stops being love"], HUG),
]
IG_LINE = "The quiet second. The 'who was that?' laughed off. The hand held tighter in a crowd... want to know how they love? 60-second test in our bio."
IG_CAPS = ["the quiet second 🤍","the hand held","tighter in a crowd","want to know yours?","60-second test","in our bio 🔗","take it together","and see if they","know yours 💌"]
IG_RESULT = "Physical Touch"
TT_LINE = "We're two little pups trying to find a thousand people who love like this... If this made you think of someone... follow us. We'll keep making them for you."
