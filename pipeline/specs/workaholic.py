import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
import jjlib as J
from _kit import S, HUG, SHARE
TITLE = "when a workaholic loves you"
BODY_LINES = [
"When a workaholic loves you... they'll fall asleep mid-sentence, still trying to finish telling you about their day.",
"Not because you're boring them — they gave you what was left after giving everyone else everything first.",
"They'll answer one more email at midnight, then still make it to bed before you fall asleep.",
"They'll reschedule a call for your appointment, then feel guilty about it for the rest of the day.",
"If someone's tired, but still chooses the last twenty minutes of their day for you... send this to them.",
"But if \"just this one project\" becomes every project, and you're always what's left over... that's not ambition anymore, that's avoidance.",
"Because a workaholic who still shows up exhausted, every single night... is telling you exactly where you rank, even when they can't say it.",
]
SCENES = [
S(["when a workaholic","loves you 😴","they'll fall asleep","mid-sentence","still trying to","finish telling you","about their day"], '''  room('#3d4b6c','#303b57','rgba(255,255,255,.05)');
  pup({kind:'boy',x:460,y:G+10,s:1.28,look:[0,.2],eyes:'closed',mouth:'flat',hy:6,tilt:.1});
  pup({kind:'girl',x:700,y:G+10,s:1.28,flip:-1,eyes:'happy',mouth:'smile',blush:.3,tilt:-.05});
  zzz(560,G-180,u*1.6);'''),
S(["not because","you're boring","them 🤍","they gave you","what was left","after giving everyone","else everything first"], '''  room('#e3c9a0','#bf9670');
  pup({kind:'boy',x:540,y:G+10,s:1.34,look:[0,.1],brows:'sad',mouth:'flat',hy:4});'''),
S(["they'll answer","one more email","at midnight 💻","then still","make it to bed","before you","fall asleep"], '''  room('#3d4b6c','#303b57','rgba(255,255,255,.05)');
  pup({kind:'boy',x:620,y:G+10,s:1.2,look:[-.1,-.1],eyes:'wide',mouth:'flat',earLift:-.1,hy:6});
  ctx.save();ctx.globalAlpha=.9;ctx.font='28px Poppins';ctx.textAlign='center';ctx.fillText('💻',620,G-250);ctx.restore();'''),
S(["they'll reschedule","a call for","your appointment 🗓️","then feel guilty","about it","for the rest","of the day"], '''  room('#f1d5b0','#caa070');
  phoneMock(730,780,.62,-.04,()=>{ctx.fillStyle='#eef0f5';ctx.fillRect(-70,-290,140,280);ctx.font='14px Poppins';ctx.fillStyle=INK;ctx.textAlign='center';ctx.fillText('moved my 2pm for you',0,-150);});
  pup({kind:'girl',x:340,y:G+10,s:1.26,flip:-1,look:[.3,0],eyes:'happy',mouth:'smile',blush:.3});'''),
S(["if someone's tired","but still chooses","the last twenty","minutes of their day","for you 🤍","send this","to them 💌"], SHARE),
S(["but if","\"just this one","project\" 🌧️","becomes every project","and you're always","what's left over","that's not ambition","anymore, that's avoidance"], '''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  pup({kind:'boy',x:640,y:G+10,s:1.3,look:[-.2,0],brows:'sad',mouth:'flat',hy:4});
  phoneMock(420,800,.48,.06,()=>{ctx.fillStyle='#2b2830';ctx.fillRect(-70,-290,140,280);});
  if(u>1)raincloudSmall(640,720,win(u,1,7));'''),
S(["because a workaholic","who still shows up","exhausted, every","single night 🤍","is telling you","exactly where","you rank"], HUG),
]
IG_LINE = "Falling asleep mid-sentence. One more email at midnight. The guilty rescheduled call... want to know how they love? 60-second test in our bio."
IG_CAPS = ["asleep mid-sentence","telling you 😴","the last","twenty minutes 🤍","want to know yours?","60-second test","in our bio 🔗","and see if they","know yours 💌"]
IG_RESULT = "Acts of Service"
TT_LINE = "We're two little pups trying to find a thousand people who love like this... If this made you think of someone... follow us. We'll keep making them for you."
