import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD
TITLE = "a loyal woman"
BODY_LINES = [
"A loyal woman doesn't flip her phone face down. She's got nothing on it to hide.",
"She tells you about the guy at work who flirted with her... before you even ask.",
"She leaves the night out early. Not because she has to. Because she misses you.",
"When another man flirts with her, she says \"my boyfriend\" in the first sentence.",
"If she's loyal like this... send this to the man who deserves her.",
"But if you're always guessing where you stand with her... you're not paranoid.",
"Because a loyal woman never makes you feel replaceable.",
]
D = [
'''  room('#f3cfa8','#d09d72');
  ell(560,G+40,420,70,'#e7b9a0',{lw:5});
  const sl=P(u,1.2,2.8);
  pup({kind:'boy',x:780,y:G+10,s:1.3,flip:-1,look:[-.7,0],eyes:'open',mouth:'smile',blush:.3,tilt:.04});
  pup({kind:'girl',x:300,y:G+10,s:1.3,look:[.7,0],eyes:'happy',mouth:'smile',tilt:-.05,paw:{x:150,y:-60,k:sl}});
  phoneMock(lerp(380,600,sl),lerp(1000,1050,sl),.36,lerp(-.1,.4,sl),()=>{ctx.fillStyle='#dfe4ee';ctx.fillRect(-70,-290,140,280);ctx.fillStyle='#ec7489';ctx.fillRect(-60,-260,120,26);ctx.fillStyle='#b7c0d4';for(let i=0;i<5;i++)ctx.fillRect(-60,-215+i*38,120,8);});
  if(u>3.4)floatHearts(560,860,3.4,u,4,160);''',
'''  room('#d9e2c8','#a9b38f');
  pup({kind:'girl',x:330,y:G+10,s:1.3,look:[.6,0],eyes:'open',mouth:'smile',tilt:-.04,brows:u<2?'sad':undefined});
  pup({kind:'boy',x:760,y:G+10,s:1.3,flip:-1,look:[-.6,0],eyes:'open',mouth:'smile',blush:.3});
  const k=pop(u,.6,.5);ctx.save();ctx.globalAlpha=win(u,.6,6);bubbleText(360,700,"a guy at work flirted 🙄",1,.85*k);ctx.restore();
  if(u>3)floatHearts(760,820,3,u,3,120);''',
'''  room('#3d4b6c','#303b57','rgba(255,255,255,.06)');
  blob(rectPts(700,520,300,660,16),'#b98a5e');blob(rectPts(730,560,240,620,10),'#f6d688',{stroke:false});
  const lg=ctx.createRadialGradient(850,860,20,850,860,420);lg.addColorStop(0,'rgba(255,214,120,.5)');lg.addColorStop(1,'rgba(255,214,120,0)');ctx.fillStyle=lg;ctx.fillRect(300,400,800,900);
  pup({kind:'boy',x:880,y:G+10,s:1.0,flip:-1,eyes:'happy',mouth:'smile',blush:.5,wag:.4});
  const wk=P(u,.6,4.6);
  pup({kind:'girl',x:lerp(120,600,wk),y:G+14,s:1.3,bob:(wk>0&&wk<1)?-Math.abs(Math.sin(u*8))*12:0,flip:1,eyes:'happy',mouth:'smile',wag:.3});
  if(u>4.6)floatHearts(760,780,4.6,u,4,120);''',
'''  room('#d9b9c9','#a98496','rgba(255,255,255,.1)');
  pup({kind:'boy',x:780,y:G+10,s:1.15,flip:-1,look:[-.6,0],eyes:'happy',mouth:'smile',blush:.6,tilt:.08,bandana:false});shadesProp(780,1005,.85);
  if(u>.8&&u<2.6){ctx.save();ctx.globalAlpha=win(u,.8,2.6);heart(690,720,40,'#ff6b9d');ctx.restore();}
  pup({kind:'girl',x:340,y:G+10,s:1.4,look:[.6,0],eyes:'open',mouth:'smile',tilt:-.05});
  if(u>2.2){const k=pop(u,2.2,.4);ctx.save();ctx.globalAlpha=win(u,2.2,8);bubbleText(380,730,"my boyfriend says hi 🙂",1,.85*k);ctx.restore();}''',
SHARE,
'''  room('#8f8b95','#716c75','rgba(255,255,255,.07)');
  blob(rectPts(160,G-140,760,26,10),'#a58363');
  phoneMock(560,G-160,.3,.03,()=>{ctx.fillStyle='#2b2830';ctx.fillRect(-70,-290,140,280);});
  pup({kind:'boy',x:290,y:G+10,s:1.25,look:[.7,.3],brows:'sad',mouth:'flat',earLift:-.3});
  pup({kind:'girl',x:800,y:G+10,s:1.25,flip:-1,look:[.2,.7],eyes:'open',mouth:'flat'});
  if(u>1)raincloudSmall(290,720,win(u,1,9));''',
HUG,
]
SCENES = spec(BODY_LINES, D, [{'phone':'📱'},{'ask':'🤍'},{'misses':'🏡'},{'boyfriend':'🙂'},{'deserves':'💌'},None,{'replaceable':'🤍'}])
IG_LINE = "The phone. The night out. My boyfriend. Every girl shows love her own way... Want to know hers? There's a sixty second test in our bio. Take it together."
from _kit2 import C
IG_CAPS = C(IG_LINE, {'phone':'📱','hers':'🤍','bio':'🔗'})
IG_RESULT = "Quality Time"
TT_LINE = TT_STD
