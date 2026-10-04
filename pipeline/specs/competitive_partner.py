import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
import jjlib as J
from _kit import S, HUG, SHARE
TITLE = "when a competitive partner"
BODY_LINES = [
"When a competitive partner loves you... they'll race you to the car, to the remote — and still let you win the one that matters.",
"They'll turn grocery runs into a contest for the better deal... that's how they make errands fun.",
"They'll argue the smallest fact to the death, then bring you a blanket mid-argument — right and caring were never opposite teams.",
"They'll keep score at games they invented an hour ago, but you'll never lose the one that counts.",
"If someone's turned your relationship into a running tally of silly wins... send them this.",
"But if winning starts mattering more than how you feel... that's not playful anymore.",
"Because a competitive partner who still picks you first, every time it counts... loves you as hard as they play.",
]
SCENES = [
S(["when a competitive","partner loves you 🏁","they'll race you","to the car","to the remote","and still let you","win the one","that matters"], '''  room('#f1d5b0','#caa070');
  const k=pop(u,.1,.4);
  pup({kind:'girl',x:lerp(760,620,P(u,.2,1.4)),y:G+10,s:1.28,flip:-1,look:[-.4,0],eyes:'happy',mouth:'open',tilt:-.1,blush:.3,wag:.5});
  pup({kind:'boy',x:lerp(300,420,P(u,.2,1.4)),y:G+10,s:1.3,look:[.4,0],eyes:'wide',mouth:'open',tilt:.08,earLift:.15});
  if(u>1.6)floatHearts(540,850,1.6,u,3,150);'''),
S(["they'll turn","grocery runs","into a contest 🛒","for the","better deal","that's how they","make errands fun"], '''  room('#e3c9a0','#bf9670');
  ctx.save();ctx.translate(560,600);const k2=pop(u,.2,.5);ctx.scale(k2,k2);blob(rectPts(-60,-70,120,140,14),'#fffaf0',{lw:5});ctx.strokeStyle='#8a6a4a';ctx.lineWidth=4;ctx.beginPath();ctx.moveTo(-40,-30);ctx.lineTo(40,-30);ctx.stroke();ctx.font='34px Poppins';ctx.textAlign='center';ctx.fillText('🥕',0,20);ctx.restore();
  pup({kind:'girl',x:300,y:G+10,s:1.26,flip:-1,look:[.5,0],eyes:'happy',mouth:'smile',blush:.3,tilt:-.05});
  pup({kind:'boy',x:820,y:G+10,s:1.26,look:[-.5,0],eyes:'happy',mouth:'smile',tilt:.05,earLift:.1});'''),
S(["they'll argue","the smallest fact","to the death 😤","then bring you","a blanket","mid-argument 🤍","right and caring","were never","opposite teams"], '''  room('#f6d7c6','#d6a286');
  pup({kind:'girl',x:680,y:G+10,s:1.3,flip:-1,look:[-.3,.1],mouth:u<4?'flat':'smile',brows:u<4?'sad':'',blush:.2,tilt:-.05});
  pup({kind:'boy',x:360,y:G+10,s:1.28,look:[.3,0],mouth:u<4?'flat':'smile',brows:u<4?'sad':'',earLift:u<4?-.05:.1});
  if(u>4){ctx.save();ctx.globalAlpha=win(u,4,9);ctx.font='26px Poppins';ctx.textAlign='center';ctx.fillText('🧣',360,G-190);ctx.restore();}'''),
S(["they'll keep score","at games","they invented","an hour ago 🏆","but you'll never","lose the one","that counts"], '''  room('#f1d5b0','#caa070');
  pup({kind:'girl',x:320,y:G+10,s:1.28,flip:-1,look:[.4,0],eyes:'happy',mouth:'smile',blush:.3,tilt:-.05,wag:.3});
  pup({kind:'boy',x:740,y:G+10,s:1.28,look:[-.4,0],eyes:'happy',mouth:'open',tilt:.06,earLift:.1});
  if(u>1.5){ctx.save();ctx.globalAlpha=win(u,1.5,7);ctx.font='bold 22px Poppins';ctx.textAlign='center';ctx.fillStyle=INK;ctx.fillText('you: 1   them: 0',540,G-220);ctx.restore();}'''),
S(["if someone's turned","your relationship","into a running","tally of silly wins 🤍","send them this 💌"], SHARE),
S(["but if winning","starts mattering more 🌧️","than how","you feel","that's not","playful anymore"], '''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  pup({kind:'girl',x:640,y:G+10,s:1.3,flip:-1,look:[.1,.3],brows:'sad',mouth:'flat',hy:4});
  if(u>1)raincloudSmall(640,720,win(u,1,7));'''),
S(["because a","competitive partner","who still picks","you first 🤍","every time","it counts","loves you as","hard as they play"], HUG),
]
IG_LINE = "The car race. The grocery deals. The games they made up an hour ago... want to know how they love? 60-second test in our bio."
IG_CAPS = ["the car race 🏁","the grocery deals 🛒","the made-up games","and the win","that always goes","to you 🤍","want to know yours?","60-second test","in our bio 🔗","take it together","and see if they","know yours 💌"]
IG_RESULT = "Quality Time"
TT_LINE = "We're two little pups trying to find a thousand people who love like this... If this made you think of someone... follow us. We'll keep making them for you."
