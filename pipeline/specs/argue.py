import sys; sys.path.insert(0, '/home/claude/jj')
from dialogue import D, ENDCARD

TITLE = "same fight, round two"
MUSIC_N = 2

R1 = "room('#e9c4a8','#c08f6c');"      # round 1: warm, tense
R2 = "room('#f6dfc0','#cfa679');"      # round 2: calmer kitchen
def rnd(t): return f"chip({t!r},win(u,.1,2.4));"
def shake(u): return f"Math.sin({u}*40)*4"

LINES = [
D('girl', "You never listen to me!", R1 + rnd('ROUND 1 🥊') + '''
  SP('girl',u,{x:300,flip:-1,look:[.6,0],brows:'angry',mouth:'open',talk:1,earLift:.4,tilt:-.06,hx:Math.sin(u*40)*3});
  SP('boy',u,{x:780,look:[-.5,0],brows:'sad',mouth:'flat',eyes:'wide',earLift:-.3});
  if(u>.3)sparkle(320,700,30,win(u,.3,1.5),'#ffb3a7');''', '😤'),
D('boy', "I do listen! You just never let me finish!", R1 + '''
  SP('girl',u,{x:300,flip:-1,look:[.6,0],brows:'angry',mouth:'pout',earLift:.2});
  SP('boy',u,{x:780,look:[-.6,0],brows:'angry',talk:1,mouth:'open',earLift:.4,tilt:.06,hx:Math.sin(u*40)*3});''', '😠'),
D('girl', "See? You're doing it again!", R1 + '''
  SP('girl',u,{x:330,flip:-1,look:[.6,0],brows:'angry',talk:1,mouth:'open',earLift:.4,paw:{x:110,y:-120,k:P(u,.1,.4)}});
  SP('boy',u,{x:760,look:[-.6,0],brows:'angry',mouth:'flat'});
  raincloudSmall(540,560,win(u,.3,9));'''),
D('boy', "No, YOU'RE doing it again!", R1 + '''
  SP('girl',u,{x:330,flip:-1,look:[.6,0],brows:'angry',mouth:'flat',earLift:.2});
  SP('boy',u,{x:760,look:[-.6,0],brows:'angry',talk:1,mouth:'open',earLift:.4,paw:{x:-110,y:-120,k:P(u,.1,.4)}});
  chip('who started it? 👇',win(u,.3,9));raincloudSmall(540,680,1);if(u>.6)raincloudSmall(400,620,win(u,.6,9));''', '💢'),
D('girl', "Are we having the same fight again?", R2 + rnd('ROUND 2 · next day') + '''
  SP('girl',u,{x:300,flip:-1,look:[.4,.3],brows:'sad',talk:1,mouth:'flat',earLift:-.3});
  SP('boy',u,{x:780,look:[-.4,.3],brows:'sad',mouth:'flat',earLift:-.3});''', '😔'),
D('boy', "Yeah. Let's try it the CoupleIn way.", R2 + '''
  const r=pop(u,.5,.5);
  SP('girl',u,{x:250,s:1.1,flip:-1,look:[.5,-.2],brows:'sad',mouth:'flat'});
  SP('boy',u,{x:510,s:1.1,look:[.5,-.2],talk:1,mouth:'smile',paw:{x:90,y:-150,k:P(u,.2,.6)}});
  phoneMock(820,1020-r*40,1.4*r+.01,-.04,()=>{appUI('Resolve');
    ctx.fillStyle=INK;ctx.font='bold 13px Poppins';ctx.textAlign='center';ctx.fillText('Step 2 of 4',0,-205);
    ctx.font='bold 15px Poppins';ctx.fillText('One speaks.',0,-170);ctx.fillText('One repeats',0,-150);ctx.fillText('what they heard.',0,-130);
    pill(-100,'🗣️  her turn',true);pill(-60,'👂  his turn',false);});'''),
D('girl', "When you're on your phone while I talk... I feel like I don't matter.", R2 + '''
  SP('girl',u,{x:330,flip:-1,look:[.5,.2],brows:'sad',talk:1,mouth:'flat',earLift:-.2});
  SP('boy',u,{x:760,look:[-.5,.1],eyes:'open',mouth:'flat',earLift:.1});
  chip('🗣️ SHE SPEAKS',win(u,.1,9));''', '🥺'),
D('boy', "What I heard is... when I'm on my phone, you feel like you don't matter.", R2 + '''
  SP('girl',u,{x:330,flip:-1,look:[.5,.1],eyes:u>2.5?'wide':'open',brows:'sad',mouth:'flat'});
  SP('boy',u,{x:760,look:[-.5,.1],brows:'sad',talk:1,mouth:'flat',earLift:-.1});
  chip('👂 HE REPEATS IT BACK',win(u,.1,9));''', '👂'),
D('girl', "Yeah. That's exactly it.", R2 + '''
  SP('girl',u,{x:330,flip:-1,look:[.5,.1],eyes:'happy',blush:.5,talk:1,mouth:'smile',tilt:-.08});
  SP('boy',u,{x:760,look:[-.5,.1],eyes:'open',mouth:'smile',blush:.2});
  sparkle(540,640,50*pop(u,.4,.4),win(u,.4,9));''', '🥹'),
D('boy', "I'm sorry, love. Phone down. I'm all yours.", R2 + '''
  const hug=P(u,1.2,2.2);
  phoneMock(lerp(860,560,P(u,.1,.8)),lerp(1000,G+40,P(u,.1,.8)),.55,lerp(.2,1.57,P(u,.1,.8)),()=>{ctx.fillStyle='#262530';ctx.fillRect(-70,-290,140,280);});
  SP('girl',u,{x:lerp(330,420,hug),flip:-1,look:[.4,.1],eyes:'happy',mouth:'smile',blush:.6,paw:{x:70,y:-190,k:hug}});
  SP('boy',u,{x:lerp(760,650,hug),look:[-.4,.1],eyes:'happy',talk:1,blush:.5,wag:.5});
  if(u>2)floatHearts(530,800,2,u,5,150);''', '🤍'),
]

END = D('boy', "Round one, we yelled. Round two, we listened. Send this to your round one partner. CoupleIn is free, link in bio!",
        ENDCARD('fights → hugs 🤍', speaker='boy'), '🔗')
