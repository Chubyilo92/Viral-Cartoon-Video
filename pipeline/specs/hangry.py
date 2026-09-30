import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
import jjlib as J
from _kit import S, HUG, SHARE
TITLE = "when she's hangry but loves you"
BODY_LINES = [
"When she's tired or hangry... but still loves you... she'll snap about the dishes, not because of the dishes. Feed her first.",
"She'll go quiet in the car and stare out the window. It's not you, it's the day, stacked on the day before it.",
"She'll say, I'm fine, in a tone that means the opposite... but still reach for your hand at the same time.",
"She doesn't need advice. She needs a snack, a blanket, and ten minutes without being asked if she's okay.",
"If you've been handed the feed her warning by someone who loves her... send this to him.",
"But if you take the snapping personally every time... you'll turn a bad day into a bad week.",
"Because the girl who's exhausted and still shows up for you... is showing you her love on its worst day.",
]
SCENES = [
S(["when she's tired","or hangry 😤","but still","loves you","she'll snap","about the dishes","that have nothing","to do with","the dishes 🍽️","feed her before","you respond 🚨"], '''  room('#f6d7c6','#d6a286');
  dishPile(760,G-10,.7);
  pup({kind:'girl',x:400,y:G+10,s:1.34,look:[.4,0],mouth:'pout',brows:'sad',blush:.2,tilt:-.05,earLift:-.1});
  if(u>1.2&&u<5.4){ctx.save();ctx.globalAlpha=win(u,1.2,5.4);bubbleText(400,800,"whose turn was it?! 😤",1,.9);ctx.restore();}
  if(u>6){ctx.save();ctx.globalAlpha=win(u,6,10);ctx.font='bold 30px Poppins';ctx.textAlign='center';ctx.fillStyle='#ec7489';ctx.strokeStyle='#fff';ctx.lineWidth=5;ctx.strokeText('🚨 FEED HER FIRST 🚨',700,500);ctx.fillText('🚨 FEED HER FIRST 🚨',700,500);ctx.restore();}'''),
S(["she'll go quiet","in the car 🚗","and stare","out the window","it's not you","it's the day","stacked on the","day before it","finally","catching up"], '''  room('#e3c9a0','#bf9670');
  windowBox(600,440,320,280,()=>{const g=ctx.createLinearGradient(0,440,0,720);g.addColorStop(0,'#8ea7c9');g.addColorStop(1,'#c7d6e6');ctx.fillStyle=g;ctx.fillRect(590,430,340,300);});
  pup({kind:'girl',x:700,y:G+10,s:1.3,flip:-1,look:[-.7,-.1],mouth:'flat',brows:'sad',blush:.1,hy:4});
  if(u>2.6)raincloudSmall(700,720,win(u,2.6,8)*.4);'''),
S(["she'll say","\"i'm fine\" 🙂","in a tone that","means the opposite","but she'll","still reach","for your hand","at the","same time 🤍"], '''  room('#f1d5b0','#caa070');
  pup({kind:'girl',x:620,y:G+10,s:1.36,flip:-1,look:[-.2,.1],mouth:'flat',brows:'sad',blush:.2,tilt:.02});
  pup({kind:'boy',x:340,y:G+10,s:1.3,look:[.5,0],eyes:'open',mouth:'flat',earLift:-.1,paw:{x:150,y:-20,k:P(u,2,3)}});
  if(u>.6&&u<3.4){ctx.save();ctx.globalAlpha=win(u,.6,3.4);bubbleText(620,820,"i'm fine 🙂",1,.9);ctx.restore();}
  if(u>3.6)floatHearts(480,850,3.6,u,3,140);'''),
S(["she doesn't","need advice 🙅","she needs a snack 🍪","a blanket","and you to","stop asking","if she's okay","for exactly","ten minutes ⏱️"], '''  room('#f6d7c6','#d6a286');
  bowl(760,G-10,true);
  const k=pop(u,.3,.6);ctx.save();ctx.translate(360,700);ctx.scale(k,k);blob(rectPts(-90,-50,180,100,18),'#e8d9c3',{lw:4});ctx.restore();
  pup({kind:'girl',x:360,y:G+30,s:1.3,look:[.3,-.1],eyes:'closed',mouth:'flat',breath:1,tilt:-.03});'''),
S(["if you've been","handed the","\"feed her\"","warning 🚨","by someone","who loves her","send this","to him 💌"], SHARE),
S(["but if you","take the snapping","personally","every single time 🌧️","you'll turn","a bad day","into a","bad week"], '''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  pup({kind:'girl',x:340,y:G+10,s:1.3,flip:-1,look:[.5,.4],brows:'sad',mouth:'flat',hy:4});
  pup({kind:'boy',x:740,y:G+10,s:1.2,look:[-.3,.3],eyes:'open',mouth:'flat',brows:'sad',hy:6});
  if(u>1.4)raincloudSmall(340,720,win(u,1.4,8));'''),
S(["because the girl","who's exhausted","and still shows","up for you 🤍","is showing you","what her love","looks like on","its worst day"], HUG),
]
IG_LINE = "The snapping that isn't about dishes. The quiet car ride. Reaching for your hand anyway... want to know how she loves? Test in our bio... see if he knows yours."
IG_CAPS = ["the snapping that","isn't about the dishes","the quiet car ride","reaching for your","hand anyway 🤍","want to know hers?","60-second test","in our bio 🔗","take it together","and see if he","knows yours 💌"]
IG_RESULT = "Physical Touch"
TT_LINE = "We're two little pups trying to find a thousand people who love like this... If this made you think of someone... follow us. We'll keep making them for you."
