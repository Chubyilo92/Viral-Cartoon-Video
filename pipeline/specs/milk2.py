import sys; sys.path.insert(0, '/home/claude/jj')
from dialogue import D, ENDCARD

# Twist: role reversal loop - he becomes the one who remembers, she's now the forgetter.
TITLE = "did you get the milk?"
MUSIC_N = 1

K = "room('#f6dfc0','#cfa679');"
def day(n): return f"chip('DAY {n}',win(u,.1,2.6));"

LINES = [
D('girl', "Babe... did you get the milk?", K + day(1) + '''
  fridge(800,G-2,P(u,.1,.6),false);
  SP('girl',u,{x:560,flip:-1,look:[.5,0],brows:'sad',talk:1,mouth:'flat',tilt:-.05});
  SP('boy',u,{x:260,look:[.5,0],eyes:'open',mouth:'smile'});'''),
D('boy', "The milk! Tomorrow, I promise!", K + '''
  fridge(800,G-2,1,false);
  SP('girl',u,{x:560,flip:-1,look:[-.5,0],mouth:'flat',brows:'sad'});
  SP('boy',u,{x:260,look:[.5,0],eyes:u<1?'wide':'open',brows:'sad',earLift:-.2,talk:1,mouth:'o',paw:{x:70,y:-200,k:P(u,.2,.6)}});''', '😬'),
D('girl', "Day two. Still no milk.", K + day(2) + '''
  cereal(560,G+70,.75,false);
  SP('girl',u,{x:300,flip:-1,look:[0,0],mouth:'flat',eyes:'squint',talk:1});
  SP('boy',u,{x:800,look:[-.4,0],mouth:'flat',eyes:'open',brows:'sad'});''', '🥣'),
D('girl', "That's it. You're going in CoupleIn.", K + '''
  const r=pop(u,.3,.5);
  SP('girl',u,{x:260,flip:-1,look:[.5,-.2],mouth:'smile',brows:'angry',talk:1});
  phoneMock(720,1010-r*40,1.55*r+.01,-.04,()=>{appUI('shared calendar');
    ctx.fillStyle=INK;ctx.font='bold 13px Poppins';ctx.textAlign='center';ctx.fillText('every day',0,-205);
    ctx.save();ctx.strokeStyle='#ff6b9d';ctx.lineWidth=3;ctx.fillStyle='#fff';ctx.beginPath();ctx.roundRect(-58,-185,116,60,12);ctx.fill();ctx.stroke();ctx.restore();
    ctx.font='22px "Noto Color Emoji"';ctx.fillText('🥛',-34,-148);ctx.fillStyle=INK;ctx.font='bold 13px Poppins';ctx.textAlign='left';ctx.fillText('get milk',-16,-158);
    ctx.font='11px Poppins';ctx.fillText('5:02 pm',-16,-140);
    if(u>1.4){ctx.textAlign='center';ctx.fillStyle='#3fae6a';ctx.font='bold 12px Poppins';ctx.fillText('added for him ✓',0,-100);}
  });''', '📲'),
D('boy', "Ooh! Milk! On my way!", '''cityOut(['#f7b58a','#f6d9b8']);chip('DAY 3 · 5:02 PM',win(u,.1,2.6));
  SP('boy',u,{x:330,y:G+10,look:[.5,-.3],eyes:u>.6?'wide':'open',mouth:'o',talk:1,wag:.6,earLift:.3,bob:-Math.abs(Math.sin(u*6))*10});
  bag(150,G+6);
  const r=pop(u,.15,.45);
  phoneMock(740,1010,1.5,-.05,()=>{ctx.fillStyle='#262530';ctx.fillRect(-70,-290,140,280);
    ctx.fillStyle='#fff';ctx.font='bold 26px Poppins';ctx.textAlign='center';ctx.fillText('5:02',0,-220);
    ctx.save();ctx.translate(0,-170+(1-r)*-40);ctx.globalAlpha=r;ctx.fillStyle='rgba(255,255,255,.92)';ctx.beginPath();ctx.roundRect(-60,-26,120,64,12);ctx.fill();
    heart(-44,-10,8,'#ff6b9d');ctx.fillStyle=INK;ctx.font='bold 10px Poppins';ctx.textAlign='left';ctx.fillText('CoupleIn · now',-34,-6);
    ctx.font='bold 12px Poppins';ctx.fillText('🥛 get milk',-50,14);ctx.font='10px Poppins';ctx.fillText('from your girl 💗',-50,30);ctx.restore();});''', '🏃'),
D('boy', "Guess who remembered the milk!", K + '''
  const k=pop(u,.05,.45);
  SP('girl',u,{x:330,flip:-1,look:[.5,0],eyes:u>.8?'wide':'open',mouth:u>.8?'o':'flat'});
  SP('boy',u,{x:lerp(980,700,k),look:[-.4,-.1],eyes:'happy',mouth:'open',talk:1,wag:.8,earLift:.3,blush:.3});
  milk(lerp(1100,880,k),G-60+Math.sin(u*6)*6,.8,.12);
  if(u>.4){sparkle(700,640,46,win(u,.4,3));sparkle(860,740,30,win(u,.6,3));}''', '🥛'),
D('girl', "Okay... I'm actually impressed.", K + '''
  SP('girl',u,{x:330,flip:-1,look:[.5,0],eyes:'happy',mouth:'smile',talk:1,blush:.6,tilt:-.06});
  SP('boy',u,{x:700,look:[-.4,0],eyes:'happy',mouth:'smile',wag:.6,blush:.4});
  milk(880,G-60,.8,.12);
  if(u>.8)floatHearts(520,820,.8,u,4,140);''', '🥹'),
D('boy', "So... I added one for you too.", K + day(4) + '''
  const r=pop(u,.6,.5);
  SP('girl',u,{x:220,s:1.05,flip:-1,look:[.5,-.1],eyes:'open',mouth:'flat'});
  SP('boy',u,{x:480,s:1.05,look:[.5,-.2],eyes:'squint',mouth:'smile',talk:1,tilt:.08,paw:{x:90,y:-150,k:P(u,.3,.7)}});
  phoneMock(830,1020-r*40,1.4*r+.01,-.04,()=>{appUI('shared calendar');
    ctx.save();ctx.strokeStyle='#5aa0d8';ctx.lineWidth=3;ctx.fillStyle='#fff';ctx.beginPath();ctx.roundRect(-58,-190,116,64,12);ctx.fill();ctx.stroke();ctx.restore();
    ctx.font='22px "Noto Color Emoji"';ctx.textAlign='center';ctx.fillText('🥚',-34,-152);ctx.fillStyle=INK;ctx.font='bold 13px Poppins';ctx.textAlign='left';ctx.fillText('get eggs',-16,-162);
    ctx.font='11px Poppins';ctx.fillText('added for her 😏',-16,-143);});''', '😏'),
D('boy', "Babe... did YOU get the eggs?", K + '''
  fridge(840,G-2,P(u,.1,.6),true);
  SP('girl',u,{x:280,flip:-1,look:[.5,0],eyes:u>.9?'wide':'open',mouth:u>.9?'o':'flat',earLift:u>.9?.4:0});
  SP('boy',u,{x:560,look:[-.5,0],eyes:'squint',talk:1,mouth:'smile',tilt:.1});''', '🥚'),
D('girl', "Tomorrow... I promise.", K + '''
  SP('girl',u,{x:300,flip:-1,look:[.5,.2],eyes:'open',brows:'sad',talk:1,mouth:'flat',earLift:-.3,blush:.6});
  SP('boy',u,{x:740,look:[-.5,0],eyes:'happy',mouth:'smile',wag:1});
  chip('🔁 back to DAY 1',win(u,.6,9));''', '😬'),
]

END = D('boy', "So who's the forgetful one in yours? CoupleIn is free, link in bio!",
        ENDCARD('remember it together', 'milk(470,G+30,.5,0);', speaker='boy'), '🔗')
