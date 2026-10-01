import sys; sys.path.insert(0, '/home/claude/jj')
from dialogue import D, ENDCARD

# Twist: what looks like a cheeky "browny points for brownies" bit is a proposal he saved 3 months of points for.
TITLE = "he's been saving browny points"
MUSIC_N = 3

K = "room('#f6dfc0','#cfa679');"
N = "room('#3d4b6c','#303b57','rgba(255,255,255,.05)');"
PRELUDE = r'''
function ringBox(x,y,s,open){ctx.save();ctx.translate(x,y);ctx.scale(s,s);
  blob(rectPts(-70,-60,140,60,10),'#b8324b',{lw:6});
  ctx.save();ctx.translate(0,-60);ctx.rotate(-open*1.2);blob(rectPts(-70,-44,140,44,10),'#c94660',{lw:6});ctx.restore();
  if(open>.3){ctx.save();ctx.globalAlpha=clamp((open-.3)/.5);blob(rectPts(-46,-92,92,40,8),'#6d3f27',{lw:5});
    ell(0,-118,24,24,'none',{lw:9,sc:'#f2c55c'});ell(0,-118,24,24,'none',{lw:3});
    ctx.save();ctx.translate(0,-146);ctx.rotate(Math.PI/4);blob(rectPts(-12,-12,24,24,3),'#dff4ff',{lw:4});ctx.restore();
    sparkle(26,-160,22,.5+.5*Math.sin(T*6));ctx.restore();}
  ctx.restore();}
function tears(x,y,u){ctx.save();ctx.fillStyle='#8fc8f0';ctx.strokeStyle=INK;ctx.lineWidth=3;for(const sd of[-1,1]){const yy=y+fract(u*.9+(sd>0?.5:0))*60;ctx.beginPath();ctx.ellipse(x+sd*56,yy,8,12,0,0,7);ctx.fill();ctx.stroke();}ctx.restore();}
'''

def pts_phone(n, sub):
    return '''phoneMock(830,1020-r*40,1.4*r+.01,-.04,()=>{appUI('browny points');
    ctx.fillStyle=INK;ctx.textAlign='center';ctx.font='bold 42px Poppins';ctx.fillText(Math.round(%d*P(u,.4,2)),0,-160);
    ctx.font='12px Poppins';ctx.fillText(%r,0,-138);
    pill(-118,'🍽️ dishes x40',true,'#3fae6a');pill(-82,'🧺 laundry x25',true,'#3fae6a');pill(-46,'💗 mood check x90',true,'#3fae6a');});''' % (n, sub)

