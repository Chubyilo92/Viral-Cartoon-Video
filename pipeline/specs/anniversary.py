import sys; sys.path.insert(0, '/home/claude/jj'); sys.path.insert(0, '/home/claude/jj/specs')
from dialogue import D, ENDCARD
import biscuit as B

# VIRAL-BLUEPRINT adapted to the SHARED CALENDAR + NOTIFICATIONS feature.
# Real problem: important dates live in one person's head. Forgotten thing: their anniversary.
# Feature "fails": the day is empty in the shared calendar. TWIST: she was the one who was supposed to
# put every important date in (so he'd get notified) - "so why are you mad at ME?"
# Solution: she adds it, his phone pings instantly. Laugh button: his mum's birthday is tomorrow.
TITLE = "she broke up with me over this"
MUSIC_N = 1
PRELUDE = B.PRELUDE + r'''
function calPhone(x,y,s,rot,day,rows,empty){phoneMock(x,y,s,rot,()=>{appUI('shared calendar');
  ctx.fillStyle=INK;ctx.textAlign='center';ctx.font='bold 15px Poppins';ctx.fillText(day,0,-206);
  if(empty){ctx.save();ctx.setLineDash([5,5]);ctx.strokeStyle='#c9b9be';ctx.lineWidth=2;ctx.beginPath();ctx.roundRect(-58,-190,116,60,12);ctx.stroke();ctx.restore();
    ctx.fillStyle='#a8979c';ctx.font='12px Poppins';ctx.fillText('nothing today',0,-155);}
  rows.forEach((r,i)=>{ctx.save();ctx.strokeStyle='#ff6b9d';ctx.lineWidth=3;ctx.fillStyle='#fff';ctx.beginPath();ctx.roundRect(-58,-190+i*64,116,56,12);ctx.fill();ctx.stroke();ctx.restore();
    ctx.fillStyle=INK;ctx.textAlign='center';ctx.font='bold 12px Poppins, "Noto Color Emoji"';ctx.fillText(r[0],0,-166+i*64);ctx.font='10px Poppins, "Noto Color Emoji"';ctx.fillText(r[1],0,-148+i*64);});});}
function ping(x,y,s,title,sub,a){if(a<=0)return;ctx.save();ctx.translate(x,y);ctx.scale(s*(.8+.2*back(clamp(a*2))),s*(.8+.2*back(clamp(a*2))));ctx.globalAlpha=clamp(a*3);
  ctx.fillStyle='rgba(255,255,255,.97)';ctx.strokeStyle=INK;ctx.lineWidth=5;ctx.beginPath();ctx.roundRect(-230,-70,460,140,30);ctx.fill();ctx.stroke();
  heart(-180,-30,22,'#ff6b9d');ctx.fillStyle='#8a7b80';ctx.font='bold 22px Poppins';ctx.textAlign='left';ctx.textBaseline='middle';ctx.fillText('reminder · now',-148,-30);
  ctx.fillStyle=INK;ctx.font='bold 32px Poppins, "Noto Color Emoji"';ctx.fillText(title,-200,14);ctx.font='22px Poppins, "Noto Color Emoji"';ctx.fillText(sub,-200,48);ctx.restore();}
function ring(x,y,u){ctx.save();ctx.strokeStyle=INK;ctx.lineWidth=5;ctx.lineCap='round';for(let i=0;i<3;i++){const r=30+i*22+Math.sin(u*14)*3;ctx.globalAlpha=.7-i*.2;ctx.beginPath();ctx.arc(x,y,r,-.7,.7);ctx.stroke();ctx.beginPath();ctx.arc(x,y,r,Math.PI-.7,Math.PI+.7);ctx.stroke();}ctx.restore();}
'''
RED, SAD, CALM, FLICK, SH, STAKES = B.RED, B.SAD, B.CALM, B.FLICK, B.SH, B.STAKES
HOOK = "corner('he forgot something HUGE 👇',1);"

