import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
import jjlib as J
from _kit import S, HUG, SHARE
TITLE = "when opposites love each other"
BODY_LINES = [
"When opposites love each other... one of you has a five-year plan, one doesn't know what's for dinner — and you've never missed a flight.",
"One of you replies in seconds, one reads it Tuesday and answers Thursday, and you've learned neither one is wrong.",
"One of you needs the weekend planned, one needs to wake up and see — so you take turns choosing, instead of losing.",
"The loud one got quieter around you. The quiet one got louder around them.",
"If your opposite somehow balances you instead of fighting you... send this to them.",
"But if different stops balancing and starts just colliding, every time... that's worth a real conversation.",
"Because opposites who choose each other, on purpose, every day... build something neither one could build alone.",
]
SCENES = [
S(["when opposites","love each other 🧲","one of you has","a five-year plan","one doesn't know","what's for dinner","and you've never","missed a flight"], '''  room('#f1d5b0','#caa070');
  pup({kind:'girl',x:320,y:G+10,s:1.28,flip:-1,look:[.4,0],eyes:'open',mouth:'flat',blush:.1,tilt:-.03,paw:{x:60,y:-170,k:.6}});
  pup({kind:'boy',x:740,y:G+10,s:1.28,look:[-.4,0],eyes:'wide',mouth:'open',earLift:.1});
  ctx.save();ctx.globalAlpha=.9;ctx.font='22px Poppins';ctx.textAlign='center';ctx.fillText('📋',320,G-220);ctx.fillText('🤷',740,G-220);ctx.restore();'''),
S(["one of you","replies in seconds ⚡","one reads it","tuesday and","answers thursday 😅","and you've learned","neither one","is wrong"], '''  room('#e3c9a0','#bf9670');
  phoneMock(700,780,.6,-.04,()=>{ctx.fillStyle='#eef0f5';ctx.fillRect(-70,-290,140,280);ctx.font='11px Poppins';ctx.fillStyle=INK;ctx.textAlign='center';ctx.fillText('seen Tue',0,-150);});
  pup({kind:'girl',x:320,y:G+10,s:1.26,flip:-1,look:[.5,0],eyes:'happy',mouth:'smile',blush:.2,wag:.4});'''),
S(["one of you needs","the weekend planned 📋","one needs to","wake up and see 🌅","so you take turns","choosing, instead","of losing"], '''  room('#f6d7c6','#d6a286');
  pup({kind:'girl',x:360,y:G+10,s:1.27,flip:-1,look:[.4,0],eyes:'happy',mouth:'smile',blush:.2,tilt:-.04});
  pup({kind:'boy',x:740,y:G+10,s:1.27,look:[-.4,0],eyes:'happy',mouth:'smile',tilt:.04,earLift:.1});'''),
S(["the loud one","got quieter","around you 🤍","the quiet one","got louder","around them"], '''  room('#f1d5b0','#caa070');
  pup({kind:'boy',x:360,y:G+10,s:1.3,look:[.3,0],eyes:'happy',mouth:'smile',tilt:.05,earLift:.1});
  pup({kind:'girl',x:720,y:G+10,s:1.3,flip:-1,look:[-.3,.1],eyes:'happy',mouth:'open',blush:.3,tilt:-.06,wag:.4});'''),
S(["if your opposite","somehow balances you 🤍","instead of","fighting you","send this","to them 💌"], SHARE),
S(["but if different","stops balancing 🌧️","and starts just","colliding, every time","that's worth","a real conversation"], '''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  pup({kind:'girl',x:420,y:G+10,s:1.25,flip:-1,look:[.3,.2],brows:'sad',mouth:'flat',hy:3});
  pup({kind:'boy',x:700,y:G+10,s:1.25,look:[-.3,.2],brows:'sad',mouth:'flat',hy:3});
  if(u>1)raincloudSmall(560,700,win(u,1,7));'''),
S(["because opposites","who choose each other 🤍","on purpose","every day","build something","neither one","could build alone"], HUG),
]
IG_LINE = "The five-year plan next to \"what's for dinner.\" The seconds-reply next to the Tuesday-reply... 60-second test in our bio."
IG_CAPS = ["the five-year plan","next to \"what's","for dinner\" 📋","the loud one","and the","quiet one 🤍","want to know yours?","60-second test","in our bio 🔗","and see if they","know yours 💌"]
IG_RESULT = "Physical Touch"
TT_LINE = "We're two little pups trying to find a thousand people who love like this... If this made you think of someone... follow us. We'll keep making them for you."
