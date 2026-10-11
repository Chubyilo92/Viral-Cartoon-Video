import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
import jjlib as J
from _kit import S, HUG, SHARE
TITLE = "when they need space to heal"
BODY_LINES = [
"When someone who needs space to process loves you... they'll text \"I just need a bit of time, I'm not going anywhere\" — before you've even asked what's wrong.",
"Not because they're shutting you out — they can't find the right words until the hurt stops being so loud.",
"They'll ask for a night alone after something hurts, not a conversation right away.",
"They'll come back ready to actually talk, instead of saying something in the moment they'd take back later.",
"If someone's taught you that space isn't rejection, it's just how they come back whole... send this to them.",
"But if the space turns into days of silence with nothing attached to it... that's not processing, that's disappearing.",
"Because someone who asks for space and still comes back every time... isn't pulling away, they're loving you the long way round.",
]
SCENES = [
S(["when someone","needs space to heal","loves you, they'll text 📱","'I just need","a bit of time,","I'm not going","anywhere' 🤍"], '''  room('#3d4b6c','#303b57','rgba(255,255,255,.05)');
  phoneMock(540,780,.62,0,()=>{ctx.fillStyle='#eef0f5';ctx.fillRect(-70,-290,140,280);ctx.font='13px Poppins';ctx.fillStyle=INK;ctx.textAlign='center';ctx.fillText('not going anywhere 🤍',0,-150);});'''),
S(["not because","they're shutting","you out 🤍","they can't find","the right words","until the hurt","stops being so loud"], '''  room('#e3c9a0','#bf9670');
  pup({kind:'girl',x:540,y:G+10,s:1.3,flip:-1,look:[0,.1],brows:'sad',mouth:'flat',hy:4});'''),
S(["they'll ask for","a night alone 🌙","after something hurts","not a","conversation right away"], '''  room('#f6d7c6','#d6a286');
  pup({kind:'girl',x:720,y:G+10,s:1.22,flip:-1,look:[.2,.1],brows:'sad',mouth:'flat',hy:3});
  pup({kind:'boy',x:380,y:G+10,s:1.26,look:[.3,0],mouth:'flat',earLift:-.05});'''),
S(["they'll come back","ready to actually","talk 🤍","instead of saying","something in the","moment they'd","take back later"], '''  room('#f1d5b0','#caa070');
  pup({kind:'girl',x:680,y:G+10,s:1.26,flip:-1,eyes:'happy',mouth:'smile',blush:.3});
  pup({kind:'boy',x:400,y:G+10,s:1.28,eyes:'happy',mouth:'smile',blush:.3,paw:{x:90,y:-150,k:.9}});'''),
S(["if someone's","taught you that","space isn't","rejection 🤍","it's how they","come back whole","send this to them 💌"], SHARE),
S(["but if the space","turns into days","of silence 🌧️","with nothing","attached to it","that's not","processing, that's","disappearing"], '''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  phoneMock(420,800,.48,.06,()=>{ctx.fillStyle='#2b2830';ctx.fillRect(-70,-290,140,280);});
  pup({kind:'boy',x:680,y:G+10,s:1.28,look:[-.2,.1],brows:'sad',mouth:'flat',hy:4});
  if(u>1)raincloudSmall(680,710,win(u,1,7));'''),
S(["because someone","who asks for space","and still comes","back every time 🤍","is loving you","the long way round"], HUG),
]
IG_LINE = "'I'm not going anywhere' texted first. Space that isn't rejection... want to know how they love? 60-second test in our bio."
IG_CAPS = ["'I'm not","going anywhere' 🤍","texted first","the space,","asked for gently 🌙","want to know yours?","60-second test","in our bio 🔗","and see if they","know yours 💌"]
IG_RESULT = "Quality Time"
TT_LINE = "We're two little pups trying to find a thousand people who love like this... If this made you think of someone... follow us. We'll keep making them for you."
