import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
import jjlib as J
from _kit import S, HUG, SHARE
TITLE = "love languages"
BODY_LINES = [
"Not everyone says I love you... the same way.",
"Some say it with words. Text me when you're home.",
"Some say it with time. The phone goes away when you talk.",
"Some say it with gifts. The snack they bought because it reminded them of you.",
"Some say it with touch. A hand on your back in a crowded room.",
"Some say it with help. Your car's already warm.",
"If you only listen for the words... you'll miss half the ways you're being loved. Because love isn't always loud... sometimes it's already making your tea.",
]
SCENES = [
S(["not everyone","says \"i love you\"","the same way 🤍"], '''  room('#f1d5b0','#caa070');
  pup({kind:'girl',x:340,y:G+10,s:1.4,flip:-1,look:[.6,0],eyes:'happy',mouth:'smile',blush:.4,tilt:-.06});
  pup({kind:'boy',x:740,y:G+10,s:1.4,look:[-.6,0],eyes:'open',mouth:'smile',tilt:.12});
  ctx.save();ctx.globalAlpha=win(u,.6,5);bubbleText(330,640,"i love you 🥰",1,.9);ctx.restore();
  if(u>1.6){ctx.save();ctx.globalAlpha=win(u,1.6,5);ctx.font='bold 60px Poppins';ctx.textAlign='center';ctx.fillStyle=INK;ctx.fillText('❓',760,700);ctx.restore();}'''),
S(["some say it","with words 💬","\"text me when","you're home\""], '''  room('#f6d7c6','#d6a286');
  pup({kind:'girl',x:420,y:G+10,s:1.35,flip:-1,look:[.4,.3],eyes:'happy',mouth:'smile',blush:.4});
  const p=pop(u,.5,.6);phoneMock(760,1000-p*40,.6*p,-.06,()=>{ctx.fillStyle='#eef0f5';ctx.fillRect(-70,-290,140,280);ctx.fillStyle='#ec7489';ctx.beginPath();ctx.roundRect(-58,-230,116,52,14);ctx.fill();ctx.font='bold 17px Poppins';ctx.fillStyle='#fff';ctx.textAlign='center';ctx.fillText('text me when',0,-208);ctx.fillText("you're home 🏡",0,-186);});
  if(u>2)floatHearts(700,760,2,u,4,120);'''),
S(["some say it","with time ⏳","the phone goes","away when","you talk 📵"], '''  room('#f1d5b0','#caa070');
  const put=P(u,1.6,2.6);
  phoneMock(870-put*40,880-put*140,.42*(1-put*.25),.1-put*.25,()=>{ctx.fillStyle='#dfe4ee';ctx.fillRect(-70,-290,140,280);ctx.fillStyle='#b7c0d4';for(let i=0;i<6;i++)ctx.fillRect(-60,-260+i*38,120,8);});
  pup({kind:'boy',x:560,y:G+10,s:1.3,look:[lerp(.7,-.6,put),lerp(-.2,.2,put)],tilt:lerp(0,-.1,put),eyes:'open',mouth:u>3?'smile':'w'});
  pup({kind:'girl',x:300,y:G+10,s:1.3,flip:-1,look:[.6,-.1],mouth:u>3.2?'smile':'flat',tilt:u>3.2?.1:0,blush:.35*P(u,3.2,4.2),eyes:u>3.2?'happy':'open'});
  if(u>3.2)floatHearts(430,800,3.2,u,3,100);'''),
S(["some say it","with gifts 🎁","the snack they bought","because it reminded","them of you 🍪"], '''  room('#f3cfa8','#d09d72');
  pup({kind:'girl',x:700,y:G+10,s:1.3,flip:-1,look:[-.5,.2],eyes:u>2?'happy':'wide',mouth:'smile',blush:.4*P(u,2,3),tilt:-.05});
  const g=P(u,.6,2);
  pup({kind:'boy',x:lerp(200,380,g),y:G+10,s:1.3,look:[.6,0],eyes:'happy',mouth:'smile',paw:{x:110,y:-90,k:g},bob:(g>0&&g<1)?-Math.abs(Math.sin(u*8))*10:0});
  ctx.save();ctx.translate(lerp(300,540,g),G-110+Math.sin(u*3)*4);blob(rectPts(-60,-70,120,130,14),'#f6c37a',{lw:5});blob(rectPts(-60,-70,120,34,10),'#ec7489',{lw:5});heart(0,-6,28,'#fff3c4');ctx.restore();
  if(u>2.4)floatHearts(620,780,2.4,u,4,120);'''),
S(["some say it","with touch 🫶","a hand on your back","in a crowded room"], '''  room('#d9b9c9','#a98496','rgba(255,255,255,.1)');
  for(let i=0;i<5;i++){pup({kind:i%2?'boy':'girl',x:100+i*220,y:G-60,s:.62,flip:i%2?-1:1,look:[0,0],mouth:'w'});}
  ctx.fillStyle='rgba(217,185,201,.55)';ctx.fillRect(0,G-330,W,420);
  const t=P(u,.8,2);
  pup({kind:'girl',x:420,y:G+30,s:1.4,flip:-1,look:[.3,.4],eyes:'open',mouth:'flat',tilt:.03,brows:t>.9?null:'sad'});
  pup({kind:'boy',x:700,y:G+30,s:1.4,look:[-.6,0],eyes:'happy',mouth:'smile',paw:{x:-150,y:-80,k:t},tilt:.05});
  if(u>2)floatHearts(560,800,2,u,4,120);'''),
S(["some say it","with help 🚗","your car's","already warm ♨️"], '''  room('#3d4b6c','#303b57','rgba(255,255,255,.05)');
  ctx.save();ctx.translate(-110,0);
  blob([[120,G-40],[200,G-120],[420,G-160],[560,G-160],[720,G-120],[840,G-40],[840,G+20],[120,G+20]],'#ec7489',{lw:6});
  blob([[240,G-115],[430,G-150],[500,G-150],[500,G-70],[240,G-70]],'#cfe8f5',{lw:5});blob([[520,G-150],[600,G-150],[700,G-115],[700,G-70],[520,G-70]],'#cfe8f5',{lw:5});
  ell(280,G+20,52,52,'#3b2a20');ell(690,G+20,52,52,'#3b2a20');
  for(let i=0;i<4;i++){const k=fract(u*.5+i/4);ctx.save();ctx.globalAlpha=Math.sin(k*Math.PI)*.8;ctx.strokeStyle='#ffd58a';ctx.lineWidth=6;ctx.lineCap='round';ctx.beginPath();ctx.moveTo(340+i*90,G-190);ctx.bezierCurveTo(320+i*90,G-240-k*60,360+i*90,G-260-k*60,340+i*90,G-310-k*60);ctx.stroke();ctx.restore();}
  ctx.restore();
  pup({kind:'boy',x:880,y:G+30,s:1.0,flip:-1,eyes:'happy',mouth:'smile',blush:.3,wag:.4});
  if(u>2)floatHearts(400,G-300,2,u,4,140);'''),
S(["if you only listen","for the words","you'll miss half","the ways","you're loved","love isn't","always loud","sometimes it's already","making your tea ☕"], '''  room('#f3cfa8','#d09d72');
  ell(560,G+40,420,60,'#b98a5e',{lw:5});
  const k=pop(u,.3,.6);mug(540,G-90,1.6*k);
  for(let i=0;i<3;i++){const s=fract(u*.4+i/3);ctx.save();ctx.globalAlpha=Math.sin(s*Math.PI)*.6;ctx.strokeStyle='#fffaf0';ctx.lineWidth=6;ctx.lineCap='round';ctx.beginPath();ctx.moveTo(510+i*30,G-260);ctx.bezierCurveTo(490+i*30,G-320-s*50,540+i*30,G-350-s*50,510+i*30,G-400-s*50);ctx.stroke();ctx.restore();}
  pup({kind:'boy',x:290,y:G+10,s:1.05,look:[.7,0],eyes:'happy',mouth:'smile',tilt:.05});
  pup({kind:'girl',x:800,y:G+10,s:1.05,flip:-1,look:[-.7,0],eyes:'happy',mouth:'smile',blush:.5,tilt:-.05});
  if(u>3)floatHearts(540,G-420,3,u,6,220);'''),
]
IG_LINE = "Words. Time. Gifts. Touch. Help. Every one of us has a language... Want to know yours? There's a sixty second test in our bio. Take it together... and see if he knows yours."
IG_CAPS = ["words 💬 time ⏳","gifts 🎁 touch 🫶","help 🚗","every one of us","has a language 🤍","want to know yours?","60-second test","in our bio 🔗","take it together","and see if he","knows yours 💌"]
IG_RESULT = "Acts of Service"
TT_LINE = "We're two little pups trying to find a thousand people who love like this... If this made you think of someone... follow us. We'll keep making them for you."
