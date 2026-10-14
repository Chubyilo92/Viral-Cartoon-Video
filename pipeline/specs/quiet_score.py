import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
import jjlib as J
from _kit import S, HUG, SHARE
TITLE = "when they keep quiet score"
BODY_LINES = [
"When someone who keeps quiet score loves you... they'll say \"it's fine\" about the thing that clearly wasn't fine, three days ago.",
"Not because they're holding a grudge — they just never learned how to say \"that hurt\" in the moment it happened.",
"They'll bring up something small from last month, out of nowhere, and not even know why it's surfacing now.",
"They'll apologize for \"overreacting\" right after finally saying the thing they'd been sitting on for weeks.",
"If someone's learning to say it small, right when it happens, instead of saving it up... send this to them.",
"But if every fight becomes a greatest-hits list of everything that's ever bothered them... that's not honesty, that's a bill coming due all at once.",
"Because someone who finally says \"that hurt\" in the moment, instead of a month later... is choosing you over the score they used to keep.",
]
SCENES = [
S(["when someone","keeps quiet score","loves you 🤐","they'll say","'it's fine' about","the thing that","wasn't fine"], '''  room('#e3c9a0','#bf9670');
  pup({kind:'girl',x:540,y:G+10,s:1.3,flip:-1,look:[0,.1],brows:'sad',mouth:'flat'});
  if(u>.6&&u<5){ctx.save();ctx.globalAlpha=win(u,.6,5);bubbleText(540,610,"it's fine, don't worry",1,.55);ctx.restore();}'''),
S(["not because","they're holding","a grudge 🤍","they just never","learned how to","say 'that hurt'","in the moment"], '''  room('#f1d5b0','#caa070');
  pup({kind:'girl',x:540,y:G+10,s:1.32,flip:-1,look:[0,.1],brows:'sad',mouth:'flat',hy:3});'''),
S(["they'll bring up","something small","from last month 📅","out of nowhere","and not even know","why it's surfacing"], '''  room('#f6d7c6','#d6a286');
  pup({kind:'boy',x:400,y:G+10,s:1.26,look:[.2,0],eyes:'wide',mouth:'flat'});
  pup({kind:'girl',x:700,y:G+10,s:1.24,flip:-1,look:[-.2,.1],brows:'sad',mouth:'flat'});'''),
S(["they'll apologize","for 'overreacting' 🤍","right after finally","saying the thing","they'd been sitting","on for weeks"], '''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  pup({kind:'girl',x:620,y:G+10,s:1.26,flip:-1,look:[-.1,.2],brows:'sad',mouth:'flat',hy:4});
  if(u>1)raincloudSmall(620,710,win(u,1,4));'''),
S(["if someone's","learning to say","it small, right","when it happens 🤍","instead of","saving it up","send this to them 💌"], SHARE),
S(["but if every","fight becomes a","greatest-hits list 🌧️","of everything that's","ever bothered them","that's not honesty,","that's a bill"], '''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  pup({kind:'boy',x:680,y:G+10,s:1.26,look:[-.2,.1],brows:'sad',mouth:'flat',hy:4});
  if(u>1)raincloudSmall(680,710,win(u,1,8));'''),
S(["because someone","who finally says","'that hurt' 🤍","in the moment,","instead of a","month later 🤍","is choosing you"], HUG),
]
IG_LINE = "Finally saying 'that hurt' in the moment. Choosing you over the score they used to keep... want to know how they love? 60-second test in our bio."
IG_CAPS = ["finally saying","'that hurt' 🤍","in the moment","not a month later","want to know yours?","60-second test","in our bio 🔗","and see if they","know yours 💌"]
IG_RESULT = "Words of Affirmation"
TT_LINE = "We're two little pups trying to find a thousand people who love like this... If this made you think of someone... follow us. We'll keep making them for you."
