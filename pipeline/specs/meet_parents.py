import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD, C
TITLE = "when he finally meets your parents"
BODY_LINES = [
"When he finally meets your parents, the nerves are the whole point.",
"Not because he's not ready. Because this dinner matters more than he's letting on.",
"He wipes his palms twice before your mom even opens the door.",
"He laughs at your dad's oldest joke like it's the funniest thing he's heard all year.",
"If he showed up nervous and stayed anyway... send this to the one who tried.",
"But if he can't sit through one dinner for you... that's not shyness, that's a preview.",
"Because the nerves before meeting your parents... aren't weakness, they're proof it matters.",
]
D = [
'''  room('#f3cfa8','#d09d72');
  pup({kind:'boy',x:380,y:G+10,s:1.25,look:[.3,.1],eyes:'open',mouth:'flat',brows:'sad'});
  pup({kind:'girl',x:740,y:G+10,s:1.2,flip:-1,look:[-.3,.1],eyes:'happy',mouth:'smile',blush:.3,wag:.2});''',
'''  room('#e3c9a0','#bf9670');
  pup({kind:'boy',x:400,y:G+10,s:1.25,look:[.3,0],eyes:'open',mouth:'flat'});
  pup({kind:'girl',x:740,y:G+10,s:1.2,flip:-1,look:[-.3,0],eyes:'open',mouth:'smile',blush:.3});''',
'''  room('#cfe3ec','#98b6c2');
  windowBox(700,330,300,240,(w,h)=>{ctx.fillStyle='#8fd0f0';ctx.fillRect(0,0,w,h);});
  pup({kind:'boy',x:360,y:G+10,s:1.3,look:[.3,.2],eyes:'open',mouth:'flat',brows:'sad'});
  if(u>.6){ctx.save();ctx.globalAlpha=win(u,.6,8);bubbleText(360,680,"okay. okay. here we go.",1,.8);ctx.restore();}''',
'''  room('#d9e2c8','#a9b38f');
  pup({kind:'boy',x:380,y:G+10,s:1.3,look:[.3,0],eyes:'happy',mouth:'smile',blush:.3});
  pup({kind:'girl',x:740,y:G+10,s:1.25,flip:-1,look:[-.3,0],eyes:'happy',mouth:'smile',blush:.5,wag:.4});
  if(u>.9)sparkle(560,700,42*pop(u,.9,.4),win(u,.9,8));''',
SHARE,
'''  room('#6f6a78','#5a5562','rgba(255,255,255,.05)');
  pup({kind:'boy',x:380,y:G+10,s:1.25,look:[.4,.3],brows:'sad',mouth:'flat'});
  pup({kind:'girl',x:760,y:G+10,s:1.2,flip:-1,look:[-.4,.3],brows:'sad',mouth:'flat'});
  if(u>.8){ctx.save();ctx.globalAlpha=win(u,.8,8);bubbleText(560,680,"I should probably go...",1,.8);ctx.restore();}
  if(u>1.6)raincloudSmall(540,580,win(u,1.6,9)*.6);''',
HUG,
]
SCENES = spec(BODY_LINES, D, [{'whole point':'🤍'},{'letting on':'🤍'},{'the door':'😅'},{'all year':'🥹'},{'who tried':'💌'},{'a preview':'🚩'},{'it matters':'🤍'}])
IG_LINE = "The sweaty palms. The old joke. Dinner with your parents, done right. Everyone shows up nervous their own way... Want to know yours? There's a sixty second test in our bio. Take it together."
IG_CAPS = C(IG_LINE, {'palms':'🤍','yours?':'🤍','bio':'🔗'})
IG_RESULT = "Words of Affirmation"
TT_LINE = TT_STD
