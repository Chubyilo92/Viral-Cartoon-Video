import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
import jjlib as J
from _kit import S, HUG, SHARE
TITLE = "when they're bad at compliments"
BODY_LINES = [
"When someone bad at receiving compliments loves you... they'll deflect \"you look amazing\" with a joke before it even lands.",
"Not because they don't want to hear it — they just never learned where to put it.",
"They'll argue with \"you're so thoughtful\" like it's a fact to be checked, then go quietly do something thoughtful an hour later.",
"They can't say \"thank you, I know\" — so they say it back in actions instead, over and over.",
"If someone shows you what they can't say out loud... send this to them.",
"But if every kind word just bounces off and nothing ever lands... that's worth gently naming.",
"Because someone who can't take a compliment but keeps earning them anyway... is still trying, in the only language that feels safe.",
]
SCENES = [
S(["when someone bad","at receiving compliments","loves you 😅","they'll deflect","\"you look amazing\"","with a joke","before it even lands"], '''  room('#f1d5b0','#caa070');
  pup({kind:'girl',x:540,y:G+10,s:1.32,flip:-1,look:[0,.1],eyes:'happy',mouth:'open',blush:.4,tilt:-.08,earLift:.1});
  if(u>2&&u<6.5){ctx.save();ctx.globalAlpha=win(u,2,6.5);bubbleText(540,730,"haha this old thing?",1,.85);ctx.restore();}'''),
S(["not because","they don't","want to hear it 🤍","they just","never learned","where to put it"], '''  room('#e3c9a0','#bf9670');
  pup({kind:'girl',x:540,y:G+10,s:1.3,flip:-1,look:[0,.2],brows:'sad',mouth:'flat',blush:.1});'''),
S(["they'll argue with","\"you're so thoughtful\" 🤨","like it's a fact","to be checked","then go quietly","do something thoughtful","an hour later"], '''  room('#f6d7c6','#d6a286');
  pup({kind:'girl',x:620,y:G+10,s:1.3,flip:-1,look:[-.2,.1],brows:'sad',mouth:'flat',blush:.1});
  pup({kind:'boy',x:320,y:G+10,s:1.26,look:[.4,0],eyes:'happy',mouth:'smile',tilt:.04,earLift:.1});'''),
S(["they can't say","\"thank you, i know\" 🙈","so they say it","back in actions","instead, over","and over"], '''  room('#f1d5b0','#caa070');
  pup({kind:'girl',x:540,y:G+10,s:1.3,flip:-1,look:[0,.1],eyes:'happy',mouth:'smile',blush:.4,tilt:-.06,paw:{x:60,y:-180,k:.6}});
  if(u>2)floatHearts(540,860,2,u,3,140);'''),
S(["if someone shows","you what they","can't say out loud 🤍","send this","to them 💌"], SHARE),
S(["but if every","kind word just","bounces off 🌧️","and nothing","ever lands","that's worth","gently naming"], '''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  pup({kind:'boy',x:640,y:G+10,s:1.3,look:[.1,.3],brows:'sad',mouth:'flat',hy:4});
  if(u>1)raincloudSmall(640,720,win(u,1,7));'''),
S(["because someone","who can't take","a compliment 🤍","but keeps earning","them anyway","is still trying","in the only language","that feels safe"], HUG),
]
IG_LINE = "The deflected \"you look amazing.\" The thoughtful thing done quietly an hour later... every person shows love in their own way. 60-second test in our bio."
IG_CAPS = ["the deflected","\"you look amazing\" 😅","the thoughtful thing","done quietly","an hour later 🤍","want to know yours?","60-second test","in our bio 🔗","and see if they","know yours 💌"]
IG_RESULT = "Acts of Service"
TT_LINE = "We're two little pups trying to find a thousand people who love like this... If this made you think of someone... follow us. We'll keep making them for you."
