import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
import jjlib as J
from _kit import S, HUG, SHARE
TITLE = "loving someone from far away"
BODY_LINES = [
"When someone loves you from far away... they'll fall asleep on a video call, just to hear you breathing on the other end.",
"They'll send you a picture of their lunch, their commute, nothing special. It's the only way to share a day you can't share in person.",
"They'll count down the days out loud, even when you didn't ask. The countdown makes the distance feel temporary.",
"They'll get upset over three seconds of video lag. Losing three seconds of you feels bigger when three seconds is all you get.",
"If someone's loved you from miles away... send this to them tonight.",
"But if the calls get shorter and the days stop getting counted... the distance isn't the problem anymore.",
"Because loving someone you can't touch, can't hold, and choosing to stay anyway... that's the real thing.",
]
SCENES = [
S(["when someone","loves you","from far away 🌍","they'll fall asleep","on a video call","just to hear you","breathing on","the other end 🤍"], '''  room('#3d4b6c','#303b57','rgba(255,255,255,.05)');
  phoneMock(540,760,.85,0,()=>{ctx.fillStyle='#1c2233';ctx.fillRect(-70,-290,140,280);ctx.fillStyle='#e8ac6a';ell(0,-160,30,30,'#e8ac6a');});
  pup({kind:'boy',x:540,y:1010,s:.7,look:[0,.4],eyes:'closed',mouth:'flat',breath:1,tilt:.1});
  zzz(650,900,u,win(u,1,7));'''),
S(["they'll send you","a picture of","their lunch 🍝","their commute","nothing special","because nothing special","is the only way","to share a day","you can't share","in person"], '''  room('#e3c9a0','#bf9670');
  phoneMock(700,780,.68,-.05,()=>{ctx.fillStyle='#eef0f5';ctx.fillRect(-70,-290,140,280);ctx.fillStyle='#d9a86a';ctx.beginPath();ell(0,-140,50,40,'#d9a86a');ctx.fill();ctx.font='10px Poppins';ctx.fillStyle=INK;ctx.textAlign='center';ctx.fillText('lunch was mid lol',0,-60);});
  pup({kind:'girl',x:320,y:G+10,s:1.28,flip:-1,look:[.5,-.1],eyes:'happy',mouth:'smile',blush:.3,tilt:-.05});
  if(u>3)floatHearts(500,850,3,u,3,130);'''),
S(["they'll count down","the days","out loud 📅","even when","you didn't ask","not to pressure you","because the countdown","makes the distance","feel temporary"], '''  room('#f6d7c6','#d6a286');
  const k=pop(u,.2,.5);
  ctx.save();ctx.translate(700,560);ctx.scale(k,k);blob(rectPts(-140,-100,280,200,16),'#fffaf0',{lw:5});ctx.fillStyle='#ec7489';ctx.fillRect(-140,-100,280,50);ctx.font='bold 30px Poppins';ctx.fillStyle='#fff';ctx.textAlign='center';ctx.fillText('12 DAYS',0,-65);
  ctx.font='bold 60px Poppins';ctx.fillStyle=INK;ctx.fillText('12',0,50);ctx.restore();
  pup({kind:'boy',x:300,y:G+10,s:1.25,look:[.5,0],eyes:'happy',mouth:'smile',tilt:.05});'''),
S(["they'll get upset","over three seconds","of video lag 📶","not because","they're petty","losing three seconds","of you feels bigger","when three seconds","is all you get"], '''  room('#3d4b6c','#303b57','rgba(255,255,255,.05)');
  phoneMock(540,760,.85,0,()=>{ctx.fillStyle='#1c2233';ctx.fillRect(-70,-290,140,280);const gl=Math.sin(u*10)>0;if(gl){ctx.fillStyle='#3a4258';for(let i=0;i<8;i++)ctx.fillRect(-70+i*18,-290+Math.random()*280,14,8);}});
  if(u>1.2&&u<5){ctx.save();ctx.globalAlpha=win(u,1.2,5);ctx.font='22px Poppins';ctx.textAlign='center';ctx.fillStyle='#fff8e8';ctx.fillText('no no no come back 😩',540,1000);ctx.restore();}'''),
S(["if someone's","loved you","from miles away 🤍","send this","to them","tonight 💌"], SHARE),
S(["but if the calls","get shorter 📉","and the days","stop getting","counted","the distance","isn't the problem","anymore"], '''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  phoneMock(540,760,.7,0,()=>{ctx.fillStyle='#1c2233';ctx.fillRect(-70,-290,140,280);ctx.font='12px Poppins';ctx.fillStyle='#8a94a8';ctx.textAlign='center';ctx.fillText('missed call',0,-140);});
  pup({kind:'girl',x:320,y:G+10,s:1.3,flip:-1,look:[.5,.4],brows:'sad',mouth:'flat',hy:4});
  if(u>1.6)raincloudSmall(320,720,win(u,1.6,8));'''),
S(["because loving","someone you","can't touch,","can't hold 🤍","and choosing","to stay anyway","that's the","real thing"], HUG),
]
IG_LINE = "The video call they fell asleep on. The boring photos. Counting down the days... want to know how they love? Sixty second test in our bio... see if they know yours."
IG_CAPS = ["falling asleep","on the call 🤍","the boring photos","counting down","the days 📅","want to know yours?","60-second test","in our bio 🔗","take it together","and see if they","know yours 💌"]
IG_RESULT = "Quality Time"
TT_LINE = "We're two little pups trying to find a thousand people who love like this... If this made you think of someone... follow us. We'll keep making them for you."
