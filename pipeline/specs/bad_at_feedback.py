import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
import jjlib as J
from _kit import S, HUG, SHARE
TITLE = "when they're bad at feedback"
BODY_LINES = [
"When someone who struggles to hear feedback loves you... they'll walk away from the conversation, then come back twenty minutes later having thought about it.",
"Not because they don't want to grow — every critique used to feel like proof they weren't enough.",
"They'll go quiet and hurt the second you say \"can we talk about something?\" — an old reflex, not today's truth.",
"They'll bring it up again, days later, with \"you were right\" — completely unprompted.",
"If someone's learning to hear you without hearing an attack... send this to them, and tell them you noticed.",
"But if the conversation never gets revisited, and every bit of feedback just gets buried... that's not processing, that's avoidance.",
"Because someone who used to flinch at feedback and now circles back to actually hear it... is choosing growth over their pride, for you.",
]
SCENES = [
S(["when someone bad","at feedback loves you 🚶","they'll walk away","from the","conversation first","then come back","twenty minutes later"], '''  room('#f1d5b0','#caa070');
  pup({kind:'boy',x:540,y:G+10,s:1.3,look:[0,.2],brows:'sad',mouth:'flat',hy:4});'''),
S(["not because","they don't want","to grow 🤍","every critique","used to feel like","proof they weren't","enough"], '''  room('#e3c9a0','#bf9670');
  pup({kind:'boy',x:540,y:G+10,s:1.32,look:[0,.1],brows:'sad',mouth:'flat',hy:4});'''),
S(["they'll go quiet","and hurt 😶","the second you say","'can we talk","about something?'","an old reflex,","not today's truth"], '''  room('#f6d7c6','#d6a286');
  pup({kind:'girl',x:720,y:G+10,s:1.22,flip:-1,look:[.2,0],mouth:'flat'});
  pup({kind:'boy',x:380,y:G+10,s:1.26,look:[.2,.1],brows:'sad',mouth:'flat',hy:4,earLift:-.1});'''),
S(["they'll bring it","up again, days","later 🤍","'you were","right' 🤍","completely","unprompted"], '''  room('#3d4b6c','#303b57','rgba(255,255,255,.05)');
  phoneMock(540,780,.62,0,()=>{ctx.fillStyle='#eef0f5';ctx.fillRect(-70,-290,140,280);ctx.font='13px Poppins';ctx.fillStyle=INK;ctx.textAlign='center';ctx.fillText('you were right 🤍',0,-150);});'''),
S(["if someone's","learning to hear","you 🤍","without hearing","an attack","send this to them,","and tell them","you noticed 💌"], SHARE),
S(["but if the","conversation never","gets revisited 🌧️","and every bit","of feedback","just gets buried","that's not processing,","that's avoidance"], '''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  pup({kind:'girl',x:640,y:G+10,s:1.3,flip:-1,look:[.1,.3],brows:'sad',mouth:'flat',hy:4});
  if(u>1)raincloudSmall(640,720,win(u,1,7));'''),
S(["because someone","who used to flinch","at feedback 🤍","and now circles","back to hear it","is choosing growth","over their pride"], HUG),
]
IG_LINE = "The walk away, then back in twenty minutes. 'You were right,' said days later... how do they love? 60-second test in our bio."
IG_CAPS = ["the twenty","minutes to think 🚶","'you were right,'","days later 🤍","want to know yours?","60-second test","in our bio 🔗","and see if they","know yours 💌"]
IG_RESULT = "Words of Affirmation"
TT_LINE = "We're two little pups trying to find a thousand people who love like this... If this made you think of someone... follow us. We'll keep making them for you."
