import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
import jjlib as J
from _kit import S, HUG, SHARE
TITLE = "when they forgive you easily"
BODY_LINES = [
"When someone who forgives easily loves you... they cut you off mid-apology, because they already decided it's not worth the fight.",
"They won't bring up the fight from last month. To them, it's already closed, filed away, done.",
"They'll choose to believe the kindest reason you were short with them, even when the worst reason is sitting right there, easier to grab.",
"They'll forgive you before you've even forgiven yourself, because being right has never mattered to them as much as being together.",
"If someone's handed you grace you didn't ask for... send this to them, right now, before you forget.",
"But if you keep handing them the same thing to forgive, over and over... their patience was never a free pass.",
"Because someone who forgives easily isn't naive. They just decided choosing you, every time, mattered more than keeping score.",
]
SCENES = [
S(["when someone","who forgives easily","loves you 🤍","they cut you off","mid-apology","because they","already decided","it's not worth","the fight"], '''  room('#f6d7c6','#d6a286');
  pup({kind:'boy',x:620,y:G+10,s:1.3,flip:-1,look:[-.3,.1],mouth:'flat',brows:'sad',earLift:-.1});
  pup({kind:'girl',x:340,y:G+10,s:1.32,look:[.4,0],eyes:'happy',mouth:'smile',blush:.3,tilt:-.04});
  if(u>1.6&&u<6){ctx.save();ctx.globalAlpha=win(u,1.6,6);bubbleText(340,740,"hey, it's already okay 🤍",1,.85);ctx.restore();}'''),
S(["they won't","bring up the","fight from","last month 📅","to them","it's already closed","filed away","done"], '''  room('#e3c9a0','#bf9670');
  frame(150,420,190,220,(cx,cy)=>{ctx.font='34px Poppins';ctx.textAlign='center';ctx.fillText('✅',cx,cy+12);});
  pup({kind:'girl',x:700,y:G+10,s:1.3,flip:-1,look:[-.4,.1],eyes:'happy',mouth:'smile',blush:.3,tilt:-.06});'''),
S(["they'll choose","to believe","the kindest reason","you were short","with them 🤍","even when the","worst reason","is sitting right there","easier to grab"], '''  room('#f1d5b0','#caa070');
  pup({kind:'boy',x:360,y:G+10,s:1.28,look:[.4,.2],mouth:'flat',brows:'sad',earLift:-.1});
  pup({kind:'girl',x:680,y:G+10,s:1.32,flip:-1,look:[-.4,0],eyes:'happy',mouth:'smile',blush:.3,tilt:-.05});'''),
S(["they'll forgive you","before you've even","forgiven yourself 🤍","because being right","has never mattered","to them as much","as being together"], HUG),
S(["if someone's","handed you grace","you didn't ask for 🤍","send this to them","right now","before you forget 💌"], SHARE),
S(["but if you","keep handing them","the same thing","to forgive 🌧️","over and over","their patience","was never","a free pass"], '''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  pup({kind:'girl',x:640,y:G+10,s:1.3,flip:-1,look:[.1,.3],brows:'sad',mouth:'flat',hy:4});
  if(u>1)raincloudSmall(640,720,win(u,1,7));'''),
S(["because someone","who forgives","easily isn't naive 🤍","they just decided","choosing you","every time","mattered more","than keeping score"], '''  room('#f1d5b0','#caa070');plant(970,G+6,.9);
  pup({kind:'boy',x:360,y:G+10,s:1.3,look:[.3,0],eyes:'happy',mouth:'smile',tilt:.05,earLift:.1});
  pup({kind:'girl',x:680,y:G+10,s:1.3,flip:-1,look:[-.3,.1],eyes:'happy',mouth:'smile',blush:.4,tilt:-.06,wag:.3});
  if(u>2)floatHearts(540,860,2,u,4,150);'''),
]
IG_LINE = "Cutting you off mid-apology. Choosing the kindest reason. Forgiving you before you forgive yourself... want to know how they love? Test in our bio... see if they know yours."
IG_CAPS = ["cutting you off","mid-apology 🤍","choosing the","kindest reason","forgiving you first","want to know yours?","60-second test","in our bio 🔗","take it together","and see if they","know yours 💌"]
IG_RESULT = "Words of Affirmation"
TT_LINE = "We're two little pups trying to find a thousand people who love like this... If this made you think of someone... follow us. We'll keep making them for you."
