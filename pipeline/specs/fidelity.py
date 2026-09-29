import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
import jjlib as J
from _kit import S, HUG, SHARE
TITLE = "a loyal man"
BODY_LINES = [
"A loyal man hands you his phone without thinking. Not because you asked. Because there's nothing to hide.",
"He mentions you in rooms you're not even in.",
"He leaves the party early... not because he has to. Because home is where he wants to be.",
"When someone flirts, he gets awkward... not flattered.",
"If he's loyal like this... send this to the girl who deserves it.",
"But if you always feel like you're competing... for his time... his attention... his phone... you're not being dramatic.",
"Because a loyal man never makes you feel like an option.",
]
SCENES = [
S(["a loyal man","hands you","his phone 📱","without thinking","not because","you asked","because there's","nothing to hide 🤍"], '''  room('#f3cfa8','#d09d72');
  ell(560,G+40,420,70,'#e7b9a0',{lw:5});
  const sl=P(u,1.2,2.8);
  pup({kind:'girl',x:300,y:G+10,s:1.3,flip:-1,look:[.7,0],eyes:'open',mouth:'smile',blush:.3,tilt:-.04});
  pup({kind:'boy',x:760,y:G+10,s:1.3,look:[-.7,0],eyes:'open',mouth:'smile',tilt:.05,paw:{x:-150,y:-60,k:sl}});
  phoneMock(lerp(700,480,sl),lerp(1000,1050,sl),.36,lerp(.1,-.5,sl),()=>{ctx.fillStyle='#dfe4ee';ctx.fillRect(-70,-290,140,280);ctx.fillStyle='#ec7489';ctx.fillRect(-60,-260,120,26);ctx.fillStyle='#b7c0d4';for(let i=0;i<5;i++)ctx.fillRect(-60,-215+i*38,120,8);});
  if(u>3.4)floatHearts(540,860,3.4,u,4,160);'''),
S(["he mentions you","in rooms","you're not","even in 🚪"], '''  room('#d9b9c9','#a98496','rgba(255,255,255,.1)');
  for(let i=0;i<3;i++){ctx.save();ctx.globalAlpha=.9;ell(220+i*260,300,9,60,'#7a5a3a',{stroke:false});ctx.restore();ctx.beginPath();ctx.moveTo(220+i*260,240);ctx.lineTo(220+i*260,300);ctx.stroke();}
  pup({kind:'boy',x:150,y:G+10,s:.9,flip:1,look:[.6,0],mouth:'smile'});
  pup({kind:'boy',x:930,y:G+10,s:.9,flip:-1,look:[-.6,0],mouth:'smile',earLift:.1});
  pup({kind:'boy',x:540,y:G+10,s:1.35,eyes:'happy',mouth:'smile',blush:.3,tilt:.05,bandana:true,wag:.3});
  const k=pop(u,1.0,.5);ctx.save();ctx.globalAlpha=win(u,1,5.4);bubbleText(540,650,"my girl would\\nlove this 🥹".replace('\\\\n',' '),1,.95*k);ctx.restore();
  if(u>2.2)floatHearts(540,760,2.2,u,4,160);'''),
S(["he leaves","the party early 🎉","not because","he has to","because home is","where he","wants to be 🏡"], '''  room('#3d4b6c','#303b57','rgba(255,255,255,.06)');
  blob(rectPts(700,520,300,660,16),'#b98a5e');blob(rectPts(730,560,240,620,10),'#f6d688',{stroke:false});
  const lg=ctx.createRadialGradient(850,860,20,850,860,420);lg.addColorStop(0,'rgba(255,214,120,.5)');lg.addColorStop(1,'rgba(255,214,120,0)');ctx.fillStyle=lg;ctx.fillRect(300,400,800,900);
  pup({kind:'girl',x:880,y:G+10,s:1.0,flip:-1,eyes:'happy',mouth:'smile',blush:.5,wag:.4});
  const wk=P(u,.6,4.6);
  pup({kind:'boy',x:lerp(120,600,wk),y:G+14,s:1.3,bob:(wk>0&&wk<1)?-Math.abs(Math.sin(u*8))*12:0,flip:-1,eyes:'happy',mouth:'smile',wag:.3});
  if(u>4.6)floatHearts(760,780,4.6,u,4,120);'''),
S(["when someone","flirts","he gets awkward","not flattered 😳"], '''  room('#d9b9c9','#a98496','rgba(255,255,255,.1)');
  const wn=P(u,.5,1.3);
  pup({kind:'girl',x:220,y:G+10,s:1.15,flip:-1,look:[.6,0],eyes:'happy',mouth:'smile',blush:.6,tilt:-.08});
  if(u>1){ctx.save();ctx.globalAlpha=win(u,1,4.6);heart(330,720,42,'#ff6b9d');ctx.restore();}
  const sh=P(u,1.6,2.4);
  pup({kind:'boy',x:700,y:G+10,s:1.4,flip:1,look:[-.6,.4],eyes:'wide',mouth:'flat',blush:.7*sh,earLift:-.5*sh,tilt:.12*sh,paw:{x:-40,y:-150,k:sh}});
  if(u>2.4){ctx.save();ctx.globalAlpha=win(u,2.4,7);bubbleText(760,780,"sorry, i'm taken 😳",1,.85);ctx.restore();}'''),
S(["if he's loyal","like this","send this to","the girl who","deserves it 💌"], SHARE),
S(["but if you always","feel like you're","competing","for his time","his attention","his phone","you're not being","dramatic"], '''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  blob(rectPts(160,G-140,760,26,10),'#a58363');
  ell(280,G-150,90,18,'#f0e7d6',{lw:4});ell(280,G-158,50,8,'#d9cdb7',{stroke:false});
  ell(800,G-150,90,18,'#f0e7d6',{lw:4});
  pup({kind:'girl',x:290,y:G+10,s:1.25,flip:-1,look:[.7,.3],brows:'sad',mouth:'flat',earLift:-.3});
  pup({kind:'boy',x:800,y:G+10,s:1.25,look:[.2,.7],eyes:'open',mouth:'flat'});
  phoneMock(560,G-160,.3,.03,()=>{ctx.fillStyle='#dfe4ee';ctx.fillRect(-70,-290,140,280);ctx.fillStyle='#9fb4d8';for(let i=0;i<6;i++)ctx.fillRect(-60,-260+i*38,120,10);});
  if(u>1)raincloudSmall(290,720,win(u,1,9));'''),
S(["because a loyal man","never makes you","feel like","an option 🤍"], HUG),
]
IG_LINE = "The phone. The party. Coming home. Every boy shows love in his own way... Want to know his? There's a sixty second test in our bio. Take it together... and see if he knows yours."
IG_CAPS = ["the phone 📱","the party 🎉","coming home 🏡","every boy shows","love in his own way 🤍","want to know his?","60-second test","in our bio 🔗","take it together","and see if he","knows yours 💌"]
IG_RESULT = "Acts of Service"
TT_LINE = "We're two little pups trying to find a thousand people who love like this... If this made you think of someone... follow us. We'll keep making them for you."
