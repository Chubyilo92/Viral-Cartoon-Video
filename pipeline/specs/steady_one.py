import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
import jjlib as J
from _kit import S, HUG, SHARE
TITLE = "when the steady one loves you"
BODY_LINES = [
"When the responsible one loves you... they'll answer the 2am crisis call, then still show up to your thing, exhausted.",
"Not because they lack limits — they just never learned it was allowed to say \"not today.\"",
"They'll organize everyone else's chaos, then sit quietly in their own — no one taught them how to ask back.",
"They'll apologize for crying in front of you, like needing you is an inconvenience instead of the point.",
"If someone holds everyone together and rarely falls apart except with you... send this to them.",
"But if \"I'm fine, I'll handle it\" becomes the only thing they ever say... that's loneliness wearing a good attitude.",
"Because the responsible one who finally lets you catch them... is trusting you with something they never show anyone else.",
]
SCENES = [
S(["when the","responsible one loves you 📞","they'll answer the","2am crisis call","then still show up","to your thing, exhausted"], '''  room('#3d4b6c','#303b57','rgba(255,255,255,.05)');
  pup({kind:'boy',x:540,y:G+10,s:1.3,eyes:'closed',mouth:'flat',hy:6,tilt:.08});
  phoneMock(760,900,.5,-.05,()=>{ctx.fillStyle='#111';ctx.fillRect(-70,-290,140,280);ctx.fillStyle='#8fd0ff';ctx.font='24px Poppins';ctx.textAlign='center';ctx.fillText('02:14',0,-150);});'''),
S(["not because","they don't have","limits 🤍","they just never","learned it was","allowed to say","'not today'"], '''  room('#e3c9a0','#bf9670');
  pup({kind:'boy',x:540,y:G+10,s:1.34,look:[0,.1],brows:'sad',mouth:'flat',hy:4});'''),
S(["they'll organize","everyone else's chaos 📝","then sit quietly","in their own","because no one","taught them to","ask for help back"], '''  room('#f1d5b0','#caa070');
  pup({kind:'boy',x:540,y:G+10,s:1.3,look:[0,.2],brows:'sad',mouth:'flat',hy:4});
  ctx.save();ctx.globalAlpha=win(u,.5,6);ctx.translate(330,720);ctx.rotate(-.08);blob(rectPts(-40,-30,80,60,6),'#fde98a',{lw:4});ctx.restore();
  ctx.save();ctx.globalAlpha=win(u,1,6);ctx.translate(770,760);ctx.rotate(.1);blob(rectPts(-36,-26,72,52,6),'#a8d8e8',{lw:4});ctx.restore();'''),
S(["they'll apologize","for crying","in front of you 🥺","like needing you","is an inconvenience","instead of the","whole point"], '''  room('#f6d7c6','#d6a286');
  pup({kind:'boy',x:420,y:G+10,s:1.28,look:[.2,.2],brows:'sad',mouth:'flat',hy:4});
  pup({kind:'girl',x:700,y:G+10,s:1.26,flip:-1,eyes:'happy',mouth:'smile',blush:.3,paw:{x:-90,y:-150,k:.9}});'''),
S(["if someone holds","everyone together","and rarely","falls apart 🤍","in front of anyone","but you","send this to them 💌"], SHARE),
S(["but if","'I'm fine, I'll","handle it' 🌧️","becomes the only","thing they","ever say","that's loneliness","with a good attitude"], '''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  pup({kind:'boy',x:640,y:G+10,s:1.3,look:[-.1,.2],brows:'sad',mouth:'flat',hy:4});
  if(u>1)raincloudSmall(640,720,win(u,1,7));'''),
S(["because the","responsible one who","finally lets you","catch them 🤍","is trusting you","with the one thing","they never show","anyone else"], HUG),
]
IG_LINE = "The 2am crisis call, answered anyway. Learning to let you catch them... want to know how they love? 60-second test in our bio."
IG_CAPS = ["the 2am call,","answered anyway 📞","learning to let","you catch them 🤍","want to know yours?","60-second test","in our bio 🔗","and see if they","know yours 💌"]
IG_RESULT = "Acts of Service"
TT_LINE = "We're two little pups trying to find a thousand people who love like this... If this made you think of someone... follow us. We'll keep making them for you."
