import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
import jjlib as J
from _kit import S, HUG, SHARE
TITLE = "when a peacemaker loves you"
BODY_LINES = [
"When a peacemaker loves you... they'll say sorry first, even when the fight wasn't their fault to begin with.",
"Not because they're a pushover — it's because the relationship matters more to them than being right.",
"They'll change the topic the second it gets too sharp, not to dodge it, but because they hate seeing you hurt more than losing.",
"They'll check in an hour later with your favorite snack, like nothing happened, because to them, nothing did.",
"If someone keeps the peace even when it costs them being right... send this to them.",
"But if they're always the one bending, and you're never the one who says sorry first... that peace is costing them more than you know.",
"Because a peacemaker who keeps choosing calm over winning... isn't weak, they just love you more than they love being right.",
]
SCENES = [
S(["when a peacemaker","loves you 🤍","they'll say sorry","first, even when","the fight wasn't","their fault","to begin with"], '''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  pup({kind:'girl',x:540,y:G+10,s:1.3,flip:-1,look:[0,.1],brows:'sad',mouth:'flat',hy:4,paw:{x:80,y:-150,k:.6}});
  if(u>1&&u<5){ctx.save();ctx.globalAlpha=win(u,1,5);bubbleText(540,720,"I'm sorry, that was on me",1,.68);ctx.restore();}'''),
S(["not because","they're a","pushover 🤍","it's because the","relationship matters","more to them","than being right"], '''  room('#e3c9a0','#bf9670');
  pup({kind:'girl',x:540,y:G+10,s:1.34,flip:-1,look:[0,.1],eyes:'happy',mouth:'smile',blush:.3,tilt:-.04});'''),
S(["they'll change","the topic","the second","it gets too sharp 😅","not to dodge it","but because they","hate seeing you","hurt more than losing"], '''  room('#f1d5b0','#caa070');
  pup({kind:'girl',x:420,y:G+10,s:1.28,flip:-1,eyes:'happy',mouth:'open',blush:.3});
  pup({kind:'boy',x:660,y:G+10,s:1.28,look:[-.2,.1],mouth:'flat'});'''),
S(["they'll check in","an hour later","with your","favorite snack 🍪","like nothing","happened, because","to them, nothing did"], '''  room('#f6d7c6','#d6a286');
  bowl(760,G+40,1);
  pup({kind:'girl',x:360,y:G+10,s:1.3,flip:-1,eyes:'happy',mouth:'smile',blush:.4,tilt:-.05});
  if(u>2)floatHearts(540,880,2,u,3,140);'''),
S(["if someone keeps","the peace 🤍","even when","it costs them","being right","send this","to them 💌"], SHARE),
S(["but if they're","always the","one bending 🌧️","and you're never","the one who","says sorry first","that peace is","costing them more"], '''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  pup({kind:'girl',x:640,y:G+10,s:1.3,flip:-1,look:[.1,.3],brows:'sad',mouth:'flat',hy:4});
  if(u>1)raincloudSmall(640,720,win(u,1,7));'''),
S(["because a peacemaker","who keeps choosing","calm over winning 🤍","isn't weak","they just love you","more than they","love being right"], HUG),
]
IG_LINE = "The sorry said first. The topic changed before it gets sharp. The snack an hour later, like nothing happened... want to know how they love? 60-second test in our bio."
IG_CAPS = ["the sorry","said first 🤍","the snack","an hour later","want to know yours?","60-second test","in our bio 🔗","and see if they","know yours 💌"]
IG_RESULT = "Words of Affirmation"
TT_LINE = "We're two little pups trying to find a thousand people who love like this... If this made you think of someone... follow us. We'll keep making them for you."
