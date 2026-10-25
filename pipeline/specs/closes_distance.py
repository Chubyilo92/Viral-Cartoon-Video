import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD, C
TITLE = "when you finally close the distance"
LINE_SPEED = {4: 0.78}
BODY_LINES = [
"When you finally close the distance, the time difference stops running your life.",
"Not because the waiting was easy. Because you never once talked about giving up.",
"You fall asleep on a video call for years, then wake up beside them for real.",
"They keep every boarding pass from every flight it ever took to see you.",
"If you made it to the same city... send this to the one who waited with you.",
"But if 'someday' never turns into a date on a calendar... that's not distance, that's hesitation.",
"Because closing the distance... isn't the flight, it's everything before you book it.",
]
D = [
'''  room('#3d4b6c','#303b57','rgba(255,255,255,.05)');
  phoneMock(540,900,.7,0,()=>{ctx.fillStyle='#fde9b0';ctx.fillRect(-70,-280,140,270);ctx.font='40px "Noto Color Emoji"';ctx.textAlign='center';ctx.fillText('💤',0,-150);});
  if(u>.6)zzz(680,760,u,win(u,.6,8)*.6);''',
'''  room('#cfe3ec','#98b6c2');
  pup({kind:'boy',x:380,y:G+10,s:1.25,look:[.3,0],eyes:'open',mouth:'smile'});
  pup({kind:'girl',x:740,y:G+10,s:1.2,flip:-1,look:[-.3,0],eyes:'happy',mouth:'smile',blush:.4});''',
'''  room('#6f6a78','#5a5562','rgba(255,255,255,.08)');
  windowBox(760,320,290,230,(w,h)=>{ctx.fillStyle='#1c2440';ctx.fillRect(0,0,w,h);for(let i=0;i<30;i++){ctx.fillStyle='rgba(255,255,255,.8)';ctx.fillRect((i*53)%w,(i*91)%h,2,2);}});
  pup({kind:'boy',x:360,y:G+10,s:1.25,look:[.3,.2],eyes:'open',mouth:'flat'});
  if(u>.9)zzz(400,620,u,win(u,.9,9)*.5);''',
'''  room('#f6d7c6','#d6a286');
  pup({kind:'girl',x:400,y:G+10,s:1.3,look:[.3,0],eyes:'happy',mouth:'smile',blush:.5,wag:.4});
  pup({kind:'boy',x:740,y:G+10,s:1.25,flip:-1,look:[-.3,0],eyes:'happy',mouth:'smile'});
  if(u>.8)floatHearts(560,800,.8,u,4,150);''',
SHARE,
'''  room('#3d4b6c','#303b57','rgba(255,255,255,.05)');
  pup({kind:'boy',x:380,y:G+10,s:1.2,look:[.4,.3],brows:'sad',mouth:'flat'});
  pup({kind:'girl',x:760,y:G+10,s:1.2,flip:-1,look:[-.4,.3],brows:'sad',mouth:'flat'});
  if(u>.8){ctx.save();ctx.globalAlpha=win(u,.8,8);bubbleText(560,680,"...someday, maybe",1,.8);ctx.restore();}
  if(u>1.6)raincloudSmall(540,580,win(u,1.6,9)*.6);''',
HUG,
]
SCENES = spec(BODY_LINES, D, [{'your life':'🤍'},{'giving up':'🤍'},{'for real':'🥹'},{'see you':'✈️'},{'with you':'💌'},{'hesitation':'🚩'},{'book it':'🤍'}])
IG_LINE = "The video calls. The boarding passes. The someday that finally became a date. Everyone closes the distance their own way... Want to know yours? There's a sixty second test in our bio. Take it together."
IG_CAPS = C(IG_LINE, {'calls':'🤍','yours?':'🤍','bio':'🔗'})
IG_RESULT = "Acts of Service"
TT_LINE = TT_STD
