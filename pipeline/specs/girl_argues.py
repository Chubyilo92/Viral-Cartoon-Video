import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD, C
TITLE = "when a girl argues with you"
PRELUDE = r'''
function tears(x,y,u){ctx.save();ctx.fillStyle='#8fc8f0';ctx.strokeStyle=INK;ctx.lineWidth=3;for(const sd of[-1,1]){const yy=y+fract(u*.9+(sd>0?.5:0))*60;ctx.beginPath();ctx.ellipse(x+sd*56,yy,8,12,0,0,7);ctx.fill();ctx.stroke();}ctx.restore();}
'''
BODY_LINES = [
"When a girl argues with you, she's not trying to win. She's trying to be understood.",
"She'll explain the same thing three times. Not because she thinks you're stupid. Because she still believes you'll get it.",
"She'll cry halfway through a sentence... and keep going anyway.",
"She'll bring it up again the next morning. Because she'd rather fix it than pretend it didn't happen.",
"If you still fight for him like this... send this to him.",
"But the day she stops arguing and just says \"okay\"... she hasn't calmed down. She's given up.",
"Because a girl who argues with you... still thinks you're worth the fight.",
]
D = [
'''  room('#f3cfa8','#d09d72');
  pup({kind:'girl',x:380,y:G+10,s:1.3,look:[.4,.1],brows:'angry',mouth:'pout'});
  pup({kind:'boy',x:760,y:G+10,s:1.25,flip:-1,look:[-.4,.1],eyes:'open',mouth:'flat'});
  if(u>.8){ctx.save();ctx.globalAlpha=win(u,.8,9);bubbleText(400,660,"just listen to me!",1,.85);ctx.restore();}''',
'''  room('#e3c9a0','#bf9670');
  pup({kind:'girl',x:380,y:G+10,s:1.3,look:[.4,.1],brows:'sad',mouth:'flat'});
  pup({kind:'boy',x:760,y:G+10,s:1.25,flip:-1,look:[-.4,.1],eyes:'wide',mouth:'o'});
  if(u>.5){ctx.save();ctx.globalAlpha=win(u,.5,9);bubbleText(420,660,"okay, ONE more time...",1,.85);ctx.restore();}''',
'''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  pup({kind:'girl',x:400,y:G+10,s:1.3,look:[.4,.2],brows:'sad',mouth:'open'});
  if(u>.4)tears(400,G-215,u);
  pup({kind:'boy',x:770,y:G+10,s:1.25,flip:-1,look:[-.4,.2],brows:'sad',mouth:'flat'});''',
'''  room('#fbe7c6','#e2c08f');
  windowBox(680,330,300,240,(w,h)=>{ctx.fillStyle='#ffe2a8';ctx.fillRect(0,0,w,h);});
  mug(560,G-40,1);
  pup({kind:'girl',x:380,y:G+10,s:1.3,look:[.4,.1],eyes:'open',mouth:'flat'});
  pup({kind:'boy',x:780,y:G+10,s:1.25,flip:-1,look:[-.4,.1],eyes:'open',mouth:'flat'});
  if(u>.8){ctx.save();ctx.globalAlpha=win(u,.8,9);bubbleText(420,660,"about last night...",1,.85);ctx.restore();}''',
SHARE,
'''  room('#6f6a78','#5a5562','rgba(255,255,255,.05)');
  pup({kind:'girl',x:380,y:G+10,s:1.3,flip:-1,look:[-.4,.3],brows:'sad',mouth:'flat',earLift:-.3});
  pup({kind:'boy',x:760,y:G+10,s:1.25,flip:-1,look:[-.4,.1],eyes:'open',mouth:'smile'});
  if(u>.6){ctx.save();ctx.globalAlpha=win(u,.6,9);bubbleText(380,720,"okay.",1,.85);ctx.restore();}
  if(u>1.6)raincloudSmall(380,540,win(u,1.6,9)*.8);''',
HUG,
]
SCENES = spec(BODY_LINES, D, [{'understood':'🤍'},{'get it':'🥺'},{'anyway':'😢'},{'happen':'☀️'},{'him':'💌'},{'given up':'🚩'},{'fight':'🤍'}])
IG_LINE = "The explaining. The tears. The next morning. Everyone fights for love their own way... Want to know yours? There's a sixty second test in our bio. Take it together."
IG_CAPS = C(IG_LINE, {'tears':'😢','yours?':'🤍','bio':'🔗'})
IG_RESULT = "Quality Time"
TT_LINE = TT_STD