LINES = [
D('girl', "Okay. Why are you doing the dishes AGAIN?", K + "chip('DAY 87 🧽',win(u,.1,2.6));" + '''
  SP('girl',u,{x:300,flip:-1,look:[.6,0],eyes:'squint',brows:'angry',talk:1,mouth:'flat',tilt:-.06});
  SP('boy',u,{x:780,look:[-.3,.3],eyes:'open',mouth:'smile',wag:.4,paw:{x:-70,y:-100,k:.6+.2*Math.sin(u*8)}});
  for(let i=0;i<4;i++){ell(880+Math.sin(T*3+i)*30,800-((u*80+i*60)%240),12+i*2,12+i*2,'rgba(255,255,255,.75)',{lw:3});}''', '🤨'),
D('boy', "No reason! Just... earning browny points.", K + '''
  SP('girl',u,{x:300,flip:-1,look:[.6,0],eyes:'squint',mouth:'flat'});
  SP('boy',u,{x:780,look:[-.5,0],eyes:'happy',talk:1,blush:.5,wag:.8,tilt:.08});''', '😇'),
D('girl', "Babe. You have nine hundred points.", K + '''
  const r=pop(u,.2,.5);
  SP('girl',u,{x:260,s:1.1,flip:-1,look:[.6,-.2],eyes:'wide',talk:1,mouth:'o'});
  SP('boy',u,{x:510,s:1.1,look:[-.4,0],eyes:'happy',mouth:'smile',blush:.4});
  ''' + pts_phone(900, 'saved since July'), '😳'),
D('boy', "I'm saving for something big.", K + '''
  SP('girl',u,{x:300,flip:-1,look:[.6,0],eyes:'squint',mouth:'pout'});
  SP('boy',u,{x:780,look:[-.5,0],eyes:'squint',talk:1,mouth:'smile',tilt:.1});''', '🤫'),
D('girl', "If this is another tray of brownies...", K + '''
  SP('girl',u,{x:300,flip:-1,look:[.6,0],eyes:'squint',brows:'angry',talk:1,mouth:'smile',tilt:-.08});
  SP('boy',u,{x:780,look:[-.5,0],eyes:'happy',mouth:'smile',wag:.5});''', '🍫'),
D('boy', "It is brownies.", N + "chip('that night',win(u,.1,2.4));" + '''
  const lg=ctx.createRadialGradient(540,880,20,540,880,520);lg.addColorStop(0,'rgba(255,210,140,.45)');lg.addColorStop(1,'rgba(255,210,140,0)');ctx.fillStyle=lg;ctx.fillRect(-100,-100,W+200,H+200);
  brownies(560,G+40,1,1);
  SP('girl',u,{x:300,flip:-1,look:[.5,.3],eyes:'happy',mouth:'smile',blush:.3,shadow:false});
  SP('boy',u,{x:800,look:[-.5,.2],eyes:'open',talk:1,mouth:'smile',blush:.4,shadow:false});''', '🍫'),
D('boy', "...With something on top.", N + '''
  const lg=ctx.createRadialGradient(540,880,20,540,880,520);lg.addColorStop(0,'rgba(255,210,140,.5)');lg.addColorStop(1,'rgba(255,210,140,0)');ctx.fillStyle=lg;ctx.fillRect(-100,-100,W+200,H+200);
  brownies(560,G+40,1,1);
  ringBox(560,G-10,2.1,P(u,.6,1.4));
  if(u>1.3)sparkle(600,G-380,70,win(u,1.3,9));
  SP('girl',u,{x:300,flip:-1,look:[.5,.3],eyes:u>1.2?'wide':'happy',mouth:u>1.2?'o':'smile',blush:.5,earLift:u>1.2?.4:0,shadow:false});
  SP('boy',u,{x:800,look:[-.5,.2],eyes:'open',talk:1,mouth:'smile',blush:.6,shadow:false});''', '💍'),
D('boy', "Will you marry me?", N + '''
  const lg=ctx.createRadialGradient(540,880,20,540,880,520);lg.addColorStop(0,'rgba(255,210,140,.55)');lg.addColorStop(1,'rgba(255,210,140,0)');ctx.fillStyle=lg;ctx.fillRect(-100,-100,W+200,H+200);
  brownies(560,G+40,1,1);ringBox(560,G-10,2.1,1);
  SP('girl',u,{x:300,flip:-1,look:[.5,.2],eyes:'wide',mouth:'o',blush:.9,earLift:.4,shadow:false});
  if(u>.9)tears(300-0,G-210,u);
  SP('boy',u,{x:800,look:[-.5,0],eyes:'open',talk:1,mouth:'smile',blush:.7,shadow:false,tilt:.06});''', '💍'),
D('girl', "YES! Yes, yes, yes!", N + '''
  const lg=ctx.createRadialGradient(540,880,20,540,880,560);lg.addColorStop(0,'rgba(255,190,200,.55)');lg.addColorStop(1,'rgba(255,190,200,0)');ctx.fillStyle=lg;ctx.fillRect(-100,-100,W+200,H+200);
  const hug=P(u,.3,1);
  SP('girl',u,{x:lerp(300,440,hug),flip:-1,look:[.4,.1],eyes:'happy',talk:1,mouth:'open',blush:1,wag:1,paw:{x:70,y:-190,k:hug},bob:-Math.abs(Math.sin(u*8))*14,shadow:false});
  SP('boy',u,{x:lerp(800,650,hug),look:[-.4,.1],eyes:'happy',mouth:'smile',blush:.7,wag:1,shadow:false});
  floatHearts(540,820,0,u,8,240);sparkle(400,560,50,win(u,.3,9));sparkle(720,520,40,win(u,.5,9));''', '😭💍'),
]

END = D('girl', "He saved nine hundred browny points for this. Tag the one who'd do it for you. CoupleIn, link in bio!",
        ENDCARD('earn points. spend on love.', 'ringBox(400,G+60,.6,1);'), '💍')
