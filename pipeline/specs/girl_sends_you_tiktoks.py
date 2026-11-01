import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD, C
from _r3props import R3_PROPS
TITLE = "when a girl sends you tiktoks"
PRELUDE = R3_PROPS
LINE_SPEED = {6: 0.85}  # voicecheck: line 7 low word match at 0.9
BODY_LINES = [
"When a girl sends you fifteen TikToks a day, she's not spamming you.",
"Every single one is a little \"this is literally us.\"",
"She sends the funny ones at 2am, knowing you're asleep, so they're the first thing you see.",
"And she checks if you've watched them. Every time.",
"If your DMs are full of her videos... send her this one back.",
"But the day she stops sending them... she didn't run out of videos. She just stopped seeing you in them.",
"Because a girl who floods your DMs... sees you in everything.",
]
D = [
'''  room('#f3cfa8','#d09d72');
  pup({kind:'girl',x:300,y:G+10,s:1.25,look:[.5,0],eyes:'happy',mouth:'smile',blush:.4});
  pup({kind:'boy',x:800,y:G+10,s:1.2,flip:-1,look:[-.5,-.3],eyes:'wide',mouth:'o'});
  for(let i=0;i<6;i++){const t=P(u,.3+i*.35,1.1+i*.35);if(t>0&&t<1)playCard(lerp(380,720,t),lerp(700,620,t)-Math.sin(t*Math.PI)*160,.9);}
  const n=Math.min(15,Math.floor(Math.max(0,u-.3)/.35)+ (u>.3?1:0));
  if(n>0){ctx.save();ctx.fillStyle='#ec7489';ctx.beginPath();ctx.arc(860,640,40,0,7);ctx.fill();ctx.strokeStyle=INK;ctx.lineWidth=4;ctx.stroke();
   ctx.font='bold 36px Poppins';ctx.fillStyle='#fff';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText(String(n),860,642);ctx.restore();}''',
'''  room('#e8d8c8','#c2a98f');
  pup({kind:'girl',x:360,y:G+10,s:1.3,look:[.3,.1],eyes:'happy',mouth:'open',blush:.5,tilt:-.06});
  playCard(560,820,1.4);
  if(u>.5){const k=pop(u,.5,.4);ctx.save();ctx.globalAlpha=win(u,.5,9);bubbleText(420,610,"this is literally us 😂",1,.8*k);ctx.restore();}''',
'''  bedNight();bedBack();
  pup({kind:'boy',x:560,y:G-100,s:1.1,flip:-1,look:[0,0],eyes:'closed',mouth:'flat',shadow:false});
  blanket(150,935,G-190);zzz(680,G-470,u);
  const buzz=Math.sin(u*40)*(u%1.2<.4?4:0);
  playCard(860+buzz,G-260,.8);''',
'''  room('#cfe3ec','#98b6c2');
  pup({kind:'girl',x:340,y:G+10,s:1.3,look:[.5,-.1],eyes:'wide',mouth:'flat',tilt:-.04});
  bigPhone(760,720,.75,()=>{playCard(0,-60,1.4);ctx.font='bold 28px Poppins';ctx.fillStyle='#7a726c';ctx.textAlign='center';ctx.fillText(u>1.4?'Seen ✓':'Delivered',0,150);});
  if(u>.5){ctx.save();ctx.globalAlpha=win(u,.5,9);bubbleText(360,640,"did you watch it? 👀",1,.8);ctx.restore();}''',
SHARE,
'''  room('#6f6a78','#5a5562','rgba(255,255,255,.05)');
  pup({kind:'boy',x:380,y:G+10,s:1.3,look:[.5,.3],brows:'sad',mouth:'flat',earLift:-.3});
  bigPhone(760,720,.75,()=>{ctx.font='bold 24px Poppins';ctx.fillStyle='#9a928c';ctx.textAlign='center';ctx.fillText('no new',0,-16);ctx.fillText('messages',0,16);});
  if(u>1.4)raincloudSmall(380,640,win(u,1.4,9)*.7);''',
HUG,
]
SCENES = spec(BODY_LINES, D, [None,{'us':'😂'},{'see':'🌙'},{'every time':'👀'},{'back':'💌'},{'in them':'💔'},{'everything':'🤍'}])
IG_LINE = "The videos. The middle of the night sends. The checking if you watched. Everyone shows love their own way... Want to know yours? There's a sixty second test in our bio. Take it together."
IG_CAPS = C(IG_LINE, {'videos':'📲','yours?':'🤍','bio':'🔗'})
IG_RESULT = "Quality Time"
TT_LINE = TT_STD
