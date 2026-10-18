import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD, C
TITLE = "the girl who stayed"
BODY_LINES = [
"The girl who stayed when you had nothing... split one meal with you and called it date night.",
"She never asked when you'd make it. She asked if you'd eaten.",
"She believed in you out loud... on the days you couldn't.",
"When the first good thing happened, she cheered like it happened to her.",
"If a girl stayed with you through the broke years... send this to her.",
"But if you finally make it, and forget who was there at the start... you didn't make it at all.",
"Because a girl who stays when you have nothing... deserves everything once you do.",
]
D = [
'''  room('#3d4b6c','#303b57','rgba(255,255,255,.06)');
  const lg=ctx.createRadialGradient(540,900,20,540,900,420);lg.addColorStop(0,'rgba(255,214,120,.45)');lg.addColorStop(1,'rgba(255,214,120,0)');ctx.fillStyle=lg;ctx.fillRect(0,400,W,1000);
  bowl(540,G-10,true);
  pup({kind:'boy',x:330,y:G+10,s:1.25,look:[.5,.4],eyes:'happy',mouth:'smile',blush:.3});
  pup({kind:'girl',x:750,y:G+10,s:1.25,flip:-1,look:[-.5,.4],eyes:'happy',mouth:'smile',blush:.5});
  if(u>1.5)floatHearts(540,820,1.5,u,4,140);''',
'''  room('#e3c9a0','#bf9670');
  blob(rectPts(160,G-170,520,30,10),'#8a6a4c');for(let i=0;i<4;i++)blob(rectPts(200+i*60,G-200-i*6,70,40,4),'#f5f0e4',{lw:3});
  pup({kind:'boy',x:400,y:G+10,s:1.25,look:[-.2,.6],eyes:'closed',mouth:'flat',brows:'sad',tilt:.06});
  pup({kind:'girl',x:820,y:G+10,s:1.25,flip:-1,look:[-.6,0],eyes:'open',mouth:'smile',blush:.4});
  if(u>.8){const k=pop(u,.8,.4);ctx.save();ctx.globalAlpha=win(u,.8,8);bubbleText(690,690,"did you eat today? 🍜",1,.85*k);ctx.restore();}''',
'''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  pup({kind:'boy',x:340,y:G+10,s:1.3,look:[.2,.6],brows:'sad',mouth:'flat',earLift:-.3});
  raincloudSmall(340,700,win(u,0,9)*.7);
  pup({kind:'girl',x:740,y:G+10,s:1.3,flip:-1,look:[-.6,0],eyes:'happy',mouth:'smile',wag:.3});
  if(u>.8){const k=pop(u,.8,.4);ctx.save();ctx.globalAlpha=win(u,.8,8);bubbleText(700,680,"you've got this 💪",1,.85*k);ctx.restore();}''',
'''  room('#f6d7c6','#d6a286');
  const j=P(u,1.0,1.6);
  pup({kind:'boy',x:360,y:G+10,s:1.3,look:[.4,-.1],eyes:'happy',mouth:'smile',blush:.4});
  phoneMock(520,960,.38,-.1,()=>{ctx.fillStyle='#e8f6e8';ctx.fillRect(-70,-290,140,280);ctx.fillStyle='#3a8a4a';ctx.font='bold 18px Poppins';ctx.textAlign='center';ctx.fillText("you're hired! 🎉",0,-160);});
  pup({kind:'girl',x:780,y:G+10,s:1.35,flip:-1,bob:-Math.abs(Math.sin(u*8))*22*j,eyes:'happy',mouth:'smile',blush:.6,wag:.8});
  if(u>1.2){sparkle(780,640,50,win(u,1.2,8));floatHearts(780,760,1.2,u,5,180);}''',
SHARE,
'''  room('#6f6a78','#5a5562','rgba(255,255,255,.05)');
  pup({kind:'boy',x:340,y:G+10,s:1.35,look:[-.5,-.3],eyes:'open',mouth:'smile',tilt:.05});
  shadesProp(340,990,1.0);
  for(let i=0;i<3;i++)sparkle(200+i*140,560+i*30,24,.8,'#ffd75e');
  pup({kind:'girl',x:820,y:G+10,s:1.15,flip:-1,look:[-.6,.3],brows:'sad',mouth:'flat',earLift:-.4});
  if(u>1)raincloudSmall(820,720,win(u,1,9));''',
HUG,
]
SCENES = spec(BODY_LINES, D, [{'date night':'🍜'},{'eaten':'🍜'},{'couldn':'💪'},{'her':'🎉'},{'send this':'💌'},{'at all':'🚩'},{'once you do':'🤍'}])
IG_LINE = "One meal. Did you eat? You've got this. Every girl shows love her own way... Want to know hers? There's a sixty second test in our bio. Take it together."
IG_CAPS = C(IG_LINE, {'one meal':'🍜','hers?':'🤍','bio':'🔗'})
IG_RESULT = "Acts of Service"
TT_LINE = TT_STD
LINE_SPEED = {5: 0.8}
