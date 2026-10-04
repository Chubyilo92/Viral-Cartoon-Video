import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
import jjlib as J
from _kit import S, HUG, SHARE
TITLE = "when a private partner loves you"
BODY_LINES = [
"When a private partner loves you... they won't post the anniversary, the flowers, the relationship for strangers to rate.",
"Not because they're not proud — the best parts feel too good to perform.",
"They'll tell their best friend everything, and still never caption a single photo of you two.",
"They'll hold your hand under the table at dinner, where no one's watching, because that's who it's actually for.",
"If \"we don't post each other\" has people asking if something's wrong, when nothing's ever been more right... send this to them.",
"But if private starts meaning hidden, like you're a secret instead of a person... that's worth asking about.",
"Because a private partner who loves you loud behind closed doors... was never performing it for anyone but you.",
]
SCENES = [
S(["when a private","partner loves you 🤍","they won't post","the anniversary","the flowers","the relationship","for strangers to rate"], '''  room('#f1d5b0','#caa070');
  phoneMock(760,780,.6,-.04,()=>{ctx.fillStyle='#eef0f5';ctx.fillRect(-70,-290,140,280);ctx.font='30px Poppins';ctx.textAlign='center';ctx.fillText('🚫📸',0,-140);});
  pup({kind:'girl',x:340,y:G+10,s:1.3,flip:-1,look:[.4,0],eyes:'happy',mouth:'smile',blush:.3,tilt:-.05});'''),
S(["not because","they're not proud 🤍","the best parts","feel too good","to perform"], '''  room('#e3c9a0','#bf9670');
  pup({kind:'girl',x:540,y:G+10,s:1.32,flip:-1,look:[0,.1],eyes:'happy',mouth:'smile',blush:.4,tilt:-.08});'''),
S(["they'll tell their","best friend","everything 🗣️","and still never","caption a single","photo of you two"], '''  room('#f6d7c6','#d6a286');
  pup({kind:'girl',x:680,y:G+10,s:1.26,flip:-1,look:[-.4,0],eyes:'happy',mouth:'open',blush:.3});
  pup({kind:'boy',x:360,y:G+10,s:1.0,look:[.4,0],eyes:'happy',mouth:'smile'});
  if(u>2&&u<6){ctx.save();ctx.globalAlpha=win(u,2,6);bubbleText(680,740,"ok but he's actually perfect",1,.85);ctx.restore();}'''),
S(["they'll hold your","hand under the","table at dinner 🤍","where no","one's watching","because that's who","it's actually for"], '''  room('#f1d5b0','#caa070');
  ell(540,G+16,300,30,'#00000010',{stroke:false});
  pup({kind:'girl',x:420,y:G+10,s:1.3,flip:-1,eyes:'happy',mouth:'smile',blush:.4,tilt:-.06,paw:{x:90,y:-150,k:.7}});
  pup({kind:'boy',x:660,y:G+10,s:1.3,eyes:'happy',mouth:'smile',blush:.3,tilt:.06,paw:{x:-90,y:-150,k:.7}});
  if(u>1.6)floatHearts(540,760,1.6,u,3,140);'''),
S(["if \"we don't","post each other\" 🤍","has people asking","if something's wrong","when nothing's ever","been more right","send this","to them 💌"], SHARE),
S(["but if private","starts meaning hidden 🌧️","like you're a","secret instead","of a person","that's worth","asking about"], '''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  pup({kind:'girl',x:640,y:G+10,s:1.3,flip:-1,look:[.1,.3],brows:'sad',mouth:'flat',hy:4});
  if(u>1)raincloudSmall(640,720,win(u,1,7));'''),
S(["because a private","partner who loves","you loud 🤍","behind closed doors","was never","performing it","for anyone but you"], HUG),
]
IG_LINE = "No anniversary post. No caption. Just a hand held under the table where no one's watching... want to know how they love? 60-second test in our bio."
IG_CAPS = ["no anniversary post","no caption 🚫📸","just a hand","held under","the table 🤍","want to know yours?","60-second test","in our bio 🔗","and see if they","know yours 💌"]
IG_RESULT = "Quality Time"
TT_LINE = "We're two little pups trying to find a thousand people who love like this... If this made you think of someone... follow us. We'll keep making them for you."
