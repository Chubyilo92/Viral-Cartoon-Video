import sys; sys.path.insert(0, '/home/claude/jj')
from dialogue import D, ENDCARD

# Twist: the repeat-back step reveals they were never fighting about the same thing.
# "You never let me finish" = she keeps finishing his FOOD.
TITLE = "you never let me finish"
MUSIC_N = 2

R1 = "room('#e9c4a8','#c08f6c');"
R2 = "room('#f6dfc0','#cfa679');"

LINES = [
D('boy', "You NEVER let me finish!", R1 + "chip('ROUND 1 🥊',win(u,.1,2.4));" + '''
  SP('girl',u,{x:300,flip:-1,look:[.6,0],brows:'sad',mouth:'flat',eyes:'wide',earLift:-.3});
  SP('boy',u,{x:780,look:[-.6,0],brows:'angry',talk:1,mouth:'open',earLift:.4,tilt:.06,hx:Math.sin(u*40)*3});''', '😤'),
D('girl', "I always let you finish! You talk for hours!", R1 + '''
  SP('girl',u,{x:300,flip:-1,look:[.6,0],brows:'angry',talk:1,mouth:'open',earLift:.4,tilt:-.06,hx:Math.sin(u*40)*3});
  SP('boy',u,{x:780,look:[-.6,0],brows:'angry',mouth:'pout'});''', '🙄'),
D('boy', "That's not what I MEAN!", R1 + '''
  SP('girl',u,{x:330,flip:-1,look:[.6,0],brows:'angry',mouth:'flat'});
  SP('boy',u,{x:760,look:[-.6,0],brows:'angry',talk:1,mouth:'open',earLift:.4,paw:{x:-110,y:-120,k:P(u,.1,.4)}});
  raincloudSmall(540,680,win(u,.2,9));''', '💢'),
D('girl', "Then say what you mean!", R1 + '''
  SP('girl',u,{x:330,flip:-1,look:[.6,0],brows:'angry',talk:1,mouth:'open',earLift:.4,paw:{x:110,y:-120,k:P(u,.1,.4)}});
  SP('boy',u,{x:760,look:[-.6,0],brows:'angry',mouth:'flat'});
  chip('who is right? 👇',win(u,.3,9));raincloudSmall(540,680,1);raincloudSmall(400,620,win(u,.4,9));'''),
D('boy', "Okay. CoupleIn. Resolve. You say it back.", R2 + "chip('ROUND 2',win(u,.1,2.4));" + '''
  const r=pop(u,.5,.5);
  SP('girl',u,{x:250,s:1.1,flip:-1,look:[.5,-.2],brows:'sad',mouth:'flat'});
  SP('boy',u,{x:510,s:1.1,look:[.5,-.2],talk:1,mouth:'flat',brows:'sad',paw:{x:90,y:-150,k:P(u,.2,.6)}});
  phoneMock(830,1020-r*40,1.4*r+.01,-.04,()=>{appUI('Resolve');
    ctx.fillStyle=INK;ctx.font='bold 15px Poppins';ctx.textAlign='center';ctx.fillText('One speaks.',0,-190);ctx.fillText('One repeats',0,-170);ctx.fillText('what they heard.',0,-150);
    pill(-118,'🗣️  his turn',true,'#5aa0d8');pill(-80,'👂  her turn',false);});'''),
D('boy', "Every night, you never let me finish...", R2 + "chip('🗣️ HE SPEAKS',win(u,.1,9));" + '''
  SP('girl',u,{x:330,flip:-1,look:[.5,.1],eyes:'open',mouth:'flat'});
  SP('boy',u,{x:760,look:[-.5,.1],brows:'sad',talk:1,mouth:'flat',earLift:-.2});'''),
D('boy', "...my DINNER.", R2 + '''
  const k=pop(u,.1,.4);
  bowl(560,G+70,0);
  SP('girl',u,{x:330,flip:-1,look:[.5,.3],eyes:'wide',mouth:'chomp',earLift:.3,blush:.3});
  ctx.save();ctx.translate(330,G-188);ctx.rotate(-.1);ctx.scale(k,k);tube([[-50,0],[50,0]],22,'#fbeed8');for(const sx of[-1,1])for(const sy of[-1,1])ell(sx*54,sy*12,15,14,'#fbeed8');ctx.restore();if(u>.4){ctx.save();ctx.globalAlpha=win(u,.4,9);bubbleText(330,760,'*chomp*',1,.9);ctx.restore();}
  SP('boy',u,{x:780,look:[-.5,.3],brows:'sad',talk:1,mouth:'open',hx:Math.sin(u*30)*2});''', '🍖'),
D('girl', "What I heard is... I've been eating your dinner.", R2 + "chip('👂 SHE REPEATS',win(u,.1,9));" + '''
  bowl(560,G+70,0);
  SP('girl',u,{x:330,flip:-1,look:[.4,.3],eyes:'open',brows:'sad',talk:1,mouth:'flat',blush:.7,earLift:-.3});
  SP('boy',u,{x:780,look:[-.5,0],eyes:'open',mouth:'flat'});'''),
D('boy', "Every. Single. Night.", R2 + '''
  bowl(560,G+70,0);
  SP('girl',u,{x:330,flip:-1,look:[.4,.3],eyes:'closed2',brows:'sad',mouth:'pout',blush:.8});
  SP('boy',u,{x:780,look:[-.5,0],eyes:'squint',talk:1,mouth:'flat',tilt:.1});''', '😐'),
D('girl', "...It just tastes better from yours.", R2 + '''
  const hug=P(u,1.2,2.1);
  bowl(560,G+70,0);
  SP('girl',u,{x:lerp(330,420,hug),flip:-1,look:[.4,.1],eyes:'happy',talk:1,mouth:'smile',blush:.8,paw:{x:70,y:-190,k:hug}});
  SP('boy',u,{x:lerp(780,650,hug),look:[-.4,.1],eyes:'happy',mouth:'smile',blush:.5,wag:.6});
  if(u>1.8)floatHearts(530,800,1.8,u,5,150);''', '🥺'),
]

END = D('girl', "Half your fights aren't about what you think. Find out with CoupleIn. Link in bio!",
        ENDCARD('say it back. fix it.', 'bowl(400,G+70,0);'), '🔗')
