import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
import jjlib as J
from _kit import S, HUG, SHARE
TITLE = "when they can't sit still"
BODY_LINES = [
"When someone who can't sit still loves you... they'll fold the laundry mid-movie, because sitting still for too long makes their skin itch.",
"Not because they don't want to relax with you — rest has always felt like something they have to earn first.",
"They'll reorganize the pantry at 11pm instead of just saying out loud that they're anxious.",
"They'll finally sit down next to you... and ask if there's anything else that needs doing, like stillness itself is a waste.",
"If someone's learning that doing nothing with you is still doing something... send this to them.",
"But if the moving never stops long enough for you to even reach them... that's not energy, that's avoidance wearing a to-do list.",
"Because someone who finally sits down and stays... is choosing you over the next task, for once.",
]
SCENES = [
S(["when someone","can't sit still","loves you 🧺","they'll fold the","laundry mid-movie","because sitting still","makes their skin itch"], '''  room('#e3c9a0','#bf9670');
  pup({kind:'girl',x:620,y:G+10,s:1.28,flip:-1,look:[-.2,.1],eyes:'open',mouth:'flat',earLift:.1,paw:{x:100,y:-60,k:.8}});
  blob(rectPts(700,980,160,50,10),'#fbf1e2',{lw:3});
  if(u>.6){ctx.save();ctx.globalAlpha=win(u,.6,5);bubbleText(420,560,"just folding this real quick",1,.55);ctx.restore();}'''),
S(["not because they","don't want to","relax with you 🤍","rest has always","felt like something","they have to","earn first"], '''  room('#f1d5b0','#caa070');
  pup({kind:'boy',x:540,y:G+10,s:1.32,look:[0,.1],brows:'sad',mouth:'flat',hy:3});'''),
S(["they'll reorganize","the pantry at","11pm 🌙","instead of just","saying out loud","that they're anxious"], '''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  pup({kind:'boy',x:700,y:G+10,s:1.24,look:[-.2,0],eyes:'wide',mouth:'flat',earLift:-.05,paw:{x:90,y:-80,k:.9}});
  blob(rectPts(380,900,90,170,8),'#caa070');blob(rectPts(480,900,90,170,8),'#caa070');'''),
S(["they'll finally","sit down next","to you 🤍","and ask if","there's anything else","that needs doing"], '''  room('#f6d7c6','#d6a286');
  pup({kind:'boy',x:420,y:G+10,s:1.26,look:[.2,.1],brows:'sad',mouth:'flat'});
  pup({kind:'girl',x:700,y:G+10,s:1.26,flip:-1,eyes:'happy',mouth:'smile',blush:.3});'''),
S(["if someone's","learning that","doing nothing","with you 🤍","is still","doing something","send this to them 💌"], SHARE),
S(["but if the","moving never","stops 🌧️","long enough","for you to","even reach them","that's not energy,","that's avoidance"], '''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  pup({kind:'girl',x:680,y:G+10,s:1.26,flip:-1,look:[-.2,.1],brows:'sad',mouth:'flat',hy:4,paw:{x:90,y:-80,k:1}});
  if(u>1)raincloudSmall(680,710,win(u,1,8));'''),
S(["because someone","who finally sits","down and stays 🤍","is choosing you","over the next","task, for once"], HUG),
]
IG_LINE = "Finally sitting down and staying. Choosing you over the next task... want to know how they love? 60-second test in our bio."
IG_CAPS = ["finally sitting","down and staying 🤍","choosing you over","the next task","want to know yours?","60-second test","in our bio 🔗","and see if they","know yours 💌"]
IG_RESULT = "Quality Time"
TT_LINE = "We're two little pups trying to find a thousand people who love like this... If this made you think of someone... follow us. We'll keep making them for you."
