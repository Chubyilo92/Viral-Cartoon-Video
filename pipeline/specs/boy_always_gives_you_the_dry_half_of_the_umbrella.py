import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD, C
from _r3props import R3_PROPS
TITLE = "when a boy takes the wet side"
# Local props just for this script: an umbrella (canopy shifted off its handle pivot so it
# visibly favours one side) and a bit of falling rain, plus a wet blue patch to mark a soaked
# shoulder/sleeve. Not added to the shared _r3props.py since no other script needs them yet.
PRELUDE = R3_PROPS + r'''
function brolly(px,py){
  // px,py: where the holding paw grips the handle. The pole is a STRAIGHT VERTICAL line
  // straight up from the grip -- it never strays sideways, so it can never cross a face.
  // From the pole-top, a THICK CURVED SHAFT-EXTENSION bends over to the canopy's near edge
  // -- drawn as a continuation of the pole itself (same dark colour, nearly as thick), so the
  // whole thing reads as one umbrella whose shaft bends and tilts the canopy to one side, not
  // two separate floating pieces. The open triangle below that bend, between the canopy fabric
  // and the vertical pole, is the uncovered side where rain falls through. The far (left) edge
  // reaches well past it to fully cover whoever stands further left. Coverage is unambiguous:
  // anyone whose body sits to the right of the canopy's near edge (px-200 in absolute coords)
  // is NOT covered and gets rained on; anyone left of the far edge (px-760) is fully covered.
  const ty=py-300;
  ctx.save();ctx.strokeStyle=INK;ctx.lineWidth=10;ctx.lineCap='round';
  ctx.beginPath();ctx.moveTo(px,py+16);ctx.lineTo(px,ty);ctx.stroke();
  ctx.beginPath();ctx.arc(px-22,py+22,22,Math.PI*1.1,Math.PI*2.05);ctx.stroke();
  ctx.restore();
  ctx.save();ctx.translate(px,ty);
  ctx.strokeStyle=INK;ctx.lineWidth=8;ctx.lineCap='round';
  ctx.beginPath();ctx.moveTo(0,0);ctx.quadraticCurveTo(-80,-16,-200,16);ctx.stroke();
  ctx.fillStyle='#4a6fa5';ctx.strokeStyle=INK;ctx.lineWidth=5;ctx.lineJoin='round';
  ctx.beginPath();
  ctx.moveTo(-200,16);
  ctx.quadraticCurveTo(-260,-178,-410,-200);
  ctx.quadraticCurveTo(-590,-178,-760,40);
  ctx.quadraticCurveTo(-590,6,-410,16);
  ctx.quadraticCurveTo(-280,22,-200,16);
  ctx.closePath();ctx.fill();ctx.stroke();
  ctx.strokeStyle='#38507c';ctx.lineWidth=3;
  for(const dx of [-760,-615,-470,-330,-200]){ctx.beginPath();ctx.moveTo(-390,8);ctx.lineTo(dx,dx<-470?40:16);ctx.stroke();}
  ctx.restore();
}
function rainFall(u,x0,x1,n){
  ctx.save();ctx.strokeStyle='rgba(215,232,248,.72)';ctx.lineWidth=4;ctx.lineCap='round';
  for(let i=0;i<n;i++){
    const rx=x0+((i*83+u*420)%(x1-x0));
    const ry=((i*131+u*680)%1400)-220;
    ctx.beginPath();ctx.moveTo(rx,ry);ctx.lineTo(rx-18,ry+70);ctx.stroke();
  }
  ctx.restore();
}
function wetPatch(x,y,r,a){
  ctx.save();ctx.globalAlpha=a;
  ctx.fillStyle='#2f6fae';ctx.beginPath();ctx.ellipse(x,y,r,r*.72,0,0,7);ctx.fill();
  ctx.strokeStyle='#1f5690';ctx.lineWidth=3;ctx.beginPath();ctx.ellipse(x,y,r,r*.72,0,0,7);ctx.stroke();
  ctx.strokeStyle='#2f6fae';ctx.lineWidth=4;ctx.lineCap='round';
  for(const dx of [-r*.35,0,r*.4]){ctx.beginPath();ctx.moveTo(x+dx,y+r*.5);ctx.lineTo(x+dx,y+r*1.15);ctx.stroke();}
  ctx.restore();
}
'''
LINE_SPEED = {1: 0.8, 5: 0.82}
BODY_LINES = [
"He always angles the umbrella so your shoulder stays dry and his gets soaked.",
"You've pointed it out a dozen times and he still does it.",
"By the time you get where you're going, one of his sleeves is always wet through.",
"He says he didn't notice. He notices every time.",
"Send this to whoever's shoulder is always the dry one.",
"Try to swap sides and he'll just switch hands and do it again.",
"Next time it rains, take the wet side. Just once.",
]
D = [
'''  room('#7f8fa6','#637290',1180,'rgba(255,255,255,.05)');
  rainFall(u,600,1180,22);
  pup({kind:'girl',x:360,y:G+10,s:1.2,eyes:'happy',mouth:'smile',blush:.2,look:[.3,-.1]});
  pup({kind:'boy',x:700,y:G+10,s:1.2,eyes:'open',mouth:'flat',look:[.2,-.1],paw:{x:150,y:-225,k:1}});
  brolly(880,G-270);
  wetPatch(812,1008,45,.85+Math.sin(u*6)*.06);''',
'''  room('#7f8fa6','#637290',1180,'rgba(255,255,255,.05)');
  rainFall(u,600,1180,22);
  pup({kind:'girl',x:340,y:G+10,s:1.25,eyes:'squint',mouth:'flat',look:[.3,-.1]});
  pup({kind:'boy',x:700,y:G+10,s:1.2,eyes:'happy',mouth:'smile',look:[-.2,-.1],paw:{x:150,y:-225,k:1}});
  brolly(880,G-270);
  wetPatch(812,1008,45,.85+Math.sin(u*6)*.06);
  if(u>.4){ctx.save();ctx.globalAlpha=win(u,.4,9);bubbleText(400,580,"you're getting soaked again!",1,.48);ctx.restore();}''',
'''  room('#637290','#505c74',1180,'rgba(255,255,255,.04)');
  pup({kind:'boy',x:540,y:G+10,s:1.55,eyes:'open',mouth:'flat',look:[0,-.1],paw:{x:170,y:-140,k:1}});
  wetPatch(740,G-170,46,.85+Math.sin(u*6)*.06);
  wetPatch(798,G-212,34,.8+Math.sin(u*7)*.06);
  ctx.save();ctx.translate(360,560);ctx.globalAlpha=win(u,.3,9);
  blob(rectPts(-130,-40,260,80,16),'#fffaf0',{lw:4});
  ctx.fillStyle=INK;ctx.font='bold 24px Poppins';ctx.textAlign='center';ctx.fillText('soaked through 💧',0,8);
  ctx.restore();''',
'''  room('#f1d5b0','#caa070');
  pup({kind:'boy',x:620,y:G+10,s:1.25,eyes:'squint',mouth:'smile',look:[-.1,-.1],tilt:.05});
  pup({kind:'girl',x:340,y:G+10,s:1.2,eyes:'happy',mouth:'smile',blush:.3,look:[.3,-.1]});
  if(u>.4){ctx.save();ctx.globalAlpha=win(u,.4,9);bubbleText(620,580,"didn't notice...",1,.62);ctx.restore();}''',
SHARE,
'''  room('#7f8fa6','#637290',1180,'rgba(255,255,255,.05)');
  rainFall(u,760,1180,18);
  pup({kind:'girl',x:380,y:G+10,s:1.2,eyes:'open',mouth:'o',look:[.5,-.2],paw:{x:110,y:-130,k:1}});
  pup({kind:'boy',x:740,y:G+10,s:1.2,eyes:'squint',mouth:'smile',look:[-.3,-.1],paw:{x:150,y:-265,k:1}});
  brolly(925+Math.sin(u*2.4)*10,G-270);
  wetPatch(858,1018,42,.85+Math.sin(u*6)*.06);
  ctx.save();ctx.translate(560,680);ctx.globalAlpha=win(u,.5,9);
  blob(rectPts(-150,-34,300,68,14),'#fffaf0',{lw:4});
  ctx.fillStyle=INK;ctx.font='bold 21px Poppins';ctx.textAlign='center';ctx.fillText('switched hands 🔄',0,7);
  ctx.restore();''',
'''  room('#7f8fa6','#637290',1180,'rgba(255,255,255,.05)');
  rainFall(u,600,1180,22);
  pup({kind:'boy',x:360,y:G+10,s:1.2,eyes:'happy',mouth:'smile',blush:.2,look:[.3,-.1]});
  pup({kind:'girl',x:700,y:G+10,s:1.2,eyes:'happy',mouth:'smile',blush:.4,look:[-.2,-.1],paw:{x:150,y:-225,k:1}});
  brolly(880,G-270);
  wetPatch(812,1008,45,.85+Math.sin(u*6)*.06);
  if(u>1.2)floatHearts(540,760,1.2,u,4,150);''',
]
SCENES = spec(BODY_LINES, D, [{'soaked':'☔'},{'does it':'🙄'},{'wet through':'💧'},{'every time':'😏'},{'dry one':'💌'},{'again':'😅'},{'just once':'🤍'}])
IG_LINE = "The umbrella he always tilts your way. The sleeve that's always soaked. The one time he'll actually let you take it. Everyone shows love their own way... Want to know yours? There's a sixty second test in our bio. Take it together."
IG_CAPS = C(IG_LINE, {'your way':'☔','yours?':'🤍','bio':'🔗'})
IG_RESULT = "Acts of Service"
TT_LINE = TT_STD
