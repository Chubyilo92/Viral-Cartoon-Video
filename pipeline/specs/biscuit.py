import sys; sys.path.insert(0, '/home/claude/jj')
from dialogue import D, ENDCARD

# Nasty fight -> walk-out -> "remember why we got the app? if it doesn't help, we break up" (live stakes)
# -> Resolve fails once -> real cause revealed (the last biscuit) -> promise + spare packet.
# Open loop from 0.2s: "it started over something stupid".
TITLE = "we almost broke up over this"
MUSIC_N = 2

PRELUDE = r'''
function appUI(head){const g=ctx.createLinearGradient(0,-290,0,-10);g.addColorStop(0,'#fff5f8');g.addColorStop(1,'#ffe3ec');ctx.fillStyle=g;ctx.fillRect(-70,-290,140,280);
  heart(0,-256,12,'#ff6b9d');if(head){ctx.font='bold 13px Poppins';ctx.fillStyle='#ff6b9d';ctx.textAlign='center';ctx.textBaseline='alphabetic';ctx.fillText(head,0,-228);}}
function corner(txt,a){if(a<=0)return;ctx.save();ctx.setTransform(1,0,0,1,0,0);ctx.globalAlpha=clamp(a);ctx.font='bold 46px Poppins, "Noto Color Emoji"';const w=ctx.measureText(txt).width+56;
  ctx.translate(540,1690);ctx.fillStyle='rgba(255,250,240,.95)';ctx.strokeStyle='#2c1d13';ctx.lineWidth=5;ctx.beginPath();ctx.roundRect(-w/2,-40,w,80,40);ctx.fill();ctx.stroke();
  ctx.fillStyle='#2c1d13';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText(txt,0,3);ctx.restore();}
function biscuit(x,y,s){ctx.save();ctx.translate(x,y);ctx.scale(s,s);ell(0,0,30,30,'#e0a95c',{lw:4});for(let i=0;i<5;i++){ctx.fillStyle='#b9793a';ctx.beginPath();ctx.arc(Math.cos(i*1.3)*14,Math.sin(i*1.3)*14,3.5,0,7);ctx.fill();}ctx.restore();}
function packet(x,y,s,rot=0){ctx.save();ctx.translate(x,y);ctx.rotate(rot);ctx.scale(s,s);
  blob(rectPts(-110,-60,220,120,26),'#3f7fc7',{lw:6});blob(rectPts(-70,-40,140,80,14),'#fbe9c8',{lw:4});
  biscuit(-30,0,.9);biscuit(26,0,.9);ctx.fillStyle='#fff';ctx.font='bold 18px Poppins';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText('BISCUITS',0,-48);ctx.restore();}
'''

RED = "ctx.translate(Math.sin(u*47)*5,Math.cos(u*39)*3);room('#d98f84','#a55f55','rgba(255,255,255,.08)');"
SAD = "room('#56607e','#454e6a','rgba(255,255,255,.05)');"
CALM = "room('#f6dfc0','#cfa679');"
FLICK = "if(Math.sin(u*14)>.2){ctx.fillStyle='rgba(217,80,70,.35)';ctx.fillRect(-200,-200,W+400,H+400);}"
SH = "hx:Math.sin(u*45)*4"
HOOK = "corner('it started over something stupid 👇',1);"
STAKES = "corner('last try 💔',1);"

