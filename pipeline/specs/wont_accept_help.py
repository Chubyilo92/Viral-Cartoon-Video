import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
import jjlib as J
from _kit import S, HUG, SHARE
TITLE = "when they can't accept help"
BODY_LINES = [
"When someone who can't accept help loves you... they'll wave you off mid-struggle with the box, then drop it two steps later.",
"Not because they don't trust you — somewhere, needing help got filed away as proof they'd finally used up someone's patience.",
"They'll say \"I've got it\" with their arms visibly shaking.",
"They'll let you help exactly once, then spend the next hour making sure you know they didn't need to.",
"If someone's learning that letting you carry half the box doesn't make them less capable, and doesn't use up your patience either... send this to them.",
"But if \"I've got it\" means they never actually let you in, on anything... that's not independence, that's a wall with good posture.",
"Because someone who finally hands you one end of the box... is trusting you with more than furniture.",
]
SCENES = [
S(["when someone","can't accept help","loves you 📦","they'll wave you","off mid-struggle","with the box"], '''  room('#e3c9a0','#bf9670');
  pup({kind:'boy',x:460,y:G+10,s:1.3,look:[.2,.1],eyes:'wide',mouth:'open',earLift:-.05,paw:{x:150,y:-60,k:1}});
  blob(rectPts(640,940,150,130,8),'#caa070',{lw:3});'''),
S(["not because they","don't trust you 🤍","somewhere, needing","help got filed","away as the","same thing as","being a burden"], '''  room('#f1d5b0','#caa070');
  pup({kind:'boy',x:540,y:G+10,s:1.32,look:[0,.1],brows:'sad',mouth:'flat',hy:3});'''),
S(["they'll say","'I've got it' 💪","with their arms","visibly shaking"], '''  room('#f6d7c6','#d6a286');
  pup({kind:'boy',x:620,y:G+10,s:1.28,look:[-.1,0],eyes:'wide',mouth:'flat',paw:{x:100,y:-110,k:1}});
  if(u>.5&&u<4){ctx.save();ctx.globalAlpha=win(u,.5,4);bubbleText(620,610,"I've got it, really",1,.55);ctx.restore();}'''),
S(["they'll let you","help exactly once 🤍","then spend the","next hour making","sure you know","they didn't need to"], '''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  pup({kind:'boy',x:420,y:G+10,s:1.26,look:[.2,0],eyes:'open',mouth:'flat'});
  pup({kind:'girl',x:700,y:G+10,s:1.24,flip:-1,look:[-.2,0],eyes:'happy',mouth:'smile',blush:.3});'''),
S(["if someone's","learning that","letting you carry","half the box 📦","doesn't make them","less capable","send this to them 💌"], SHARE),
S(["but if 'I've","got it' means they","never actually","let you in 🌧️","on anything","that's not independence,","that's a wall"], '''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  pup({kind:'boy',x:680,y:G+10,s:1.26,look:[-.2,.1],brows:'sad',mouth:'flat',hy:4});
  if(u>1)raincloudSmall(680,710,win(u,1,8));'''),
S(["because someone","who finally hands","you one end","of the box 🤍","is trusting you","with more than","furniture"], HUG),
]
IG_LINE = "Finally handing you one end of the box. Trusting you with more than furniture... want to know how they love? 60-second test in our bio."
IG_CAPS = ["handing you","one end of","the box 📦🤍","trusting you with","more than furniture","want to know yours?","60-second test","in our bio 🔗"]
IG_RESULT = "Acts of Service"
TT_LINE = "We're two little pups trying to find a thousand people who love like this... If this made you think of someone... follow us. We'll keep making them for you."
