import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
import jjlib as J
from _kit import S, HUG, SHARE
TITLE = "when a frugal partner loves you"
BODY_LINES = [
"When a frugal partner loves you... they'll wear the same old jacket for five years, then buy you the coffee you actually like without blinking.",
"It's not that they're cheap — it's that they grew up counting every penny, and they're not about to waste one on themselves.",
"They'll drive the long way to save on parking, then quietly cover the whole bill when you're not looking.",
"They'll say \"we don't need that\" about everything they want, and \"get it\" about anything you need.",
"If someone's careful with every penny except the ones spent on you... send this to them.",
"But if careful turns into controlling what you spend, or guilt over every purchase... that's not frugal anymore, that's fear with a grip on you.",
"Because someone who goes without so you don't have to... isn't being careful with money, they're being careful with you.",
]
SCENES = [
S(["when a frugal","partner loves you 🧥","they'll wear the","same old jacket","for five years"], '''  room('#e3c9a0','#bf9670');
  pup({kind:'boy',x:540,y:G+10,s:1.3,look:[0,.1],eyes:'happy',mouth:'smile',tilt:.04,earLift:.05});
  ctx.save();ctx.globalAlpha=.3;ctx.font='18px Poppins';ctx.textAlign='center';ctx.fillText('(5 years old)',540,G-280);ctx.restore();'''),
S(["then buy you","the coffee you","actually like 🤍","without blinking"], '''  room('#f1d5b0','#caa070');
  mug(700,G+40,1);
  pup({kind:'girl',x:360,y:G+10,s:1.3,flip:-1,eyes:'happy',mouth:'smile',blush:.4,tilt:-.05});'''),
S(["they'll drive","the long way","to save on","parking 🚗","then quietly","cover the whole bill","when you're not looking"], '''  room('#f6d7c6','#d6a286');
  pup({kind:'boy',x:620,y:G+10,s:1.28,look:[-.2,0],eyes:'happy',mouth:'smile',earLift:.08});
  if(u>2)floatHearts(540,880,2,u,3,140);'''),
S(["they'll say","\"we don't","need that\" 🤍","about everything","they want","and \"get it\"","about anything","you need"], '''  room('#f1d5b0','#caa070');
  phoneMock(730,780,.62,-.04,()=>{ctx.fillStyle='#eef0f5';ctx.fillRect(-70,-290,140,280);ctx.font='14px Poppins';ctx.fillStyle=INK;ctx.textAlign='center';ctx.fillText('get it, you need it',0,-150);});
  pup({kind:'girl',x:340,y:G+10,s:1.26,flip:-1,eyes:'happy',mouth:'smile',blush:.3});'''),
S(["if someone's","careful with","every penny 🤍","except the ones","spent on you","send this","to them 💌"], SHARE),
S(["but if careful","turns into","controlling what","you spend 🌧️","or guilt over","every purchase","that's not frugal","anymore, that's fear"], '''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  pup({kind:'boy',x:640,y:G+10,s:1.3,look:[-.1,.2],brows:'sad',mouth:'flat',hy:4});
  if(u>1)raincloudSmall(640,720,win(u,1,7));'''),
S(["because someone","who goes without","so you don't","have to 🤍","isn't being careful","with money","they're being","careful with you"], HUG),
]
IG_LINE = "The five-year-old jacket. The coffee you like, bought without blinking. The bill covered quietly... want to know how they love? 60-second test in our bio."
IG_CAPS = ["the five-year-old","jacket 🧥","the coffee","bought without","blinking 🤍","want to know yours?","60-second test","in our bio 🔗","and see if they","know yours 💌"]
IG_RESULT = "Acts of Service"
TT_LINE = "We're two little pups trying to find a thousand people who love like this... If this made you think of someone... follow us. We'll keep making them for you."
