import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
import jjlib as J
from _kit import S, HUG, SHARE
TITLE = "when they need the plan"
BODY_LINES = [
"When someone who needs the plan loves you... they'll go quiet and pale the second you say \"actually, let's just wing it.\"",
"Not because they're controlling — somewhere, growing up, not knowing what was coming usually meant something bad actually did.",
"They'll ask \"what time, exactly\" three times, not because they didn't hear you, because certainty is how they breathe.",
"They'll have a backup plan for the backup plan, and still apologize for needing one.",
"If someone's learning that you winging it isn't the same as things falling apart... send this to them.",
"But if every unplanned moment turns into a full shutdown... that's not preference, that's old fear still running the room.",
"Because someone who finally says \"okay, let's just see what happens\"... is trusting you with the one thing that used to scare them most.",
]
SCENES = [
S(["when someone","needs the plan","loves you 📋","they'll go quiet","and pale the","second you say","'let's just wing it'"], '''  room('#e3c9a0','#bf9670');
  pup({kind:'boy',x:540,y:G+10,s:1.3,look:[0,.1],eyes:'wide',mouth:'flat',earLift:-.1});
  if(u>.6&&u<5){ctx.save();ctx.globalAlpha=win(u,.6,5);bubbleText(540,610,"wait, what time though",1,.55);ctx.restore();}'''),
S(["not because","they're controlling 🤍","somewhere, not","knowing what's next","used to mean","something bad","was coming"], '''  room('#f1d5b0','#caa070');
  pup({kind:'boy',x:540,y:G+10,s:1.32,look:[0,.1],brows:'sad',mouth:'flat',hy:3});'''),
S(["they'll ask 'what","time, exactly' 🕐","three times","not because they","didn't hear you","certainty is how","they breathe"], '''  room('#f6d7c6','#d6a286');
  pup({kind:'boy',x:420,y:G+10,s:1.26,look:[.2,0],eyes:'wide',mouth:'flat'});
  pup({kind:'girl',x:700,y:G+10,s:1.24,flip:-1,look:[-.2,.1],eyes:'happy',mouth:'smile',blush:.3});'''),
S(["they'll have a","backup plan for","the backup plan 📋","and still apologize","for needing one"], '''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  pup({kind:'boy',x:620,y:G+10,s:1.26,look:[-.1,0],brows:'sad',mouth:'flat',paw:{x:100,y:-110,k:.9}});'''),
S(["if someone's","learning that you","winging it isn't","the same as","things falling","apart 🤍","send this to them 💌"], SHARE),
S(["but if every","unplanned moment","turns into a","full shutdown 🌧️","that's not preference,","that's old fear"], '''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  pup({kind:'boy',x:680,y:G+10,s:1.26,look:[-.2,.1],brows:'sad',mouth:'flat',hy:4});
  if(u>1)raincloudSmall(680,710,win(u,1,7));'''),
S(["because someone","who finally says","'okay, let's just","see what happens' 🤍","is trusting you","with the unknown"], HUG),
]
IG_LINE = "Finally saying 'okay, let's just see what happens'. Trusting you with the unknown... want to know how they love? 60-second test in our bio."
IG_CAPS = ["finally saying","'let's just see","what happens' 🤍","trusting you with","the unknown","want to know yours?","60-second test","in our bio 🔗"]
IG_RESULT = "Quality Time"
TT_LINE = "We're two little pups trying to find a thousand people who love like this... If this made you think of someone... follow us. We'll keep making them for you."
