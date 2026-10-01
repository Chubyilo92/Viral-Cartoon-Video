import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
import jjlib as J
from _kit import S, HUG, SHARE
TITLE = "when an introvert loves you"
BODY_LINES = [
"When an introvert loves you... they'll cancel plans with everyone else, just to stay in with you.",
"They'll go quiet in a loud room, not checked out, just recharging so they can actually be present with you later.",
"They'll text less than you'd like, but read every message twice, because it's from you.",
"They'll let you into the one hour of their day they protect from everyone else.",
"If you're the loud one who learned to love the quiet one... send this to them.",
"But if you mistake their quiet for not caring... you'll miss the biggest compliment they know how to give.",
"Because when an introvert chooses to be around you... it costs them more energy than you'll ever see, and they spend it on you anyway.",
]
SCENES = [
S(["when an introvert","loves you 🤍","they'll cancel plans","with everyone else","just to stay in","with you"], '''  room('#f1d5b0','#caa070');
  phoneMock(760,780,.62,-.04,()=>{ctx.fillStyle='#eef0f5';ctx.fillRect(-70,-290,140,280);ctx.font='11px Poppins';ctx.fillStyle=INK;ctx.textAlign='center';ctx.fillText('sorry, staying in tonight',0,-140);});
  pup({kind:'girl',x:340,y:G+10,s:1.32,flip:-1,look:[.4,0],eyes:'happy',mouth:'smile',blush:.3,tilt:-.05,wag:.3});'''),
S(["they'll go quiet","in a loud room 🔈","not checked out","just recharging","so they can","actually be present","with you later"], '''  room('#f6d7c6','#d6a286');
  pup({kind:'boy',x:900,y:G+60,s:.65,flip:-1,eyes:'happy',mouth:'smile'});
  pup({kind:'girl',x:980,y:G+70,s:.6,eyes:'happy',mouth:'smile'});
  pup({kind:'boy',x:400,y:G+10,s:1.3,look:[.1,-.1],eyes:'open',mouth:'flat',earLift:-.2,hy:4});
  if(u>2){ctx.save();ctx.globalAlpha=win(u,2,7);ctx.font='26px Poppins';ctx.textAlign='center';ctx.fillText('🔋',400,G-160);ctx.restore();}'''),
S(["they'll text","less than you'd","like 📱","but read every","message twice","because it's from you 🤍"], '''  room('#e3c9a0','#bf9670');
  phoneMock(540,760,.78,0,()=>{ctx.fillStyle='#eef0f5';ctx.fillRect(-70,-290,140,280);ctx.font='11px Poppins';ctx.fillStyle=INK;ctx.textAlign='center';ctx.fillText('(read again)',0,-120);});
  if(u>2.5)floatHearts(540,900,2.5,u,3,140);'''),
S(["they'll let you","into the one hour","of their day 🕐","they protect","from everyone else"], '''  room('#f1d5b0','#caa070');plant(970,G+6,.9);
  pup({kind:'boy',x:360,y:G+10,s:1.3,look:[.4,.1],eyes:'happy',mouth:'smile',tilt:.06,earLift:.1});
  pup({kind:'girl',x:680,y:G+10,s:1.3,flip:-1,look:[-.4,.1],eyes:'happy',mouth:'smile',blush:.4,tilt:-.06,wag:.3});'''),
S(["if you're the","loud one","who learned to","love the quiet one 🤍","send this","to them 💌"], SHARE),
S(["but if you","mistake their quiet","for not caring 🌧️","you'll miss","the biggest compliment","they know how to give"], '''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  pup({kind:'boy',x:640,y:G+10,s:1.3,look:[.1,.3],brows:'sad',mouth:'flat',earLift:-.3,hy:4});
  if(u>1)raincloudSmall(640,720,win(u,1,7));'''),
S(["because when","an introvert","chooses to be","around you 🤍","it costs them","more energy","than you'll ever see","and they spend","it on you anyway"], HUG),
]
IG_LINE = "The cancelled plans. The quiet recharge. The one protected hour they let you into... want to know how they love? Test in our bio... see if they know yours."
IG_CAPS = ["the cancelled plans 🤍","the quiet recharge 🔋","the one hour","they protect","and let you into","want to know yours?","60-second test","in our bio 🔗","take it together","and see if they","know yours 💌"]
IG_RESULT = "Quality Time"
TT_LINE = "We're two little pups trying to find a thousand people who love like this... If this made you think of someone... follow us. We'll keep making them for you."
