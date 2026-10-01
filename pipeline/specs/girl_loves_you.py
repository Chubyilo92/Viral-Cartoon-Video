import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
import jjlib as J
from _kit import S, HUG, SHARE
TITLE = "when a girl loves you"
BODY_LINES = [
"When a girl loves you... she won't always say it first. She'll show up with your favourite snack after a long week.",
"She'll remember the little thing you mentioned once, and bring it up weeks later.",
"She might tease you in front of everyone, not to embarrass you, because she loves your laugh.",
"She'll go quiet when she's overwhelmed. Not pulling away, she just needs you close, not a hundred questions.",
"If she does this for you... tag her. Let her know it doesn't go unnoticed.",
"But if you only show up when it's convenient... she'll stop waiting for you to notice.",
"Because when a girl truly loves you... you'll never have to guess.",
]
SCENES = [
S(["when a girl","loves you 🤍","she won't","always say it","first","she'll show up","with your favourite","snack 🍪","after a long week"], '''  room('#f1d5b0','#caa070');
  pup({kind:'boy',x:340,y:G+10,s:1.3,look:[.3,0],eyes:'open',mouth:'flat',earLift:-.05,hy:4});
  pup({kind:'girl',x:680,y:G+10,s:1.3,flip:-1,look:[-.3,-.1],eyes:'happy',mouth:'smile',blush:.3,tilt:-.06,paw:{x:40,y:-170,k:P(u,.4,1.2)}});
  bowl(560,G+70,P(u,.6,1.4));'''),
S(["she'll remember","the little thing 💭","you mentioned","once","and bring it up","weeks later","just to let you","know she heard you"], '''  room('#e3c9a0','#bf9670');
  frame(150,420,190,220,(cx,cy)=>heart(cx,cy,52,'#ec7489'));
  pup({kind:'girl',x:700,y:G+10,s:1.3,flip:-1,look:[-.4,.1],eyes:'happy',mouth:'smile',blush:.3,tilt:-.06});
  pup({kind:'boy',x:360,y:G+10,s:1.28,look:[.4,0],eyes:'wide',mouth:'open',earLift:.1});
  if(u>2.4){ctx.save();ctx.globalAlpha=win(u,2.4,7);bubbleText(700,740,"wait, you remembered that?",1,.85);ctx.restore();}'''),
S(["she might tease","you in front","of everyone 😏","not to embarrass you","because she loves","your laugh"], '''  room('#f6d7c6','#d6a286');
  pup({kind:'boy',x:900,y:G+60,s:.7,flip:-1,eyes:'happy',mouth:'smile',blush:.3});
  pup({kind:'girl',x:980,y:G+70,s:.65,eyes:'happy',mouth:'smile',blush:.3});
  pup({kind:'girl',x:620,y:G+10,s:1.32,flip:-1,look:[-.3,.1],eyes:'happy',mouth:'smile',blush:.4,tilt:-.08,wag:.4});
  pup({kind:'boy',x:320,y:G+10,s:1.28,look:[.5,0],eyes:u>2?'happy':'open',mouth:u>2?'smile':'flat',blush:.3*P(u,2,4)});
  if(u>1&&u<5){ctx.save();ctx.globalAlpha=win(u,1,5);bubbleText(620,740,"he always does that thing 😏",1,.85);ctx.restore();}'''),
S(["she'll go quiet","when she's","overwhelmed 🌫️","not pulling away","she just needs","you close","not a hundred","questions"], '''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  pup({kind:'girl',x:680,y:G+10,s:1.3,flip:-1,look:[.2,.3],brows:'sad',mouth:'flat',earLift:-.3,hy:4});
  if(u>.8)raincloudSmall(680,710,win(u,.8,7));
  const near=P(u,2,3.6);
  pup({kind:'boy',x:lerp(320,460,near),y:G+10,s:1.28,look:[.4,.1],eyes:'open',mouth:'flat'});'''),
S(["if she does","this for you 🤍","tag her","let her know","it doesn't go","unnoticed 💌"], SHARE),
S(["but if you","only show up","when it's","convenient 🌧️","she'll stop","waiting for you","to notice"], '''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  pup({kind:'girl',x:640,y:G+10,s:1.3,flip:-1,look:[.1,.3],brows:'sad',mouth:'flat',hy:4});
  if(u>1)raincloudSmall(640,720,win(u,1,7));
  ctx.save();ctx.globalAlpha=.5*P(u,2,4);
  pup({kind:'boy',x:980,y:G+40,s:.7,look:[0,0],eyes:'open',mouth:'flat'});
  ctx.restore();'''),
S(["because when","a girl truly","loves you 🤍","you'll never","have to guess"], HUG),
]
IG_LINE = "The favourite snack. The little thing she remembered. The tease that means she loves your laugh... Every girl shows love in her own way. Want to know hers? There's a 60-second test in our bio. Take it together... and see if she knows yours."
IG_CAPS = ["the favourite snack 🍪","the little thing","she remembered 💭","the tease that means","she loves your laugh","every girl shows love","in her own way 🤍","want to know hers?","60-second test","in our bio 🔗","take it together","and see if she","knows yours 💌"]
IG_RESULT = "Acts of Service"
TT_LINE = "We're two little pups trying to find a thousand people who love like this... If this made you think of someone... follow us. We'll keep making them for you."
