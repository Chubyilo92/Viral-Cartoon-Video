import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD, C
from _r3props import R3_PROPS
TITLE = "when a boy shows up anyway"
# Local prop: a simple side-view car (two stacked blobs for body+cab, two wheels, one headlight
# glow) plus a reused rainFall (same function as boy_always_gives_you_the_dry_half_of_the_umbrella.py,
# copied here since it's generic falling-rain and not yet promoted to a shared props file).
PRELUDE = R3_PROPS + r'''
function rainFall(u,x0,x1,n){
  ctx.save();ctx.strokeStyle='rgba(215,232,248,.72)';ctx.lineWidth=4;ctx.lineCap='round';
  for(let i=0;i<n;i++){
    const rx=x0+((i*83+u*420)%(x1-x0));
    const ry=((i*131+u*680)%1400)-220;
    ctx.beginPath();ctx.moveTo(rx,ry);ctx.lineTo(rx-18,ry+70);ctx.stroke();
  }
  ctx.restore();
}
'''
LINE_SPEED = {3: 0.75}
CAR = '''  ctx.save();ctx.translate(x,y);
  blob(rectPts(-170,-66,340,86,24),'#4a6fa5',{lw:5});
  blob(rectPts(-96,-128,192,78,20),'#4a6fa5',{lw:5});
  ctx.strokeStyle='#38507c';ctx.lineWidth=3;
  ctx.beginPath();ctx.moveTo(-70,-124);ctx.lineTo(-54,-56);ctx.moveTo(70,-124);ctx.lineTo(54,-56);ctx.stroke();
  ell(-110,16,36,36,'#2b2830',{lw:4});
  ell(110,16,36,36,'#2b2830',{lw:4});
  ell(-110,16,14,14,'#8a8f9a',{stroke:false});
  ell(110,16,14,14,'#8a8f9a',{stroke:false});
  ctx.fillStyle='#fff3c4';ctx.beginPath();ctx.ellipse(176,-22,22,15,0,0,7);ctx.fill();
  ctx.strokeStyle=INK;ctx.lineWidth=3;ctx.beginPath();ctx.ellipse(176,-22,22,15,0,0,7);ctx.stroke();
  ctx.restore();'''
BODY_LINES = [
"When a boy shows up even when it's inconvenient, he's not doing it for credit.",
"He drives forty-five minutes after a double shift because you said you had a bad day.",
"He shows up to the thing he didn't even like, just because you're in it.",
"He never once brings up what it cost him to be there.",
"If he's ever shown up when it would've been easier not to... send this to him.",
"But if you've stopped asking him to come because you already know he won't... you're not being low-maintenance. You're being let down.",
"Because a boy who shows up when it's hard... is choosing you.",
]
D = [
'''  room('#394867','#2c3652');
  pup({kind:'girl',x:320,y:G+10,s:1.25,look:[.4,-.2],eyes:'wide',mouth:'o'});
  pup({kind:'boy',x:760,y:G+10,s:1.2,flip:-1,look:[-.3,-.1],eyes:'open',mouth:'smile'});''',
'''  room('#505c74','#3f4a60',1180,'rgba(255,255,255,.05)');
  rainFall(u,640,1080,20);
  ''' + CAR.replace('x,y', '760,G-20') + '''
  pup({kind:'boy',x:360,y:G+10,s:1.2,look:[.3,-.1],eyes:'open',mouth:'flat',brows:'sad'});''',
'''  room('#cfe3ec','#98b6c2');
  pup({kind:'boy',x:760,y:G+10,s:1.2,flip:-1,eyes:'squint',mouth:'flat',look:[-.2,-.1]});
  pup({kind:'girl',x:330,y:G+10,s:1.25,eyes:'happy',mouth:'smile',blush:.2,look:[.3,-.1]});
  if(u>.4){ctx.save();ctx.globalAlpha=win(u,.4,9);bubbleText(545,560,"3 hour poetry reading",1,.68);ctx.restore();}''',
'''  room('#f1d5b0','#caa070');
  pup({kind:'boy',x:620,y:G+10,s:1.25,eyes:'happy',mouth:'smile',look:[-.1,-.1],tilt:.03});
  pup({kind:'girl',x:340,y:G+10,s:1.2,eyes:'happy',mouth:'smile',blush:.3,look:[.3,-.1]});''',
SHARE,
'''  room('#333c54','#28304a','rgba(255,255,255,.05)');
  pup({kind:'girl',x:540,y:G+10,s:1.2,look:[0,-.1],brows:'sad',mouth:'flat',shadow:false});''',
'''  room('#f1d5b0','#caa070');
  pup({kind:'girl',x:380,y:G+10,s:1.2,look:[.3,-.3],eyes:'happy',mouth:'smile',blush:.3});
  pup({kind:'boy',x:680,y:G+10,s:1.2,flip:-1,look:[-.3,-.3],eyes:'happy',mouth:'smile',blush:.3});
  sparkle(540,G-440,24,win(u,.2,3.8));
  heart(500,G-400,20,'#ec7489',1,-.1);
  if(u>.6)floatHearts(530,700,.6,u,3,130);''',
]
SCENES = spec(BODY_LINES, D, [{'credit':'🤍'},{'bad day':'🚗'},{'in it':'💛'},{'be there':'🤍'},{'to him':'💌'},{'let down':'💔'},{'choosing you':'🤍'}])
IG_LINE = "The forty-five minute drive after a double shift. The thing he didn't even like but came anyway. The cost he never once brings up. Everyone shows love their own way... Want to know yours? There's a sixty second test in our bio. Take it together."
IG_CAPS = C(IG_LINE, {'drive':'🚗','yours?':'🤍','bio':'🔗'})
IG_RESULT = "Acts of Service"
TT_LINE = TT_STD
