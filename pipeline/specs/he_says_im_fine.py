import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
import jjlib as J
from _kit import S, HUG, SHARE
TITLE = "when he says i'm fine"
BODY_LINES = [
"When he says I'm fine... he's not always fine. He's just not sure how to say what's actually wrong.",
"He might go quiet and disappear into a task, not to shut you out, just to feel useful for a minute.",
"He might snap about something small. It's about carrying something all day with no one to hand it to.",
"He doesn't need you to fix it. He needs you to sit with him and not take the silence personally.",
"If you're the one who goes quiet to cope... send this to the one who stays anyway.",
"But if you only check on him when it's easy... one day he'll stop saying anything at all.",
"Because the boy who still says I'm fine, even when he isn't... is still trying to protect you from his bad day.",
]
SCENES = [
S(["when he says","\"i'm fine\" 😕","he's not","always fine","he's just not sure","how to say","what's actually wrong"], '''  room('#f1d5b0','#caa070');
  pup({kind:'girl',x:700,y:G+10,s:1.3,flip:-1,look:[-.3,.1],eyes:'open',mouth:'flat',blush:.1,tilt:-.05});
  pup({kind:'boy',x:360,y:G+10,s:1.3,look:[.4,0],eyes:'open',mouth:'flat',earLift:-.1});
  if(u>.8&&u<5){ctx.save();ctx.globalAlpha=win(u,.8,5);bubbleText(360,740,"i'm fine, really",1,.85);ctx.restore();}'''),
S(["he might go quiet","and disappear","into a task 🔧","not to shut","you out","just to feel useful","for a minute"], '''  room('#e3c9a0','#bf9670');
  pup({kind:'boy',x:560,y:G+10,s:1.34,look:[0,.4],eyes:'open',mouth:'flat',earLift:-.1,hy:6});
  pup({kind:'girl',x:260,y:G+30,s:1.0,flip:-1,look:[.6,0],eyes:'open',mouth:'flat',blush:.1});
  if(u>1.5){ctx.save();ctx.globalAlpha=win(u,1.5,7);ctx.font='34px Poppins';ctx.textAlign='center';ctx.fillText('🔧',700,G-180);ctx.restore();}'''),
S(["he might snap","about something small 😮‍💨","it's not","about the thing","it's about carrying","something all day","with no one","to hand it to"], '''  room('#f6d7c6','#d6a286');
  dishPile(760,G-10,.6);
  pup({kind:'boy',x:400,y:G+10,s:1.32,look:[.4,0],mouth:'pout',brows:'sad',blush:.1,tilt:.05,earLift:-.1});
  if(u>1.2&&u<5.2){ctx.save();ctx.globalAlpha=win(u,1.2,5.2);bubbleText(400,740,"can everyone just slow down?!",1,.85);ctx.restore();}'''),
S(["he doesn't","need you","to fix it 🙅","he needs you","to sit with him","and not take","the silence","personally"], '''  room('#f1d5b0','#caa070');
  pup({kind:'boy',x:540,y:G+10,s:1.32,look:[0,.2],eyes:'open',mouth:'flat',earLift:-.1,hy:4});
  pup({kind:'girl',x:720,y:G+10,s:1.28,flip:-1,look:[-.6,0],eyes:'open',mouth:'flat',blush:.2,tilt:-.03});
  if(u>3)floatHearts(620,860,3,u,3,130);'''),
S(["if you're the one","who goes quiet","to cope 🤍","send this to","the one who","stays anyway 💌"], SHARE),
S(["but if you","only check on him","when it's easy 🌧️","one day","he'll stop saying","anything at all"], '''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  pup({kind:'boy',x:640,y:G+10,s:1.3,look:[.1,.3],brows:'sad',mouth:'flat',earLift:-.3,hy:4});
  if(u>1)raincloudSmall(640,720,win(u,1,7));'''),
S(["because the boy","who still says","\"i'm fine\" 🤍","even when","he isn't","is still trying","to protect you","from his bad day"], HUG),
]
IG_LINE = "The quiet task. The snap that isn't about the dishes. Sitting with him instead of fixing him... want to know how he loves? Test in our bio... see if he knows yours."
IG_CAPS = ["the quiet task 🔧","the snap that isn't","about the dishes","sitting with him","instead of fixing him 🤍","want to know his?","60-second test","in our bio 🔗","take it together","and see if he","knows yours 💌"]
IG_RESULT = "Quality Time"
TT_LINE = "We're two little pups trying to find a thousand people who love like this... If this made you think of someone... follow us. We'll keep making them for you."
