import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD, C
TITLE = "years together"
BODY_LINES = [
"Years together... and he still kisses your forehead when you fall asleep first.",
"The fights get shorter. Not because you care less. Because you both know the way back now.",
"Friday night is pyjamas and a takeaway. You wouldn't swap it for the world.",
"You can tell he's had a bad day just from the way he says hey.",
"If it's been years and it still feels like this... send this to them.",
"But if you're still together, and you haven't really talked in months... that's not love lasting. That's just time passing.",
"Because real love isn't the butterflies. It's choosing each other after they're gone.",
]
D = [
'''  room('#3d4b6c','#303b57','rgba(255,255,255,.05)');
  pup({kind:'girl',x:380,y:G+10,s:1.25,look:[0,.4],eyes:'closed',mouth:'smile',breath:1,tilt:.18});
  zzz(470,760,u,win(u,.4,8));
  const k=P(u,1.6,2.6);
  pup({kind:'boy',x:lerp(780,640,k),y:G+10,s:1.25,flip:-1,look:[-.5,.4],eyes:k>.9?'closed':'happy',mouth:'smile',blush:.4,tilt:-.12*k});
  if(u>2.6)floatHearts(500,820,2.6,u,4,120);''',
'''  room('#f6d7c6','#d6a286');
  const m=u>2.6;
  pup({kind:'girl',x:340,y:G+10,s:1.3,look:[.4,0],mouth:m?'smile':'pout',eyes:m?'happy':'open',brows:m?undefined:'sad',blush:m?.4:.2});
  pup({kind:'boy',x:700,y:G+10,s:1.3,flip:-1,look:[-.4,0],mouth:m?'smile':'pout',eyes:m?'happy':'open',brows:m?undefined:'sad',paw:{x:-120,y:-60,k:m?P(u,2.6,3.2):0}});
  if(m)floatHearts(520,820,2.8,u,3,120);''',
'''  room('#f1d5b0','#caa070');
  ctx.save();ctx.translate(820,560);blob(rectPts(-110,-70,220,140,10),'#2b2830',{lw:4});ctx.fillStyle=Math.sin(u*5)>0?'#8ea7c9':'#a7bfdc';ctx.fillRect(-100,-60,200,120);ctx.restore();
  blob(rectPts(160,G-80,560,60,20),'#c97a6a');
  bowl(440,G+20,true);
  pup({kind:'girl',x:300,y:G+10,s:1.15,look:[.6,-.2],eyes:'happy',mouth:'smile',blush:.4});
  pup({kind:'boy',x:580,y:G+10,s:1.15,flip:-1,look:[.6,-.2],eyes:'happy',mouth:'smile',blush:.3});''',
'''  room('#e9ceb8','#c39a76',1180,'rgba(255,255,255,.2)');
  blob(rectPts(760,500,240,680,16),'#b98a5e');
  const w=P(u,.2,1.4);
  pup({kind:'boy',x:lerp(900,700,w),y:G+10,s:1.3,flip:-1,look:[-.3,.5],eyes:'open',mouth:'flat',brows:'sad',earLift:-.3});
  if(u>1.2&&u<4){ctx.save();ctx.globalAlpha=win(u,1.2,4);bubbleText(720,700,"hey.",1,.8);ctx.restore();}
  const c=P(u,2.6,3.4);
  pup({kind:'girl',x:lerp(260,400,c),y:G+10,s:1.25,look:[.6,0],eyes:'open',mouth:'flat',brows:'sad',paw:{x:140,y:-80,k:c}});''',
SHARE,
'''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  ell(540,G+20,420,60,'#a99a8a',{lw:4});
  pup({kind:'girl',x:300,y:G+10,s:1.2,flip:1,look:[-.2,.6],eyes:'open',mouth:'flat'});
  phoneMock(400,1110,.26,-.1,()=>{ctx.fillStyle='#9fb4d8';ctx.fillRect(-70,-290,140,280);});
  pup({kind:'boy',x:780,y:G+10,s:1.2,flip:-1,look:[.2,.6],eyes:'open',mouth:'flat'});
  phoneMock(680,1110,.26,.1,()=>{ctx.fillStyle='#9fb4d8';ctx.fillRect(-70,-290,140,280);});
  if(u>1.4)raincloudSmall(540,620,win(u,1.4,10)*.6);''',
HUG,
]
SCENES = spec(BODY_LINES, D, [{'first':'😴'},{'way back':'🤍'},{'world':'🍕'},{'hey':'🥺'},{'them':'💌'},{'passing':'⏳'},{'gone':'🤍'}])
IG_LINE = "The forehead kiss. The way back. Friday nights. Every couple loves in their own way... Want to know yours? There's a sixty second test in our bio. Take it together."
IG_CAPS = C(IG_LINE, {'kiss':'😴','yours?':'🤍','bio':'🔗'})
IG_RESULT = "Physical Touch"
TT_LINE = TT_STD
LINE_SPEED = {3: 0.8}
