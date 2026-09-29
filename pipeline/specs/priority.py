import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
import jjlib as J
from _kit import S, HUG, SHARE
TITLE = "when you're someone's priority"
BODY_LINES = [
"When you're really someone's priority... they'll reply even when they're busy. Not a paragraph. Just enough so you're not left wondering.",
"They'll remember what you had going on today... and ask how it went.",
"They'll make plans with you... not around you.",
"Being busy is real. But a priority always gets a minute.",
"If someone made you feel like this... send it to them. Say thank you.",
"But if it's always, I'll call you later... and later never comes... believe the pattern, not the promises.",
"Because when you're someone's priority... you never have to ask to be one.",
]
SCENES = [
S(["when you're really","someone's priority","they'll reply","even when","they're busy 📚","not a paragraph","just enough so","you're not left","wondering 💌"], '''  room('#e3c9a0','#bf9670');
  ell(560,G+40,460,60,'#b98a5e',{lw:5});
  for(let i=0;i<4;i++){blob(rectPts(90+i*18,G-120-i*16,150,20,4),'#fbf1e2',{lw:3.5});}
  blob(rectPts(720,G-200,200,140,10),'#fbf1e2',{lw:4});
  pup({kind:'boy',x:520,y:G+8,s:1.35,look:[.3,.4],eyes:'open',mouth:'flat',bob:Math.sin(u*3)*3,paw:{x:130,y:-30,k:.6}});
  const tx=P(u,2.2,3);phoneMock(820,G-40,.3+.04*tx,-.1,()=>{ctx.fillStyle='#eef0f5';ctx.fillRect(-70,-290,140,280);ctx.fillStyle='#ec7489';ctx.beginPath();ctx.roundRect(-58,-230,116,44,14);ctx.fill();ctx.font='bold 20px Poppins';ctx.fillStyle='#fff';ctx.textAlign='center';ctx.fillText('omw home 🐾',0,-201);});
  if(u>3)floatHearts(820,760,3,u,4,100);'''),
S(["they'll remember","what you had","going on today 💭","and ask","how it went"], '''  room('#f6d7c6','#d6a286');
  frame(150,470,190,220,(cx,cy)=>heart(cx,cy,52,'#ec7489'));
  pup({kind:'boy',x:340,y:G+10,s:1.32,look:[.7,0],eyes:'open',mouth:'smile',tilt:.05,earLift:.15});
  pup({kind:'girl',x:700,y:G+10,s:1.32,flip:-1,look:[-.6,0],eyes:u>2.6?'happy':'open',mouth:'smile',blush:.5*P(u,2.6,3.4),tilt:-.05});
  ctx.save();ctx.globalAlpha=win(u,.6,3.6);bubbleText(360,800,"how did the\\nmeeting go? 🤞".split('\\\\n').join(' '),1,.9);ctx.restore();
  if(u>3.4)floatHearts(560,780,3.4,u,4,150);'''),
S(["they'll make plans","with you 🗓️","not around you"], '''  room('#f1d5b0','#caa070');
  const k=pop(u,.2,.6);
  ctx.save();ctx.translate(540,650);ctx.scale(k,k);
  blob(rectPts(-230,-200,460,400,22),'#fffaf0',{lw:6});blob(rectPts(-230,-200,460,80,22),'#ec7489',{lw:6});
  ctx.font='bold 40px Poppins';ctx.fillStyle='#fff';ctx.textAlign='center';ctx.fillText('SATURDAY',0,-145);
  ctx.strokeStyle='#e8d9c3';ctx.lineWidth=3;for(let i=1;i<4;i++){ctx.beginPath();ctx.moveTo(-210,-100+i*60);ctx.lineTo(210,-100+i*60);ctx.stroke();}
  heart(0,20,64,'#ec7489');ctx.font='bold 34px Poppins';ctx.fillStyle=INK;ctx.fillText('you 🤍',0,120);ctx.restore();
  pup({kind:'girl',x:260,y:G+10,s:1.15,flip:-1,look:[.5,-.2],eyes:'happy',mouth:'smile',blush:.4,tilt:-.06});
  pup({kind:'boy',x:820,y:G+10,s:1.15,look:[-.5,-.2],eyes:'happy',mouth:'smile',tilt:.06});
  if(u>1.6)floatHearts(540,930,1.6,u,4,180);'''),
S(["being busy","is real 📚","but a priority","always gets","a minute ⏱️"], '''  room('#e3c9a0','#bf9670');
  ctx.save();ctx.translate(800,520);ell(0,0,90,90,'#fffaf0',{lw:6});ctx.strokeStyle=INK;ctx.lineWidth=6;ctx.lineCap='round';
  ctx.beginPath();ctx.moveTo(0,0);ctx.lineTo(Math.sin(u*2)*50,-Math.cos(u*2)*50);ctx.stroke();ctx.beginPath();ctx.moveTo(0,0);ctx.lineTo(Math.sin(u*.3)*35,-Math.cos(u*.3)*35);ctx.stroke();ctx.restore();
  ell(500,G+40,440,60,'#b98a5e',{lw:5});blob(rectPts(120,G-130,160,20,4),'#fbf1e2',{lw:3.5});
  const tp=P(u,1.4,2.2);
  pup({kind:'boy',x:500,y:G+8,s:1.35,look:[lerp(.3,0,tp),lerp(.4,.1,tp)],eyes:'open',mouth:u>2?'smile':'flat',paw:{x:130,y:-40,k:tp},tilt:.04});
  if(u>2.2){ctx.save();ctx.globalAlpha=win(u,2.2,6);ctx.font='bold 36px Poppins';ctx.textAlign='center';ctx.fillStyle='#fff8e8';ctx.strokeStyle=INK;ctx.lineWidth=6;ctx.lineJoin='round';ctx.strokeText('miss you 🤍',740,860-P(u,2.2,4)*80);ctx.fillText('miss you 🤍',740,860-P(u,2.2,4)*80);ctx.restore();floatHearts(700,900,2.4,u,4,120);}'''),
S(["if someone made","you feel like this","send it to them","say thank you 💌"], SHARE),
S(["but if it's always","\"i'll call you later\"","and later","never comes 🌙","believe the pattern","not the promises"], '''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  windowBox(620,430,320,320,()=>{const s=P(u,0,6);const g=ctx.createLinearGradient(0,430,0,750);g.addColorStop(0,s<.5?'#f6a878':'#2c3350');g.addColorStop(1,s<.5?'#f9dca8':'#4d5670');ctx.fillStyle=g;ctx.fillRect(610,420,340,340);ell(790,600,40,40,'#f3ecd0',{lw:4});});
  pup({kind:'girl',x:420,y:G+10,s:1.36,look:[.6,.5],brows:'sad',mouth:'flat',earLift:-.3,hy:6});
  phoneMock(730,1000,.4,.06,()=>{ctx.fillStyle='#2b2830';ctx.fillRect(-70,-290,140,280);});
  if(u>1.4){ctx.save();ctx.globalAlpha=win(u,1.4,4.2);bubbleText(700,860,"later 😅",1,.9);ctx.restore();}
  if(u>3.6)raincloudSmall(420,720,win(u,3.6,9));'''),
S(["because when you're","someone's priority","you never have","to ask to be one 🤍"], HUG),
]
IG_LINE = "The quick reply. The follow up. Making time. Every boy shows love in his own way... Want to know his? There's a sixty second test in our bio. Take it together... and see if he knows yours."
IG_CAPS = ["the quick reply 💌","the follow up 💭","making time ⏱️","every boy shows","love in his own way 🤍","want to know his?","60-second test","in our bio 🔗","take it together","and see if he","knows yours 💌"]
IG_RESULT = "Quality Time"
TT_LINE = "We're two little pups trying to find a thousand people who love like this... If this made you think of someone... follow us. We'll keep making them for you."
