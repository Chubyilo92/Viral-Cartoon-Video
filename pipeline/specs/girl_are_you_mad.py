import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD, C
from _r3props import R3_PROPS
TITLE = "when a girl asks if you're mad"
PRELUDE = R3_PROPS
LINE_SPEED = {1: 1.05}  # voicecheck: line 2 ended rising (+13%) at 0.9; 1.05 → +5%
BODY_LINES = [
"When a girl asks \"are you mad at me?\" for the third time, she's not being annoying.",
"You replied with one word instead of your usual paragraph, and she noticed.",
"She's already gone back through your last ten messages looking for what she did.",
"She'll say sorry for something she's not even sure happened.",
"If you're the girl who asks... send this to the one you keep asking.",
"But if you keep saying \"I'm fine\" when you're not... you're not protecting her. You're making her guess.",
"Because a girl who asks if you're mad... just wants to fix it before it gets bigger.",
]
D = [
'''  room('#e3c9a0','#bf9670');
  pup({kind:'girl',x:360,y:G+10,s:1.3,look:[.5,.1],brows:'sad',mouth:'flat'});
  pup({kind:'boy',x:780,y:G+10,s:1.22,flip:-1,look:[-.4,.1],eyes:'wide',mouth:'o'});
  if(u>.5){const k=pop(u,.5,.4);ctx.save();ctx.globalAlpha=win(u,.5,9);bubbleText(380,640,"are you mad at me? 🥺",1,.85*k);ctx.restore();}''',
'''  room('#e8d8c8','#c2a98f');
  bigPhone(600,780,1.0,()=>{chatBub(-100,-200,170,92,false);chatBub(-100,-96,190,72,false);chatBub(-100,-12,150,92,false);
    if(u>.8)chatTxt(100,110,'ok',true);});
  pup({kind:'girl',x:300,y:G+10,s:1.15,look:[.6,-.3],brows:'sad',mouth:'flat'});''',
'''  room('#cfe3ec','#98b6c2');
  const sc=(u*90)%260;
  bigPhone(660,780,1.0,()=>{for(let i=0;i<8;i++){chatBub(i%2?-30:-100,-210+i*70-sc+130,140,52,i%2==1);}});
  pup({kind:'girl',x:300,y:G+10,s:1.2,look:[.6,-.2],brows:'sad',mouth:'flat',earLift:-.2});''',
'''  room('#f1d5b0','#caa070');
  pup({kind:'girl',x:360,y:G+10,s:1.3,look:[.5,.2],brows:'sad',mouth:'flat',earLift:-.3});
  pup({kind:'boy',x:770,y:G+10,s:1.22,flip:-1,look:[-.4,.1],eyes:'open',mouth:'o'});
  if(u>.5){const k=pop(u,.5,.4);ctx.save();ctx.globalAlpha=win(u,.5,9);bubbleText(380,650,"sorry... 😔",1,.9*k);ctx.restore();}''',
SHARE,
'''  room('#4a3f4f','#3a3140','rgba(255,255,255,.05)');
  pup({kind:'boy',x:760,y:G+10,s:1.25,flip:-1,look:[-.2,.1],brows:'sad',mouth:'flat'});
  pup({kind:'girl',x:350,y:G+10,s:1.25,look:[.5,.2],brows:'sad',mouth:'flat',earLift:-.3});
  if(u>.5){ctx.save();ctx.globalAlpha=win(u,.5,9);bubbleText(740,640,"I'm fine.",1,.9);ctx.restore();}
  if(u>1.8)raincloudSmall(350,640,win(u,1.8,9)*.7);''',
HUG,
]
SCENES = spec(BODY_LINES, D, [{'mad at me':'🥺'},{'noticed':'👀'},{'messages':'📱'},{'happened':'😔'},{'keep asking':'💌'},{'guess':'🚩'},{'bigger':'🤍'}])
IG_LINE = "The asking. The noticing. The sorry. Everyone shows love their own way... Want to know yours? There's a sixty second test in our bio. Take it together."
IG_CAPS = C(IG_LINE, {'asking':'🥺','yours?':'🤍','bio':'🔗'})
IG_RESULT = "Words of Affirmation"
TT_LINE = TT_STD
