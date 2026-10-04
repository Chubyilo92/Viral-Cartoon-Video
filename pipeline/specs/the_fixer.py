import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
import jjlib as J
from _kit import S, HUG, SHARE
TITLE = "when the fixer loves you"
BODY_LINES = [
"When \"the fixer\" loves you... they'll have three solutions ready before you've finished the sentence.",
"Not because your feelings don't matter — fixing is the only way they know to show they heard you.",
"They'll search the problem at midnight instead of just lying there with you in it.",
"They'll go quiet and hurt when you say \"I just need you to listen\" — because to them, fixing was listening.",
"If someone loves you loud through solutions but is learning to love you quiet too... send this to them.",
"But if every feeling gets turned into a problem to solve instead of a moment to share... that's worth saying out loud.",
"Because a fixer who learns to just listen first... is doing the hardest rewiring love ever asked of them.",
]
SCENES = [
S(["when \"the fixer\"","loves you 🔧","they'll have","three solutions ready","before you've","finished the sentence"], '''  room('#f1d5b0','#caa070');
  pup({kind:'boy',x:540,y:G+10,s:1.32,look:[0,.1],eyes:'wide',mouth:'open',earLift:.15,hy:4});
  if(u>1.2){ctx.save();ctx.globalAlpha=win(u,1.2,7);ctx.font='26px Poppins';ctx.textAlign='center';ctx.fillText('💡💡💡',540,G-230);ctx.restore();}'''),
S(["not because","your feelings","don't matter 🤍","fixing is the","only way they know","to show","they heard you"], '''  room('#e3c9a0','#bf9670');
  pup({kind:'boy',x:540,y:G+10,s:1.3,look:[0,.1],eyes:'open',mouth:'flat',earLift:.05});'''),
S(["they'll search","the problem","at midnight 🌙","instead of","just lying there","with you in it"], '''  room('#3d4b6c','#303b57','rgba(255,255,255,.05)');
  phoneMock(700,780,.62,-.04,()=>{ctx.fillStyle='#111';ctx.fillRect(-70,-290,140,280);ctx.fillStyle='#8fd0ff';ctx.font='11px Poppins';ctx.textAlign='center';ctx.fillText('how to fix...',0,-150);});
  pup({kind:'girl',x:340,y:G+30,s:1.26,flip:-1,look:[.3,-.2],eyes:'open',mouth:'flat',blush:.1,shadow:false});'''),
S(["they'll go quiet","and hurt 😔","when you say","\"i just need","you to listen\"","to them, fixing","was listening"], '''  room('#f6d7c6','#d6a286');
  pup({kind:'boy',x:620,y:G+10,s:1.3,flip:-1,look:[-.2,.2],brows:'sad',mouth:'flat',hy:4,earLift:-.1});
  pup({kind:'girl',x:320,y:G+10,s:1.26,look:[.4,0],eyes:'open',mouth:'flat',blush:.1});'''),
S(["if someone loves","you loud through","solutions 🤍","but is learning","to love you","quiet too","send this","to them 💌"], SHARE),
S(["but if every","feeling gets turned","into a problem 🌧️","to solve instead","of a moment","to share","that's worth","saying out loud"], '''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  pup({kind:'girl',x:640,y:G+10,s:1.3,flip:-1,look:[.1,.3],brows:'sad',mouth:'flat',hy:4});
  if(u>1)raincloudSmall(640,720,win(u,1,7));'''),
S(["because a fixer","who learns to","just listen first 🤍","is doing the","hardest rewiring","love ever","asked of them"], HUG),
]
IG_LINE = "Three solutions before you finished the sentence. The midnight search. Learning to just listen first... want to know how they love? 60-second test in our bio."
IG_CAPS = ["three solutions","before you finished","the sentence 💡","the midnight search","learning to","just listen first 🤍","want to know yours?","60-second test","in our bio 🔗","and see if they","know yours 💌"]
IG_RESULT = "Words of Affirmation"
TT_LINE = "We're two little pups trying to find a thousand people who love like this... If this made you think of someone... follow us. We'll keep making them for you."
