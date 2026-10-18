import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD, C
TITLE = "when she's been cheated on"
BODY_LINES = [
"When a girl who's been cheated on loves you... she notices when your phone goes face down.",
"Not because she thinks you're like him. Her heart just remembers how it started last time.",
"She asks who you were texting... then says sorry for asking.",
"And the first time you hand her your phone without being asked... she cries.",
"If she's learning to trust again with you... send this to her.",
"But if you make her feel crazy for asking... you're not helping her heal. You're him.",
"Because when she trusts again after that... she's trusting you with everything.",
]
D = [
'''  room('#f3cfa8','#d09d72');
  blob(rectPts(330,G-150,420,26,10),'#a58363');
  const fl=P(u,1.0,1.6);
  phoneMock(560,G-170,.3,lerp(0,3.1,fl)*0+.03,()=>{ctx.fillStyle=fl>.5?'#2b2830':'#dfe4ee';ctx.fillRect(-70,-290,140,280);});
  pup({kind:'boy',x:800,y:G+10,s:1.25,flip:-1,look:[-.4,.4],eyes:'open',mouth:'flat'});
  pup({kind:'girl',x:270,y:G+10,s:1.3,look:[.7,.3],eyes:fl>.5?'wide':'open',mouth:'flat',earLift:-.2*fl});''',
'''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  pup({kind:'girl',x:420,y:G+10,s:1.4,look:[.3,.4],brows:'sad',mouth:'flat',earLift:-.3,tilt:-.04});
  const k=pop(u,.6,.5);
  ctx.save();ctx.translate(740,760);ctx.scale(k,k);heart(0,0,90,'#ec7489');ctx.rotate(-.6);blob(rectPts(-70,-16,140,32,10),'#fbeedd',{lw:4});ctx.restore();
  if(u>2)raincloudSmall(420,600,win(u,2,9)*.5);''',
'''  room('#d9e2c8','#a9b38f');
  pup({kind:'boy',x:760,y:G+10,s:1.3,flip:-1,look:[-.6,0],eyes:u>3?'happy':'open',mouth:'smile',blush:.3});
  pup({kind:'girl',x:330,y:G+10,s:1.3,look:[.6,0],eyes:'open',mouth:u<2.4?'flat':'pout',brows:u>2.4?'sad':undefined,blush:u>2.4?.5:0});
  if(u>.5){ctx.save();ctx.globalAlpha=win(u,.5,2.6);bubbleText(360,700,"who was that? 👀",1,.85);ctx.restore();}
  if(u>2.6){ctx.save();ctx.globalAlpha=win(u,2.6,8);bubbleText(360,700,"...sorry for asking 🙈",1,.85);ctx.restore();}''',
'''  room('#f6d7c6','#d6a286');
  ell(560,G+40,420,70,'#e7b9a0',{lw:5});
  const sl=P(u,.6,2.0);
  pup({kind:'girl',x:300,y:G+10,s:1.3,look:[.7,.2],eyes:u>2.6?'happy':'wide',mouth:u>2.6?'smile':'flat',blush:u>2.6?.7:0,tilt:-.06});
  pup({kind:'boy',x:780,y:G+10,s:1.3,flip:-1,look:[-.7,0],eyes:'open',mouth:'smile',paw:{x:-150,y:-60,k:sl}});
  phoneMock(lerp(700,470,sl),lerp(1000,1040,sl),.36,lerp(.1,-.4,sl),()=>{ctx.fillStyle='#dfe4ee';ctx.fillRect(-70,-290,140,280);ctx.fillStyle='#b7c0d4';for(let i=0;i<5;i++)ctx.fillRect(-60,-260+i*38,120,8);});
  if(u>2.6){ctx.save();ctx.globalAlpha=win(u,2.6,9);ell(245,890,7,11,'#7ec3f0',{lw:2});ell(358,890,7,11,'#7ec3f0',{lw:2});ctx.restore();floatHearts(300,760,2.8,u,4,120);}''',
SHARE,
'''  room('#6f6a78','#5a5562','rgba(255,255,255,.05)');
  pup({kind:'boy',x:740,y:G+10,s:1.35,flip:-1,look:[-.6,0],eyes:'open',mouth:'flat',brows:'sad',tilt:-.04});
  pup({kind:'girl',x:320,y:G+10,s:1.2,look:[.6,.4],brows:'sad',mouth:'flat',earLift:-.4});
  if(u>.6){ctx.save();ctx.globalAlpha=win(u,.6,8);bubbleText(720,680,"you're being crazy 🙄",1,.85);ctx.restore();}
  if(u>1.4)raincloudSmall(320,700,win(u,1.4,9));''',
HUG,
]
SCENES = spec(BODY_LINES, D, [{'face down':'📱'},{'last time':'🩹'},{'asking':'🙈'},{'cries':'🥹'},{'her':'💌'},{'him':'🚩'},{'everything':'🤍'}])
IG_LINE = "The phone. The sorry. The happy tears. Everyone heals and loves their own way... Want to know yours? There's a sixty second test in our bio. Take it together."
IG_CAPS = C(IG_LINE, {'phone':'📱','yours?':'🤍','bio':'🔗'})
IG_RESULT = "Words of Affirmation"
TT_LINE = TT_STD
