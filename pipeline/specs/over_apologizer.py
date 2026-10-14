import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
import jjlib as J
from _kit import S, HUG, SHARE
TITLE = "when they always say sorry"
BODY_LINES = [
"When the over-apologizer loves you... they'll say sorry for the weather, for being thirty seconds late, for taking up space on the couch.",
"Not because they did something wrong — somewhere along the way, \"sorry\" became how they ask \"are we okay?\"",
"They'll apologize for crying, then apologize for apologizing.",
"They'll flinch and say sorry before you've even finished your sentence, bracing for anger that was never coming.",
"If someone's learning that they don't need to apologize for existing near you... send this to them.",
"But if \"sorry\" replaces ever actually fixing anything... that's not remorse, that's a reflex standing in for change.",
"Because someone who finally says \"I was scared, not sorry\"... is learning the difference, for you.",
]
SCENES = [
S(["when the","over-apologizer","loves you 🤍","they'll say sorry","for the weather,","for being 30","seconds late"], '''  room('#f1d5b0','#caa070');
  pup({kind:'girl',x:540,y:G+10,s:1.32,flip:-1,look:[0,.1],brows:'sad',mouth:'flat',earLift:-.05});
  if(u>.6&&u<5){ctx.save();ctx.globalAlpha=win(u,.6,5);bubbleText(540,610,"sorry, sorry, I know",1,.58);ctx.restore();}'''),
S(["not because they","did something wrong 🤍","somewhere along","the way, 'sorry'","became how they","ask 'are we okay?'"], '''  room('#e3c9a0','#bf9670');
  pup({kind:'girl',x:540,y:G+10,s:1.3,look:[0,.1],brows:'sad',mouth:'flat',hy:3});'''),
S(["they'll apologize","for crying 😢","then apologize","for apologizing"], '''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  pup({kind:'girl',x:620,y:G+10,s:1.26,flip:-1,look:[-.1,.2],brows:'sad',mouth:'flat',hy:5});
  if(u>1)raincloudSmall(620,710,win(u,1,4));'''),
S(["they'll flinch and","say sorry before","you finish your","sentence 🤍","bracing for anger","that was never coming"], '''  room('#f6d7c6','#d6a286');
  pup({kind:'girl',x:420,y:G+10,s:1.24,flip:-1,look:[.2,.1],eyes:'wide',mouth:'flat',earLift:-.1});
  pup({kind:'boy',x:700,y:G+10,s:1.26,eyes:'open',mouth:'flat',paw:{x:90,y:-140,k:.9}});'''),
S(["if someone's","learning they don't","need to apologize","for existing","near you 🤍","send this to them 💌"], SHARE),
S(["but if 'sorry'","replaces ever","actually fixing","anything 🌧️","that's not remorse,","that's a reflex"], '''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  pup({kind:'girl',x:680,y:G+10,s:1.26,flip:-1,look:[-.2,.1],brows:'sad',mouth:'flat',hy:4});
  if(u>1)raincloudSmall(680,710,win(u,1,7));'''),
S(["because someone","who finally says","'I was scared,","not sorry' 🤍","is learning the","difference, for you"], HUG),
]
IG_LINE = "Finally saying 'I was scared, not sorry'. Learning the difference... want to know how they love? 60-second test in our bio."
IG_CAPS = ["'I was scared,","not sorry' 🤍","learning the","difference, for you","want to know yours?","60-second test","in our bio 🔗","and see if they","know yours 💌"]
IG_RESULT = "Words of Affirmation"
TT_LINE = "We're two little pups trying to find a thousand people who love like this... If this made you think of someone... follow us. We'll keep making them for you."
