import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
import jjlib as J
from _kit import S, HUG, SHARE

# --- CoupleIn ad: "the fight you keep having" -----------------------------
# Angle: painkiller, not vitamin. Opens on the ache of a recurring, never-
# actually-resolved fight, escalates it, then reframes it as a five-minute
# fix rather than a character flaw, and closes on a direct app-download CTA
# (not the usual quiz/follow-counter ending -- this is an ad, not organic
# JJ content, so both platform cuts share the same body and end card).

TITLE = "the fight you keep having"

PRELUDE = '''
function adTag(){ctx.save();ctx.setTransform(1,0,0,1,0,0);ctx.font='bold 20px Poppins';ctx.fillStyle='rgba(255,255,255,.92)';ctx.strokeStyle=INK;ctx.lineWidth=3;ctx.beginPath();ctx.roundRect(898,40,162,44,22);ctx.fill();ctx.stroke();ctx.fillStyle=INK;ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText('Ad \\u00b7 CoupleIn',979,64);ctx.restore();}
function appBadge(x,y,w,sub,label){ctx.save();blob(rectPts(x,y,w,66,14),'#232025',{stroke:false});ctx.fillStyle='#fff';ctx.textAlign='left';ctx.font='11px Poppins';ctx.fillText(sub,x+16,y+24);ctx.font='bold 20px Poppins';ctx.fillText(label,x+16,y+48);ctx.restore();}
'''

BODY_LINES = [
"Still having the same fight? You know the one. It starts over the dishes, but it's never really about the dishes.",
"You go quiet. They go quiet. You both go to bed angry, and \"fine\" in the morning is just the fight on pause.",
"By the fifth time, you're not fighting about tonight anymore. You're fighting about the last ten times too.",
"That's not a communication problem. That's two people who need five minutes, not another apology that doesn't stick.",
"CoupleIn's five-minute fight fix asks the one question that actually gets you both talking. No yelling, no silent treatment.",
"Same fight. Five minutes. Actually resolved, not shelved for next week.",
"Because the couples who stop repeating the fight... are the ones who stopped avoiding it.",
]
END_LINE = "Download CoupleIn free. Fix tonight's fight instead of carrying it into tomorrow's. Link in bio."

