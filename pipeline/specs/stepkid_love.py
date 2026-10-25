import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD, C
TITLE = "when you love someone who already has a kid"
BODY_LINES = [
"When you love someone who already has a kid, you're not competing, you're building something new.",
"Not because you forget you're not the parent. Because you show up anyway, every day.",
"You learn their favorite cereal before you ever ask their favorite color.",
"You wait in the car during pickup so no one ever feels replaced.",
"If you've loved someone's kid like your own without needing the title... send this to the one who earned it quietly.",
"But if you make a child feel like competition for your attention... that's not a relationship, that's a rivalry.",
"Because loving someone's family... isn't about fitting in, it's about being let in.",
]
D = [
'''  room('#f3cfa8','#d09d72');
  pup({kind:'girl',x:380,y:G+10,s:1.25,look:[.3,.1],eyes:'open',mouth:'smile'});
  pup({kind:'boy',x:740,y:G+10,s:1.2,flip:-1,look:[-.3,.1],eyes:'happy',mouth:'smile',blush:.3});''',
'''  room('#d9e2c8','#a9b38f');
  pup({kind:'girl',x:400,y:G+10,s:1.25,look:[.3,0],eyes:'open',mouth:'smile'});
  pup({kind:'boy',x:740,y:G+10,s:1.2,flip:-1,look:[-.3,0],eyes:'happy',mouth:'smile'});''',
'''  room('#cfe3ec','#98b6c2');
  bowl(540,G-10,true);
  pup({kind:'girl',x:380,y:G+10,s:1.2,look:[.3,-.1],eyes:'happy',mouth:'smile',blush:.3});''',
'''  room('#6f6a78','#5a5562','rgba(255,255,255,.06)');
  windowBox(760,320,290,230,(w,h)=>{ctx.fillStyle='#8fd0f0';ctx.fillRect(0,0,w,h);});
  pup({kind:'girl',x:380,y:G+20,s:1.2,look:[.4,.1],eyes:'open',mouth:'flat'});
  if(u>.9){ctx.save();ctx.globalAlpha=win(u,.9,8);bubbleText(380,680,"take your time, I've got the radio",1,.8);ctx.restore();}''',
SHARE,
'''  room('#6f6a78','#5a5562','rgba(255,255,255,.05)');
  pup({kind:'girl',x:380,y:G+10,s:1.25,look:[.4,.3],brows:'sad',mouth:'flat'});
  pup({kind:'boy',x:760,y:G+10,s:1.2,flip:-1,look:[-.4,.3],brows:'sad',mouth:'flat'});
  if(u>.8){ctx.save();ctx.globalAlpha=win(u,.8,8);bubbleText(560,680,"pick. me or them.",1,.8);ctx.restore();}
  if(u>1.6)raincloudSmall(540,580,win(u,1.6,9)*.6);''',
HUG,
]
SCENES = spec(BODY_LINES, D, [{'something new':'🤍'},{'every day':'🤍'},{'favorite color':'🥣'},{'replaced':'🚗'},{'quietly':'💌'},{'a rivalry':'🚩'},{'let in':'🤍'}])
IG_LINE = "The favorite cereal. The car radio during pickup. The family you joined without asking for credit. Everyone shows up for a blended family their own way... Want to know yours? There's a sixty second test in our bio. Take it together."
IG_CAPS = C(IG_LINE, {'cereal':'🥣','yours?':'🤍','bio':'🔗'})
IG_RESULT = "Acts of Service"
TT_LINE = TT_STD
