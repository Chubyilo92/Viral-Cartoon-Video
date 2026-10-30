import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD, C
TITLE = "when a girl steals your hoodie"
PRELUDE = r'''
const HOOD='#5b7fb5', HOOD_D='#4a6a9a';
function hoodieOn(x,s,flip){ctx.save();ctx.translate(x,G+10);ctx.scale(s*(flip||1),s);
 ctx.lineWidth=4/s;ctx.strokeStyle=INK;ctx.fillStyle=HOOD;
 ctx.beginPath();ctx.moveTo(-62,-150);ctx.quadraticCurveTo(-92,-120,-96,-40);ctx.lineTo(-92,-4);ctx.lineTo(92,-4);ctx.lineTo(96,-40);ctx.quadraticCurveTo(92,-120,62,-150);ctx.quadraticCurveTo(0,-128,-62,-150);ctx.closePath();ctx.fill();ctx.stroke();
 ctx.fillStyle=HOOD_D;ctx.beginPath();ctx.moveTo(-40,-60);ctx.lineTo(40,-60);ctx.lineTo(48,-22);ctx.lineTo(-48,-22);ctx.closePath();ctx.fill();ctx.stroke();
 ctx.beginPath();ctx.moveTo(-16,-138);ctx.lineTo(-20,-96);ctx.moveTo(16,-138);ctx.lineTo(20,-96);ctx.stroke();
 ctx.fillStyle='#fff';ctx.beginPath();ctx.arc(-20,-94,4,0,7);ctx.arc(20,-94,4,0,7);ctx.fill();
 ctx.restore();}
function hoodieFolded(x,y,s){ctx.save();ctx.translate(x,y);ctx.scale(s,s);ctx.lineWidth=4;ctx.strokeStyle=INK;
 ctx.fillStyle=HOOD;ctx.beginPath();ctx.roundRect(-80,-46,160,46,10);ctx.fill();ctx.stroke();
 ctx.fillStyle=HOOD_D;ctx.beginPath();ctx.roundRect(-70,-70,140,28,8);ctx.fill();ctx.stroke();
 ctx.strokeStyle='#ffffffaa';ctx.lineWidth=3;ctx.beginPath();ctx.moveTo(-60,-24);ctx.lineTo(60,-24);ctx.stroke();ctx.restore();}
'''
BODY_LINES = [
"When a girl steals your hoodie, she's not just cold.",
"She wears it when you're away. Because it still smells like you.",
"She'll swear she's giving it back... and you'll never see it again.",
"She wears it the night after a fight, even when she's still mad at you.",
"If your wardrobe is half his hoodies... send this to him.",
"But the day she gives it back washed and folded... she's not being tidy. She's saying goodbye.",
"Because a girl in your hoodie... is keeping you close.",
]
D = [
'''  room('#f3cfa8','#d09d72');
  pup({kind:'girl',x:380,y:G+10,s:1.3,look:[.4,.1],eyes:'happy',mouth:'smile',blush:.4});
  hoodieOn(380,1.3);
  pup({kind:'boy',x:760,y:G+10,s:1.25,flip:-1,look:[-.4,.1],eyes:'wide',mouth:'o'});''',
'''  room('#e8d8c8','#c2a98f');
  windowBox(680,330,300,240,(w,h)=>{ctx.fillStyle='#8fd0f0';ctx.fillRect(0,0,w,h);});
  pup({kind:'girl',x:440,y:G+10,s:1.35,look:[.1,.1],eyes:'closed',mouth:'smile',blush:.5});
  hoodieOn(440,1.35);
  if(u>.6)floatHearts(440,780,.6,u,3,120);''',
'''  room('#e3c9a0','#bf9670');
  pup({kind:'girl',x:380,y:G+10,s:1.3,look:[.4,.1],eyes:'happy',mouth:'smile',blush:.3});
  hoodieOn(380,1.3);
  pup({kind:'boy',x:760,y:G+10,s:1.25,flip:-1,look:[-.4,.1],eyes:'squint',mouth:'flat'});
  if(u>.5){ctx.save();ctx.globalAlpha=win(u,.5,9);bubbleText(400,700,"I'll give it back tomorrow 😇",1,.8);ctx.restore();}''',
'''  room('#3d4b6c','#303b57','rgba(255,255,255,.05)');
  pup({kind:'girl',x:380,y:G+10,s:1.3,look:[.4,.1],brows:'angry',mouth:'pout'});
  hoodieOn(380,1.3);
  pup({kind:'boy',x:770,y:G+10,s:1.25,flip:-1,look:[-.4,.2],brows:'sad',mouth:'flat'});''',
SHARE,
'''  room('#6f6a78','#5a5562','rgba(255,255,255,.05)');
  pup({kind:'girl',x:340,y:G+10,s:1.25,look:[.4,.3],brows:'sad',mouth:'flat',earLift:-.3});
  hoodieFolded(565,G+12,1.7);
  pup({kind:'boy',x:790,y:G+10,s:1.25,flip:-1,look:[-.5,.3],eyes:'wide',mouth:'o'});
  if(u>1.4)raincloudSmall(565,640,win(u,1.4,9)*.8);''',
HUG,
]
SCENES = spec(BODY_LINES, D, [{'cold':'🥶'},{'like you':'🤍'},{'again':'😇'},{'mad at you':'😤'},{'him':'💌'},{'goodbye':'💔'},{'close':'🤍'}])
IG_LINE = "The hoodie. The stealing. The keeping it after a fight. Everyone shows love their own way... Want to know yours? There's a sixty second test in our bio. Take it together."
IG_CAPS = C(IG_LINE, {'hoodie':'🧥','yours?':'🤍','bio':'🔗'})
IG_RESULT = "Physical Touch"
TT_LINE = TT_STD
