import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
import jjlib as J
from _kit import S, HUG, SHARE
TITLE = "when a loyal woman loves you"
BODY_LINES = [
"When a loyal woman loves you... she'll put her phone face-down the second someone else's name lights it up, without even thinking about it.",
"Not because she's hiding anything — loyalty, to her, means you never have to wonder.",
"She'll mention who she talked to today before you even ask, like transparency is just how she breathes.",
"She'll turn down the attention that used to feel flattering, because it stopped meaning anything the day she met you.",
"A loyal woman never makes you feel like an option. Send this to the one who deserves her.",
"But if loyalty becomes something you have to keep proving, over and over, to earn basic trust... that's not love, that's an audit.",
"Because a loyal woman who never makes you ask twice... isn't just faithful, she's safe.",
]
SCENES = [
S(["when a loyal","woman loves you 📱","she'll put her","phone face-down","the second someone","else's name lights it up"], '''  room('#e3c9a0','#bf9670');
  pup({kind:'girl',x:540,y:G+10,s:1.3,flip:-1,look:[0,.1],eyes:'open',mouth:'flat',paw:{x:0,y:-110,k:1}});
  blob(rectPts(500,980,80,50,8),'#2b2830');'''),
S(["not because","she's hiding","anything 🤍","loyalty, to her,","means you never","have to wonder"], '''  room('#f1d5b0','#caa070');
  pup({kind:'girl',x:540,y:G+10,s:1.32,flip:-1,look:[0,.1],eyes:'happy',mouth:'smile',blush:.4});'''),
S(["she'll mention","who she talked","to today 🤍","before you","even ask"], '''  room('#f6d7c6','#d6a286');
  pup({kind:'girl',x:420,y:G+10,s:1.28,flip:-1,look:[.2,.1],eyes:'happy',mouth:'smile',blush:.3});
  pup({kind:'boy',x:700,y:G+10,s:1.26,look:[-.2,0],eyes:'open',mouth:'flat'});'''),
S(["she'll turn down","the attention that","used to feel","flattering 🤍","because it stopped","meaning anything","the day she met you"], '''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  pup({kind:'girl',x:620,y:G+10,s:1.26,flip:-1,look:[-.2,0],eyes:'open',mouth:'flat',earLift:-.05});'''),
S(["a loyal woman","never makes you","feel like an","option 🐶🤍","send this to","the one who","deserves her 💌"], SHARE),
S(["but if loyalty","becomes something","you have to keep","proving 🌧️","over and over,","to earn basic trust","that's not love,","that's an audit"], '''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  pup({kind:'boy',x:680,y:G+10,s:1.26,look:[-.2,.1],brows:'sad',mouth:'flat',hy:4});
  if(u>1)raincloudSmall(680,710,win(u,1,8));'''),
S(["because a","loyal woman who","never makes you","ask twice 🤍","isn't just faithful,","she's safe"], HUG),
]
IG_LINE = "Never makes you ask twice. Isn't just faithful, she's safe... want to know how she loves? 60-second test in our bio."
IG_CAPS = ["never makes you","ask twice 🤍","isn't just faithful,","she's safe","want to know yours?","60-second test","in our bio 🔗","and see if she","knows yours 💌"]
IG_RESULT = "Physical Touch"
TT_LINE = "We're two little pups trying to find a thousand people who love like this... If this made you think of someone... follow us. We'll keep making them for you."
