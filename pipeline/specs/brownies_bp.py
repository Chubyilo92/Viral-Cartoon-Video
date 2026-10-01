import sys; sys.path.insert(0, '/home/claude/jj'); sys.path.insert(0, '/home/claude/jj/specs')
from dialogue import D, ENDCARD
import biscuit as B   # shared blueprint helpers: corner(), unbranded appUI(), RED/SAD/CALM rooms

# VIRAL-BLUEPRINT applied to browny points -> gestures.
# Cause ("something stupid"): she made herself a tea and not him - while he makes hers every morning.
# Fail: his points read ZERO (he never logged anything). Twist: she'd already baked the brownies... to throw at him.
TITLE = "we almost broke up over this"
MUSIC_N = 3
PRELUDE = B.PRELUDE + r'''
function ptsPhone(x,y,s,val,rows,label){phoneMock(x,y,s,-.04,()=>{appUI('browny points');
  ctx.fillStyle=val==0?'#d9503f':INK;ctx.textAlign='center';ctx.font='bold 46px Poppins';ctx.fillText(val,0,-165);
  ctx.fillStyle=INK;ctx.font='12px Poppins';ctx.fillText(label||'his points',0,-142);
  rows.forEach((r,i)=>pill(-120+i*36,r,true,'#3fae6a'));});}
'''
RED, SAD, CALM, FLICK, SH, HOOK, STAKES = B.RED, B.SAD, B.CALM, B.FLICK, B.SH, B.HOOK, B.STAKES

