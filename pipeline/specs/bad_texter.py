import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
import jjlib as J
from _kit import S, HUG, SHARE
TITLE = "when a bad texter loves you"
BODY_LINES = [
"When he's terrible at texting... but loves you... he'll leave you on read for hours. He's not ignoring you, he's just wherever his hands already are.",
"He'll reply to a whole paragraph with just, lol. It's not that he doesn't care. Words on a screen just don't come easy to him.",
"He'll forget good morning texts... but show up at your door with your coffee order memorized.",
"He'd rather say it in person than type it. A text just can't hold what he actually means.",
"If you've been mad at a read receipt from someone who shows up for everything else... send this to him.",
"But if weeks go by and the effort never shows up at all... that's not a texting problem anymore.",
"Because a bad texter who still shows up for you... loves you in the language that actually counts.",
]
SCENES = [
S(["when he's terrible","at texting 📵","but loves you","he'll leave your","message on read","for three hours","not because","he's ignoring you","he's the kind","who's fully wherever","his hands","already are 🐾"], '''  room('#e3c9a0','#bf9670');
  frame(760,470,190,220,(cx,cy)=>heart(cx,cy,52,'#ec7489'));
  pup({kind:'boy',x:440,y:G+10,s:1.34,look:[.5,.2],eyes:'open',mouth:'flat',earLift:.1,paw:{x:130,y:-40,k:.6}});
  phoneMock(340,860,.5,.12,()=>{ctx.fillStyle='#eef0f5';ctx.fillRect(-70,-290,140,280);ctx.fillStyle='#8a94a8';ctx.font='11px Poppins';ctx.textAlign='center';ctx.fillText('Read 2:14pm',0,-40);});'''),
S(["he'll reply","to your whole","paragraph","with just","\"lol\" 😅","it's not that","he doesn't care","words on a screen","have just never","come easy to him"], '''  room('#f6d7c6','#d6a286');
  phoneMock(700,780,.68,-.05,()=>{ctx.fillStyle='#eef0f5';ctx.fillRect(-70,-290,140,280);ctx.fillStyle='#ec7489';ctx.beginPath();ctx.roundRect(-64,-250,128,110,14);ctx.fill();ctx.font='10px Poppins';ctx.fillStyle='#fff';ctx.textAlign='left';const lines=['so today was crazy,','the whole meeting got','moved and then i had to','explain everything twice','and honestly i just','need to vent lol'];lines.forEach((l,i)=>ctx.fillText(l,-58,-224+i*15));
  ctx.beginPath();ctx.roundRect(-30,-110,60,30,14);ctx.fillStyle='#e3e6ec';ctx.fill();ctx.fillStyle=INK;ctx.textAlign='center';ctx.fillText('lol',0,-92);});
  pup({kind:'girl',x:320,y:G+10,s:1.3,flip:-1,look:[.5,-.1],mouth:'flat',brows:'sad',blush:.1,tilt:-.06});'''),
S(["he'll forget","to text","good morning 🌅","but he'll show up","at your door","with your coffee","order memorized ☕"], '''  room('#f1d5b0','#caa070');
  windowBox(150,430,250,260,()=>{const g=ctx.createLinearGradient(0,430,0,690);g.addColorStop(0,'#fbdca0');g.addColorStop(1,'#f6a878');ctx.fillStyle=g;ctx.fillRect(140,420,270,270);});
  const k=pop(u,.3,.6);
  ctx.save();ctx.translate(780,720);ctx.scale(k,k);mug(0,0,1.4);ctx.restore();
  pup({kind:'boy',x:650,y:G+10,s:1.32,look:[-.3,.1],eyes:'happy',mouth:'smile',tilt:.05,earLift:.1,paw:{x:110,y:-40,k:.6}});
  pup({kind:'girl',x:340,y:G+10,s:1.28,flip:-1,look:[.5,-.1],eyes:u>2?'happy':'wide',mouth:'smile',blush:.4*P(u,2,3),tilt:-.06});
  if(u>3)floatHearts(500,860,3,u,4,150);'''),
S(["he'd rather","say it in person","than type it","not because","he's hiding","a text just can't","hold what he","actually means 🤍"], '''  room('#e9ceb8','#c39a76',1180,'rgba(255,255,255,.2)');
  const k=pop(u,.2,.5);
  pup({kind:'boy',x:440,y:G+10,s:1.4,look:[.4,.1],eyes:'happy',mouth:'smile',tilt:.08,earLift:.1});
  pup({kind:'girl',x:660,y:G+10,s:1.4,flip:-1,look:[-.4,.2],eyes:'happy',mouth:'smile',blush:.5,tilt:-.08});
  if(u>1.4){ctx.save();ctx.globalAlpha=win(u,1.4,7);bubbleText(440,800,"i mean it though 🤍",1,.9);ctx.restore();}'''),
S(["if you've ever","been mad","at a read receipt","from someone who","shows up for","everything else","send this","to him 💌"], SHARE),
S(["but if weeks","go by 📆","and the effort","never shows up","anywhere","not in texts","not in person","that's not a","texting problem","anymore"], '''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  ctx.save();ctx.translate(700,540);blob(rectPts(-140,-100,280,200,16),'#fffaf0',{lw:5});ctx.strokeStyle='#e8d9c3';ctx.lineWidth=3;for(let i=1;i<4;i++){ctx.beginPath();ctx.moveTo(-120,-60+i*50);ctx.lineTo(120,-60+i*50);ctx.stroke();}ctx.font='16px Poppins';ctx.fillStyle='#9a9a9a';ctx.textAlign='center';ctx.fillText('(nothing planned)',0,20);ctx.restore();
  pup({kind:'girl',x:320,y:G+10,s:1.3,flip:-1,look:[.6,.4],brows:'sad',mouth:'flat',earLift:-.3,hy:6});
  if(u>1.6)raincloudSmall(320,720,win(u,1.6,8));'''),
S(["because a","bad texter","who still","shows up for you","loves you in the","language that","actually counts 🤍"], HUG),
]
IG_LINE = "The read receipts. The one-word replies. Showing up anyway... want to know how he loves? Sixty second test in our bio... see if he knows yours."
IG_CAPS = ["the read receipts 📵","the one-word replies","showing up anyway 🤍","every guy shows","love in his own way","want to know his?","60-second test","in our bio 🔗","take it together","and see if he","knows yours 💌"]
IG_RESULT = "Acts of Service"
TT_LINE = "We're two little pups trying to find a thousand people who love like this... If this made you think of someone... follow us. We'll keep making them for you."
