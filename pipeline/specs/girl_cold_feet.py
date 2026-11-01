import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD, C
from _r3props import R3_PROPS
TITLE = "when she puts her cold feet on you"
PRELUDE = R3_PROPS
LINE_SPEED = {6: 0.8}  # voicecheck: line 7 pace 3.7 w/s at 0.9
B = "bedNight();bedBack();"
BLK = "blanket(150,935,G-190);"
BODY_LINES = [
"When a girl puts her freezing feet on you in bed, she's not trying to annoy you.",
"She waits until you're almost asleep. Then she does it.",
"She'll swear her feet aren't that cold... while you jump out of your skin.",
"And she'll do it every single night until spring.",
"If you've been her hot water bottle all winter... send this to her.",
"But the night she keeps her socks on and stays on her own side... it's not her feet that went cold.",
"Because a girl who puts her cold feet on you... just wants to be as close to you as she can get.",
]
D = [
B + '''
  pup({kind:'girl',x:380,y:G-100,s:1.1,flip:1,look:[.5,0],eyes:'squint',mouth:'smile',shadow:false});
  pup({kind:'boy',x:700,y:G-100,s:1.1,flip:-1,look:[-.5,0],eyes:u>1?'wide':'open',mouth:u>1?'o':'flat',shadow:false});
  ''' + BLK + '''
  for(let i=0;i<3;i++)snowflake(520+i*40,G-60-Math.sin(u*3+i)*14,18,win(u,.8,9));''',
B + '''
  pup({kind:'boy',x:700,y:G-100,s:1.1,flip:-1,look:[0,0],eyes:'closed',mouth:'flat',shadow:false});
  pup({kind:'girl',x:380,y:G-100,s:1.1,flip:1,look:[.6,0],eyes:u>1.6?'squint':'open',mouth:'smile',shadow:false});
  ''' + BLK + '''
  zzz(800,G-470,u);
  if(u>1.8)for(let i=0;i<3;i++)snowflake(560+i*40,G-60-Math.sin(u*3+i)*14,18,win(u,1.8,9));''',
B + '''
  const j=u>.6?Math.max(0,1-Math.abs(u-1.1)*1.6):0;
  pup({kind:'boy',x:720,y:G-100,s:1.1,flip:-1,look:[-.4,-.3],eyes:'wide',mouth:'o',bob:-j*120,shadow:false});
  pup({kind:'girl',x:380,y:G-100,s:1.1,flip:1,look:[.5,0],eyes:'happy',mouth:'smile',blush:.4,shadow:false});
  ''' + BLK + '''
  if(u>1.4){ctx.save();ctx.globalAlpha=win(u,1.4,9);bubbleText(330,600,"they're not even cold 😇",1,.75);ctx.restore();}''',
B + '''
  pup({kind:'girl',x:480,y:G-100,s:1.1,flip:1,look:[0,0],eyes:'closed',mouth:'smile',tilt:.1,shadow:false});
  pup({kind:'boy',x:660,y:G-100,s:1.1,flip:-1,look:[0,0],eyes:'closed',mouth:'flat',tilt:-.06,shadow:false});
  ''' + BLK + '''
  for(let i=0;i<9;i++){const sx=80+i*115,sy=(i*137+u*90)%560+60;snowflake(sx,sy,14,.8);}''',
SHARE,
B + '''
  pup({kind:'girl',x:280,y:G-100,s:1.1,flip:-1,look:[-.5,0],eyes:'open',mouth:'flat',shadow:false});
  pup({kind:'boy',x:780,y:G-100,s:1.1,flip:-1,look:[-.6,.2],brows:'sad',mouth:'flat',shadow:false});
  ''' + BLK + '''
  if(u>1.2)raincloudSmall(540,G-520,win(u,1.2,9)*.8);''',
B + '''
  pup({kind:'boy',x:640,y:G-100,s:1.1,flip:-1,look:[0,0],eyes:'closed',mouth:'smile',blush:.5,tilt:-.12,shadow:false});
  pup({kind:'girl',x:470,y:G-100,s:1.1,flip:1,look:[0,0],eyes:'closed',mouth:'smile',blush:.5,tilt:.14,shadow:false});
  ''' + BLK + '''
  zzz(760,G-480,u);floatHearts(560,G-470,.4,u,4,120);''',
]
SCENES = spec(BODY_LINES, D, [{'annoy you':'🥶'},{'does it':'😈'},{'skin':'😱'},{'spring':'❄️'},{'winter':'💌'},{'went cold':'💔'},{'can get':'🤍'}])
IG_LINE = "The cold feet. The perfect timing. The every single night. Everyone shows love their own way... Want to know yours? There's a sixty second test in our bio. Take it together."
IG_CAPS = C(IG_LINE, {'cold feet':'🥶','yours?':'🤍','bio':'🔗'})
IG_RESULT = "Physical Touch"
TT_LINE = TT_STD
