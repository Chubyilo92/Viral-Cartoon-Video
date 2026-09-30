import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
import jjlib as J
from _kit import S, HUG, SHARE
TITLE = "the first year you live together"
BODY_LINES = [
"The first year you live together... you'll find out he leaves cabinet doors open, every single time. That's just the real him, uncurated.",
"You'll fight about towels, dishes, whose turn it was. It's because you finally have enough of a life together to fight over.",
"She'll fall asleep with the TV on, and you'll learn to love the noise. Because it means she's home.",
"You'll learn what he sounds like sick, what she's like before coffee, all the parts no one else gets to see. That's the real thing starting.",
"If you're in the messy, real, unfiltered first year with someone... send this to them.",
"But if a year in, you still feel like guests in each other's space... that's worth a real conversation.",
"Because the first year isn't about staying in love the way you started. It's loving the real, unpolished version even more.",
]
SCENES = [
S(["the first year","you live together 🏠","you'll find out","he leaves","cabinet doors","open 🚪","every single time","that's not annoying","that's just the","real him, uncurated"], '''  room('#e3c9a0','#bf9670');
  blob(rectPts(600,430,320,300,10),'#a9774f');
  const op=P(u,.4,1.4);
  ctx.save();ctx.translate(600,430);ctx.rotate(-op*1.1);blob(rectPts(0,0,160,300,8),'#c9915a',{lw:4});ctx.restore();
  pup({kind:'boy',x:340,y:G+10,s:1.3,look:[.5,.1],eyes:'open',mouth:'flat',earLift:-.1});
  pup({kind:'girl',x:780,y:G+10,s:1.2,flip:-1,look:[-.6,.2],mouth:'flat',brows:'sad',hy:2});'''),
S(["you'll fight","about towels","dishes 🧺","whose turn","it was","not because","you're falling apart","because you finally","have enough of","a life together","to fight over"], '''  room('#f6d7c6','#d6a286');
  dishPile(760,G-10,.7);
  ctx.save();ctx.translate(300,650);blob(rectPts(-60,-20,120,40,10),'#dce8ee',{lw:3.5});ctx.restore();
  pup({kind:'girl',x:340,y:G+10,s:1.3,look:[.4,0],mouth:'pout',brows:'sad',blush:.2,tilt:-.05});
  pup({kind:'boy',x:680,y:G+10,s:1.28,flip:-1,look:[-.4,0],mouth:'pout',brows:'sad',tilt:.05});
  if(u>1&&u<4.4){ctx.save();ctx.globalAlpha=win(u,1,4.4);bubbleText(340,800,"it was your turn! 😤",1,.85);ctx.restore();}'''),
S(["she'll fall asleep","with the TV on 📺","and you'll learn","to love","the noise","not because you","don't mind it","because it means","she's home 🤍"], '''  room('#f1d5b0','#caa070');
  ctx.save();ctx.translate(760,560);blob(rectPts(-90,-60,180,120,10),'#2b2830',{lw:4});const fl=Math.sin(u*6)>0;ctx.fillStyle=fl?'#8ea7c9':'#c9915a';ctx.fillRect(-80,-50,160,100);ctx.restore();
  pup({kind:'girl',x:420,y:1000,s:.85,look:[0,.4],eyes:'closed',mouth:'flat',breath:1,tilt:.08});
  zzz(510,920,u,win(u,1,8));'''),
S(["you'll learn what","he sounds like","when he's sick 🤒","what she's like","before coffee ☕","all the parts","no one else","gets to see","that's the real","thing starting"], '''  room('#e9ceb8','#c39a76',1180,'rgba(255,255,255,.2)');
  pup({kind:'boy',x:360,y:G+10,s:1.3,look:[.3,.1],eyes:u<3?'closed':'open',mouth:'flat',blush:.3,tilt:-.03});
  pup({kind:'girl',x:700,y:G+10,s:1.3,flip:-1,look:[-.3,.1],eyes:'open',mouth:u>3?'smile':'flat',blush:.3,tilt:.03});
  if(u>4)floatHearts(530,880,4,u,4,150);'''),
S(["if you're in","the messy, real","unfiltered","first year","with someone","send this","to them 💌"], SHARE),
S(["but if a","year in 📆","you still feel","like guests","in each other's","space","that's worth","a real conversation","not just","more time"], '''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  pup({kind:'girl',x:320,y:G+10,s:1.28,flip:-1,look:[.5,.3],brows:'sad',mouth:'flat',hy:4});
  pup({kind:'boy',x:740,y:G+10,s:1.22,look:[-.3,.3],eyes:'open',mouth:'flat',brows:'sad',hy:6});
  if(u>1.4)raincloudSmall(320,720,win(u,1.4,8)*.5);'''),
S(["because the","first year","isn't about staying","in love the way","you started 🤍","it's about loving","the real,","unpolished version","even more"], HUG),
]
IG_LINE = "The open cabinet doors. The towel fights. Falling asleep to the TV together... want to know how you love? Sixty second test in our bio... see if you match."
IG_CAPS = ["the open","cabinet doors 🚪","the towel fights 🧺","falling asleep","to the TV 📺","want to know yours?","60-second test","in our bio 🔗","take it together","and see if","you match 💌"]
IG_RESULT = "Acts of Service"
TT_LINE = "We're two little pups trying to find a thousand people who love like this... If this made you think of someone... follow us. We'll keep making them for you."
