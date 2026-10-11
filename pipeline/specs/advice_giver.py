import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
import jjlib as J
from _kit import S, HUG, SHARE
TITLE = "when the advice-giver loves you"
BODY_LINES = [
"When the advice-giver in the relationship loves you... they'll catch themselves mid-sentence, right before \"well, what I'd do is...\" comes out.",
"Not because they think you can't decide — caring and directing have always felt like the same thing to them.",
"They'll have an opinion on your job, your friends, your whole life, ready before you even finish asking.",
"They'll ask \"do you want advice, or do you just want me to listen?\" and actually wait for the answer.",
"If someone's learning to just listen first, after a lifetime of jumping to fix it... send this to them.",
"But if the opinions turn into decisions made for you, without you... that's not love, that's control in a helpful voice.",
"Because someone who used to have all the answers and is learning to just ask the question... is doing real work, for you.",
]
SCENES = [
S(["when the","advice-giver loves you 🤐","they'll catch","themselves mid-sentence","right before 'well,","what I'd do is...'"], '''  room('#e3c9a0','#bf9670');
  pup({kind:'boy',x:540,y:G+10,s:1.32,look:[0,.1],eyes:'wide',mouth:'flat',earLift:-.05});
  if(u>.6&&u<5){ctx.save();ctx.globalAlpha=win(u,.6,5);bubbleText(540,620,"well, what I'd—",1,.6);ctx.restore();}'''),
S(["not because","they think you","can't decide 🤍","caring and directing","have always felt","like the same thing"], '''  room('#e3c9a0','#bf9670');
  pup({kind:'boy',x:540,y:G+10,s:1.32,look:[0,.1],eyes:'open',mouth:'flat',earLift:.05});'''),
S(["they'll have","an opinion on","your job 💡","your friends,","your whole life","ready before you","even finish asking"], '''  room('#f1d5b0','#caa070');
  pup({kind:'boy',x:420,y:G+10,s:1.3,look:[.2,0],eyes:'wide',mouth:'open',earLift:.15});
  pup({kind:'girl',x:700,y:G+10,s:1.24,flip:-1,look:[-.2,0],mouth:'flat'});
  ctx.save();ctx.globalAlpha=win(u,.5,6);ctx.font='24px Poppins';ctx.textAlign='center';ctx.fillText('💡💡',420,G-240);ctx.restore();'''),
S(["they'll ask","'do you want advice,","or just me","to listen?' 🤍","and actually wait","for the answer"], '''  room('#f6d7c6','#d6a286');
  pup({kind:'boy',x:400,y:G+10,s:1.28,look:[.3,0],eyes:'open',mouth:'flat'});
  pup({kind:'girl',x:700,y:G+10,s:1.26,flip:-1,eyes:'happy',mouth:'smile',blush:.4});'''),
S(["if someone's","learning to just","listen first 🤍","after a lifetime","of jumping to","fix it","send this","to them 💌"], SHARE),
S(["but if the","opinions turn into","decisions made","for you 🌧️","without you","that's not love","that's control"], '''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  pup({kind:'girl',x:640,y:G+10,s:1.3,flip:-1,look:[.1,.3],brows:'sad',mouth:'flat',hy:4});
  if(u>1)raincloudSmall(640,720,win(u,1,7));'''),
S(["because someone","learning to just","ask the question 🤍","instead of having","all the answers","is doing real","work, for you"], HUG),
]
IG_LINE = "Catching themselves mid-sentence. Learning to just listen first... want to know how they love? 60-second test in our bio."
IG_CAPS = ["catching themselves","mid-sentence 🤐","learning to","just listen 🤍","want to know yours?","60-second test","in our bio 🔗","and see if they","know yours 💌"]
IG_RESULT = "Quality Time"
TT_LINE = "We're two little pups trying to find a thousand people who love like this... If this made you think of someone... follow us. We'll keep making them for you."
