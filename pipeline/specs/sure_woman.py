import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD, C
TITLE = "a woman who's sure about you"
BODY_LINES = [
"A woman who's sure about you doesn't make you chase her. She just shows up.",
"She tells her friends all about you... before they've even met you.",
"She saves you a seat. At dinner. And in every plan she makes.",
"When she's upset, she tells you. No games. No making you guess.",
"If she's sure like this... send this to the man who's done chasing.",
"But if she's warm one day and cold the next... that's not mystery. That's her not being sure.",
"Because when a woman is sure about you... you never feel like you're auditioning.",
]
D = [
'''  room('#e3c9a0','#bf9670');
  blob(rectPts(760,500,240,680,16),'#b98a5e');
  const w=P(u,.3,1.6);
  pup({kind:'girl',x:lerp(900,680,w),y:G+10,s:1.3,flip:-1,look:[-.5,0],eyes:'happy',mouth:'smile',blush:.5,wag:.4});
  mug(lerp(820,560,w),1080,.9);
  pup({kind:'boy',x:320,y:G+10,s:1.3,look:[.5,0],eyes:u>1.8?'happy':'wide',mouth:'smile',blush:.4*P(u,1.8,2.4)});
  if(u>2.2)floatHearts(460,800,2.2,u,4,140);''',
'''  room('#d9b9c9','#a98496','rgba(255,255,255,.1)');
  pup({kind:'girl',x:220,y:G+10,s:.8,flip:1,look:[.6,0],eyes:'wide',mouth:'smile',blush:.4});
  pup({kind:'girl',x:860,y:G+10,s:.8,flip:-1,look:[-.6,0],eyes:'wide',mouth:'smile',blush:.4});
  pup({kind:'girl',x:540,y:G+10,s:1.35,eyes:'happy',mouth:'smile',blush:.7,wag:.5});
  if(u>.8){const k=pop(u,.8,.4);ctx.save();ctx.globalAlpha=win(u,.8,8);bubbleText(540,660,"he's the one I told you about 🥰",1,.8*k);ctx.restore();}''',
'''  room('#f1d5b0','#caa070');
  blob(rectPts(300,G-150,480,26,10),'#a58363');ell(420,G-160,60,14,'#f0e7d6',{lw:4});ell(660,G-160,60,14,'#f0e7d6',{lw:4});
  pup({kind:'girl',x:300,y:G+10,s:1.25,look:[.6,0],eyes:'happy',mouth:'smile',blush:.4,paw:{x:140,y:-40,k:Math.abs(Math.sin(u*3))}});
  const w=P(u,1.4,3.0);
  pup({kind:'boy',x:lerp(1040,780,w),y:G+10,s:1.25,flip:-1,look:[-.5,0],eyes:'happy',mouth:'smile'});
  if(u>.5){ctx.save();ctx.globalAlpha=win(u,.5,8);bubbleText(330,690,"saved you a seat 🤍",1,.8);ctx.restore();}''',
'''  room('#d9e2c8','#a9b38f');
  pup({kind:'girl',x:340,y:G+10,s:1.3,look:[.6,0],eyes:'open',mouth:'flat',brows:'sad'});
  const n=P(u,2.6,3.2);
  pup({kind:'boy',x:740,y:G+10,s:1.3,flip:-1,look:[-.6,.1+.2*Math.sin(u*8)*n],eyes:'open',mouth:'smile',tilt:-.05*n});
  if(u>.5){ctx.save();ctx.globalAlpha=win(u,.5,8);bubbleText(360,690,"that hurt. can we talk? 🫶",1,.8);ctx.restore();}''',
SHARE,
'''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  const hot=Math.floor(u/1.8)%2===0;
  pup({kind:'girl',x:700,y:G+10,s:1.3,flip:-1,look:[-.6,0],eyes:hot?'happy':'open',mouth:hot?'smile':'flat',blush:hot?.5:0,tilt:hot?-.06:.04});
  if(!hot){ctx.save();ctx.globalAlpha=.8;cloud(700,600,1.1,'#cfe0ee');ctx.restore();}else{sparkle(700,600,36,.9,'#ffd75e');}
  pup({kind:'boy',x:320,y:G+10,s:1.25,look:[.6,0],eyes:'open',mouth:'flat',brows:'sad',earLift:-.3});''',
HUG,
]
SCENES = spec(BODY_LINES, D, [{'shows up':'☕'},{'met you':'🥰'},{'makes':'🤍'},{'guess':'🫶'},{'chasing':'💌'},{'not being sure':'🚩'},{'auditioning':'🤍'}])
IG_LINE = "Showing up. Saving your seat. Telling you straight. Every woman shows love her own way... Want to know hers? There's a sixty second test in our bio. Take it together."
IG_CAPS = C(IG_LINE, {'showing up':'☕','hers?':'🤍','bio':'🔗'})
IG_RESULT = "Acts of Service"
TT_LINE = TT_STD
