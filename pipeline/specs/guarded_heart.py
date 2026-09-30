import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
import jjlib as J
from _kit import S, HUG, SHARE
TITLE = "when a guarded heart loves you"
BODY_LINES = [
"When someone with a guarded heart finally loves you... they won't say it first. They'll show up early, every time, and let the pattern say it for them.",
"They'll test you without meaning to, a canceled plan, a late reply, just to see if you'll leave.",
"They'll crack a joke right after a real moment. It mattered too much to sit in for long.",
"They'll let you meet the people they don't let just anyone meet. That introduction is their I love you, said in the only language they trust.",
"If someone guarded ever let you all the way in... send this to them. Let them know you noticed.",
"But if you mistake their guard for indifference and give up before they open... you'll prove them right.",
"Because when a guarded heart finally chooses you... it's the biggest risk they know how to take.",
]
SCENES = [
S(["when someone","with a guarded","heart 🔒","finally loves you","they won't","say it first","they'll show up early","every time","and let the","pattern say it","for them"], '''  room('#f1d5b0','#caa070');
  const k=pop(u,.2,.5);ctx.save();ctx.translate(540,560);ctx.scale(k,k);heart(0,0,90,'#ec7489');ctx.strokeStyle=INK;ctx.lineWidth=6;ctx.beginPath();ctx.roundRect(-34,-14,68,48,8);ctx.stroke();ell(0,10,10,10,'#fffaf0');ctx.restore();
  pup({kind:'boy',x:340,y:G+10,s:1.3,look:[.4,.2],eyes:'open',mouth:'flat',earLift:-.05});
  pup({kind:'girl',x:760,y:G+10,s:1.25,flip:-1,look:[-.5,.1],eyes:'happy',mouth:'smile',blush:.2,tilt:-.05});'''),
S(["they'll test you","without meaning to","a canceled plan 📅","a late reply","just to see","if you leave","most people did","they're just checking","if you're","most people"], '''  room('#e3c9a0','#bf9670');
  phoneMock(700,780,.6,-.05,()=>{ctx.fillStyle='#eef0f5';ctx.fillRect(-70,-290,140,280);ctx.font='11px Poppins';ctx.fillStyle=INK;ctx.textAlign='center';ctx.fillText('actually can\\'t make it',0,-140);});
  pup({kind:'boy',x:320,y:G+10,s:1.28,look:[.5,0],eyes:'open',mouth:'flat',earLift:-.15,hy:4});
  if(u>3){ctx.save();ctx.globalAlpha=win(u,3,9);ctx.font='18px Poppins';ctx.textAlign='center';ctx.fillStyle='#9a9a9a';ctx.fillText('(watching to see if you push back)',700,540);ctx.restore();}'''),
S(["they'll crack","a joke 😅","right after","a real moment","not because","it didn't matter","because it mattered","too much to","sit in for long"], '''  room('#f6d7c6','#d6a286');
  pup({kind:'girl',x:640,y:G+10,s:1.32,flip:-1,look:[-.3,.1],eyes:u<3?'happy':'open',mouth:u<3?'smile':'flat',blush:.4*P(u,0,3),tilt:-.06});
  pup({kind:'boy',x:340,y:G+10,s:1.28,look:[.5,0],eyes:'open',mouth:u>3?'smile':'flat',earLift:.05});
  if(u>3.4){ctx.save();ctx.globalAlpha=win(u,3.4,9);bubbleText(340,800,"anyway... you smell like pancakes 😅",1,.85);ctx.restore();}'''),
S(["they'll let you","meet the people","they don't let","just anyone meet 🤍","that introduction","is their","\"i love you\"","said in the","only language","they trust"], '''  room('#f1d5b0','#caa070');plant(970,G+6,.9);
  pup({kind:'boy',x:340,y:G+10,s:1.3,look:[.4,.1],eyes:'happy',mouth:'smile',tilt:.06,earLift:.1});
  pup({kind:'girl',x:640,y:G+10,s:1.3,flip:-1,look:[-.4,.1],eyes:'happy',mouth:'smile',blush:.4,tilt:-.06});
  pup({kind:'boy',x:880,y:G+40,s:.75,look:[-.5,.2],eyes:'happy',mouth:'smile',bandana:false,earLift:.1});
  if(u>2)floatHearts(600,880,2,u,4,150);'''),
S(["if someone guarded","ever let you","all the way in 🤍","send this to them","let them know","you noticed 💌"], SHARE),
S(["but if you","mistake their guard","for indifference","and give up 🌧️","before they open","you'll prove them","right about","everyone"], '''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  ctx.save();ctx.translate(700,560);heart(0,0,90,'#a89aa0');ctx.strokeStyle=INK;ctx.lineWidth=6;ctx.beginPath();ctx.roundRect(-34,-14,68,48,8);ctx.stroke();ell(0,10,10,10,'#5c5560');ctx.restore();
  pup({kind:'girl',x:320,y:G+10,s:1.28,flip:-1,look:[.5,.3],brows:'sad',mouth:'flat',hy:4});
  if(u>1.4)raincloudSmall(320,720,win(u,1.4,7));'''),
S(["because when","a guarded heart","finally chooses you 🤍","it's not","a small thing","it's the biggest","risk they know","how to take"], HUG),
]
IG_LINE = "The early arrivals. The little tests. The people they finally let you meet... want to know how they love? Test in our bio... see if they know yours."
IG_CAPS = ["showing up","early, every time","the quiet tests","letting you meet","the people that matter 🤍","want to know yours?","60-second test","in our bio 🔗","take it together","and see if they","know yours 💌"]
IG_RESULT = "Physical Touch"
TT_LINE = "We're two little pups trying to find a thousand people who love like this... If this made you think of someone... follow us. We'll keep making them for you."
