import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
import jjlib as J
from _kit import S, HUG, SHARE
TITLE = "when we rush to say fine"
BODY_LINES = [
"When someone rushes to say \"we're fine\"... it's not that the fight's over.",
"It's that they can't stand you being upset with them.",
"They'll change the subject fast, make a joke, reach for your hand — anything to skip the tense part.",
"They'll apologize for their tone before they even know what they did wrong, just to make it stop hurting faster.",
"If you've learned to rush past a fight just to feel safe again... send this to the one who's patient with your pace.",
"But if \"we're fine\" means nothing ever actually gets said, fight after fight... that's not peace, that's just postponed.",
"Because rushing to fine isn't dishonesty... it's panic dressed up as calm, and it deserves patience, not an eye roll.",
]
SCENES = [
S(["when someone","rushes to say","\"we're fine\" 😬","it's not that","the fight's over"], '''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  pup({kind:'girl',x:620,y:G+10,s:1.3,flip:-1,look:[-.1,.1],brows:'sad',mouth:'flat',hy:4});
  if(u>1&&u<5){ctx.save();ctx.globalAlpha=win(u,1,5);bubbleText(620,720,"we're fine! totally fine!",1,.7);ctx.restore();}'''),
S(["it's that","they can't stand","you being upset","with them 🤍"], '''  room('#e3c9a0','#bf9670');
  pup({kind:'girl',x:540,y:G+10,s:1.34,flip:-1,look:[0,.1],brows:'sad',mouth:'flat',hy:5});'''),
S(["they'll change","the subject fast","make a joke 😅","reach for your hand","anything to skip","the tense part"], '''  room('#f1d5b0','#caa070');
  pup({kind:'girl',x:420,y:G+10,s:1.28,flip:-1,eyes:'happy',mouth:'open',blush:.4,tilt:-.08,paw:{x:90,y:-150,k:.8}});
  pup({kind:'boy',x:660,y:G+10,s:1.28,look:[-.2,.1],mouth:'flat',paw:{x:-90,y:-150,k:.8}});'''),
S(["they'll apologize","for their tone 🤍","before they even","know what","they did wrong","just to make","it stop hurting faster"], '''  room('#f6d7c6','#d6a286');
  phoneMock(540,760,.78,0,()=>{ctx.fillStyle='#eef0f5';ctx.fillRect(-70,-290,140,280);ctx.font='13px Poppins';ctx.fillStyle=INK;ctx.textAlign='center';ctx.fillText('sorry, that came out wrong',0,-200);});
  if(u>2.5)floatHearts(540,900,2.5,u,3,130);'''),
S(["if you've learned","to rush past","a fight 🤍","just to feel","safe again","send this to the","one who's patient","with your pace 💌"], SHARE),
S(["but if","\"we're fine\" 🌧️","means nothing","ever actually","gets said","fight after fight","that's not peace","that's just postponed"], '''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  pup({kind:'boy',x:640,y:G+10,s:1.3,look:[.1,.3],brows:'sad',mouth:'flat',hy:4});
  if(u>1)raincloudSmall(640,720,win(u,1,7));'''),
S(["because rushing","to fine isn't","dishonesty 🤍","it's panic","dressed up as calm","and it deserves","patience, not","an eye roll"], HUG),
]
IG_LINE = "The fast subject change. The joke mid-tension. The sorry before they even know why... want to know how they love? 60-second test in our bio."
IG_CAPS = ["the fast subject","change 🤍","the joke","mid-tension","want to know yours?","60-second test","in our bio 🔗","and see if they","know yours 💌"]
IG_RESULT = "Quality Time"
TT_LINE = "We're two little pups trying to find a thousand people who love like this... If this made you think of someone... follow us. We'll keep making them for you."
