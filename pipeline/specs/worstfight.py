import sys; sys.path.insert(0, '/home/claude/jj')
from dialogue import D, ENDCARD

# Hook: the nastiest line lands at 0.2s. Fight -> storm off -> regret -> "remember why we downloaded CoupleIn?"
# -> Resolve repeat-back -> the real fear underneath -> comic button on the mom line.
TITLE = "we almost broke up over this"
MUSIC_N = 2

RED = "ctx.translate(Math.sin(u*47)*5,Math.cos(u*39)*3);room('#d98f84','#a55f55','rgba(255,255,255,.08)');"
SAD = "room('#56607e','#454e6a','rgba(255,255,255,.05)');"
CALM = "room('#f6dfc0','#cfa679');"
SH = "hx:Math.sin(u*45)*4"

LINES = [
D('girl', "I can't stand you anymore!", RED + '''
  SP('girl',u,{x:320,flip:-1,look:[.6,0],brows:"angry",talk:1,mouth:"open",earLift:.5,tilt:-.08,%s,s:1.4});
  SP('boy',u,{x:790,look:[-.6,0],brows:'angry',mouth:'flat',eyes:'wide',earLift:.2,s:1.3});''' % SH, '😡'),
D('boy', "Good! Because I can't stand your mom!", RED + '''
  SP('girl',u,{x:300,flip:-1,look:[.6,0],brows:'angry',mouth:'o',eyes:'wide',earLift:.5,s:1.3});
  SP('boy',u,{x:790,look:[-.6,0],brows:'angry',talk:1,mouth:'open',earLift:.5,tilt:.08,%s,s:1.4});''' % SH, '🤬'),
D('girl', "Don't you DARE talk about my mom!", RED + '''
  SP('girl',u,{x:320,flip:-1,look:[.6,0],brows:'angry',talk:1,mouth:'open',earLift:.6,%s,paw:{x:120,y:-120,k:P(u,.1,.35)},s:1.4});
  SP('boy',u,{x:790,look:[-.6,0],brows:'angry',mouth:'pout',s:1.3});
  raincloudSmall(540,640,win(u,.3,9));''' % SH, '💢'),
D('boy', "You know what? Maybe we need a break.", RED + '''
  SP('girl',u,{x:300,flip:-1,look:[.6,0],brows:'sad',mouth:'flat',eyes:'wide',earLift:-.2});
  SP('boy',u,{x:790,look:[-.6,.2],brows:'angry',talk:1,mouth:'flat',tilt:.06});
  raincloudSmall(540,640,1);raincloudSmall(400,580,win(u,.3,9));''', '💔'),
D('girl', "Fine. You were never good enough for me anyway.", RED + '''
  SP('girl',u,{x:300,flip:-1,look:[.6,-.2],brows:'angry',talk:1,mouth:'flat',eyes:'squint',tilt:-.12});
  SP('boy',u,{x:790,look:[-.6,0],brows:'sad',mouth:'o',eyes:'wide',earLift:-.5,squash:lerp(1,.94,P(u,1.6,2.2))});
  raincloudSmall(540,640,1);raincloudSmall(400,580,1);raincloudSmall(700,600,win(u,.5,9));'''),
D('boy', "Then I'm done.", RED + '''
  SP('girl',u,{x:300,flip:-1,look:[.6,0],brows:'sad',mouth:'flat',eyes:'wide'});
  SP('boy',u,{x:lerp(790,1080,P(u,.9,1.8)),flip:-1,look:[.5,.3],brows:'sad',talk:1,mouth:'flat',earLift:-.5});
  raincloudSmall(540,640,1);raincloudSmall(400,580,1);raincloudSmall(700,600,1);''', '🚪'),
D('girl', "...Why did I say that?", SAD + "chip('1 HOUR LATER',win(u,.1,2.6));" + '''
  SP('girl',u,{x:420,look:[.1,.5],brows:'sad',talk:1,mouth:'pout',eyes:'closed2',earLift:-.6,hy:10,blush:.3});
  raincloudSmall(420,640,1);''', '🥺'),
D('boy', "Babe... remember why we downloaded CoupleIn?", SAD + '''
  const k=P(u,.0,1.0);
  SP('girl',u,{x:330,flip:-1,look:[.6,0],brows:'sad',mouth:'pout',eyes:u>.6?'wide':'closed2',earLift:-.4});
  SP('boy',u,{x:lerp(1100,760,k),look:[-.5,.1],brows:'sad',talk:1,mouth:'flat',earLift:-.3});''', '📱'),
D('girl', "...For moments exactly like this.", SAD + '''
  SP('girl',u,{x:330,flip:-1,look:[.6,0],brows:'sad',talk:1,mouth:'flat',earLift:-.2,blush:.4});
  SP('boy',u,{x:760,look:[-.5,.1],brows:'sad',mouth:'smile',earLift:-.1});''', '🤍'),
D('boy', "Okay. Let's start again. You first.", CALM + "chip('ROUND 2 · Resolve',win(u,.1,2.6));" + '''
  const r=pop(u,.4,.5);
  SP('girl',u,{x:250,s:1.1,flip:-1,look:[.5,-.2],brows:'sad',mouth:'flat'});
  SP('boy',u,{x:510,s:1.1,look:[.5,-.2],talk:1,mouth:'smile',paw:{x:90,y:-150,k:P(u,.2,.6)}});
  phoneMock(830,1020-r*40,1.4*r+.01,-.04,()=>{appUI('Resolve');
    ctx.fillStyle=INK;ctx.font='bold 15px Poppins';ctx.textAlign='center';ctx.fillText('One speaks.',0,-190);ctx.fillText('One repeats',0,-170);ctx.fillText('what they heard.',0,-150);
    pill(-118,'🗣️  her turn',true);pill(-80,'👂  his turn',false);});'''),
D('girl', "When you said break... I got scared you meant it.", CALM + "chip('🗣️ SHE SPEAKS',win(u,.1,9));" + '''
  SP('girl',u,{x:330,flip:-1,look:[.5,.2],brows:'sad',talk:1,mouth:'flat',earLift:-.3,blush:.3});
  SP('boy',u,{x:760,look:[-.5,.1],eyes:'open',mouth:'flat'});''', '🥺'),
D('boy', "What I heard is... you're scared I'll really leave.", CALM + "chip('👂 HE REPEATS IT BACK',win(u,.1,9));" + '''
  SP('girl',u,{x:330,flip:-1,look:[.5,.1],eyes:u>2?'wide':'open',brows:'sad',mouth:'flat'});
  SP('boy',u,{x:760,look:[-.5,.1],brows:'sad',talk:1,mouth:'flat'});'''),
D('boy', "I'm not going anywhere.", CALM + '''
  const hug=P(u,.3,1.1);
  SP('girl',u,{x:lerp(330,420,hug),flip:-1,look:[.4,.1],eyes:'happy',mouth:'smile',blush:.7,paw:{x:70,y:-190,k:hug}});
  SP('boy',u,{x:lerp(760,650,hug),look:[-.4,.1],eyes:'happy',talk:1,mouth:'smile',blush:.5,wag:.6});
  if(u>.9)floatHearts(530,800,.9,u,6,160);''', '🤍'),
D('boy', "And... I'm sorry about your mom.", CALM + '''
  SP('girl',u,{x:420,flip:-1,look:[.4,.1],eyes:'happy',mouth:'smile',blush:.6});
  SP('boy',u,{x:650,look:[-.4,.1],eyes:'open',talk:1,mouth:'flat',blush:.4,earLift:-.2});'''),
D('girl', "...Okay, she does talk a lot.", CALM + '''
  SP('girl',u,{x:420,flip:-1,look:[.4,.1],eyes:'squint',talk:1,mouth:'smile',blush:.6,tilt:-.08});
  SP('boy',u,{x:650,look:[-.4,.1],eyes:'happy',mouth:'open',wag:1,bob:-Math.abs(Math.sin(u*8))*10});''', '😂'),
]

END = D('girl', "Every couple says things they don't mean. CoupleIn helps you say what you do. Link in bio!",
        ENDCARD('say what you mean', ''), '🔗')
