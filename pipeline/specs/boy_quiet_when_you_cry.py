import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD, C
from _r3props import R3_PROPS
TITLE = "when he goes quiet while you cry"
PRELUDE = R3_PROPS
LINE_SPEED = {1: 0.8}  # voicecheck: line 2 pace 3.7 w/s at 0.9
BODY_LINES = [
"When a boy goes quiet while you cry, he's not being cold.",
"He doesn't know what to say, so he gets you a glass of water.",
"He sits close enough that his shoulder touches yours, and stays there.",
"Later, when you're not looking, he googles \"how to help when she's sad.\"",
"If he tries like this... send this to the boy who doesn't always get it right.",
"But if he ever tells you to stop crying... he's thinking about himself, not you.",
"Because a boy who goes quiet when you cry... is trying so hard not to say the wrong thing.",
]
D = [
'''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  pup({kind:'girl',x:360,y:G+10,s:1.3,look:[.2,.4],brows:'sad',mouth:'flat',earLift:-.3});
  tears(360,G-282,u);
  pup({kind:'boy',x:780,y:G+10,s:1.25,flip:-1,look:[-.5,.1],eyes:'open',mouth:'flat'});''',
'''  room('#e8d8c8','#c2a98f');
  pup({kind:'girl',x:340,y:G+10,s:1.3,look:[.4,.3],brows:'sad',mouth:'flat',earLift:-.3});
  if(u<2.5)tears(340,G-282,u);
  const wk=P(u,.2,1.6);
  pup({kind:'boy',x:lerp(860,640,wk),y:G+10,s:1.25,flip:-1,look:[-.5,.1],eyes:'open',mouth:'flat',paw:{x:120,y:-40,k:1}});
  glassWater(lerp(860,640,wk)-1.25*120,G+10-1.25*30,.9);''',
'''  room('#f1d5b0','#caa070');plant(970,G+6,.9);
  const sl=P(u,.2,1.2);
  pup({kind:'girl',x:410,y:G+10,s:1.3,look:[.3,.3],brows:'sad',mouth:'flat',tilt:.06*sl});
  pup({kind:'boy',x:lerp(800,700,sl),y:G+10,s:1.28,flip:-1,look:[-.3,.2],eyes:'open',mouth:'flat',tilt:-.08*sl});
  if(u>2)floatHearts(520,760,2,u,2,100);''',
'''  room('#3d4b6c','#303b57','rgba(255,255,255,.05)');
  pup({kind:'boy',x:290,y:G+10,s:1.2,look:[.6,-.2],eyes:'open',mouth:'flat',brows:'sad'});
  const q="how to help when she's sad";const n=Math.floor(P(u,.3,2.6)*q.length);
  bigPhone(720,700,1.0,()=>{ctx.fillStyle='#fff';ctx.strokeStyle='#c9c1b8';ctx.lineWidth=3;ctx.beginPath();ctx.roundRect(-100,-180,200,60,30);ctx.fill();ctx.stroke();
    ctx.font='bold 18px Poppins';ctx.fillStyle='#3a3330';ctx.textAlign='left';ctx.textBaseline='middle';
    const s=q.slice(0,n);ctx.fillText(s.slice(0,12),-84,-159);if(s.length>12)ctx.fillText(s.slice(12),-84,-139);
    if(u>2.8){ctx.fillStyle='#dcd6cf';for(let i=0;i<4;i++)ctx.fillRect(-96,-80+i*60,192-i*20,14);}});''',
SHARE,
'''  room('#4a3f4f','#3a3140','rgba(255,255,255,.05)');
  pup({kind:'girl',x:360,y:G+10,s:1.3,look:[.3,.4],brows:'sad',mouth:'flat',earLift:-.4});
  tears(360,G-282,u);
  pup({kind:'boy',x:780,y:G+10,s:1.25,flip:-1,look:[-.4,0],brows:'angry',mouth:'flat'});
  if(u>.5){ctx.save();ctx.globalAlpha=win(u,.5,9);bubbleText(760,640,"just stop crying.",1,.85);ctx.restore();}
  if(u>1.8)raincloudSmall(360,620,win(u,1.8,9)*.7);''',
HUG,
]
SCENES = spec(BODY_LINES, D, [{'cold':'🥺'},{'water':'🥛'},{'stays there':'🤍'},{'sad':'🔍'},{'right':'💌'},{'not you':'🚩'},{'wrong thing':'🤍'}])
IG_LINE = "The glass of water. The shoulder. The search at midnight. Everyone shows love their own way... Want to know yours? There's a sixty second test in our bio. Take it together."
IG_CAPS = C(IG_LINE, {'water':'🥛','yours?':'🤍','bio':'🔗'})
IG_RESULT = "Acts of Service"
TT_LINE = TT_STD
