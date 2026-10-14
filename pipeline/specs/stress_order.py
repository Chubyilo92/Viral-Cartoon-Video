import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
import jjlib as J
from _kit import S, HUG, SHARE
TITLE = "when they know your stress"
BODY_LINES = [
"When someone who remembers exactly how you take your stress loves you... they'll put the kettle on the second your voice changes, before you've said a word.",
"Not because they're psychic — they've just memorized you, the way some people memorize a map.",
"They'll know you go quiet first, then snappy, then apologize for the snappy part.",
"They'll hand you the blanket, not the solution, because they learned the hard way which one you actually need.",
"If someone knows your stress order better than your coffee order... send this to them.",
"But if \"I know what you need\" turns into deciding for you instead of asking... that's not care, that's control with a good memory.",
"Because someone who studies how you fall apart, just to catch you better... is loving you in the details.",
]
SCENES = [
S(["when someone","remembers exactly","how you take","your stress 🫖","they'll put the","kettle on before","you've said a word"], '''  room('#e3c9a0','#bf9670');
  pup({kind:'boy',x:420,y:G+10,s:1.3,look:[.2,0],eyes:'open',mouth:'flat',earLift:.1});
  mug(700,G-40,1.3);'''),
S(["not because","they're psychic 🤍","they've just","memorized you","the way some","people memorize","a map"], '''  room('#f1d5b0','#caa070');
  pup({kind:'boy',x:540,y:G+10,s:1.32,look:[0,.1],eyes:'happy',mouth:'smile',blush:.3});'''),
S(["they'll know you","go quiet first 🤐","then snappy","then apologize","for the","snappy part"], '''  room('#f6d7c6','#d6a286');
  pup({kind:'girl',x:620,y:G+10,s:1.28,flip:-1,look:[-.2,.1],brows:'sad',mouth:'flat',hy:3});'''),
S(["they'll hand you","the blanket 🧣","not the solution","because they learned","the hard way","which one you","actually need"], '''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  pup({kind:'boy',x:400,y:G+10,s:1.26,look:[.2,0],eyes:'open',mouth:'flat',paw:{x:110,y:-60,k:1}});
  pup({kind:'girl',x:700,y:G+10,s:1.22,flip:-1,look:[-.2,.1],brows:'sad',mouth:'flat',hy:3});'''),
S(["if someone knows","your stress order","better than your","coffee order 🤍","send this to them 💌"], SHARE),
S(["but if 'I know","what you need'","turns into","deciding for you 🌧️","instead of asking","that's not care,","that's control"], '''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  pup({kind:'boy',x:680,y:G+10,s:1.26,look:[-.2,.1],brows:'sad',mouth:'flat',hy:4});
  if(u>1)raincloudSmall(680,710,win(u,1,8));'''),
S(["because someone","who studies how","you fall apart 🤍","just to catch","you better","is loving you","in the details"], HUG),
]
IG_LINE = "Knowing your stress order better than your coffee order. Loving you in the details... want to know how they love? 60-second test in our bio."
IG_CAPS = ["knows your","stress order 🤍","better than your","coffee order","want to know yours?","60-second test","in our bio 🔗","and see if they","know yours 💌"]
IG_RESULT = "Acts of Service"
TT_LINE = "We're two little pups trying to find a thousand people who love like this... If this made you think of someone... follow us. We'll keep making them for you."
