import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD, C
TITLE = "when a girl goes quiet after a fight"
BODY_LINES = [
"When a girl goes quiet after a fight, she's not punishing you with silence.",
"Not because she doesn't care. Because the next five minutes could say something you can't take back.",
"She goes to the other room... just long enough to stop shaking.",
"Then she comes back first, every time, ready to actually talk it out.",
"If she comes back to fix it instead of running... send this to the girl who never gives up on you.",
"But if her quiet turns into days of nothing... that's not processing, that's shutting you out.",
"Because a girl who comes back to fix it... never stopped loving you, she was protecting it.",
]
D = [
'''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  pup({kind:'girl',x:420,y:G+10,s:1.3,look:[.3,.5],brows:'sad',mouth:'flat',earLift:-.3,tilt:-.04});
  pup({kind:'boy',x:800,y:G+10,s:1.25,flip:-1,look:[-.5,.3],brows:'sad',mouth:'flat'});
  if(u>1.4)raincloudSmall(420,600,win(u,1.4,9)*.4);''',
'''  room('#6f6a78','#5a5562','rgba(255,255,255,.05)');
  pup({kind:'girl',x:540,y:G+10,s:1.35,look:[0,.5],brows:'sad',mouth:'flat',earLift:-.3});
  if(u>.6)raincloudSmall(540,620,win(u,.6,9));''',
'''  room('#cfe3ec','#98b6c2');
  windowBox(700,330,300,240,(w,h)=>{ctx.fillStyle='#8fd0f0';ctx.fillRect(0,0,w,h);});
  const sh=Math.sin(u*26)*4*win(u,0,2.2,.6);
  pup({kind:'girl',x:340+sh,y:G+10,s:1.25,look:[.2,.3],brows:'sad',mouth:'flat',earLift:-.2});''',
'''  room('#f6d7c6','#d6a286');
  const w2=P(u,.4,1.4);
  pup({kind:'girl',x:lerp(760,560,w2),y:G+10,s:1.3,flip:-1,look:[-.4,.2],eyes:'open',mouth:'flat'});
  pup({kind:'boy',x:320,y:G+10,s:1.3,look:[.5,.2],eyes:'open',mouth:'smile',blush:.2});
  if(u>1.2){ctx.save();ctx.globalAlpha=win(u,1.2,8);bubbleText(600,660,"can we talk? 🤍",1,.85);ctx.restore();}''',
SHARE,
'''  room('#3d4b6c','#303b57','rgba(255,255,255,.05)');
  pup({kind:'boy',x:540,y:G+10,s:1.3,look:[0,.4],brows:'sad',mouth:'flat',earLift:-.3});
  if(u>.5)raincloudSmall(540,610,win(u,.5,9)*.8);
  if(u>2)zzz(700,560,u,win(u,2,9)*.5);''',
HUG,
]
SCENES = spec(BODY_LINES, D, [{'silence':'🤍'},{'damage':'💭'},{'shaking':'🚪'},{'talk it out':'🤍'},{'you':'💌'},{'out':'🚩'},{'protecting it':'🤍'}])
IG_LINE = "The quiet room. The coming back. The talking it out. Everyone processes a fight their own way... Want to know yours? There's a sixty second test in our bio. Take it together."
IG_CAPS = C(IG_LINE, {'room':'🚪','yours?':'🤍','bio':'🔗'})
IG_RESULT = "Words of Affirmation"
TT_LINE = TT_STD
