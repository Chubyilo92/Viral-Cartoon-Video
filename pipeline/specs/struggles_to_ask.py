import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
import jjlib as J
from _kit import S, HUG, SHARE
TITLE = "when they can't ask for help"
BODY_LINES = [
"When someone who struggles to ask for help loves you... they'll carry six bags up three flights rather than say the word \"help.\"",
"Not stubbornness — asking has always felt like proof they couldn't manage.",
"They'll say \"I'm fine, I've got it\" through gritted teeth, and mean it, even when they clearly don't.",
"They'll quietly do the favor back double, because receiving feels like debt and giving feels like safety.",
"If you've learned to just start helping, without waiting to be asked... send this to them.",
"But if \"I've got it\" turns into carrying everything alone, every time... that's not independence anymore.",
"Because someone who struggles to ask for help and still lets you in, even a little... is trusting you with the hardest thing they own.",
]
SCENES = [
S(["when someone who","struggles to ask","for help loves you 🛍️","they'll carry six bags","up three flights","rather than say","the word \"help\""], '''  room('#f1d5b0','#caa070');
  pup({kind:'boy',x:460,y:G+10,s:1.3,look:[0,-.1],eyes:'wide',mouth:'flat',earLift:-.1,hy:8,paw:{x:-60,y:-170,k:.8},paw2:{x:60,y:-170,k:.8}});
  ctx.save();ctx.globalAlpha=.9;ctx.font='30px Poppins';ctx.textAlign='center';ctx.fillText('🛍️🛍️',460,G-230);ctx.restore();'''),
S(["not stubbornness 🤍","asking has","always felt","like proof","they couldn't manage"], '''  room('#e3c9a0','#bf9670');
  pup({kind:'boy',x:540,y:G+10,s:1.32,look:[0,.2],brows:'sad',mouth:'flat',earLift:-.1,hy:4});'''),
S(["they'll say","\"i'm fine,","i've got it\" 😬","through gritted teeth","and mean it","even when","they clearly don't"], '''  room('#f6d7c6','#d6a286');
  pup({kind:'boy',x:560,y:G+10,s:1.32,look:[-.1,.1],mouth:'flat',brows:'sad',earLift:-.1});
  if(u>1.5&&u<6.5){ctx.save();ctx.globalAlpha=win(u,1.5,6.5);bubbleText(560,730,"no really, I've got it",1,.85);ctx.restore();}'''),
S(["they'll quietly do","the favor back","double 🔁","because receiving","feels like debt","and giving","feels like safety"], '''  room('#f1d5b0','#caa070');
  pup({kind:'boy',x:540,y:G+10,s:1.3,look:[0,.1],eyes:'happy',mouth:'smile',tilt:.04,earLift:.1,paw:{x:60,y:-180,k:.6}});
  if(u>2)floatHearts(540,860,2,u,3,140);'''),
S(["if you've learned","to just start","helping 🤍","without waiting","to be asked","send this","to them 💌"], SHARE),
S(["but if","\"i've got it\" 🌧️","turns into","carrying everything","alone, every time","that's not","independence anymore"], '''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  pup({kind:'boy',x:640,y:G+10,s:1.3,look:[.1,.3],brows:'sad',mouth:'flat',hy:4,earLift:-.2});
  if(u>1)raincloudSmall(640,720,win(u,1,7));'''),
S(["because someone","who struggles","to ask for help","and still lets","you in, even","a little 🤍","is trusting you","with the","hardest thing","they own"], HUG),
]
IG_LINE = "The six bags up three flights. The gritted-teeth \"I've got it.\" The favor paid back double... want to know how they love? 60-second test in our bio."
IG_CAPS = ["the six bags","up three flights 🛍️","the gritted-teeth","\"I've got it\"","the favor","paid back double 🤍","want to know yours?","60-second test","in our bio 🔗","and see if they","know yours 💌"]
IG_RESULT = "Acts of Service"
TT_LINE = "We're two little pups trying to find a thousand people who love like this... If this made you think of someone... follow us. We'll keep making them for you."
