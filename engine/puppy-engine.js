<!doctype html><html><head><meta charset="utf-8">
<style>html,body{margin:0;background:#000}canvas{display:block}</style></head>
<body><canvas id="c"></canvas>
<script>
const W=1080,H=1920;
const cv=document.getElementById('c');cv.width=W;cv.height=H;
const MAIN=cv.getContext('2d');
const off=document.createElement('canvas');off.width=W;off.height=H;const OFF=off.getContext('2d');
let ctx=MAIN,T=0,BOIL=0,SC=0,SIL=null;
const INK='#3b2a20';
const fract=x=>x-Math.floor(x);
const hash=n=>fract(Math.sin(n*127.1+311.7)*43758.5453);
const seed=()=>{SC++;return SC*1.731+BOIL*17.37};
const clamp=(x,a=0,b=1)=>Math.max(a,Math.min(b,x));
const lerp=(a,b,k)=>a+(b-a)*k;
const ease=k=>{k=clamp(k);return k<.5?4*k*k*k:1-Math.pow(-2*k+2,3)/2};
const P=(u,a,b)=>ease((u-a)/(b-a));
const back=k=>{k=clamp(k);const c1=1.9,c3=c1+1;return 1+c3*Math.pow(k-1,3)+c1*Math.pow(k-1,2)};
const pop=(u,a,d=.4)=>back((u-a)/d);
const win=(u,a,b,f=.25)=>clamp((u-a)/f)*clamp((b-u)/f); // on/off window

function paint(fill,o={}){
  if(SIL){if(fill&&fill!=='none'){ctx.fillStyle=SIL;ctx.fill();}return;}
  if(fill&&fill!=='none'){ctx.fillStyle=fill;ctx.fill();}
  if(o.stroke!==false){ctx.strokeStyle=o.sc||INK;ctx.lineWidth=o.lw||5.5;ctx.lineJoin='round';ctx.lineCap='round';ctx.stroke();}
}
function ell(cx,cy,rx,ry,fill,o={}){
  const s=seed(),p1=hash(s)*6.28,p2=hash(s+1)*6.28,amp=o.amp??2.4,rot=o.rot||0;
  ctx.beginPath();const N=44;
  for(let i=0;i<=N;i++){const a=i/N*Math.PI*2,n=Math.sin(3*a+p1)*.6+Math.sin(5*a+p2)*.4;
    const x=Math.cos(a)*(rx+n*amp),y=Math.sin(a)*(ry+n*amp);
    const X=cx+x*Math.cos(rot)-y*Math.sin(rot),Y=cy+x*Math.sin(rot)+y*Math.cos(rot);
    i?ctx.lineTo(X,Y):ctx.moveTo(X,Y);}
  ctx.closePath();paint(fill,o);
}
function jit(pts,j){const s=seed();return pts.map((p,i)=>[p[0]+(hash(s+i*3.1)-.5)*2*j,p[1]+(hash(s+i*5.7)-.5)*2*j]);}
function blob(pts,fill,o={}){
  const q=jit(pts,o.j??1.8),n=q.length,m=(a,b)=>[(a[0]+b[0])/2,(a[1]+b[1])/2];
  ctx.beginPath();let st=m(q[n-1],q[0]);ctx.moveTo(st[0],st[1]);
  for(let i=0;i<n;i++){const nx=m(q[i],q[(i+1)%n]);ctx.quadraticCurveTo(q[i][0],q[i][1],nx[0],nx[1]);}
  ctx.closePath();paint(fill,o);
}
function openPath(q){ctx.beginPath();ctx.moveTo(q[0][0],q[0][1]);
  if(q.length==2){ctx.lineTo(q[1][0],q[1][1]);return;}
  for(let i=1;i<q.length-1;i++){const e=i==q.length-2;ctx.quadraticCurveTo(q[i][0],q[i][1],e?q[i+1][0]:(q[i][0]+q[i+1][0])/2,e?q[i+1][1]:(q[i][1]+q[i+1][1])/2);}}
function line(pts,o={}){const q=jit(pts,o.j??1.2);if(SIL)return;openPath(q);ctx.strokeStyle=o.c||INK;ctx.lineWidth=o.lw||5.5;ctx.lineCap='round';ctx.lineJoin='round';ctx.stroke();}
function tube(pts,w,color){const q=jit(pts,1.6);ctx.lineCap='round';ctx.lineJoin='round';
  openPath(q);ctx.strokeStyle=SIL||INK;ctx.lineWidth=w+11;ctx.stroke();if(SIL)return;
  openPath(q);ctx.strokeStyle=color;ctx.lineWidth=w;ctx.stroke();}
function rectPts(x,y,w,h,r){return[[x+r,y],[x+w-r,y],[x+w,y],[x+w,y+r],[x+w,y+h-r],[x+w,y+h],[x+w-r,y+h],[x+r,y+h],[x,y+h],[x,y+h-r],[x,y+r],[x,y]];}
function heart(x,y,sz,col='#ec7489',alpha=1,rot=0){
  if(alpha<=.01)return;ctx.save();ctx.globalAlpha*=clamp(alpha);ctx.translate(x,y);ctx.rotate(rot);ctx.scale(sz/34,sz/34);
  ctx.beginPath();ctx.moveTo(0,16);ctx.bezierCurveTo(-34,-4,-26,-36,0,-17);ctx.bezierCurveTo(26,-36,34,-4,0,16);ctx.closePath();
  ctx.fillStyle=col;ctx.fill();ctx.strokeStyle=INK;ctx.lineWidth=4.5;ctx.lineJoin='round';ctx.stroke();
  ctx.fillStyle='rgba(255,255,255,.7)';ctx.beginPath();ctx.ellipse(-11,-12,5,3.2,-.6,0,7);ctx.fill();
  ctx.restore();}
function floatHearts(x,y,t0,u,n=4,spread=110,col){
  for(let i=0;i<n;i++){const st=t0+i*.45,k=(u-st)/1.8;if(k<0||k>1)continue;
    const hx=x+(hash(i+7)-.5)*spread+Math.sin(k*6+i)*14,hy=y-k*190;
    heart(hx,hy,lerp(18,34,pop(u,st,.3))*(1-k*.2),col||(i%2?'#f08aa0':'#e8667f'),Math.min(1,(1-k)*2.2),Math.sin(k*5+i)*.25);}
}
function sparkle(x,y,sz,a=1,col='#fff3c4'){if(a<=0)return;ctx.save();ctx.globalAlpha*=a;ctx.translate(x,y);ctx.scale(sz/30,sz/30);
  ctx.beginPath();for(let i=0;i<8;i++){const r=i%2?9:30,an=i*Math.PI/4-Math.PI/2;ctx.lineTo(Math.cos(an)*r,Math.sin(an)*r);}ctx.closePath();
  ctx.fillStyle=col;ctx.fill();ctx.strokeStyle=INK;ctx.lineWidth=4;ctx.lineJoin='round';ctx.stroke();ctx.restore();}

/* ---------------- PUPPY ---------------- */
const PAL={boy:{fur:'#dca46a',ear:'#8a5534',muz:'#f6e5c8',patch:'#b67a48'},girl:{fur:'#f8efe3',ear:'#e8b48d',muz:'#fffcf6'}};
function pup(o){
  o=Object.assign({pose:'sit',s:1,flip:1,eyes:'open',look:[0,0],blush:0,mouth:'w',wag:0,earLift:0,tilt:0,hx:0,hy:0,brows:null,paw:null,squash:1,bob:0,puff:0,shades:false,breath:0,blink:0,bandana:true,shadow:true},o);
  const c=PAL[o.kind];
  ctx.save();ctx.translate(o.x,o.y);ctx.scale(o.s*o.flip,o.s);
  if(o.shadow&&!SIL){ctx.save();ctx.globalAlpha=.16;ctx.fillStyle='#4a2e18';ctx.beginPath();ctx.ellipse(o.pose=='sit'?0:10,2,o.pose=='sit'?125:200,17,0,0,7);ctx.fill();ctx.restore();}
  ctx.translate(0,o.bob/o.s);
  if(o.pose=='sit'){
    ctx.save();ctx.scale(1,o.squash);
    const ta=-.55+Math.sin(T*(11+11*o.wag))*.6*o.wag,tb=[52,-48];
    const r=(x,y)=>[tb[0]+x*Math.cos(ta)-y*Math.sin(ta),tb[1]+x*Math.sin(ta)+y*Math.cos(ta)];
    tube([tb,r(46,-18),r(78,-66)],24,c.fur);
    ell(-62,-36,43,34,c.fur);ell(62,-36,43,34,c.fur);
    ell(0,-98,80,93,c.fur);
    if(!SIL)ell(0,-76,44,54,c.muz,{stroke:false});
    if(o.kind=='boy'&&o.bandana)blob([[-68,-160],[0,-150],[68,-160],[42,-126],[0,-100],[-42,-126]],'#6f95ba');
    ell(-33,-14,28,18,c.fur);
    if(!SIL){line([[-40,-8],[-40,-2]],{lw:3.5});line([[-27,-8],[-27,-2]],{lw:3.5});}
    if(o.paw&&o.paw.k>0){const px=lerp(33,o.paw.x,o.paw.k),py=lerp(-14,o.paw.y,o.paw.k);
      tube([[36,-78],[lerp(36,px,.55),lerp(-78,py,.35)],[px,py]],32,c.fur);ell(px,py,26,20,c.fur);
    } else {ell(33,-14,28,18,c.fur);if(!SIL){line([[26,-8],[26,-2]],{lw:3.5});line([[39,-8],[39,-2]],{lw:3.5});}}
    ctx.restore();
    head(o,c,o.hx,-222*o.squash+o.hy,1);
  } else {
    const br=1+Math.sin(T*2.1)*.03*o.breath;
    const ta=.35+Math.sin(T*(7+11*o.wag))*.5*o.wag,tb=[-138,-70];
    const r=(x,y)=>[tb[0]+x*Math.cos(ta)-y*Math.sin(ta),tb[1]+x*Math.sin(ta)+y*Math.cos(ta)];
    tube([tb,r(-40,-22),r(-72,-58)],22,c.fur);
    ell(0,-58*br,150,60*br,c.fur);
    ell(-86,-46*br,56,42*br,c.fur);
    if(!SIL)ell(-86,-8,34,12,c.fur,{lw:4.5});
    ell(100,-16,33,18,c.fur);ell(160,-16,33,18,c.fur);
    head(o,c,122+o.hx,-122*br+o.hy,.95);
  }
  ctx.restore();
}
function eye(x,y,type,look,k=1){
  if(type=='open'||type=='wide'){const s=type=='wide'?1.28:1,ex=x+look[0]*6,ey=y+look[1]*6;
    ctx.fillStyle=INK;ctx.beginPath();ctx.ellipse(ex,ey,13*s,17*s,0,0,7);ctx.fill();
    ctx.fillStyle='#fff';ctx.beginPath();ctx.arc(ex+4*s,ey-6*s,5.2*s,0,7);ctx.fill();
    ctx.beginPath();ctx.arc(ex-4*s,ey+6*s,2.6*s,0,7);ctx.fill();
    if(type=='wide'){ctx.beginPath();ctx.arc(ex+6*s,ey+3*s,1.8*s,0,7);ctx.fill();}
    return;}
  ctx.strokeStyle=INK;ctx.lineWidth=6;ctx.lineCap='round';ctx.beginPath();
  if(type=='happy')ctx.arc(x,y+8,14,Math.PI*1.15,Math.PI*1.85);
  else if(type=='closed')ctx.arc(x,y-8,14,Math.PI*.15,Math.PI*.85);
  else if(type=='squint'){const d=x<0?1:-1;ctx.moveTo(x-12*d,y-10);ctx.lineTo(x+8*d,y);ctx.lineTo(x-12*d,y+10);}
  ctx.stroke();
}
function head(o,c,hx,hy,sc){
  ctx.save();ctx.translate(hx,hy);ctx.rotate(o.tilt);ctx.scale(sc,sc);
  const rx=112+o.puff*9,ry=98+o.puff*3;
  ell(0,0,rx,ry,c.fur);
  if(!SIL){
    if(o.kind=='boy')ell(44,-14,37,33,c.patch,{stroke:false});
    ell(0,40,58,38,c.muz,{lw:3.5});
    // eyes w/ auto blink
    let et=o.eyes;const bl=fract(T*.27+o.blink);if(et=='open'&&bl<.022)et='closed2';
    for(const sd of[-1,1]){if(et=='closed2'){ctx.strokeStyle=INK;ctx.lineWidth=6;ctx.lineCap='round';ctx.beginPath();ctx.moveTo(sd*44-12,-10);ctx.lineTo(sd*44+12,-10);ctx.stroke();}else eye(sd*44,-12,et,o.look);}
    // brows
    if(o.brows){ctx.strokeStyle=INK;ctx.lineWidth=5.5;ctx.lineCap='round';
      for(const sd of[-1,1]){ctx.beginPath();if(o.brows=='sad'){ctx.moveTo(sd*62,-40);ctx.lineTo(sd*30,-50);}else{ctx.moveTo(sd*62,-52);ctx.lineTo(sd*30,-40);}ctx.stroke();}}
    // nose
    ctx.fillStyle=INK;ctx.beginPath();ctx.ellipse(0,15,17,11.5,0,0,7);ctx.fill();
    ctx.fillStyle='rgba(255,255,255,.75)';ctx.beginPath();ctx.ellipse(-5,11,5.5,3,0,0,7);ctx.fill();
    // mouth
    ctx.strokeStyle=INK;ctx.lineWidth=4.5;ctx.lineCap='round';
    const m=o.mouth;
    if(m=='w'||m=='open'){ctx.beginPath();ctx.moveTo(0,25);ctx.lineTo(0,32);ctx.stroke();
      if(m=='open'){ctx.beginPath();ctx.moveTo(-22,34);ctx.quadraticCurveTo(0,72,22,34);ctx.closePath();ctx.fillStyle='#8a3b35';ctx.fill();ctx.stroke();
        ctx.fillStyle='#f28b93';ctx.beginPath();ctx.ellipse(0,50,11,8,0,0,7);ctx.fill();}
      ctx.beginPath();ctx.arc(-11,32,11,.1,Math.PI*.95);ctx.stroke();ctx.beginPath();ctx.arc(11,32,11,Math.PI*.05,Math.PI*.9);ctx.stroke();}
    else if(m=='smile'){ctx.beginPath();ctx.moveTo(0,25);ctx.lineTo(0,31);ctx.stroke();ctx.beginPath();ctx.arc(0,18,24,Math.PI*.25,Math.PI*.75);ctx.stroke();}
    else if(m=='flat'){ctx.beginPath();ctx.moveTo(0,25);ctx.lineTo(0,34);ctx.stroke();ctx.beginPath();ctx.moveTo(-13,40);ctx.quadraticCurveTo(0,36,13,40);ctx.stroke();}
    else if(m=='pout'){ctx.beginPath();ctx.moveTo(0,25);ctx.lineTo(0,32);ctx.stroke();ctx.beginPath();ctx.arc(0,42,7,0,7);ctx.stroke();}
    else if(m=='o'){ctx.beginPath();ctx.moveTo(0,25);ctx.lineTo(0,31);ctx.stroke();ctx.beginPath();ctx.ellipse(0,42,7,9,0,0,7);ctx.fillStyle='#8a3b35';ctx.fill();ctx.stroke();}
    else if(m=='chomp'){ctx.beginPath();ctx.moveTo(0,25);ctx.lineTo(0,32);ctx.stroke();ctx.beginPath();ctx.moveTo(-18,36);ctx.lineTo(-8,42);ctx.lineTo(0,36);ctx.lineTo(8,42);ctx.lineTo(18,36);ctx.stroke();}
    if(o.blush>0){ctx.fillStyle=`rgba(238,110,122,${.55*o.blush})`;for(const sd of[-1,1]){ctx.beginPath();ctx.ellipse(sd*74,30,21,11,0,0,7);ctx.fill();}
      if(o.blush>.6){ctx.strokeStyle=`rgba(200,80,90,${o.blush-.5})`;ctx.lineWidth=3;for(const sd of[-1,1])for(let i=0;i<3;i++){ctx.beginPath();ctx.moveTo(sd*74+(i-1)*9-3,24);ctx.lineTo(sd*74+(i-1)*9+3,34);ctx.stroke();}}}
  }
  // floppy ears
  for(const sd of[-1,1]){ctx.save();ctx.translate(sd*80,-58);ctx.scale(sd,1);
    ctx.rotate(-(.14+o.earLift*.6)+Math.sin(T*3+sd)*.035);
    blob([[-6,-12],[26,-10],[46,24],[50,78],[32,110],[6,104],[-8,62],[-12,18]],c.ear);ctx.restore();}
  if(o.kind=='girl'&&!SIL){ctx.save();ctx.translate(-66,-84);ctx.rotate(-.35);
    blob([[0,0],[-44,-26],[-50,4],[-40,28]],'#ee8fa2');blob([[0,0],[44,-26],[50,4],[40,28]],'#ee8fa2');ell(0,0,14,13,'#f4a9b8');ctx.restore();}
  if(o.shades&&!SIL){ctx.fillStyle='#1f1a1a';ctx.strokeStyle=INK;ctx.lineWidth=5;
    for(const sd of[-1,1]){ctx.beginPath();ctx.roundRect(sd*44-34,-34,68,42,[8,8,20,20]);ctx.fill();ctx.stroke();
      ctx.strokeStyle='rgba(255,255,255,.7)';ctx.lineWidth=4;ctx.beginPath();ctx.moveTo(sd*44-18,-24);ctx.lineTo(sd*44-6,-24);ctx.stroke();ctx.strokeStyle=INK;ctx.lineWidth=5;}
    ctx.beginPath();ctx.moveTo(-10,-26);ctx.lineTo(10,-26);ctx.stroke();}
  ctx.restore();
}
function shadesProp(x,y,s){ctx.save();ctx.translate(x,y);ctx.scale(s,s);ctx.rotate(-.12);ctx.fillStyle='#1f1a1a';ctx.strokeStyle=INK;ctx.lineWidth=5;
  for(const sd of[-1,1]){ctx.beginPath();ctx.roundRect(sd*44-34,-34,68,42,[8,8,20,20]);ctx.fill();ctx.stroke();}ctx.beginPath();ctx.moveTo(-10,-26);ctx.lineTo(10,-26);ctx.stroke();ctx.restore();}

/* ---------------- PROPS / BG ---------------- */
function room(wall,floor,fy=1180,dots='rgba(255,255,255,.16)'){
  ctx.fillStyle=wall;ctx.fillRect(-200,-200,W+400,H+400);
  ctx.fillStyle=dots;for(let y=-40;y<fy;y+=70)for(let x=-40+((y/70)%2)*35;x<W+40;x+=70){ctx.beginPath();ctx.arc(x,y,4,0,7);ctx.fill();}
  ctx.fillStyle=floor;ctx.fillRect(-200,fy,W+400,H);
  ctx.save();ctx.globalAlpha=.25;for(let i=0;i<5;i++)line([[-60,fy+80+i*i*38],[W/2,fy+78+i*i*38],[W+60,fy+82+i*i*38]],{lw:3});ctx.restore();
  line([[-60,fy],[300,fy+3],[760,fy-2],[W+60,fy+1]],{lw:6});
}
function windowBox(x,y,w,h,drawSky){
  blob(rectPts(x-18,y-18,w+36,h+36,20),'#f7ead5');
  ctx.save();blob(rectPts(x,y,w,h,12),'#fff',{stroke:false});ctx.clip();drawSky();ctx.restore();
  blob(rectPts(x,y,w,h,12),'none');
  line([[x+w/2,y],[x+w/2,y+h]],{lw:10,c:'#f7ead5'});line([[x,y+h/2],[x+w,y+h/2]],{lw:10,c:'#f7ead5'});
  line([[x+w/2-6,y],[x+w/2-6,y+h]],{lw:3.5});line([[x+w/2+6,y],[x+w/2+6,y+h]],{lw:3.5});
  line([[x,y+h/2-6],[x+w,y+h/2-6]],{lw:3.5});line([[x,y+h/2+6],[x+w,y+h/2+6]],{lw:3.5});
  blob(rectPts(x-40,y+h+14,w+80,26,8),'#efdcc0');
}
function plant(x,y,s){ctx.save();ctx.translate(x,y);ctx.scale(s,s);
  for(const [a,l] of [[-.5,150],[-.15,190],[.2,170],[.55,130],[-.8,110]]){ctx.save();ctx.rotate(a);blob([[0,0],[-26,-l*.5],[0,-l],[26,-l*.5]],'#8fae7a');line([[0,0],[0,-l*.85]],{lw:3});ctx.restore();}
  blob([[-60,-70],[60,-70],[46,0],[-46,0]],'#cf7f5f');ell(0,-70,62,12,'#e0967a');ctx.restore();}
function frame(x,y,w,h,inner){blob(rectPts(x,y,w,h,10),'#b98a5e');blob(rectPts(x+14,y+14,w-28,h-28,6),'#fbf1e2');inner&&inner(x+w/2,y+h/2);}
function bowl(x,y,treat){ctx.save();ctx.translate(x,y);
  if(treat>0){ctx.save();ctx.translate(0,-66);ctx.scale(treat,treat);tube([[-38,0],[38,0]],20,'#fbeed8');for(const sx of[-1,1])for(const sy of[-1,1])ell(sx*42,sy*11,14,13,'#fbeed8');ctx.restore();}
  blob([[-96,-58],[96,-58],[80,-4],[0,4],[-80,-4]],'#d8705c');ell(0,-58,96,17,'#ee907c');ell(0,-58,76,10,'#9c4a3c',{stroke:false});
  heart(0,-30,20,'#fbeed8');ctx.restore();}
function mug(x,y,s){ctx.save();ctx.translate(x,y);ctx.scale(s,s);
  for(let i=0;i<3;i++){const ph=T*2+i*2;ctx.save();ctx.globalAlpha=.55;line([[-20+i*20,-120],[-28+i*20+Math.sin(ph)*8,-150],[-16+i*20,-180],[-24+i*20+Math.sin(ph+1)*8,-205]],{lw:5,c:'#fff'});ctx.restore();}
  ell(52,-55,24,26,'none',{lw:11});ell(52,-55,24,26,'none',{lw:5,sc:'#fbf5ec'});
  blob(rectPts(-52,-112,104,112,18),'#fbf5ec');ell(0,-108,52,11,'#9b6644');heart(0,-52,26,'#ec7489');ctx.restore();}
function flower(x,y,s){ctx.save();ctx.translate(x,y);ctx.scale(s,s);line([[0,0],[4,-50],[0,-95]],{lw:6,c:'#6f9a5c'});
  blob([[0,-55],[26,-70],[10,-52]],'#8fae7a',{lw:4});for(let i=0;i<5;i++){const a=i/5*6.28;ell(Math.cos(a)*18,-100+Math.sin(a)*18,14,14,'#f6b8c4',{lw:4});}ell(0,-100,11,11,'#f7d76e',{lw:4});ctx.restore();}
function cloud(x,y,s,col){ctx.save();ctx.translate(x,y);ctx.scale(s,s);
  blob([[-110,20],[-120,-10],[-80,-40],[-40,-60],[10,-70],[60,-50],[100,-35],[120,0],[100,25],[0,32]],col||'#aeb4bb');ctx.restore();}
function note(x,y,s,a){if(a<=0)return;ctx.save();ctx.globalAlpha*=a;ctx.translate(x,y);ctx.scale(s,s);ctx.fillStyle=INK;
  ctx.beginPath();ctx.ellipse(-10,0,13,10,-.4,0,7);ctx.fill();ctx.beginPath();ctx.ellipse(30,-12,13,10,-.4,0,7);ctx.fill();
  ctx.lineWidth=5;ctx.strokeStyle=INK;ctx.beginPath();ctx.moveTo(2,-3);ctx.lineTo(2,-55);ctx.lineTo(42,-67);ctx.lineTo(42,-15);ctx.stroke();ctx.restore();}
function zzz(x,y,u,a=1){for(let i=0;i<3;i++){const k=fract(u*.45+i/3);ctx.save();ctx.globalAlpha=a*Math.sin(k*Math.PI);ctx.font='bold '+(26+k*22)+'px Poppins';ctx.fillStyle='#fff8e8';ctx.strokeStyle=INK;ctx.lineWidth=5;ctx.lineJoin='round';
  const zx=x+k*70+Math.sin(k*6)*10,zy=y-k*150;ctx.strokeText('z',zx,zy);ctx.fillText('z',zx,zy);ctx.restore();}}
function bubbleText(x,y,txt,a,sc=1,bg='#fffaf0'){if(a<=0)return;ctx.save();ctx.globalAlpha*=clamp(a);ctx.translate(x,y);ctx.scale(sc,sc);
  ctx.font='bold 40px Poppins';const w=ctx.measureText(txt).width+48;blob([...rectPts(-w/2,-38,w,70,26)],bg,{lw:5});
  ctx.fillStyle=INK;ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText(txt,0,-2);ctx.restore();}

