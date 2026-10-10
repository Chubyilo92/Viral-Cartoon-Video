import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
import jjlib as J
from _kit import S, HUG, SHARE
TITLE = "when a protector loves you"
BODY_LINES = [
"When a protector loves you... they'll ask who's picking you up tonight, before you've even said you're going out.",
"Not to control your night — they'd just rather be the one who knows you got there safe.",
"They'll walk on the side closest to traffic without even thinking about it.",
"They'll text \"let me know when you're home\" and actually stay awake until you do.",
"If someone needs to know you got home safe before they can really relax... send this to them.",
"But if \"who were you with\" turns into questioning every plan you make without them... that's not protection anymore, that's control.",
"Because real protection makes you feel safer, not smaller... and the moment it shrinks you, it was never about you at all.",
]
SCENES = [
S(["when a protector","loves you 🤍","they'll ask","who's picking","you up tonight","before you've","even said","you're going out"], '''  room('#f1d5b0','#caa070');
  pup({kind:'girl',x:340,y:G+10,s:1.26,flip:-1,eyes:'happy',mouth:'open',blush:.3});
  pup({kind:'boy',x:660,y:G+10,s:1.26,look:[-.2,0],eyes:'wide',mouth:'flat',earLift:.05});
  if(u>1.6&&u<6){ctx.save();ctx.globalAlpha=win(u,1.6,6);bubbleText(660,730,"who's picking you up?",1,.68);ctx.restore();}'''),
S(["not to control","your night 🤍","they'd just","rather be the","one who knows","you got there safe"], '''  room('#e3c9a0','#bf9670');
  pup({kind:'boy',x:540,y:G+10,s:1.34,look:[0,.1],eyes:'happy',mouth:'smile',blush:.3,tilt:.04,earLift:.1});'''),
S(["they'll walk on","the side closest","to traffic 🚗","without even","thinking about it"], '''  room('#f1d5b0','#caa070');
  ell(540,G+16,320,30,'#00000010',{stroke:false});
  pup({kind:'boy',x:700,y:G+10,s:1.3,eyes:'happy',mouth:'smile',tilt:.05,earLift:.1});
  pup({kind:'girl',x:420,y:G+10,s:1.3,flip:-1,eyes:'happy',mouth:'smile',blush:.3,tilt:-.05});
  ctx.save();ctx.globalAlpha=.8;ctx.font='24px Poppins';ctx.fillText('🚗',880,G-30);ctx.restore();'''),
S(["they'll text","\"let me know","when you're home\" 📱","and actually","stay awake","until you do"], '''  room('#3d4b6c','#303b57','rgba(255,255,255,.05)');
  phoneMock(540,760,.78,0,()=>{ctx.fillStyle='#eef0f5';ctx.fillRect(-70,-290,140,280);ctx.font='13px Poppins';ctx.fillStyle=INK;ctx.textAlign='center';ctx.fillText("text me when you're home",0,-200);});
  pup({kind:'boy',x:540,y:G+10,s:1.15,look:[0,-.1],eyes:'half',mouth:'flat'});'''),
S(["if someone needs","to know you","got home safe 🤍","before they can","really relax","send this","to them 💌"], SHARE),
S(["but if","\"who were","you with\" 🌧️","turns into","questioning every plan","you make without them","that's not protection","anymore, that's control"], '''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  pup({kind:'boy',x:640,y:G+10,s:1.3,look:[-.2,.1],brows:'sad',mouth:'flat',hy:4});
  if(u>1)raincloudSmall(640,720,win(u,1,7));'''),
S(["because real","protection makes","you feel safer","not smaller 🤍","and the moment","it shrinks you","it was never","about you at all"], HUG),
]
IG_LINE = "Who's picking you up, asked before you even said you were going out. Staying awake for the text home... want to know how they love? 60-second test in our bio."
IG_CAPS = ["who's picking","you up? 🤍","staying awake","for the text","want to know yours?","60-second test","in our bio 🔗","and see if they","know yours 💌"]
IG_RESULT = "Acts of Service"
TT_LINE = "We're two little pups trying to find a thousand people who love like this... If this made you think of someone... follow us. We'll keep making them for you."
