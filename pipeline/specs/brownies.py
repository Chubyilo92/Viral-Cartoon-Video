import sys; sys.path.insert(0, '/home/claude/jj')
from dialogue import D, ENDCARD

TITLE = "browny points 🍫"
MUSIC_N = 3

K = "room('#f6dfc0','#cfa679');"
P2 = "room('#fbdfe4','#f3b8c6',1180,'rgba(255,255,255,.18)');"

def phone_points(extra=''):
    return '''phoneMock(820,1030-r*40,1.4*r+.01,-.04,()=>{appUI('browny points');
    ctx.fillStyle=INK;ctx.textAlign='center';ctx.font='bold 40px Poppins';ctx.fillText(Math.round(50*P(u,.6,2.2)),0,-170);
    ctx.font='12px Poppins';ctx.fillText('points this week',0,-150);
    pill(-130,'🍽️ dishes  +20',P(u,.6,1)>.5,'#3fae6a');pill(-94,'📅 date night  +20',P(u,1.1,1.5)>.5,'#3fae6a');pill(-58,'💗 mood check  +10',P(u,1.6,2)>.5,'#3fae6a');%s});''' % extra

LINES = [
D('boy', "Babe... can I swap my browny points for actual brownies?", K + '''
  SP('girl',u,{x:300,flip:-1,look:[.5,0],eyes:'open',mouth:'smile'});
  SP('boy',u,{x:760,look:[-.5,-.1],eyes:'open',talk:1,blush:.4,tilt:.08,wag:.5,paw:{x:-60,y:-180,k:P(u,.3,.7)}});
  if(u>1.4){ctx.save();ctx.globalAlpha=win(u,1.4,9);bubbleText(760,700,'🍫 ?',1,1);ctx.restore();}''', '🍫'),
D('girl', "Did you even earn any?", K + '''
  SP('girl',u,{x:300,flip:-1,look:[.5,0],eyes:'squint',brows:'angry',talk:1,mouth:'smile',tilt:-.08});
  SP('boy',u,{x:760,look:[-.5,0],eyes:'wide',mouth:'o',earLift:.2});''', '🤨'),
D('boy', "Dishes. Date night booked. Mood check. Fifty points!", K + '''
  const r=pop(u,.2,.5);
  SP('girl',u,{x:260,s:1.1,flip:-1,look:[.6,-.2],eyes:u>2.6?'wide':'open',mouth:u>2.6?'o':'flat'});
  SP('boy',u,{x:510,s:1.1,look:[.5,-.2],eyes:'happy',talk:1,wag:.7,blush:.3,paw:{x:90,y:-150,k:P(u,.2,.6)}});
  ''' + phone_points("if(u>2.4){ctx.save();ctx.globalAlpha=win(u,2.4,9);ctx.font='bold 13px Poppins';ctx.fillStyle='#3fae6a';ctx.fillText('+50 ✨',0,-22);ctx.restore();}") + '''
  if(u>2.4)sparkle(820,560,40,win(u,2.4,9));''', '😎'),
D('girl', "Okay, okay. I'm impressed. Pick a gesture.", K + '''
  SP('girl',u,{x:300,flip:-1,look:[.5,0],eyes:'happy',talk:1,blush:.4,tilt:-.06});
  SP('boy',u,{x:760,look:[-.5,0],eyes:'happy',mouth:'open',wag:.8,bob:-Math.abs(Math.sin(u*7))*12});''', '😏'),
D('boy', "Warm brownies. Baked by you. Final answer.", P2 + '''
  const r=pop(u,.1,.5);
  SP('boy',u,{x:300,look:[.5,-.2],eyes:'happy',talk:1,blush:.5,wag:.5,paw:{x:90,y:-160,k:P(u,.1,.5)}});
  phoneMock(740,1030-r*40,1.45*r+.01,-.04,()=>{appUI('spend 50 points on...');
    pill(-210,'💆 back rub',false);pill(-172,'🍳 breakfast in bed',false);pill(-134,'🎬 movie pick',false);
    const k=P(u,1,1.4);pill(-96,'🍫 warm brownies',k>.5);
    if(u>1.6){ctx.save();ctx.globalAlpha=win(u,1.6,9);ctx.font='bold 12px Poppins';ctx.fillStyle='#3fae6a';ctx.textAlign='center';ctx.fillText('sent to her 💌',0,-40);ctx.restore();}});''', '🍫'),
D('girl', "One tray of warm brownies... for my favourite point collector.", K + '''chip('1 HOUR LATER',win(u,.1,2.6));
  const k=pop(u,.2,.5);
  SP('girl',u,{x:300,flip:-1,look:[.5,0],eyes:'happy',talk:1,blush:.4,paw:{x:110,y:-120,k:P(u,.1,.5)}});
  SP('boy',u,{x:780,look:[-.5,0],eyes:'wide',mouth:'o',wag:.9,earLift:.3});
  brownies(540,G+50-k*20,k+.01,1);
  if(u>.6)sparkle(540,880,44,win(u,.6,9));''', '🍫'),
D('boy', "Best. Points. Ever. I'm doing the dishes again tomorrow!", K + '''
  SP('girl',u,{x:300,flip:-1,look:[.5,0],eyes:'happy',mouth:'smile',blush:.5});
  SP('boy',u,{x:760,look:[-.4,.1],eyes:'happy',mouth:Math.sin(u*10)>0?'chomp':'smile',talk:u>1.2?1:0,wag:1,blush:.5,squash:1+Math.sin(u*10)*.02});
  brownies(540,G+30,1,1);
  if(u>.8)floatHearts(700,820,.8,u,4,120);''', '😋'),
D('girl', "Works every time.", K + '''
  SP('girl',u,{x:420,s:1.5,flip:-1,look:[0,0],eyes:Math.sin(u*3)>.6?'happy':'open',talk:1,mouth:'smile',blush:.5,tilt:-.1});
  SP('boy',u,{x:830,s:1.0,look:[-.4,.1],eyes:'happy',mouth:'chomp',wag:.8});
  sparkle(560,650,40*pop(u,.5,.4),win(u,.5,9));''', '😉'),
D('girl', "Oh, by the way... I have three hundred points.", K + '''
  SP('girl',u,{x:330,flip:-1,look:[.5,0],eyes:'squint',talk:1,mouth:'smile',tilt:-.1});
  SP('boy',u,{x:760,look:[-.5,0],eyes:u>1.6?'wide':'happy',mouth:u>1.6?'o':'chomp',earLift:u>1.6?.4:0});
  if(u>1.4){ctx.save();ctx.globalAlpha=win(u,1.4,9);bubbleText(330,700,'300 🍫',1,1.1);ctx.restore();}''', '😈'),
D('boy', "Wait. What are you spending them on?", K + '''
  SP('girl',u,{x:330,flip:-1,look:[.5,0],eyes:'happy',mouth:'smile'});
  SP('boy',u,{x:760,look:[-.5,0],eyes:'wide',brows:'sad',talk:1,mouth:'o',earLift:-.3,hx:Math.sin(u*30)*2});''', '😳'),
D('girl', "Laundry. For a month.", K + '''
  SP('girl',u,{x:330,flip:-1,look:[.5,0],eyes:'happy',talk:1,mouth:'smile',blush:.4,tilt:-.08});
  SP('boy',u,{x:760,look:[-.3,.4],eyes:'closed2',brows:'sad',mouth:'flat',earLift:-.5,hy:8,squash:lerp(1,.9,P(u,.6,1.2))});
  raincloudSmall(760,620,win(u,.6,9));''', '🧺'),
]

END = D('girl', "So... who has more points in your relationship? CoupleIn is free, link in bio!",
        ENDCARD('points → love 🍫', 'brownies(400,G+60,.5,1);'), '🔗')
