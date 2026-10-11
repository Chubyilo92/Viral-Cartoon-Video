import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
import jjlib as J
from _kit import S, HUG, SHARE
TITLE = "when they're slow to let go"
BODY_LINES = [
"When someone still healing from their last relationship loves you... they'll flinch at a notification before they even look at the screen.",
"Not because they're comparing you — their body just remembers what came before you did.",
"They'll ask \"are we okay?\" after a totally normal quiet moment, because quiet used to mean something was wrong.",
"They'll move slower with the big words, because they've learned what it costs to say them too soon.",
"If someone's letting you prove the past wrong, one patient day at a time... send this to them.",
"But if you use what scared them before against them in a fight... you become the thing they were afraid of.",
"Because someone still healing who keeps choosing you anyway... isn't holding onto the past, they're building proof it's over.",
]
SCENES = [
S(["when someone","still healing loves you 📳","they'll flinch at","a notification","before they even","look at the screen"], '''  room('#3d4b6c','#303b57','rgba(255,255,255,.05)');
  pup({kind:'girl',x:540,y:G+10,s:1.3,eyes:'wide',mouth:'flat',hy:6,tilt:-.05});
  ctx.save();ctx.globalAlpha=win(u,.3,5);ctx.font='30px Poppins';ctx.textAlign='center';ctx.fillText('📳',540,G-260);ctx.restore();'''),
S(["not because","they're comparing you 🤍","their body just","remembers what came","before you did"], '''  room('#e3c9a0','#bf9670');
  pup({kind:'girl',x:540,y:G+10,s:1.3,flip:-1,look:[0,.1],brows:'sad',mouth:'flat',hy:4});'''),
S(["they'll ask","'are we okay?' 🥺","after a totally","normal quiet moment","because quiet","used to mean","something was wrong"], '''  room('#f1d5b0','#caa070');
  pup({kind:'boy',x:380,y:G+10,s:1.26,look:[.3,0],mouth:'flat',earLift:.05});
  pup({kind:'girl',x:680,y:G+10,s:1.26,flip:-1,look:[-.3,0],brows:'sad',mouth:'flat'});
  if(u>.8&&u<5.5){ctx.save();ctx.globalAlpha=win(u,.8,5.5);bubbleText(680,620,"are we okay?",1,.6);ctx.restore();}'''),
S(["they'll move slower","with the big","words 🤍","because they've learned","what it costs","to say them","too soon"], '''  room('#f6d7c6','#d6a286');
  pup({kind:'boy',x:420,y:G+10,s:1.3,look:[.2,.1],eyes:'open',mouth:'flat',blush:.2});
  pup({kind:'girl',x:680,y:G+10,s:1.26,flip:-1,eyes:'happy',mouth:'smile',blush:.3});'''),
S(["if someone's","letting you prove","the past wrong 🤍","one patient day","at a time","send this","to them 💌"], SHARE),
S(["but if you use","what scared them","before 🌧️","against them","in a fight","you become the","thing they feared"], '''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  pup({kind:'girl',x:640,y:G+10,s:1.3,flip:-1,look:[-.1,.2],brows:'sad',mouth:'flat',hy:4});
  if(u>1)raincloudSmall(640,720,win(u,1,7));'''),
S(["because someone","still healing who","keeps choosing","you anyway 🤍","is building proof","it's over"], HUG),
]
IG_LINE = "The flinch at a notification. The 'are we okay?' The big words said slower, not smaller... want to know how they love? 60-second test in our bio."
IG_CAPS = ["the flinch","at a notification 📳","the big words","said slower 🤍","want to know yours?","60-second test","in our bio 🔗","and see if they","know yours 💌"]
IG_RESULT = "Words of Affirmation"
TT_LINE = "We're two little pups trying to find a thousand people who love like this... If this made you think of someone... follow us. We'll keep making them for you."
