import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
import jjlib as J
from _kit import S, HUG, SHARE
TITLE = "when an overthinker loves you"
BODY_LINES = [
"When an overthinker loves you... they'll reread your text three times before replying. They're not playing games. They're terrified of getting it wrong.",
"They'll ask, are you sure you're not mad at me, out of nowhere. Their mind invents ten reasons before you're even up.",
"They'll apologize for things that were never their fault. It's a habit built from bracing for a blow that hasn't come yet.",
"They need you to say it out loud, even when it's obvious. Their brain needs the proof their heart already has.",
"If you're the one who reads too far into everything... send this to the one who never makes you feel crazy for it.",
"But if you roll your eyes at the reassurance... they'll learn to stop asking, and start assuming the worst instead.",
"Because when an overthinker chooses to trust you anyway... they've quieted a whole war just to be with you.",
]
SCENES = [
S(["when an overthinker","loves you 💭","they'll reread","your text","three times","before replying","not because","they're playing games","they're terrified","of saying the wrong","thing to the","right person 🤍"], '''  room('#f1d5b0','#caa070');
  phoneMock(540,780,.72,-.02,()=>{ctx.fillStyle='#eef0f5';ctx.fillRect(-70,-290,140,280);ctx.fillStyle='#ec7489';ctx.beginPath();ctx.roundRect(-58,-230,116,40,14);ctx.fill();ctx.font='13px Poppins';ctx.fillStyle='#fff';ctx.textAlign='center';ctx.fillText('hey, you free',0,-206);});
  const bl=Math.sin(u*8)>0.2&&u>.6&&u<3.4;
  if(bl){ctx.save();ctx.globalAlpha=.9;ctx.translate(720,560);note(0,0,.6,1);ctx.restore();}
  pup({kind:'girl',x:300,y:G+10,s:1.3,flip:-1,look:[.6,-.1],eyes:'open',mouth:'flat',blush:.1,tilt:-.08,bob:Math.sin(u*6)*2});
  if(u>2.2){ctx.save();ctx.globalAlpha=win(u,2.2,7);ctx.font='30px Poppins';ctx.textAlign='center';ctx.fillStyle=INK;ctx.strokeStyle='#fffaf0';ctx.lineWidth=6;ctx.strokeText('💭 wait is that too much?',720,540);ctx.fillText('💭 wait is that too much?',720,540);ctx.restore();}'''),
S(["they'll ask","\"are you sure","you're not","mad at me?\" 🥺","out of nowhere","not because","you gave a reason","their mind invents","ten before","you're even up"], '''  room('#e3c9a0','#bf9670');
  frame(150,470,190,220,(cx,cy)=>heart(cx,cy,52,'#ec7489'));
  pup({kind:'girl',x:680,y:G+10,s:1.32,flip:-1,look:[-.3,.2],mouth:'flat',brows:'sad',blush:.1,tilt:-.05});
  pup({kind:'boy',x:340,y:G+10,s:1.3,look:[.7,0],eyes:u<3?'wide':'open',mouth:'flat',earLift:-.1});
  if(u>.6&&u<4){ctx.save();ctx.globalAlpha=win(u,.6,4);bubbleText(680,800,"are you mad at me? 🥺",1,.9);ctx.restore();}
  if(u>4.4){ctx.save();ctx.globalAlpha=win(u,4.4,9);ctx.font='24px Poppins';ctx.textAlign='center';ctx.fillStyle=INK;for(let i=0;i<3;i++){ctx.save();ctx.translate(300+i*90,470-i*20);ctx.font='22px Poppins';ctx.fillText('❓',0,0);ctx.restore();}ctx.restore();}'''),
S(["they'll apologize","for things","that were never","their fault","it's not weakness","it's a habit","built from bracing","for a blow","that hasn't come","yet 🩹"], '''  room('#f6d7c6','#d6a286');
  ell(560,G+40,460,60,'#c98f76');
  pup({kind:'girl',x:540,y:G+10,s:1.4,look:[0,.3],mouth:'flat',brows:'sad',earLift:-.3,hy:6,blush:.1});
  if(u>.6&&u<3.6){ctx.save();ctx.globalAlpha=win(u,.6,3.6);bubbleText(540,800,"sorry, my bad 😔",1,.9);ctx.restore();}
  if(u>4){ctx.save();ctx.globalAlpha=win(u,4,9);ctx.translate(540,540);ctx.rotate(-.05);blob(rectPts(-160,-40,320,80,14),'#fbf1e2',{lw:4});ctx.font='20px Poppins';ctx.fillStyle=INK;ctx.textAlign='center';ctx.fillText('(it genuinely wasn\\'t)',0,6);ctx.restore();}'''),
S(["they need you","to say it","out loud 🗣️","even when","it's obvious","not because","they doubt you","because their brain","needs the proof","their heart already has 🤍"], '''  room('#f1d5b0','#caa070');
  const k=pop(u,.2,.5);
  pup({kind:'boy',x:360,y:G+10,s:1.34,look:[.4,.1],eyes:'happy',mouth:'smile',tilt:.06,earLift:.1});
  pup({kind:'girl',x:700,y:G+10,s:1.34,flip:-1,look:[-.4,.1],eyes:u>2?'happy':'open',mouth:'smile',blush:.4*P(u,2,3),tilt:-.06});
  if(u>1.4){ctx.save();ctx.globalAlpha=win(u,1.4,7);bubbleText(360,820,"i love you, you know that right?",1,.85);ctx.restore();}
  if(u>4)floatHearts(700,860,4,u,4,140);'''),
S(["if you're the one","who reads too far","into everything","send this to","the one who","never makes you","feel crazy for it 💌"], SHARE),
S(["but if you","roll your eyes","at the reassurance","they'll learn","to stop asking","and start","assuming the worst","instead 🌧️"], '''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  windowBox(610,440,300,300,()=>{ctx.fillStyle='#4d5670';ctx.fillRect(600,430,320,320);ell(820,540,26,26,'#d9d5c4',{lw:4});});
  pup({kind:'girl',x:700,y:G+10,s:1.34,flip:1,look:[.5,.4],brows:'sad',mouth:'flat',earLift:-.4,hy:6});
  const sh=P(u,.6,1.6);
  pup({kind:'boy',x:300,y:G+10,s:1.2,look:[.3,-.2],eyes:'open',mouth:'flat',tilt:-sh*.1});
  if(u>1)raincloudSmall(700,730,win(u,1,7));'''),
S(["because when","an overthinker","chooses to","trust you anyway","they've quieted","a whole war","just to be","with you 🤍"], HUG),
]
IG_LINE = "The reread texts. The out-of-nowhere are-you-mad. The quiet apologies. Every overthinker shows love in her own way... want to know yours? Sixty second test in our bio... see if he knows yours."
IG_CAPS = ["the reread texts 💭","the out-of-nowhere","\"are you mad?\" 🥺","the quiet apologies","every overthinker shows","love in her own way 🤍","want to know yours?","60-second test","in our bio 🔗","take it together","and see if he","knows yours 💌"]
IG_RESULT = "Words of Affirmation"
TT_LINE = "We're two little pups trying to find a thousand people who love like this... If this made you think of someone... follow us. We'll keep making them for you."
