import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
import jjlib as J
from _kit import S, HUG, SHARE
TITLE = "when they downplay their wins"
BODY_LINES = [
"When someone who downplays their wins loves you... they'll get the good news and say \"it's not a big deal\" before you can even hug them.",
"Not because they don't care — admitting it matters has always felt like bragging to them.",
"They'll change the subject the second you start bragging about them to someone else.",
"They'll light up for a full minute when you remember a win they'd already forgotten they told you about.",
"If you've learned to celebrate loud enough for both of you... send this to them, right now.",
"But if every win gets brushed off until it stops feeling like one at all... that's worth naming, gently.",
"Because someone who can't celebrate themselves but keeps trying anyway... just needs you to believe it first.",
]
SCENES = [
S(["when they","downplay their wins 🏆","they'll get","the good news","and say 'it's not","a big deal' 😅"], '''  room('#f1d5b0','#caa070');
  phoneMock(730,780,.62,-.04,()=>{ctx.fillStyle='#eef7ef';ctx.fillRect(-70,-290,140,280);ctx.font='16px Poppins';ctx.fillStyle=INK;ctx.textAlign='center';ctx.fillText('YOU GOT IT!! 🎉',0,-150);});
  pup({kind:'boy',x:340,y:G+10,s:1.26,look:[.3,0],mouth:'flat',earLift:-.1,hy:4});
  if(u>.6&&u<5){ctx.save();ctx.globalAlpha=win(u,.6,5);bubbleText(360,620,"it's not a big deal",1,.6);ctx.restore();}'''),
S(["not because","they don't care 🤍","admitting it matters","has always felt","like bragging","to them"], '''  room('#e3c9a0','#bf9670');
  pup({kind:'boy',x:540,y:G+10,s:1.34,look:[0,.1],brows:'sad',mouth:'flat',hy:4});'''),
S(["they'll change","the subject 🙈","the second you","start bragging","about them to","someone else"], '''  room('#f6d7c6','#d6a286');
  phoneMock(330,780,.6,.05,()=>{ctx.fillStyle='#eef0f5';ctx.fillRect(-70,-290,140,280);ctx.font='13px Poppins';ctx.fillStyle=INK;ctx.textAlign='center';ctx.fillText("he's SO talented",0,-150);});
  pup({kind:'boy',x:720,y:G+10,s:1.24,flip:-1,look:[-.3,.2],mouth:'flat',earLift:-.1,hy:4,blush:.3});'''),
S(["they'll light up","for a full minute 🤍","when you remember","a win they'd","already forgotten","they told you about"], '''  room('#f1d5b0','#caa070');
  pup({kind:'girl',x:700,y:G+10,s:1.26,flip:-1,eyes:'happy',mouth:'smile',blush:.3});
  pup({kind:'boy',x:400,y:G+10,s:1.3,look:[.3,0],eyes:'happy',mouth:'open',blush:.5,earLift:.1});
  if(u>1.6)floatHearts(540,860,1.6,u,3,140);'''),
S(["if you've learned","to celebrate loud","enough for","both of you 🤍","send this","to them, right now 💌"], SHARE),
S(["but if every win","gets brushed off 🌧️","until it stops","feeling like one","at all","that's worth","naming, gently"], '''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  pup({kind:'boy',x:640,y:G+10,s:1.3,look:[-.1,.2],brows:'sad',mouth:'flat',hy:4});
  if(u>1)raincloudSmall(640,720,win(u,1,7));'''),
S(["because someone who","can't celebrate","themselves 🤍","but keeps trying","anyway, just needs","you to believe","it first"], HUG),
]
IG_LINE = "The 'it's not a big deal.' The win they forgot they told you about. Want to know how they love, out loud? 60-second test in our bio."
IG_CAPS = ["the 'not a","big deal' 😅","the win they","forgot telling you 🤍","want to know yours?","60-second test","in our bio 🔗","and see if they","know yours 💌"]
IG_RESULT = "Words of Affirmation"
TT_LINE = "We're two little pups trying to find a thousand people who love like this... If this made you think of someone... follow us. We'll keep making them for you."
