import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
import jjlib as J
from _kit import S, HUG, SHARE
TITLE = "when a nostalgic heart loves you"
BODY_LINES = [
"When a nostalgic heart loves you... they'll still have the ticket stub from your first date, folded in their wallet.",
"Not because they're stuck in the past — it's because that night is proof this was always going to be real.",
"They'll replay the same playlist from your first road trip, every single time, and never skip a single song.",
"They'll bring up a tiny thing you said months ago, word for word, because it mattered enough to keep.",
"If someone's kept every little proof that you happened... send this to them, and let them know you kept some too.",
"But if they're more in love with the memory than the person standing in front of them now... that's worth a gentle conversation.",
"Because someone who keeps the small proof of you... isn't living in the past, they're just making sure none of it gets lost.",
]
SCENES = [
S(["when a nostalgic","heart loves you 🎫","they'll still have","the ticket stub","from your first date","folded in","their wallet"], '''  room('#f1d5b0','#caa070');
  const k=pop(u,.2,.5);ctx.save();ctx.translate(680,700);ctx.scale(k,k);blob(rectPts(-70,-44,140,88,10),'#fffaf0',{lw:4});ctx.font='22px Poppins';ctx.textAlign='center';ctx.fillStyle=INK;ctx.fillText('🎫',0,8);ctx.restore();
  pup({kind:'boy',x:400,y:G+10,s:1.28,look:[.3,0],eyes:'happy',mouth:'smile',tilt:.05,earLift:.08});'''),
S(["not because","they're stuck","in the past 🤍","it's because that","night is proof","this was always","going to be real"], '''  room('#e3c9a0','#bf9670');
  pup({kind:'boy',x:540,y:G+10,s:1.34,look:[0,.1],eyes:'happy',mouth:'smile',blush:.3,tilt:.04});'''),
S(["they'll replay","the same playlist","from your first","road trip 🎵","every single time","never skipping","a single song"], '''  room('#f6d7c6','#d6a286');
  phoneMock(730,780,.62,-.04,()=>{ctx.fillStyle='#eef0f5';ctx.fillRect(-70,-290,140,280);ctx.font='28px Poppins';ctx.textAlign='center';ctx.fillText('🎵',0,-150);});
  pup({kind:'girl',x:340,y:G+10,s:1.26,flip:-1,eyes:'happy',mouth:'smile',blush:.3});'''),
S(["they'll bring up","a tiny thing","you said","months ago 🤍","word for word","because it mattered","enough to keep"], '''  room('#f1d5b0','#caa070');
  pup({kind:'boy',x:460,y:G+10,s:1.28,look:[.2,0],eyes:'happy',mouth:'open',earLift:.1});
  pup({kind:'girl',x:700,y:G+10,s:1.28,flip:-1,eyes:'wide',mouth:'smile',blush:.4});
  if(u>2)floatHearts(540,860,2,u,3,140);'''),
S(["if someone's kept","every little proof","that you","happened 🤍","send this to them","and let them know","you kept","some too 💌"], SHARE),
S(["but if they're","more in love","with the memory 🌧️","than the person","standing in","front of them now","that's worth a","gentle conversation"], '''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  pup({kind:'boy',x:640,y:G+10,s:1.3,look:[.3,.2],brows:'sad',mouth:'flat',hy:4});
  if(u>1)raincloudSmall(640,720,win(u,1,7));'''),
S(["because someone","who keeps the","small proof of you 🤍","isn't living","in the past","they're just making","sure none of it","gets lost"], HUG),
]
IG_LINE = "The ticket stub in the wallet. The playlist never skipped. The tiny thing remembered word for word... want to know how they love? 60-second test in our bio."
IG_CAPS = ["the ticket stub","in the wallet 🎫","the playlist","never skipped 🤍","want to know yours?","60-second test","in our bio 🔗","and see if they","know yours 💌"]
IG_RESULT = "Quality Time"
TT_LINE = "We're two little pups trying to find a thousand people who love like this... If this made you think of someone... follow us. We'll keep making them for you."
