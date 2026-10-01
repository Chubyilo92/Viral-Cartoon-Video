import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
import jjlib as J
from _kit import S, HUG, SHARE
TITLE = "when the planner loves you"
BODY_LINES = [
"When the planner in the relationship loves you... they'll check the weather for your trip, three days before you even pack.",
"They'll have snacks, chargers, and a backup plan in the car, just in case.",
"They'll text, did you eat, before they say anything else, every single day.",
"They'll map the route the night before, so you never have to worry about being lost.",
"If someone's quietly planned around you your whole relationship... send this to them.",
"But if the planning turns into control, and your yes stops being a choice... that's not care anymore.",
"Because someone who plans three steps ahead for you... is just trying to make sure you never have to.",
]
SCENES = [
S(["when the planner","in the relationship","loves you 📋","they'll check","the weather","for your trip ☀️","three days","before you","even pack"], '''  room('#f1d5b0','#caa070');
  phoneMock(700,780,.65,-.04,()=>{ctx.fillStyle='#d9e8f2';ctx.fillRect(-70,-290,140,280);ctx.font='28px Poppins';ctx.textAlign='center';ctx.fillText('☀️ 72°',0,-140);});
  pup({kind:'girl',x:340,y:G+10,s:1.3,flip:-1,look:[.4,-.1],eyes:'happy',mouth:'smile',blush:.3,tilt:-.05});'''),
S(["they'll have","snacks, chargers 🔌","and a backup plan","in the car","just in case"], '''  room('#e3c9a0','#bf9670');
  bowl(760,G+40,1);
  pup({kind:'boy',x:360,y:G+10,s:1.3,look:[.3,0],eyes:'happy',mouth:'smile',tilt:.04,earLift:.1});'''),
S(["they'll text","\"did you eat?\" 🍽️","before they","say anything else","every single day"], '''  room('#f6d7c6','#d6a286');
  phoneMock(540,760,.78,0,()=>{ctx.fillStyle='#eef0f5';ctx.fillRect(-70,-290,140,280);ctx.font='13px Poppins';ctx.fillStyle=INK;ctx.textAlign='center';ctx.fillText('did you eat yet?',0,-200);});
  if(u>2.5)floatHearts(540,900,2.5,u,3,130);'''),
S(["they'll map","the route","the night before 🗺️","so you never","have to worry","about being lost"], '''  room('#f1d5b0','#caa070');
  const k=pop(u,.2,.5);ctx.save();ctx.translate(700,560);ctx.scale(k,k);blob(rectPts(-140,-100,280,200,16),'#fffaf0',{lw:5});ctx.strokeStyle='#ec7489';ctx.lineWidth=5;ctx.beginPath();ctx.moveTo(-90,60);ctx.quadraticCurveTo(0,-80,90,-60);ctx.stroke();ctx.restore();
  pup({kind:'girl',x:300,y:G+10,s:1.25,flip:-1,look:[.5,0],eyes:'happy',mouth:'smile',tilt:-.05});'''),
S(["if someone's","quietly planned","around you 🤍","your whole relationship","send this","to them 💌"], SHARE),
S(["but if the","planning turns","into control 🌧️","and your yes","stops being","a choice","that's not","care anymore"], '''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  pup({kind:'girl',x:640,y:G+10,s:1.3,flip:-1,look:[.1,.3],brows:'sad',mouth:'flat',hy:4});
  if(u>1)raincloudSmall(640,720,win(u,1,7));'''),
S(["because someone","who plans","three steps","ahead for you 🤍","is just trying","to make sure","you never have to"], HUG),
]
IG_LINE = "The weather check. The backup plan in the car. Did you eat, every single day... want to know how they love? Test in our bio... see if they know yours."
IG_CAPS = ["the weather check ☀️","the backup plan","in the car 🔌","\"did you eat?\"","every single day 🤍","want to know yours?","60-second test","in our bio 🔗","take it together","and see if they","know yours 💌"]
IG_RESULT = "Acts of Service"
TT_LINE = "We're two little pups trying to find a thousand people who love like this... If this made you think of someone... follow us. We'll keep making them for you."
