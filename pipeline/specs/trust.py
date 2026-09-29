import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
import jjlib as J
from _kit import S, HUG, SHARE
TITLE = "when a hurt girl loves you"
BODY_LINES = [
"When a girl who's been hurt loves you... she'll ask the same question twice. Not because she thinks you're lying. It's because the last one did.",
"She'll go quiet when your plans change. Not to control you. She's just learning that change doesn't mean leaving.",
"She'll say, it's okay, when it isn't... because she's scared of being too much.",
"Be patient with her. She's not testing you... she's healing.",
"If you're the one who's been hurt... send this to the one who stayed.",
"But if you use her past against her... you become one more reason she can't trust.",
"Because when a hurt girl chooses to trust you... it's the bravest thing she'll ever do.",
]
SCENES = [
S(["when a girl","who's been hurt 🩹","loves you","she'll ask","the same question","twice","not because","she thinks you're lying","it's because","the last one did 💔"], '''  room('#f3cfa8','#d09d72');
  windowBox(620,430,320,320,()=>{const g=ctx.createLinearGradient(0,430,0,750);g.addColorStop(0,'#f6a878');g.addColorStop(1,'#f9dca8');ctx.fillStyle=g;ctx.fillRect(610,420,340,340);ell(790,690,58,58,'#fbe7a6',{lw:4});});
  frame(140,470,200,240,(cx,cy)=>heart(cx,cy,58,'#ec7489'));
  pup({kind:'girl',x:640,y:G+10,s:1.36,flip:-1,look:[-.5,.1],mouth:'flat',brows:'sad',blush:.1,tilt:-.05});
  pup({kind:'boy',x:340,y:G+10,s:1.36,look:[.6,0],eyes:'open',mouth:'smile',tilt:.04});
  if(u>.8&&u<3.2){ctx.save();ctx.globalAlpha=win(u,.8,3.2);bubbleText(640,830,"you'll be home at 6?",1,.85);ctx.restore();}
  if(u>3.6&&u<6.2){ctx.save();ctx.globalAlpha=win(u,3.6,6.2);bubbleText(640,830,"...at 6, right?",1,.85);ctx.restore();}
  if(u>6.6)raincloudSmall(700,760,win(u,6.6,12));'''),
S(["she'll go quiet","when your plans change","not to","control you","she's learning","change doesn't","mean leaving 🚪"], '''  room('#e3c9a0','#bf9670');
  blob(rectPts(90,560,190,620,14),'#a9774f');blob(rectPts(112,584,146,596,10),'#f0dcae',{stroke:false});
  ell(690,G+30,300,70,'#c98f76');ell(690,G+8,240,44,'#f2dcc4',{lw:4});
  pup({kind:'girl',x:700,y:G+10,s:1.3,look:[-.9,0],mouth:'flat',brows:'sad',blush:.1,tilt:-.05});
  const out=P(u,.8,2.2),back=P(u,3.4,5);const bx=lerp(190,540,back)+(-140)*out+ (out>=1&&back<=0?-999:0);
  const vis=(u<2.4)||(u>3.4);
  if(vis)pup({kind:'boy',x:u<2.4?lerp(320,190,out):lerp(190,420,back),y:G+10,s:1.2,flip:u<2.4?1:-1,eyes:'open',mouth:'smile',bob:(u>3.4&&u<5)?-Math.abs(Math.sin(u*9))*10:0});
  if(u>5.2){floatHearts(600,880,5.2,u,4,100);}'''),
S(["she'll say","\"it's okay\" 🙂","when it isn't","because she's scared","of being","too much 🥺"], '''  room('#f6d7c6','#d6a286');
  frame(150,470,190,220,(cx,cy)=>{ell(cx-24,cy,24,24,'#f3e2c8');ell(cx+24,cy,24,24,'#dca46a');});
  pup({kind:'girl',x:620,y:G+10,s:1.4,flip:-1,look:[-.3,.2],mouth:'smile',brows:'sad',blush:.2,tilt:.04});
  pup({kind:'boy',x:320,y:G+10,s:1.3,look:[.7,0],eyes:'open',mouth:'flat',earLift:-.15});
  if(u>.6){ctx.save();ctx.globalAlpha=win(u,.6,4.2);bubbleText(640,820,"it's okay 🙂",1,.95);ctx.restore();}
  if(u>3.4){ctx.save();ctx.globalAlpha=win(u,3.4,8)*.85;ctx.font='38px Poppins';ctx.textAlign='center';ctx.fillStyle=INK;ctx.strokeStyle='#fffaf0';ctx.lineWidth=6;ctx.strokeText('💭 "i\\'m too much"',700,700);ctx.fillText('💭 "i\\'m too much"',700,700);ctx.restore();}'''),
S(["be patient","with her 🤍","she's not","testing you","she's healing 🩹"], '''  room('#f1d5b0','#caa070');
  const b=pop(u,.2,.6);
  ctx.save();ctx.translate(540,690);ctx.scale(b,b);heart(0,0,150,'#ec7489');
  const pk=P(u,1.4,2.4);ctx.save();ctx.rotate(-.5);ctx.globalAlpha=pk;blob(rectPts(-95,-22,190,44,14),'#f2cf9e',{lw:5});ctx.fillStyle='#d9b27a';for(let i=0;i<4;i++)ctx.fillRect(-40+i*24,-6,8,8);ctx.restore();ctx.restore();
  pup({kind:'girl',x:340,y:G+10,s:1.25,flip:-1,look:[.5,-.1],eyes:'happy',mouth:'smile',blush:.3,tilt:-.07});
  pup({kind:'boy',x:740,y:G+10,s:1.25,look:[-.5,-.1],eyes:'happy',mouth:'smile',tilt:.07,earLift:.1});
  if(u>2.4)floatHearts(540,900,2.4,u,4,150);'''),
S(["if you're the one","who's been hurt 🩹","send this to","the one who","stayed 💌"], SHARE),
S(["but if you use","her past","against her","you become one","more reason","she can't trust"], '''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  windowBox(610,440,300,300,()=>{ctx.fillStyle='#4d5670';ctx.fillRect(600,430,320,320);ell(820,540,26,26,'#d9d5c4',{lw:4});});
  pup({kind:'girl',x:700,y:G+10,s:1.36,flip:1,look:[.6,.5],brows:'sad',mouth:'flat',earLift:-.4,hy:6});
  pup({kind:'boy',x:280,y:G+10,s:1.3,look:[-.3,.6],eyes:'open',mouth:'flat',brows:'sad',earLift:-.3,hy:8});
  if(u>1){ctx.save();ctx.globalAlpha=win(u,1,6.2);ctx.translate(470,700);ctx.rotate(.08);blob(rectPts(-110,-45,220,90,12),'#fbf1e2',{lw:4});ctx.font='bold 28px Poppins';ctx.textAlign='center';ctx.fillStyle=INK;ctx.fillText('"remember when...',0,-4);ctx.fillText('you said..."',0,28);ctx.restore();}
  if(u>2)raincloudSmall(700,730,win(u,2,7));'''),
S(["because when a","hurt girl chooses","to trust you","it's the bravest","thing she'll","ever do 🤍"], '''  room('#f1d5b0','#caa070');plant(970,G+6,.9);
  const st=P(u,.4,1.6);
  pup({kind:'girl',x:lerp(600,520,st),y:G+10,s:1.34,flip:-1,look:[-.3,.2],eyes:u>1.4?'closed':'open',mouth:'smile',tilt:lerp(0,-.14,st),blush:.5});
  pup({kind:'boy',x:lerp(340,420,st),y:G+10,s:1.34,look:[.4,.1],eyes:'happy',mouth:'smile',tilt:.06,blush:.3,earLift:.1});
  const fl=P(u,1.6,4);ctx.save();ctx.globalAlpha=1-fl;ctx.translate(500+fl*300,560+fl*560);ctx.rotate(-.5+fl*1.6);blob(rectPts(-60,-14,120,28,10),'#f2cf9e',{lw:4});ctx.restore();
  if(u>1.6)floatHearts(470,800,1.6,u,6,150);sparkle(470,700,44*pop(u,1.8,.5),win(u,1.8,6));'''),
]
IG_LINE = "The questions twice. The quiet. The it's okay. Every girl who's been hurt shows love in her own way... Want to know hers? There's a sixty second test in our bio. Take it together... and see if he knows yours."
IG_CAPS = ["the questions","asked twice 💭","the quiet 🤫","the \"it's okay\" 🩹","every girl shows","love in her own way 🤍","want to know hers?","60-second test","in our bio 🔗","take it together","and see if he","knows yours 💌"]
IG_RESULT = "Words of Affirmation"
TT_LINE = "We're two little pups trying to find a thousand people who love like this... If this made you think of someone... follow us. We'll keep making them for you."