LINES = [
D('girl', "You never satisfy me anyway!", RED + HOOK + '''
  SP('girl',u,{x:320,flip:-1,look:[.6,0],brows:'angry',talk:1,mouth:'open',earLift:.5,tilt:-.08,%s,s:1.4});
  SP('boy',u,{x:790,look:[-.6,0],brows:'sad',mouth:'o',eyes:'wide',earLift:-.3,s:1.3});''' % SH, '😡'),
D('boy', "Then go back to your ex!", RED + HOOK + '''
  SP('girl',u,{x:300,flip:-1,look:[.6,0],brows:'angry',mouth:'o',eyes:'wide',earLift:.5,s:1.3});
  SP('boy',u,{x:790,look:[-.6,0],brows:'angry',talk:1,mouth:'open',earLift:.5,tilt:.08,%s,s:1.4});''' % SH, '🤬'),
D('girl', "Maybe I will. My ex was better than you!", RED + HOOK + '''
  SP('girl',u,{x:300,flip:-1,look:[.6,-.1],brows:'angry',talk:1,mouth:'flat',eyes:'squint',tilt:-.12});
  SP('boy',u,{x:790,look:[-.6,0],brows:'sad',mouth:'o',eyes:'wide',earLift:-.5,squash:lerp(1,.94,P(u,1.6,2.2))});
  raincloudSmall(540,640,win(u,.3,9));''', '💔'),
D('boy', "Your ex CHEATED on you!", RED + HOOK + '''
  SP('girl',u,{x:300,flip:-1,look:[.6,0],brows:'sad',mouth:'o',eyes:'wide',earLift:-.4});
  SP('boy',u,{x:790,look:[-.6,-.1],brows:'angry',talk:1,mouth:'open',earLift:.5,%s});
  raincloudSmall(540,640,1);raincloudSmall(400,580,win(u,.3,9));''' % SH, '😤'),
D('girl', "At least HE remembered what today was.", RED + "corner('wait for it 👀',win(u,.5,9));" + '''
  SP('girl',u,{x:lerp(300,-80,P(u,1.6,2.4)),look:[-.5,.3],brows:'angry',talk:1,mouth:'flat',eyes:'squint'});
  SP('boy',u,{x:790,look:[-.6,0],brows:'sad',mouth:'flat',eyes:'wide'});
  raincloudSmall(540,640,1);raincloudSmall(400,580,1);raincloudSmall(700,600,1);''', '🚪'),
D('boy', "...What IS today?", SAD + "chip('1 HOUR LATER',win(u,.1,2.6));" + '''
  SP('boy',u,{x:540,look:[.2,.4],brows:'sad',talk:1,mouth:'o',eyes:'wide',earLift:-.4,tilt:.12});
  raincloudSmall(540,640,1);''', '😰'),
D('boy', "Babe... remember why we got the app?", SAD + '''
  const k=P(u,.0,1.0);
  SP('girl',u,{x:330,flip:-1,look:[.6,0],brows:'angry',mouth:'pout',eyes:'squint',earLift:-.2});
  SP('boy',u,{x:lerp(1100,760,k),look:[-.5,.1],brows:'sad',talk:1,mouth:'flat',earLift:-.3});''', '📱'),
D('girl', "Fine. Check it. If it's not in there... we're done.", SAD + "corner('last try 💔',win(u,2.2,9));" + '''
  SP('girl',u,{x:330,flip:-1,look:[.6,0],brows:'angry',talk:1,mouth:'flat',earLift:-.2});
  SP('boy',u,{x:760,look:[-.5,.1],brows:'sad',mouth:u>2.6?'o':'flat',eyes:u>2.6?'wide':'open',earLift:-.2});'''),
D('boy', "Shared calendar... today... nothing.", CALM + STAKES + '''
  const r=pop(u,.2,.5);
  SP('girl',u,{x:250,s:1.1,flip:-1,look:[.5,-.2],brows:'angry',mouth:'flat'});
  SP('boy',u,{x:510,s:1.1,look:[.5,-.2],talk:1,mouth:'flat',brows:'sad',paw:{x:90,y:-150,k:P(u,.1,.5)}});
  calPhone(830,1010-r*40,1.5*r+.01,-.04,'Today · 14 Oct',[],u>1.4);''', '📅'),
D('girl', "It's our ANNIVERSARY!", CALM + FLICK + "corner('last try 💔',1);" + '''
  SP('girl',u,{x:330,flip:-1,look:[.6,0],brows:'angry',talk:1,mouth:'open',earLift:.5,%s});
  SP('boy',u,{x:760,look:[-.5,0],eyes:'wide',brows:'sad',mouth:'o',earLift:-.4});
  if(u>.6){ctx.save();ctx.globalAlpha=win(u,.6,9);const k=pop(u,.6,.4);heart(540,640,70*k,'#ec7489');ctx.font='bold 44px Poppins, "Noto Color Emoji"';ctx.textAlign='center';ctx.fillStyle=INK;ctx.fillText('the thing he forgot',540,520);ctx.restore();}''' % SH, '💔'),
D('boy', "Wait. You said you'd put every important date in here, so I get notified.", CALM + STAKES + '''
  SP('girl',u,{x:300,flip:-1,look:[.5,.1],eyes:'open',brows:'angry',mouth:'flat'});
  SP('boy',u,{x:780,look:[-.5,.1],eyes:'squint',talk:1,mouth:'flat',tilt:.1,paw:{x:-110,y:-130,k:P(u,.6,1)}});
  calPhone(545,960,1.35,0,'Today · 14 Oct',[],1);''', '🤨'),
D('boy', "So... why are you mad at ME?", CALM + "corner('plot twist 👀',win(u,.3,9));" + '''
  SP('girl',u,{x:300,flip:-1,look:[.5,.2],eyes:u>.9?'wide':'open',brows:'sad',mouth:u>.9?'o':'flat',blush:lerp(0,.9,P(u,.9,1.6)),earLift:u>.9?-.4:0,squash:u>.9?.96:1});
  SP('boy',u,{x:780,look:[-.5,.1],eyes:'squint',talk:1,mouth:'smile',tilt:.12});
  sparkle(540,620,46*pop(u,.9,.4),win(u,.9,9));''', '😏'),
D('girl', "...I may have forgotten to put it in.", CALM + '''
  SP('girl',u,{x:300,flip:-1,look:[.3,.4],eyes:'closed2',brows:'sad',talk:1,mouth:'pout',blush:1,earLift:-.5,hy:6});
  SP('boy',u,{x:780,look:[-.5,.1],eyes:'happy',mouth:'smile',wag:.6});''', '🙈'),
D('girl', "Adding it now. Every year.", CALM + "corner('it worked 💗',win(u,1.6,9));" + '''
  const r=pop(u,.1,.5);
  SP('girl',u,{x:260,s:1.1,flip:-1,look:[.5,-.2],talk:1,mouth:'smile',blush:.6,paw:{x:90,y:-150,k:P(u,.1,.5)}});
  SP('boy',u,{x:520,s:1.1,look:[-.4,0],eyes:'happy',mouth:'smile'});
  calPhone(830,1010-r*40,1.5*r+.01,-.04,'Today · 14 Oct',u>1?[['💗 our anniversary','every year · notify him']]:[],u<=1);''', '💗'),
D('boy', "Anniversary. Tonight. Get your coat, I'm taking you out.", CALM + '''
  const hug=P(u,2.4,3.2);
  ping(540,600,1.35,'💗 our anniversary','tonight · added by her',P(u,.05,.4));
  if(u<1)ring(780,G-300,u);
  SP('girl',u,{x:lerp(300,400,hug),flip:-1,look:[.5,0],eyes:'happy',mouth:'smile',blush:.7,paw:{x:70,y:-190,k:hug}});
  SP('boy',u,{x:lerp(780,680,hug),look:[-.5,-.2],eyes:u<.8?'wide':'happy',talk:1,mouth:'smile',blush:.5,wag:1});
  if(u>2.6)floatHearts(540,820,2.6,u,6,170);''', '🥹'),
D('girl', "Oh, and your mum's birthday... is tomorrow.", CALM + '''
  ping(540,600,1.35,'🎂 his mum\\'s birthday','tomorrow · added by her',P(u,1.6,2));
  if(u>1.6&&u<2.6)ring(700,G-330,u);
  SP('girl',u,{x:400,flip:-1,look:[.5,0],eyes:'squint',talk:1,mouth:'smile',blush:.5,tilt:-.1});
  SP('boy',u,{x:680,look:[-.5,-.2],eyes:u>2?'wide':'happy',mouth:u>2?'o':'smile',earLift:u>2?.5:0,hx:u>2.2?Math.sin(u*40)*3:0});''', '😂'),
]

END = D('girl', "Love shouldn't depend on one person's memory. Put it in once, and you both get reminded. Link in bio!",
        ENDCARD('never forget the big days', ''), '🔗')