LINES = [
D('girl', "You never do ANYTHING for me!", RED + HOOK + '''
  SP('girl',u,{x:320,flip:-1,look:[.6,0],brows:'angry',talk:1,mouth:'open',earLift:.5,tilt:-.08,%s,s:1.4});
  SP('boy',u,{x:790,look:[-.6,0],brows:'angry',mouth:'flat',eyes:'wide',earLift:.2,s:1.3});''' % SH, '😡'),
D('boy', "Me? You haven't said thank you in a YEAR!", RED + HOOK + '''
  SP('girl',u,{x:300,flip:-1,look:[.6,0],brows:'angry',mouth:'o',eyes:'wide',earLift:.5,s:1.3});
  SP('boy',u,{x:790,look:[-.6,0],brows:'angry',talk:1,mouth:'open',earLift:.5,tilt:.08,%s,s:1.4});''' % SH, '🤬'),
D('girl', "Maybe I should find someone who actually tries.", RED + HOOK + '''
  SP('girl',u,{x:300,flip:-1,look:[.6,-.1],brows:'angry',talk:1,mouth:'flat',eyes:'squint',tilt:-.1});
  SP('boy',u,{x:790,look:[-.6,0],brows:'sad',mouth:'o',eyes:'wide',earLift:-.4});
  raincloudSmall(540,640,win(u,.3,9));''', '💔'),
D('boy', "Go ahead. They'll find out you're impossible too.", RED + HOOK + '''
  SP('girl',u,{x:300,flip:-1,look:[.6,0],brows:'sad',mouth:'o',eyes:'wide',earLift:-.5,squash:lerp(1,.94,P(u,1.8,2.4))});
  SP('boy',u,{x:790,look:[-.6,-.2],brows:'angry',talk:1,mouth:'flat',eyes:'squint',tilt:.12});
  raincloudSmall(540,640,1);raincloudSmall(400,580,win(u,.3,9));'''),
D('girl', "Then I'm done.", RED + "corner('wait for it 👀',win(u,.5,9));" + '''
  SP('girl',u,{x:lerp(300,-60,P(u,.7,1.6)),look:[-.5,.3],brows:'sad',talk:1,mouth:'flat',earLift:-.5});
  SP('boy',u,{x:790,look:[-.6,0],brows:'sad',mouth:'flat',eyes:'wide'});
  raincloudSmall(540,640,1);raincloudSmall(400,580,1);raincloudSmall(700,600,1);''', '🚪'),
D('boy', "...Did I really say that?", SAD + "chip('1 HOUR LATER',win(u,.1,2.6));" + '''
  SP('boy',u,{x:640,look:[-.1,.5],brows:'sad',talk:1,mouth:'pout',eyes:'closed2',earLift:-.6,hy:10});
  mug(840,G,.8);raincloudSmall(640,640,1);''', '🥺'),
D('girl', "Babe... remember why we got the app?", SAD + '''
  const k=P(u,0,1);
  SP('boy',u,{x:760,look:[-.6,0],brows:'sad',mouth:'pout',eyes:u>.6?'wide':'closed2',earLift:-.4});
  SP('girl',u,{x:lerp(-40,330,k),flip:-1,look:[.5,.1],brows:'sad',talk:1,mouth:'flat',earLift:-.3});''', '📱'),
D('boy', "For moments like this. If it doesn't help... we're done.", SAD + "corner('last try 💔',win(u,2,9));" + '''
  SP('girl',u,{x:330,flip:-1,look:[.5,.1],brows:'sad',mouth:u>2.4?'o':'flat',eyes:u>2.4?'wide':'open',earLift:-.2});
  SP('boy',u,{x:760,look:[-.5,0],brows:'sad',talk:1,mouth:'flat',earLift:-.2});'''),
D('girl', "Nice things earn points. Let's see yours.", CALM + STAKES + "chip('ROUND 2',win(u,.1,2.6));" + '''
  const r=pop(u,.4,.5);
  SP('girl',u,{x:250,s:1.1,flip:-1,look:[.5,-.2],talk:1,mouth:'flat',paw:{x:90,y:-150,k:P(u,.2,.6)}});
  SP('boy',u,{x:510,s:1.1,look:[.5,-.2],brows:'sad',mouth:'flat'});
  ptsPhone(830,1000-r*40,1.4*r+.01,'...',[]);'''),
D('girl', "Zero?! You never log anything!", CALM + FLICK + "corner('last try 💔',1);" + '''
  SP('girl',u,{x:250,s:1.1,flip:-1,look:[.5,0],brows:'angry',talk:1,mouth:'open',earLift:.4,%s});
  SP('boy',u,{x:510,s:1.1,look:[.5,-.2],eyes:'wide',brows:'sad',mouth:'o',earLift:-.4});
  ptsPhone(830,960,1.4,0,[]);''' % SH, '😤'),
D('boy', "Fine. Car washed. Bins out. Your tea, every morning.", CALM + STAKES + '''
  const n=Math.round(60*P(u,.5,2.8));
  SP('girl',u,{x:250,s:1.1,flip:-1,look:[.5,-.2],eyes:u>2.6?'wide':'open',mouth:u>2.6?'o':'flat'});
  SP('boy',u,{x:510,s:1.1,look:[.5,-.2],talk:1,mouth:'flat',paw:{x:90,y:-150,k:P(u,.1,.5)}});
  ptsPhone(830,960,1.4,n,['🚗 car  +20','🗑️ bins  +10','☕ her tea x30'].slice(0,Math.min(3,Math.floor(u/0.9))));''', '☕'),
D('girl', "Wait... YOU make my tea? I thought it just appeared.", CALM + STAKES + '''
  SP('girl',u,{x:330,flip:-1,look:[.5,.1],eyes:'wide',talk:1,mouth:'o',earLift:.3,blush:.5});
  SP('boy',u,{x:760,look:[-.5,.1],eyes:'squint',mouth:'flat',tilt:.1});
  mug(540,G,.9);''', '😳'),
D('boy', "And today you made yourself one... and not me.", CALM + STAKES + '''
  SP('girl',u,{x:250,flip:-1,look:[.5,.2],eyes:'open',brows:'sad',mouth:'pout',blush:.6,earLift:-.3});
  SP('boy',u,{x:840,look:[-.5,.1],brows:'sad',talk:1,mouth:'pout'});
  if(u>1.2){ctx.save();ctx.globalAlpha=win(u,1.2,9);mug(540,800,1.3*pop(u,1.2,.4));ctx.font='bold 44px Poppins, "Noto Color Emoji"';ctx.textAlign='center';ctx.fillStyle=INK;ctx.fillText('the something stupid',540,560);ctx.restore();}''', '☕'),
D('boy', "Sixty points... Warm brownies. Baked by you.", CALM + "corner('it worked 💗',win(u,.3,9));" + '''
  const r=pop(u,.1,.5);
  SP('boy',u,{x:300,look:[.5,-.2],eyes:'happy',talk:1,blush:.5,wag:.5,paw:{x:90,y:-160,k:P(u,.1,.5)}});
  phoneMock(740,1030-r*40,1.45*r+.01,-.04,()=>{appUI('spend 60 points on...');
    pill(-200,'💆 back rub',false);pill(-162,'🍳 breakfast in bed',false);pill(-124,'🍫 warm brownies',P(u,.8,1.2)>.5);});''', '🍫'),
D('girl', "...I already made them.", CALM + '''
  const k=pop(u,.6,.5);
  SP('girl',u,{x:330,flip:-1,look:[.5,0],eyes:'squint',talk:1,mouth:'smile',blush:.4,paw:{x:110,y:-120,k:P(u,.4,.8)}});
  SP('boy',u,{x:780,look:[-.5,0],eyes:u>1?'wide':'open',mouth:u>1?'o':'smile',earLift:u>1?.4:0});
  if(u>.6){brownies(545,G+40-k*20,k+.01,1);sparkle(560,880,44,win(u,.8,9));}''', '🍫'),
D('boy', "Before the fight?!", CALM + '''
  brownies(545,G+20,1,1);
  SP('girl',u,{x:330,flip:-1,look:[.5,0],eyes:'happy',mouth:'smile',blush:.4});
  SP('boy',u,{x:780,look:[-.5,.2],eyes:'wide',talk:1,mouth:'open',earLift:.4});''', '😳'),
D('girl', "I was going to throw them at you.", CALM + '''
  const hug=P(u,1.3,2.1);
  brownies(545,G+20,1,1);
  SP('girl',u,{x:lerp(330,400,hug),flip:-1,look:[.5,0],eyes:'squint',talk:1,mouth:'smile',blush:.6,tilt:-.1});
  SP('boy',u,{x:lerp(780,700,hug),look:[-.5,0],eyes:u<1.3?'wide':'happy',mouth:u<1.3?'o':'open',wag:1,bob:u>1.3?-Math.abs(Math.sin(u*8))*10:0});
  if(u>1.5)floatHearts(540,760,1.5,u,6,170);''', '😂'),
]

END = D('girl', "A relationship full of kindness will overcome the small fights. This is how we turn ours into a kindness machine. Link in bio!",
        ENDCARD('your kindness machine', 'brownies(400,G+60,.5,1);'), '🔗')
