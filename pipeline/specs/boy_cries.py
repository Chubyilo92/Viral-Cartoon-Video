import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD, C
TITLE = "when a boy cries in front of you"
LINE_SPEED = {5: 0.82}
PRELUDE = r'''
function tears(x,y,u){ctx.save();ctx.fillStyle='#8fc8f0';ctx.strokeStyle=INK;ctx.lineWidth=3;for(const sd of[-1,1]){const yy=y+fract(u*.9+(sd>0?.5:0))*60;ctx.beginPath();ctx.ellipse(x+sd*56,yy,8,12,0,0,7);ctx.fill();ctx.stroke();}ctx.restore();}
'''
BODY_LINES = [
"When a boy cries in front of you, he's not being weak.",
"He held it in at work, with his friends, in front of his family. You're the first person he let it out with.",
"He'll wipe his face fast and say sorry. Not because he's embarrassed. Because nobody ever told him it was okay.",
"He'll go quiet afterwards. Just let him lean on you.",
"If he's ever cried in front of you... send this to him.",
"But if you ever bring it up in an argument... he'll never cry in front of you again.",
"Because when a boy cries in front of you... it means he finally feels safe.",
]
D = [
'''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  pup({kind:'boy',x:380,y:G+10,s:1.3,look:[.3,.4],brows:'sad',mouth:'flat',earLift:-.3});
  if(u>.5)tears(380,G-215,u);
  pup({kind:'girl',x:760,y:G+10,s:1.25,flip:-1,look:[-.4,.2],brows:'sad',mouth:'flat'});''',
'''  room('#cfe3ec','#98b6c2');
  windowBox(680,330,300,240,(w,h)=>{ctx.fillStyle='#8fd0f0';ctx.fillRect(0,0,w,h);});
  pup({kind:'boy',x:400,y:G+10,s:1.3,look:[.2,.1],eyes:'open',mouth:'flat'});
  if(u>.8)raincloudSmall(400,600,win(u,.8,9)*.5);''',
'''  room('#6f6a78','#5a5562','rgba(255,255,255,.05)');
  pup({kind:'boy',x:400,y:G+10,s:1.3,look:[.4,.4],brows:'sad',mouth:'flat',earLift:-.3,tilt:.05});
  if(u<1.6)tears(400,G-215,u);
  pup({kind:'girl',x:770,y:G+10,s:1.25,flip:-1,look:[-.4,.2],brows:'sad',mouth:'flat'});
  if(u>1){ctx.save();ctx.globalAlpha=win(u,1,9);bubbleText(420,660,"sorry... 😔",1,.85);ctx.restore();}''',
'''  room('#e8d8c8','#c2a98f');
  const k=P(u,.3,1.4);
  pup({kind:'girl',x:lerp(720,600,k),y:G+10,s:1.3,flip:-1,look:[-.3,.2],eyes:'happy',mouth:'smile',blush:.3,paw:{x:70,y:-190,k:k}});
  pup({kind:'boy',x:400,y:G+10,s:1.3,look:[.4,.2],eyes:'closed',mouth:'flat',tilt:.12*k,earLift:-.2});
  if(u>1.6)floatHearts(500,780,1.6,u,3,120);''',
SHARE,
'''  room('#4a3f4f','#3a3140','rgba(255,255,255,.05)');
  pup({kind:'girl',x:740,y:G+10,s:1.25,flip:-1,look:[-.4,.1],brows:'angry',mouth:'pout'});
  pup({kind:'boy',x:380,y:G+10,s:1.3,look:[.4,.4],brows:'sad',mouth:'flat',earLift:-.4});
  if(u>.6){ctx.save();ctx.globalAlpha=win(u,.6,9);bubbleText(720,640,"at least I don't cry!",1,.85);ctx.restore();}
  if(u>1.8)raincloudSmall(380,600,win(u,1.8,9)*.7);''',
HUG,
]
SCENES = spec(BODY_LINES, D, [{'weak':'🥺'},{'out':'🤍'},{'okay':'😔'},{'lean':'🤍'},{'him':'💌'},{'again':'🚩'},{'safe':'🤍'}])
IG_LINE = "The tears. The sorry. The leaning on you. Everyone shows love their own way... Want to know yours? There's a sixty second test in our bio. Take it together."
IG_CAPS = C(IG_LINE, {'tears':'🥺','yours?':'🤍','bio':'🔗'})
IG_RESULT = "Physical Touch"
TT_LINE = TT_STD
