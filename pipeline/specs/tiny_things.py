import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
import jjlib as J
from _kit import S, HUG, SHARE
TITLE = "they remember tiny things"
BODY_LINES = [
"When someone truly loves you... they remember the tiny things. How you take your coffee. The side of the bed you like.",
"They remember the song that makes you cry, and skip it in the car without you asking.",
"They notice when you've had a haircut, before you even mention it.",
"They remember the order you always get, and already said it before you opened your mouth.",
"If someone remembers the small stuff about you... send them this. Let them know you noticed, too.",
"But if they forget the little things on purpose, again and again... that's not forgetfulness anymore.",
"Because the tiny things are never really tiny. They're proof someone's been paying attention the whole time.",
]
SCENES = [
S(["when someone","truly loves you 🤍","they remember","the tiny things","how you take","your coffee ☕","the side of","the bed you like"], '''  room('#f1d5b0','#caa070');
  mug(760,G-10,1);
  pup({kind:'boy',x:340,y:G+10,s:1.3,look:[.3,0],eyes:'happy',mouth:'smile',tilt:.05,earLift:.1});'''),
S(["they remember","the song","that makes you","cry 🎵","and skip it","in the car","without you","even asking"], '''  room('#e3c9a0','#bf9670');
  pup({kind:'girl',x:620,y:G+10,s:1.3,flip:-1,look:[-.3,.1],eyes:'happy',mouth:'smile',blush:.3,tilt:-.06});
  pup({kind:'boy',x:340,y:G+10,s:1.28,look:[.5,0],eyes:'open',mouth:'flat',earLift:.05});
  if(u>1.5){ctx.save();ctx.globalAlpha=win(u,1.5,7);ctx.font='26px Poppins';ctx.textAlign='center';ctx.fillText('⏭️🎵',340,G-170);ctx.restore();}'''),
S(["they notice","when you've","had a haircut ✂️","before you","even mention it"], '''  room('#f6d7c6','#d6a286');
  pup({kind:'girl',x:660,y:G+10,s:1.32,flip:-1,look:[-.3,0],eyes:'happy',mouth:'smile',blush:.3,tilt:-.06});
  if(u>1&&u<5){ctx.save();ctx.globalAlpha=win(u,1,5);bubbleText(660,740,"wait, you got a haircut!",1,.85);ctx.restore();}'''),
S(["they remember","the order","you always get 🥤","and already","said it before","you opened","your mouth"], '''  room('#f1d5b0','#caa070');
  bowl(760,G+40,1);
  pup({kind:'boy',x:360,y:G+10,s:1.3,look:[.3,0],eyes:'happy',mouth:'smile',tilt:.04,earLift:.1});
  if(u>2&&u<6){ctx.save();ctx.globalAlpha=win(u,2,6);bubbleText(360,740,"the usual, right?",1,.85);ctx.restore();}'''),
S(["if someone","remembers the","small stuff 🤍","send them this","let them know","you noticed, too 💌"], SHARE),
S(["but if they","forget the little","things on purpose 🌧️","again and again","that's not","forgetfulness anymore"], '''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  pup({kind:'girl',x:640,y:G+10,s:1.3,flip:-1,look:[.1,.3],brows:'sad',mouth:'flat',hy:4});
  if(u>1)raincloudSmall(640,720,win(u,1,7));'''),
S(["because the","tiny things","are never","really tiny 🤍","they're proof","someone's been","paying attention","the whole time"], HUG),
]
IG_LINE = "The coffee order. The skipped song. The haircut they noticed first... every person shows love in their own way. Want to know yours? 60-second test in our bio... take it together, and see if they know yours."
IG_CAPS = ["the coffee order ☕","the skipped song 🎵","the haircut","they noticed first","want to know yours?","60-second test","in our bio 🔗","take it together","and see if they","know yours 💌"]
IG_RESULT = "Acts of Service"
TT_LINE = "We're two little pups trying to find a thousand people who love like this... If this made you think of someone... follow us. We'll keep making them for you."