LINES = [
D('girl', "I can't stand you anymore!", RED + HOOK + '''
  SP('girl',u,{x:320,flip:-1,look:[.6,0],brows:'angry',talk:1,mouth:'open',earLift:.5,tilt:-.08,%s,s:1.4});
  SP('boy',u,{x:790,look:[-.6,0],brows:'angry',mouth:'flat',eyes:'wide',earLift:.2,s:1.3});''' % SH, '😡'),
D('boy', "Good! Because I can't stand your mom!", RED + HOOK + '''
  SP('girl',u,{x:300,flip:-1,look:[.6,0],brows:'angry',mouth:'o',eyes:'wide',earLift:.5,s:1.3});
  SP('boy',u,{x:790,look:[-.6,0],brows:'angry',talk:1,mouth:'open',earLift:.5,tilt:.08,%s,s:1.4});''' % SH, '🤬'),
D('girl', "Maybe we need a break.", RED + HOOK + '''
  SP('girl',u,{x:300,flip:-1,look:[.6,.1],brows:'angry',talk:1,mouth:'flat',tilt:-.06});
  SP('boy',u,{x:790,look:[-.6,0],brows:'sad',mouth:'o',eyes:'wide',earLift:-.2});
  raincloudSmall(540,640,win(u,.3,9));''', '💔'),
D('boy', "Fine. You were never good enough for me anyway.", RED + HOOK + '''
  SP('girl',u,{x:300,flip:-1,look:[.6,0],brows:'sad',mouth:'o',eyes:'wide',earLift:-.5,squash:lerp(1,.94,P(u,1.8,2.4))});
  SP('boy',u,{x:790,look:[-.6,-.2],brows:'angry',talk:1,mouth:'flat',eyes:'squint',tilt:.12});
  raincloudSmall(540,640,1);raincloudSmall(400,580,win(u,.3,9));'''),
D('girl', "Then get out.", RED + "corner('wait for it 👀',win(u,.5,9));" + '''
  SP('girl',u,{x:300,flip:-1,look:[.6,0],brows:'angry',talk:1,mouth:'flat',%s});
  SP('boy',u,{x:lerp(790,1100,P(u,.7,1.6)),flip:-1,look:[.5,.3],brows:'sad',mouth:'flat',earLift:-.5});
  raincloudSmall(540,640,1);raincloudSmall(400,580,1);raincloudSmall(700,600,1);''' % SH, '🚪'),
D('girl', "...Why did I say that?", SAD + "chip('1 HOUR LATER',win(u,.1,2.6));" + '''
  SP('girl',u,{x:420,look:[.1,.5],brows:'sad',talk:1,mouth:'pout',eyes:'closed2',earLift:-.6,hy:10,blush:.3});
  raincloudSmall(420,640,1);''', '🥺'),
D('boy', "Babe... remember why we got the app?", SAD + '''
  const k=P(u,0,1);
  SP('girl',u,{x:330,flip:-1,look:[.6,0],brows:'sad',mouth:'pout',eyes:u>.6?'wide':'closed2',earLift:-.4});
  SP('boy',u,{x:lerp(1100,760,k),look:[-.5,.1],brows:'sad',talk:1,mouth:'flat',earLift:-.3});''', '📱'),
D('girl', "For moments like this. If it doesn't help... we break up.", SAD + "corner('last try 💔',win(u,2,9));" + '''
  SP('girl',u,{x:330,flip:-1,look:[.6,0],brows:'sad',talk:1,mouth:'flat',earLift:-.2});
  SP('boy',u,{x:760,look:[-.5,.1],brows:'sad',mouth:u>2.4?'o':'flat',eyes:u>2.4?'wide':'open',earLift:-.2});'''),
D('boy', "Deal. You talk, I repeat it back.", CALM + STAKES + "chip('ROUND 2',win(u,.1,2.6));" + '''
  const r=pop(u,.3,.5);
  SP('girl',u,{x:250,s:1.1,flip:-1,look:[.5,-.2],brows:'sad',mouth:'flat'});
  SP('boy',u,{x:510,s:1.1,look:[.5,-.2],talk:1,mouth:'flat',paw:{x:90,y:-150,k:P(u,.2,.6)}});
  phoneMock(830,1000-r*40,1.4*r+.01,-.04,()=>{appUI('Resolve');
    ctx.fillStyle=INK;ctx.font='bold 15px Poppins';ctx.textAlign='center';ctx.fillText('One speaks.',0,-190);ctx.fillText('One repeats',0,-170);ctx.fillText('what they heard.',0,-150);
    pill(-118,'🗣️  her turn',true);pill(-80,'👂  his turn',false);});'''),
D('girl', "You ate the last biscuit. And you didn't even ask.", CALM + STAKES + "chip('🗣️ SHE SPEAKS',win(u,.1,9));" + '''
  SP('girl',u,{x:330,flip:-1,look:[.5,.2],brows:'sad',talk:1,mouth:'pout',earLift:-.2,blush:.3});
  SP('boy',u,{x:760,look:[-.5,.1],eyes:u>1.3?'wide':'open',mouth:u>1.3?'o':'flat'});
  if(u>1.2){ctx.save();ctx.globalAlpha=win(u,1.2,9);biscuit(540,780,2.2*pop(u,1.2,.4));ctx.font='bold 44px Poppins, "Noto Color Emoji"';ctx.textAlign='center';ctx.fillStyle=INK;ctx.fillText('the something stupid',540,670);ctx.restore();}''', '🍪'),
D('boy', "What I heard is... you hate me.", CALM + STAKES + "chip('👂 HE REPEATS',win(u,.1,9));" + '''
  SP('girl',u,{x:330,flip:-1,look:[.5,.1],eyes:u>1.2?'wide':'open',brows:u>1.4?'angry':'sad',mouth:u>1.4?'o':'flat',earLift:u>1.4?.4:0});
  SP('boy',u,{x:760,look:[-.5,.1],brows:'sad',talk:1,mouth:'flat'});''', '😬'),
D('girl', "That is NOT what I said!", CALM + FLICK + "corner('last try 💔',1);" + '''
  SP('girl',u,{x:330,flip:-1,look:[.6,0],brows:'angry',talk:1,mouth:'open',earLift:.5,%s});
  SP('boy',u,{x:760,look:[-.5,0],eyes:'wide',brows:'sad',mouth:'o',earLift:-.4});''' % SH, '😤'),
D('boy', "Sorry. I took the last one... and you felt forgotten.", CALM + STAKES + "chip('👂 TRY AGAIN',win(u,.1,9));" + '''
  SP('girl',u,{x:330,flip:-1,look:[.5,.1],eyes:'open',brows:'sad',mouth:'flat'});
  SP('boy',u,{x:760,look:[-.5,.1],brows:'sad',talk:1,mouth:'flat',earLift:-.2});''', '🥺'),
D('girl', "...Yeah. That's exactly it.", CALM + "corner('it worked 💗',win(u,.6,9));" + '''
  SP('girl',u,{x:330,flip:-1,look:[.5,.1],eyes:'happy',talk:1,mouth:'smile',blush:.6,tilt:-.08});
  SP('boy',u,{x:760,look:[-.5,.1],eyes:'happy',mouth:'smile',blush:.3,wag:.5});
  sparkle(540,640,50*pop(u,.4,.4),win(u,.4,9));'''),
D('boy', "Next time, I promise not to eat the last biscuit.", CALM + '''
  const k=pop(u,1.6,.5);
  SP('girl',u,{x:330,flip:-1,look:[.5,.1],eyes:u>1.8?'wide':'happy',mouth:u>1.8?'o':'smile',blush:.5,earLift:u>1.8?.4:0});
  SP('boy',u,{x:760,look:[-.5,.1],eyes:'happy',talk:1,mouth:'smile',blush:.4,paw:{x:-110,y:-130,k:P(u,1.4,1.9)}});
  if(u>1.5){packet(545,G-30-k*30,k*1.05+.01,-.1);sparkle(680,780,40,win(u,1.8,9));}''', '🍪'),
D('girl', "...You had a spare packet this whole time?!", CALM + '''
  const hug=P(u,1.4,2.2);
  packet(545,G-60,1.05,-.1);
  SP('girl',u,{x:lerp(330,400,hug),flip:-1,look:[.5,0],eyes:u<1.4?'wide':'happy',talk:1,mouth:u<1.4?'open':'smile',blush:.6,brows:u<1.4?'angry':null});
  SP('boy',u,{x:lerp(760,700,hug),look:[-.5,0],eyes:'squint',mouth:'smile',blush:.6,wag:1,tilt:.1});
  if(u>1.6)floatHearts(540,760,1.6,u,6,170);''', '😂'),
]

END = D('girl', "Every couple fights over something stupid. This is how we fix ours. Link in bio!",
        ENDCARD('fix the small stuff', 'packet(400,G+40,.5,-.1);'), '🔗')
