import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
import jjlib as J
from _kit import S, HUG, SHARE
TITLE = "a stubborn person loves you"
BODY_LINES = [
"When a stubborn person loves you... they will not say sorry first. Not because they don't mean it. The words just get stuck on the way out.",
"They'll fix the thing you were upset about, before they ever bring it up.",
"They'll sit in the same room as you, still annoyed, because leaving isn't an option they consider.",
"They'll agree to disagree out loud, then quietly do it your way anyway.",
"If someone's never once said sorry, but always shows it... send this to them.",
"But if the fixing never comes, and only the stubbornness does... that's not pride anymore.",
"Because a stubborn person who still chooses you, every single time... loves you in the only way they know how to bend.",
]
SCENES = [
S(["when a stubborn","person loves you 😤","they will not","say sorry first","not because","they don't mean it","the words just","get stuck","on the way out"], '''  room('#f6d7c6','#d6a286');
  pup({kind:'boy',x:620,y:G+10,s:1.32,flip:-1,look:[-.3,.2],mouth:'flat',brows:'sad',earLift:-.1});
  pup({kind:'girl',x:340,y:G+10,s:1.28,look:[.5,0],eyes:'open',mouth:'flat',blush:.1});
  if(u>2&&u<6){ctx.save();ctx.globalAlpha=win(u,2,6);bubbleText(620,740,"...it's fine, whatever",1,.85);ctx.restore();}'''),
S(["they'll fix","the thing","you were","upset about 🔧","before they","ever bring it up"], '''  room('#e3c9a0','#bf9670');
  pup({kind:'boy',x:560,y:G+10,s:1.34,look:[0,.4],eyes:'open',mouth:'flat',earLift:-.1,hy:6});
  if(u>1.5){ctx.save();ctx.globalAlpha=win(u,1.5,7);ctx.font='34px Poppins';ctx.textAlign='center';ctx.fillText('🔧',700,G-180);ctx.restore();}
  pup({kind:'girl',x:280,y:G+30,s:1.0,flip:-1,look:[.6,0],eyes:'wide',mouth:'open'});'''),
S(["they'll sit in","the same room","as you","still annoyed 😑","because leaving","isn't an option","they consider"], '''  room('#f6d7c6','#d6a286');
  pup({kind:'girl',x:700,y:G+10,s:1.28,flip:-1,look:[-.6,.1],mouth:'flat',brows:'sad',blush:.1});
  pup({kind:'boy',x:380,y:G+10,s:1.28,look:[.6,.1],mouth:'flat',brows:'sad'});'''),
S(["they'll agree","to disagree","out loud 🗣️","then quietly","do it","your way anyway 🤍"], '''  room('#f1d5b0','#caa070');
  pup({kind:'boy',x:360,y:G+10,s:1.3,look:[.3,0],eyes:'happy',mouth:'smile',tilt:.05,earLift:.1});
  pup({kind:'girl',x:680,y:G+10,s:1.3,flip:-1,look:[-.3,.1],eyes:'happy',mouth:'smile',blush:.3,tilt:-.06});
  if(u>2)floatHearts(540,860,2,u,3,140);'''),
S(["if someone's","never once","said sorry 😤","but always","shows it 🤍","send this","to them 💌"], SHARE),
S(["but if the","fixing never comes 🌧️","and only the","stubbornness does","that's not","pride anymore"], '''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  pup({kind:'girl',x:640,y:G+10,s:1.3,flip:-1,look:[.1,.3],brows:'sad',mouth:'flat',hy:4});
  if(u>1)raincloudSmall(640,720,win(u,1,7));'''),
S(["because a","stubborn person","who still","chooses you 🤍","every single time","loves you","in the only way","they know how to bend"], HUG),
]
IG_LINE = "Never says sorry. Always fixes it anyway. Sits annoyed in the same room, every time... want to know how they love? Test in our bio... see if they know yours."
IG_CAPS = ["never says sorry 😤","always fixes it","anyway 🔧","stays in the room","every single time 🤍","want to know yours?","60-second test","in our bio 🔗","take it together","and see if they","know yours 💌"]
IG_RESULT = "Acts of Service"
TT_LINE = "We're two little pups trying to find a thousand people who love like this... If this made you think of someone... follow us. We'll keep making them for you."
