import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
import jjlib as J
from _kit import S, HUG, SHARE
TITLE = "when he goes quiet after a fight"
BODY_LINES = [
"When he goes quiet after a fight... it's not the silent treatment. He's trying not to say something in anger he can't take back.",
"He'll leave the room for a minute. Not away from you — away from the version of himself that fights dirty.",
"He'll come back and just sit next to you, before either of you says a word. That's him choosing you over being right.",
"He might need an hour before he can talk. He cares too much to answer before he's calm.",
"If you love someone who needs quiet before they can talk... send this so he knows you finally get it.",
"But if the quiet never ends, if he shuts the door and never opens it again... that's not calming down anymore.",
"Because a man who comes back after the silence... chose the relationship over his pride.",
]
SCENES = [
S(["when he","goes quiet","after a fight 🤐","it's not the","silent treatment","he's trying not","to say something","in anger that","he can't","take back"], '''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  windowBox(610,440,300,300,()=>{ctx.fillStyle='#4d5670';ctx.fillRect(600,430,320,320);ell(820,540,26,26,'#d9d5c4',{lw:4});});
  pup({kind:'girl',x:700,y:G+10,s:1.3,flip:1,look:[-.5,.3],brows:'sad',mouth:'flat',earLift:-.3,hy:4});
  pup({kind:'boy',x:300,y:G+10,s:1.32,look:[.3,.2],eyes:'open',mouth:'flat',brows:'sad',earLift:-.4,hy:6,tilt:-.03});
  if(u>2){ctx.save();ctx.globalAlpha=win(u,2,8);ctx.font='22px Poppins';ctx.textAlign='center';ctx.fillStyle=INK;ctx.strokeStyle='#fffaf0';ctx.lineWidth=5;ctx.strokeText('💭 don\\'t say it. don\\'t say it.',300,540);ctx.fillText('💭 don\\'t say it. don\\'t say it.',300,540);ctx.restore();}'''),
S(["he'll leave","the room","for a minute 🚪","not to walk","away from you","he's walking away","from the version","of himself","that fights dirty"], '''  room('#e3c9a0','#bf9670');
  ell(690,G+30,300,70,'#c98f76');ell(690,G+8,240,44,'#f2dcc4',{lw:4});
  const out=P(u,.6,2.4);
  pup({kind:'boy',x:lerp(500,180,out),y:G+10,s:1.25,flip:1,eyes:'open',mouth:'flat',bob:Math.sin(u*4)*3});
  pup({kind:'girl',x:750,y:G+10,s:1.28,flip:-1,look:[-.4,.2],brows:'sad',mouth:'flat',hy:4});
  if(u>3)raincloudSmall(750,730,win(u,3,8)*.5);'''),
S(["he'll come back","and just sit","next to you 🤍","before either of you","says a word","that's not avoidance","that's him choosing you","over being right"], '''  room('#f1d5b0','#caa070');
  const k=pop(u,.3,.8);
  pup({kind:'girl',x:640,y:G+10,s:1.3,flip:-1,look:[-.3,0],brows:'sad',mouth:'flat',hy:2});
  pup({kind:'boy',x:lerp(180,420,P(u,.2,1.8)),y:G+10,s:1.3,look:[.4,0],eyes:'open',mouth:'flat',tilt:.02});
  if(u>2.4)floatHearts(530,880,2.4,u,3,120);'''),
S(["he might need","an hour ⏳","before he can talk","not because he","doesn't care","what you said","because he cares","too much to answer","before he's calm"], '''  room('#f6d7c6','#d6a286');
  ctx.save();ctx.translate(800,520);ell(0,0,90,90,'#fffaf0',{lw:6});ctx.strokeStyle=INK;ctx.lineWidth=6;ctx.lineCap='round';
  ctx.beginPath();ctx.moveTo(0,0);ctx.lineTo(Math.sin(u*1.2)*50,-Math.cos(u*1.2)*50);ctx.stroke();
  ctx.beginPath();ctx.moveTo(0,0);ctx.lineTo(Math.sin(u*.2)*35,-Math.cos(u*.2)*35);ctx.stroke();ctx.restore();
  pup({kind:'boy',x:420,y:G+10,s:1.32,look:[.3,.1],eyes:'closed',mouth:'flat',breath:1,tilt:-.02});
  if(u>3){ctx.save();ctx.globalAlpha=win(u,3,9);ctx.font='20px Poppins';ctx.textAlign='center';ctx.fillStyle=INK;ctx.fillText('(breathing, not brooding)',420,700);ctx.restore();}'''),
S(["if you love","someone who needs","quiet before","they can talk","send this so","he knows you","finally get it 💌"], SHARE),
S(["but if the","quiet never ends 🌫️","if he shuts","the door and","never opens","it again","that's not calming","down anymore","that's checking out"], '''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  blob(rectPts(560,430,220,560,10),'#5c5560');
  pup({kind:'girl',x:340,y:G+10,s:1.3,flip:-1,look:[.5,.3],brows:'sad',mouth:'flat',hy:4});
  if(u>1.6)raincloudSmall(340,720,win(u,1.6,8));'''),
S(["because a man","who comes back","after the silence 🤍","chose the","relationship","over his pride"], HUG),
]
IG_LINE = "The quiet after the fight. The minute he takes. Coming back to sit with you... want to know how he loves? Sixty second test in our bio... see if he knows yours."
IG_CAPS = ["the quiet after","a fight 🤐","the minute he takes","coming back","to sit with you 🤍","want to know his?","60-second test","in our bio 🔗","take it together","and see if he","knows yours 💌"]
IG_RESULT = "Quality Time"
TT_LINE = "We're two little pups trying to find a thousand people who love like this... If this made you think of someone... follow us. We'll keep making them for you."
