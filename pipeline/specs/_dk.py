"""Shared JS for the Dinkly-style JJ remakes: chibi JJ rig + scene helpers."""
DK_JS = r'''
/* CHIBI JJ (19 Nov 2026): round mochi-body pups, huge glossy eyes, tiny features, always-on blush.
   Same identity as JJ: boy = tan fur, brown ears, eye patch, blue bandana; girl = cream fur, tan ears, pink bow. */
function cheye(x,y,type,look){ctx.save();
  if(type=='open'||type=='cute'||type=='wide'){const s=type=='wide'?1.15:1,ex=x+look[0]*6,ey=y+look[1]*6;
    ctx.fillStyle=INK;ctx.beginPath();ctx.ellipse(ex,ey,21*s,26*s,0,0,7);ctx.fill();
    ctx.fillStyle='#fff';ctx.beginPath();ctx.arc(ex+7,ey-9,8.5,0,7);ctx.fill();ctx.beginPath();ctx.arc(ex-7,ey+9,4,0,7);ctx.fill();ctx.beginPath();ctx.arc(ex+9,ey+6,2.4,0,7);ctx.fill();}
  else{ctx.strokeStyle=INK;ctx.lineWidth=7;ctx.lineCap='round';ctx.beginPath();
    if(type=='happy')ctx.arc(x,y+10,17,Math.PI*1.15,Math.PI*1.85);
    else if(type=='closed')ctx.arc(x,y-6,16,Math.PI*.15,Math.PI*.85);
    else if(type=='squint'){const d=x<0?1:-1;ctx.moveTo(x-13*d,y-11);ctx.lineTo(x+9*d,y);ctx.lineTo(x-13*d,y+11);}
    ctx.stroke();}
  ctx.restore();}
pup=function(o){
  o=Object.assign({s:1,flip:1,eyes:'open',look:[0,0],blush:.6,mouth:'w',tilt:0,brows:null,paw:null,squash:1,bob:0,wag:0,shadow:true,bandana:true},o);
  const c=PAL[o.kind],boy=o.kind=='boy';
  ctx.save();ctx.translate(o.x,o.y+o.bob);ctx.scale(o.s*o.flip*1.08,o.s*1.08);
  if(o.shadow){ctx.save();ctx.globalAlpha=.15;ctx.fillStyle='#4a2e18';ctx.beginPath();ctx.ellipse(0,0,120,15,0,0,7);ctx.fill();ctx.restore();}
  ctx.rotate(o.tilt*.6);ctx.scale(1,o.squash);
  // tail nub
  const wa=Math.sin(T*(8+10*o.wag))*.35*(.3+o.wag);ctx.save();ctx.translate(108,-46);ctx.rotate(-.6+wa);ell(18,0,26,15,c.fur);ctx.restore();
  // one round mochi body/head
  ell(0,-132,128,134,c.fur,{lw:5.5});
  if(boy)ell(46,-160,40,36,c.patch,{stroke:false});
  // floppy ears, in front, hanging off the top sides
  for(const sd of[-1,1]){ctx.save();ctx.translate(sd*96,-232);ctx.scale(sd,1);ctx.rotate(-.15+Math.sin(T*3+sd)*.05);
    blob([[-26,-6],[18,-14],[44,14],[50,62],[36,96],[10,100],[-10,74],[-22,30]],c.ear,{lw:5});ctx.restore();}
  // feet + arms
  ell(-48,-6,30,17,c.fur,{lw:5});ell(48,-6,30,17,c.fur,{lw:5});
  if(o.paw&&o.paw.k>0){const px=lerp(70,o.paw.x,o.paw.k),py=lerp(-60,o.paw.y,o.paw.k);tube([[78,-80],[px,py]],34,c.fur);ell(px,py,22,18,c.fur,{lw:5});}
  else ell(84,-62,22,18,c.fur,{lw:5});
  ell(-84,-62,22,18,c.fur,{lw:5});
  // bandana (boy) / bow (girl)
  if(boy&&o.bandana){blob([[-52,-62],[0,-54],[52,-62],[22,-36],[0,-22],[-22,-36]],'#6f95ba',{lw:4.5});ell(0,-58,10,8,'#5a7fa3',{lw:3.5});}
  if(!boy){ctx.save();ctx.translate(-70,-236);ctx.rotate(-.3);blob([[0,0],[-44,-26],[-50,4],[-40,28]],'#ee8fa2');blob([[0,0],[44,-26],[50,4],[40,28]],'#ee8fa2');ell(0,0,14,13,'#f4a9b8');ctx.restore();}
  if(o.old){ctx.save();ctx.fillStyle='#f4f4f4';for(let i=0;i<5;i++){ell(-40+i*20,-262+Math.abs(i-2)*6,16,14,'#f4f4f4',{lw:3.5});}ctx.restore();}
  // face
  let et=o.eyes;const bl=fract(T*.27+(o.blink||0));if((et=='open'||et=='cute')&&bl<.02)et='closed';
  for(const sd of[-1,1])cheye(sd*46,-142,et,o.look);
  if(o.brows){ctx.strokeStyle=INK;ctx.lineWidth=6;ctx.lineCap='round';for(const sd of[-1,1]){ctx.beginPath();
    if(o.brows=='sad'){ctx.moveTo(sd*68,-178);ctx.lineTo(sd*30,-188);}else{ctx.moveTo(sd*70,-192);ctx.lineTo(sd*30,-174);}ctx.stroke();}}
  if(o.blush>0){ctx.fillStyle=`rgba(240,120,130,${.6*o.blush})`;for(const sd of[-1,1]){ctx.beginPath();ctx.ellipse(sd*80,-104,22,12,0,0,7);ctx.fill();}}
  if(o.old){ctx.save();ctx.strokeStyle=INK;ctx.lineWidth=4.5;for(const sd of[-1,1]){ctx.beginPath();ctx.arc(sd*46,-142,32,0,7);ctx.stroke();}ctx.beginPath();ctx.moveTo(-14,-146);ctx.lineTo(14,-146);ctx.stroke();ctx.restore();}
  ctx.fillStyle=INK;ctx.beginPath();ctx.ellipse(0,-118,10,7,0,0,7);ctx.fill();
  ctx.strokeStyle=INK;ctx.lineWidth=4.5;ctx.lineCap='round';const m=o.mouth;
  if(m=='w'||m=='smile'||m=='open'){ctx.beginPath();ctx.arc(-9,-108,9,.15,Math.PI*.9);ctx.stroke();ctx.beginPath();ctx.arc(9,-108,9,Math.PI*.1,Math.PI*.85);ctx.stroke();
    if(m=='open'){ctx.beginPath();ctx.moveTo(-14,-100);ctx.quadraticCurveTo(0,-74,14,-100);ctx.closePath();ctx.fillStyle='#c4525a';ctx.fill();ctx.stroke();}}
  else if(m=='flat'){ctx.beginPath();ctx.moveTo(-10,-100);ctx.quadraticCurveTo(0,-104,10,-100);ctx.stroke();}
  else if(m=='pout'){ctx.beginPath();ctx.arc(0,-96,6,0,7);ctx.stroke();}
  else if(m=='o'){ctx.beginPath();ctx.ellipse(0,-96,6,8,0,0,7);ctx.fillStyle='#c4525a';ctx.fill();ctx.stroke();}
  ctx.restore();
};

function sky(top,bot){const g=ctx.createLinearGradient(0,0,0,H);g.addColorStop(0,top);g.addColorStop(1,bot);ctx.fillStyle=g;ctx.fillRect(-200,-200,W+400,H+400);}
function stars(n,a=1){for(let i=0;i<n;i++){const x=hash(i*7.3)*W,y=hash(i*3.1)*760+420,tw=.55+.45*Math.sin(T*2.2+i);ctx.save();ctx.globalAlpha=a*tw;sparkle(x,y,10+hash(i)*12,1,'#fff3c4');ctx.restore();}}
function moon(x,y,r){ctx.save();ctx.fillStyle='rgba(255,243,196,.18)';ctx.beginPath();ctx.arc(x,y,r*1.9,0,7);ctx.fill();ctx.fillStyle='#fff3c4';ctx.beginPath();ctx.arc(x,y,r,0,7);ctx.fill();ctx.restore();}
function crescent(x,y,r,bg){ctx.save();ctx.fillStyle='#fff3c4';ctx.beginPath();ctx.arc(x,y,r,0,7);ctx.fill();ctx.fillStyle=bg;ctx.beginPath();ctx.arc(x+r*.42,y-r*.25,r*.9,0,7);ctx.fill();ctx.restore();}
function hill(col,y=1180){ctx.fillStyle=col;ctx.beginPath();ctx.moveTo(-200,y+40);ctx.quadraticCurveTo(540,y-90,W+200,y+40);ctx.lineTo(W+200,H+200);ctx.lineTo(-200,H+200);ctx.fill();}
function constellation(cx,cy,s,u){const pts=[];for(let i=0;i<=16;i++){const t=i/16*Math.PI*2;pts.push([cx+s*16*Math.pow(Math.sin(t),3),cy-s*(13*Math.cos(t)-5*Math.cos(2*t)-2*Math.cos(3*t)-Math.cos(4*t))]);}
  const k=clamp(u/1.4);ctx.save();ctx.strokeStyle='rgba(255,243,196,.7)';ctx.lineWidth=3;ctx.beginPath();const m=Math.floor(k*16);
  for(let i=0;i<=m;i++){const p=pts[i];i?ctx.lineTo(p[0],p[1]):ctx.moveTo(p[0],p[1]);}ctx.stroke();
  pts.slice(0,m+1).forEach((p,i)=>sparkle(p[0],p[1],13,1,'#fff3c4'));ctx.restore();}
function fireflyHeart(cx,cy,s){for(let i=0;i<110;i++){const t=hash(i*1.7)*Math.PI*2,r=.72+.28*hash(i*9.1);
  const x=cx+s*16*Math.pow(Math.sin(t),3)*r,y=cy-s*(13*Math.cos(t)-5*Math.cos(2*t)-2*Math.cos(3*t)-Math.cos(4*t))*r;
  ctx.save();ctx.globalAlpha=.5+.5*Math.sin(T*3+i);ctx.fillStyle='rgba(255,236,150,.35)';ctx.beginPath();ctx.arc(x,y+Math.sin(T+i)*4,14,0,7);ctx.fill();
  ctx.fillStyle='#fff6c8';ctx.beginPath();ctx.arc(x,y+Math.sin(T+i)*4,5,0,7);ctx.fill();ctx.restore();}}
function lamp(x,y,on=1){if(on){const g=ctx.createRadialGradient(x,y,10,x,y,420);g.addColorStop(0,'rgba(255,220,150,.45)');g.addColorStop(1,'rgba(255,220,150,0)');ctx.fillStyle=g;ctx.fillRect(x-420,y-420,840,840);}
  line([[x,y+40],[x,G-10]],{lw:7});blob([[x-70,y+40],[x+70,y+40],[x+44,y-60],[x-44,y-60]],'#f3d38a');ell(x,G-8,46,10,'#b98a5e');}
function sofa(col,col2){blob(rectPts(110,G-330,860,200,46),col);blob(rectPts(80,G-170,920,150,40),col2);blob(rectPts(60,G-250,110,230,40),col);blob(rectPts(910,G-250,110,230,40),col);
  line([[160,G-20],[160,G+30]],{lw:9});line([[920,G-20],[920,G+30]],{lw:9});}
'''
DK_JS += r'''
/* ---- props for the Dinkly remakes ---- */
function lblanket(w,top,col){blob([[-w/2,top+20],[-w/2+40,top],[w/2-40,top+4],[w/2,top+24],[w/2+14,-4],[-w/2-14,-4]],col);ctx.save();ctx.globalAlpha=.25;line([[-w/4,top+20],[-w/4+20,-20]],{c:'#fff',lw:6});line([[w/5,top+20],[w/5+16,-20]],{c:'#fff',lw:6});ctx.restore();}
function lsofa(w=420,col='#c9806b',col2='#d99480'){blob(rectPts(-w/2+20,-300,w-40,170,36),col);blob(rectPts(-w/2,-150,w,130,30),col2);blob(rectPts(-w/2-20,-220,70,200,30),col);blob(rectPts(w/2-50,-220,70,200,30),col);line([[-w/2+30,-20],[-w/2+30,10]],{lw:8});line([[w/2-30,-20],[w/2-30,10]],{lw:8});}
function skyline(col='#c9a9c8'){ctx.save();ctx.globalAlpha=.55;for(let i=0;i<5;i++){const h=300+hash(i+1)*260;blob(rectPts(-260+i*110,-h,90,h,6),col,{lw:4});}ctx.restore();}
function table(x,y,w=320,col='#8a6a52'){blob(rectPts(x-w/2,y-150,w,26,12),col);line([[x-w/2+30,y-124],[x-w/2+30,y]],{lw:9});line([[x+w/2-30,y-124],[x+w/2-30,y]],{lw:9});}
function roundTable(x,y,r=110,col='#f3e6d6'){ell(x,y-150,r,24,col,{lw:5});line([[x,y-128],[x,y]],{lw:10});ell(x,y-2,50,10,'#b98a5e',{lw:4});}
function plate(x,y,s=1,food='#e8b04a'){ctx.save();ctx.translate(x,y);ctx.scale(s,s);ell(0,0,58,16,'#ffffff',{lw:4});ell(0,-8,34,12,food,{lw:3.5});ctx.restore();}
function pancakes(x,y,n=5,s=1){ctx.save();ctx.translate(x,y);ctx.scale(s,s);ell(0,0,70,18,'#fff',{lw:4});for(let i=0;i<n;i++)ell(0,-14-i*16,52,13,'#e3a95b',{lw:4});
  blob(rectPts(-14,-30-n*16,28,16,5),'#fff2a8',{lw:3.5});ctx.save();ctx.globalAlpha=.9;line([[-40,-20-n*16],[-46,-10]],{c:'#a0522d',lw:8});ctx.restore();ctx.restore();}
function cupS(x,y,col='#fbf5ec',s=1){ctx.save();ctx.translate(x,y);ctx.scale(s,s);blob(rectPts(-22,-46,44,46,10),col,{lw:4});ell(26,-26,10,12,'none',{lw:5});ctx.restore();}
function basket(x,y,s=1,items=1){ctx.save();ctx.translate(x,y);ctx.scale(s,s);if(items)blob(rectPts(-14,-86,28,40,6),'#e8484f',{lw:4});
  line([[-40,-56],[-20,-110],[20,-110],[40,-56]],{lw:6,c:'#3b6ea5'});blob([[-48,-60],[48,-60],[38,0],[-38,0]],'#5b8fc9',{lw:4.5});ctx.restore();}
function trolley(x,y,s=1,full=1){ctx.save();ctx.translate(x,y);ctx.scale(s,s);
  if(full){const cols=['#e8484f','#f7c948','#7fbf6a','#5b8fc9','#f29bb3','#ffffff','#e98b3a'];
    for(let i=0;i<16;i++){const bx=-120+(i%6)*44+hash(i)*10,by=-200-Math.floor(i/6)*58-hash(i+5)*20;blob(rectPts(bx,by,40+hash(i+2)*16,60+hash(i+3)*30,8),cols[i%7],{lw:4});}
    ell(60,-370,26,26,'#f7c948',{lw:4});line([[60,-396],[66,-420]],{lw:5,c:'#6f9a5c'});ell(-90,-360,22,40,'#7fbf6a',{lw:4});}
  blob([[-150,-210],[150,-210],[120,-70],[-120,-70]],'rgba(255,255,255,.35)',{lw:6});
  ctx.save();ctx.globalAlpha=.6;for(let i=-120;i<=120;i+=30)line([[i,-205],[i*.82,-75]],{lw:3});line([[-135,-140],[135,-140]],{lw:3});ctx.restore();
  line([[150,-210],[190,-250]],{lw:7});line([[-120,-70],[-120,-30],[120,-30]],{lw:6});ell(-90,-14,16,16,'#555',{lw:4});ell(90,-14,16,16,'#555',{lw:4});ctx.restore();}
function bed(x,y,w=560,col='#f3ead9',blank='#8fb4dd'){blob(rectPts(x-w/2-20,y-380,60,380,20),'#b98a5e');blob(rectPts(x-w/2,y-140,w,120,24),col);
  line([[x-w/2+20,y-20],[x-w/2+20,y]],{lw:9});line([[x+w/2-20,y-20],[x+w/2-20,y]],{lw:9});}
function quilt(x,y,w=560,col='#8fb4dd'){blob([[x-w/2+80,y-230],[x+w/2,y-220],[x+w/2+10,y-40],[x-w/2+60,y-40]],col);
  ctx.save();ctx.globalAlpha=.25;line([[x-w/2+180,y-220],[x-w/2+200,y-50]],{c:'#fff',lw:6});line([[x,y-220],[x+20,y-50]],{c:'#fff',lw:6});ctx.restore();}
function pillow(x,y){blob(rectPts(x-90,y-70,180,70,30),'#ffffff');}
function phoneS(x,y,s=1,glow=1){ctx.save();ctx.translate(x,y);ctx.scale(s,s);if(glow){const g=ctx.createRadialGradient(0,-40,5,0,-40,160);g.addColorStop(0,'rgba(190,220,255,.5)');g.addColorStop(1,'rgba(190,220,255,0)');ctx.fillStyle=g;ctx.fillRect(-160,-200,320,320);}
  blob(rectPts(-24,-84,48,84,9),'#2b2830',{lw:4});blob(rectPts(-18,-76,36,68,5),'#bfe0ff',{stroke:false});ctx.restore();}
function bench(x,y,w=420,col='#7fa38a'){blob(rectPts(x-w/2,y-150,w,30,10),col);blob(rectPts(x-w/2,y-250,w,26,10),col);line([[x-w/2+30,y-120],[x-w/2+30,y]],{lw:9});line([[x+w/2-30,y-120],[x+w/2-30,y]],{lw:9});line([[x-w/2+30,y-250],[x-w/2+30,y-150]],{lw:7});line([[x+w/2-30,y-250],[x+w/2-30,y-150]],{lw:7});}
function picnic(x,y,w=560){blob([[x-w/2,y-20],[x+w/2,y-20],[x+w/2+60,y+90],[x-w/2-60,y+90]],'#e8a0a8');
  ctx.save();ctx.globalAlpha=.35;for(let i=1;i<6;i++){const k=i/6;line([[x-w/2+w*k,y-20],[x-w/2-60+(w+120)*k,y+90]],{c:'#fff',lw:6});}ctx.restore();}
function umbrella(x,y,s=1,col='#e8484f'){ctx.save();ctx.translate(x,y);ctx.scale(s,s);line([[0,0],[0,260]],{lw:7});
  blob([[-200,10],[-170,-70],[-90,-130],[0,-150],[90,-130],[170,-70],[200,10],[130,-6],[66,10],[0,-6],[-66,10],[-130,-6]],col);ctx.restore();}
function rain(n=60,a=1){ctx.save();ctx.globalAlpha=a*.7;ctx.strokeStyle='#6f8fb3';ctx.lineWidth=4;ctx.lineCap='round';for(let i=0;i<n;i++){const x=hash(i*3.3)*W*1.3-100,y=fract(T*1.4+hash(i*7.7))*1500-100;ctx.beginPath();ctx.moveTo(x,y);ctx.lineTo(x-8,y+34);ctx.stroke();}ctx.restore();}
function puddle(x,y,w=300){ctx.save();ctx.globalAlpha=.5;ell(x,y,w/2,22,'#a8c6e0',{stroke:false});ctx.restore();}
function flowerField(y,cols=['#f7c948','#5b8fc9','#f29bb3']){for(let i=0;i<70;i++){const x=hash(i*1.3)*1300-110,yy=y+hash(i*4.1)*520,s=.5+hash(i*2.2)*.5+(yy-y)/900;
  ctx.save();ctx.translate(x,yy);ctx.scale(s,s);line([[0,0],[0,40]],{lw:5,c:'#5f8f5a'});for(let k=0;k<5;k++){const a=k/5*6.28;ell(Math.cos(a)*14,-4+Math.sin(a)*14,12,12,cols[i%cols.length],{lw:3});}ell(0,-4,8,8,'#fff3c4',{lw:3});ctx.restore();}}
function bigHeart(x,y,s=1,col='#f29bb3',broken=0){ctx.save();ctx.translate(x,y);ctx.scale(s,s);
  const P=[];for(let i=0;i<=40;i++){const t=i/40*Math.PI*2;P.push([16*Math.pow(Math.sin(t),3)*6,-(13*Math.cos(t)-5*Math.cos(2*t)-2*Math.cos(3*t)-Math.cos(4*t))*6]);}
  const path=()=>{ctx.beginPath();P.forEach((p,i)=>i?ctx.lineTo(p[0],p[1]):ctx.moveTo(p[0],p[1]));ctx.closePath();};
  const zz=[[0,-70],[-14,-30],[12,-4],[-12,30],[0,80]];
  if(broken>0){for(const sd of[-1,1]){ctx.save();ctx.translate(sd*22*broken,10*broken);ctx.rotate(sd*.14*broken);
      ctx.beginPath();ctx.moveTo(sd*200,-200);zz.forEach(p=>ctx.lineTo(p[0],p[1]));ctx.lineTo(sd*200,200);ctx.closePath();ctx.clip();
      path();paint(col);line(zz,{lw:5});ctx.restore();}}
  else{path();paint(col);ctx.fillStyle='rgba(255,255,255,.5)';ctx.beginPath();ctx.ellipse(-40,-30,16,10,-.6,0,7);ctx.fill();}
  ctx.restore();}
function bandage(x,y,r=0){ctx.save();ctx.translate(x,y);ctx.rotate(r);blob(rectPts(-60,-18,120,36,16),'#f3d2a8',{lw:4});ctx.fillStyle='#d9b088';for(let i=0;i<4;i++){ctx.beginPath();ctx.arc(-12+(i%2)*24,-6+Math.floor(i/2)*12,3,0,7);ctx.fill();}ctx.restore();}
function sprout(x,y,s=1,stage=1){ctx.save();ctx.translate(x,y);ctx.scale(s,s);blob([[-60,-90],[60,-90],[46,0],[-46,0]],'#cf7f5f');ell(0,-90,62,12,'#8a5a3c');
  if(stage>=1){line([[0,-92],[0,-150-stage*30]],{lw:6,c:'#5f8f5a'});blob([[0,-130],[-50,-160],[-6,-150]],'#8fbf6a',{lw:4});blob([[0,-140-stage*10],[50,-175-stage*10],[6,-160-stage*10]],'#8fbf6a',{lw:4});}
  if(stage>=3){for(let k=0;k<5;k++){const a=k/5*6.28;ell(Math.cos(a)*22,-240+Math.sin(a)*22,18,18,'#f29bb3',{lw:4});}ell(0,-240,13,13,'#f7d76e',{lw:4});}
  ctx.restore();}
function jar(x,y,fill=0){blob(rectPts(x-60,y-170,120,170,24),'rgba(220,240,255,.6)',{lw:5});blob(rectPts(x-48,y-196,96,30,8),'#b98a5e');
  if(fill>0){ctx.save();ctx.beginPath();ctx.rect(x-56,y-170*fill,112,170*fill);ctx.clip();for(let i=0;i<14;i++)heart(x-30+(i%4)*20,y-20-Math.floor(i/4)*36,14,['#ec7489','#f7c948','#7fb0e0'][i%3]);ctx.restore();}}
function door(x,y,open=0,col='#f29bb3'){blob(rectPts(x-110,y-460,220,460,10),'#fbf1e2');blob(rectPts(x-96,y-446,192-open*120,446,6),col);ell(x+60-open*120,y-230,10,10,'#f7d76e',{lw:3});}
function moonBig(x,y,r){ctx.save();const g=ctx.createRadialGradient(x,y,r*.8,x,y,r*2);g.addColorStop(0,'rgba(255,255,240,.35)');g.addColorStop(1,'rgba(255,255,240,0)');ctx.fillStyle=g;ctx.fillRect(x-r*2,y-r*2,r*4,r*4);
  ell(x,y,r,r,'#f2f2ea',{lw:4});for(let i=0;i<7;i++)ell(x+(hash(i)-.5)*r*1.2,y+(hash(i+9)-.5)*r*1.2,r*.12+hash(i+3)*r*.1,r*.1+hash(i+3)*r*.08,'#dcdcd0',{stroke:false});ctx.restore();}
function butterfly(x,y,s,col){ctx.save();ctx.translate(x,y+Math.sin(T*3)*12);ctx.scale(s,s);const f=.6+.4*Math.abs(Math.sin(T*6));
  for(const sd of[-1,1]){ctx.save();ctx.scale(sd*f,1);blob([[0,0],[40,-50],[70,-20],[40,10]],col,{lw:4});blob([[0,4],[34,30],[20,50],[4,26]],col,{lw:4});ctx.restore();}line([[0,-20],[0,30]],{lw:5});ctx.restore();}
function sunset(top='#f6b8a8',bot='#ffe1c6'){sky(top,bot);ctx.save();ctx.fillStyle='#ffc78a';ctx.beginPath();ctx.arc(540,1100,180,0,7);ctx.fill();ctx.restore();}
function seaLine(col='#c98aa0',y=1100){ctx.fillStyle=col;ctx.fillRect(-200,y,W+400,400);}
function tree(x,y,s=1,col='#7fae7a'){ctx.save();ctx.translate(x,y);ctx.scale(s,s);blob(rectPts(-22,-260,44,260,10),'#9a6b4a');ell(0,-320,150,120,col);ell(-90,-260,90,70,col);ell(90,-260,90,70,col);ctx.restore();}
function gift(x,y,s=1,col='#7fb0e0'){ctx.save();ctx.translate(x,y);ctx.scale(s,s);blob(rectPts(-50,-90,100,90,10),col);blob(rectPts(-10,-90,20,90,2),'#f29bb3',{lw:3});blob(rectPts(-56,-108,112,24,8),col);
  blob([[0,-108],[-40,-140],[-46,-112]],'#f29bb3',{lw:3.5});blob([[0,-108],[40,-140],[46,-112]],'#f29bb3',{lw:3.5});ctx.restore();}
function bouquet(x,y,s=1){ctx.save();ctx.translate(x,y);ctx.scale(s,s);blob([[-40,-60],[40,-60],[8,40],[-8,40]],'#fbf1e2');for(let i=0;i<5;i++){const a=-.6+i*.3;ell(Math.sin(a)*46,-80-Math.cos(a)*30,24,22,['#e8484f','#f29bb3','#e8484f','#f7c948','#e8484f'][i]);}ctx.restore();}
function suitcase(x,y,s=1,col='#7f8fd0'){ctx.save();ctx.translate(x,y);ctx.scale(s,s);blob(rectPts(-60,-170,120,170,16),col);line([[-20,-170],[-20,-210],[20,-210],[20,-170]],{lw:6});ell(-34,6,10,10,'#555',{lw:3});ell(34,6,10,10,'#555',{lw:3});ctx.restore();}
function laptop(x,y,s=1){ctx.save();ctx.translate(x,y);ctx.scale(s,s);blob([[-90,-130],[90,-130],[90,-10],[-90,-10]],'#d9dde6');blob(rectPts(-110,-12,220,16,6),'#c4c8d2');ell(0,-70,14,12,'#ec7489',{stroke:false});ctx.restore();}
function tv(x,y,s=1){ctx.save();ctx.translate(x,y);ctx.scale(s,s);blob(rectPts(-170,-230,340,200,14),'#2b2830');blob(rectPts(-152,-214,304,168,8),'#5a6aa0',{stroke:false});line([[-60,-30],[-80,0]],{lw:7});line([[60,-30],[80,0]],{lw:7});ctx.restore();}
function headphones(x,y,s=1){ctx.save();ctx.translate(x,y);ctx.scale(s,s);ctx.strokeStyle=INK;ctx.lineWidth=14;ctx.beginPath();ctx.arc(0,0,128,Math.PI*1.08,Math.PI*1.92);ctx.stroke();ctx.strokeStyle='#4a4a58';ctx.lineWidth=8;ctx.stroke();
  ell(-126,30,24,40,'#4a4a58');ell(126,30,24,40,'#4a4a58');ctx.restore();}
function shelfBg(col='#cfe6f2'){ctx.fillStyle=col;ctx.fillRect(-200,-200,W+400,H+400);for(const yy of[700,900]){line([[-100,yy],[W+100,yy]],{lw:6,c:'#9fb8c8'});for(let i=0;i<9;i++)blob(rectPts(-60+i*140,yy-90,70,90,8),['#f29bb3','#f7c948','#7fbf6a','#e98b3a'][i%4],{lw:3.5});}}
function bubble(x,y,txt,w=330,tail=1,fs=40){ctx.save();ctx.font=fs+'px Neucha';const lines=[];let c='';for(const wd of txt.split(' ')){const t=c?c+' '+wd:wd;if(ctx.measureText(t).width>w-40&&c){lines.push(c);c=wd;}else c=t;}lines.push(c);
  const h=lines.length*fs*1.12+30;blob(rectPts(x-w/2,y-h,w,h,24),'#ffffff',{lw:4});blob([[x-20*tail,y-4],[x+10*tail,y-4],[x+30*tail,y+40]],'#ffffff',{lw:4,stroke:false});line([[x-20*tail,y-2],[x+30*tail,y+40],[x+10*tail,y-2]],{lw:4});
  ctx.fillStyle=INK;ctx.textAlign='center';ctx.textBaseline='top';lines.forEach((l,i)=>ctx.fillText(l,x,y-h+16+i*fs*1.12));ctx.restore();}
/* draw a world-coord scene (1080 wide, ground at G) into a screen rect */
function panelRect(x,y,w,h,fn,u,cx=540,cy=900,sc=null){ctx.save();ctx.beginPath();ctx.rect(x,y,w,h);ctx.clip();const s=sc||w/1080;ctx.translate(x+w/2,y+h/2);ctx.scale(s,s);ctx.translate(-cx,-cy);fn(u);ctx.restore();
  ctx.save();ctx.strokeStyle=INK;ctx.lineWidth=5;ctx.strokeRect(x,y,w,h);ctx.restore();}
'''