SCENES = [
S(["still having","the same fight? 😤","you know the one","it starts over","the dishes","but it's never","really about","the dishes"], '''  adTag();room('#e3c9a0','#bf9670');
  dishPile(760,G-10,.85);
  pup({kind:'girl',x:360,y:G+10,s:1.32,look:[.4,0],mouth:'pout',brows:'sad',blush:.2,tilt:-.05});
  pup({kind:'boy',x:680,y:G+10,s:1.28,flip:-1,look:[-.4,0],mouth:'flat',brows:'sad',tilt:.04});
  if(u>1&&u<5){ctx.save();ctx.globalAlpha=win(u,1,5);bubbleText(360,800,"here we go again 😤",1,.85);ctx.restore();}'''),
S(["you go quiet 🤐","they go quiet","you both go","to bed angry","and \"fine\" 🙂","in the morning","is just the","fight on pause"], '''  adTag();room('#3d4b6c','#303b57','rgba(255,255,255,.05)');
  windowBox(610,440,300,300,()=>{ctx.fillStyle='#242c44';ctx.fillRect(600,430,320,320);ell(820,540,20,20,'#d9d5c4',{lw:4});});
  pup({kind:'girl',x:700,y:G+10,s:1.24,flip:1,look:[.5,.4],brows:'sad',mouth:'flat',earLift:-.3,hy:6});
  pup({kind:'boy',x:300,y:G+10,s:1.2,look:[-.3,.4],eyes:'open',mouth:'flat',brows:'sad',earLift:-.3,hy:6});
  if(u>2.6){ctx.save();ctx.globalAlpha=win(u,2.6,7);bubbleText(700,760,"fine 🙂",1,.85);ctx.restore();}'''),
S(["by the","fifth time","you're not fighting","about tonight","anymore","you're fighting","about the last","ten times too"], '''  adTag();room('#f6d7c6','#d6a286');
  ctx.save();ctx.translate(700,560);blob(rectPts(-130,-80,260,160,12),'#fbf1e2',{lw:4});
  ctx.strokeStyle=INK;ctx.lineWidth=6;ctx.lineCap='round';
  for(let i=0;i<Math.min(5,Math.floor(u*1.1));i++){ctx.beginPath();ctx.moveTo(-95+i*36,-40);ctx.lineTo(-95+i*36,40);ctx.stroke();}
  if(Math.floor(u*1.1)>=5){ctx.beginPath();ctx.moveTo(-95,40);ctx.lineTo(85,-40);ctx.stroke();}
  ctx.restore();
  pup({kind:'girl',x:320,y:G+10,s:1.24,flip:-1,look:[.5,.2],mouth:'flat',brows:'sad',blush:.1,tilt:-.04});'''),
S(["that's not a","communication problem","that's two people","who need","five minutes 🕐","not another","apology that","doesn't stick"], '''  adTag();room('#f1d5b0','#caa070');
  ctx.save();ctx.translate(760,650);heart(0,0,70,'#d9b0a0');ctx.strokeStyle=INK;ctx.lineWidth=5;ctx.beginPath();ctx.moveTo(-40,10);ctx.lineTo(40,-10);ctx.stroke();ctx.restore();
  pup({kind:'boy',x:340,y:G+10,s:1.3,look:[.4,.1],eyes:'open',mouth:'flat',earLift:-.05,paw:{x:110,y:-20,k:.5}});
  pup({kind:'girl',x:640,y:G+10,s:1.26,flip:-1,look:[-.4,.1],mouth:'flat',brows:'sad',blush:.1,tilt:-.03});'''),
S(["CoupleIn's","five-minute","fight fix 💗","asks the one","question that","actually gets","you both talking","no yelling,","no silent treatment"], '''  adTag();room('#fbdfe4','#f3b8c6',1180,'rgba(255,255,255,.18)');
  const rise=pop(u,.4,.5);
  pup({kind:'girl',x:340,y:G+30,s:1.05,flip:-1,eyes:'open',mouth:'flat',tilt:-.04,shadow:false});
  pup({kind:'boy',x:600,y:G+30,s:1.05,eyes:'open',mouth:'flat',tilt:.04,shadow:false});
  phoneMock(770,900-rise*30,.66+.04*rise,-.03,()=>{
    const g=ctx.createLinearGradient(0,-290,0,-10);g.addColorStop(0,'#fff5f8');g.addColorStop(1,'#ffe3ec');ctx.fillStyle=g;ctx.fillRect(-70,-290,140,280);
    heart(-42,-256,12,'#ff6b9d');ctx.font='bold 13px Poppins';ctx.fillStyle=INK;ctx.textAlign='left';ctx.fillText('CoupleIn',-26,-254);
    ctx.font='bold 15px Poppins';ctx.textAlign='center';ctx.fillText('how are you really',0,-190);ctx.fillText('feeling right now?',0,-172);
    ctx.strokeStyle='#ff6b9d';ctx.lineWidth=2.5;ctx.beginPath();ctx.roundRect(-52,-140,104,32,16);ctx.stroke();ctx.font='12px Poppins';ctx.fillText('😤 frustrated',0,-124);
    ctx.strokeStyle='#ff6b9d';ctx.beginPath();ctx.roundRect(-52,-98,104,32,16);ctx.stroke();ctx.fillText('😔 hurt',0,-82);
    ctx.fillStyle='#f3c3d0';for(let i=0;i<5;i++){ctx.beginPath();ctx.arc(-24+i*12,-40,i==1?4:3,0,7);ctx.fill();}
  });
  if(u>2.4)floatHearts(770,760,2.4,u,3,110);'''),
S(["same fight","five minutes 🕐","actually resolved","not shelved","for next week 📅"], '''  adTag();room('#fbdfe4','#f3b8c6',1180,'rgba(255,255,255,.18)');
  pup({kind:'girl',x:400,y:G+10,s:1.3,flip:-1,eyes:'happy',mouth:'smile',blush:.4,tilt:-.06});
  pup({kind:'boy',x:680,y:G+10,s:1.3,eyes:'happy',mouth:'smile',blush:.3,tilt:.06});
  phoneMock(540,760,.5,0,()=>{ctx.fillStyle='#fff5f8';ctx.fillRect(-70,-290,140,280);ctx.font='bold 40px Poppins';ctx.textAlign='center';ctx.fillStyle='#3fae6a';ctx.fillText('✅',0,-150);ctx.font='bold 14px Poppins';ctx.fillStyle=INK;ctx.fillText('resolved',0,-110);});
  if(u>1.6)floatHearts(540,880,1.6,u,5,160);'''),
S(["because the couples","who stop repeating","the fight 🤍","are the ones","who stopped","avoiding it"], '''  adTag();''' + HUG),
]

END_SCENE_JS = S(
    ["download","CoupleIn","free 💗","fix tonight's fight","instead of carrying","it into","tomorrow's","link in bio 🔗"],
    '''  room('#fbdfe4','#f3b8c6',1180,'rgba(255,255,255,.18)');
  pup({kind:'girl',x:340,y:G+40,s:1.02,flip:-1,eyes:'happy',mouth:'smile',blush:.4,tilt:-.05,shadow:false,wag:.3});
  pup({kind:'boy',x:600,y:G+40,s:1.02,eyes:'happy',mouth:'smile',blush:.3,tilt:.05,shadow:false,wag:.3});
  const rise=pop(u,.4,.5);
  phoneMock(770,910-rise*30,.72+.05*rise,-.03,()=>{
    const g=ctx.createLinearGradient(0,-290,0,-10);g.addColorStop(0,'#fff5f8');g.addColorStop(1,'#ffe3ec');ctx.fillStyle=g;ctx.fillRect(-70,-290,140,280);
    heart(0,-220,34,'#ff6b9d');
    ctx.font='bold 20px Poppins';ctx.fillStyle=INK;ctx.textAlign='center';ctx.fillText('CoupleIn',0,-160);
    ctx.font='13px Poppins';ctx.fillText('5-minute fight fix',0,-138);
    ctx.strokeStyle='#ff6b9d';ctx.lineWidth=3;ctx.beginPath();ctx.roundRect(-46,-108,92,30,15);ctx.stroke();ctx.font='bold 13px Poppins';ctx.fillText('start free ✨',0,-89);
  });
  appBadge(150,1360,300,'Download on the','App Store');
  appBadge(150,1440,300,'GET IT ON','Google Play');
  if(u>1.2){ctx.save();ctx.globalAlpha=win(u,1.2,7);ctx.font='bold 36px Poppins';ctx.textAlign='center';ctx.fillStyle='#fff8e8';ctx.strokeStyle=INK;ctx.lineWidth=6;ctx.lineJoin='round';ctx.strokeText('🔗 CoupleIn - link in bio',540,1250);ctx.fillText('🔗 CoupleIn - link in bio',540,1250);ctx.restore();}
  adTag();'''
)
