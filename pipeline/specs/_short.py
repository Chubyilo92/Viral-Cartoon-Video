"""Props shared by the SHORT FORMAT videos (fries, cookie, popcorn, bed/blanket, snowflakes)."""
SHORT_PROPS = r'''
function fry(x,y,rot=0,len=70){ctx.save();ctx.translate(x,y);ctx.rotate(rot);blob(rectPts(-8,-len,16,len,4),'#f7c948',{lw:4});ctx.restore();}
function friesBag(x,y,s=1,full=1,rot=0){ctx.save();ctx.translate(x,y);ctx.rotate(rot);ctx.scale(s,s);
  if(full>0){const n=Math.round(7*full);for(let i=0;i<n;i++){fry(-44+i*15,-92,(i-3)*.09,62+hash(i)*30);}}
  blob([[-62,-100],[62,-100],[48,0],[-48,0]],'#e8484f',{lw:5});
  if(full<=0){ell(0,-100,60,12,'#7a2a2e',{lw:4});}
  ctx.fillStyle='#fff3c4';ctx.beginPath();ctx.arc(0,-52,20,0,7);ctx.fill();ctx.strokeStyle=INK;ctx.lineWidth=4;ctx.stroke();
  ctx.font='bold 24px Poppins';ctx.fillStyle='#e8484f';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText('F',0,-51);
  ctx.restore();}
function cookie(x,y,r=34,bite=0){ctx.save();ctx.translate(x,y);ell(0,0,r,r*.92,'#d9a05b',{lw:4.5});
  ctx.fillStyle='#5a3620';for(let i=0;i<6;i++){const a=i*1.1+.4,d=r*(.25+.45*hash(i+3));ctx.beginPath();ctx.ellipse(Math.cos(a)*d,Math.sin(a)*d,r*.11,r*.08,a,0,7);ctx.fill();}
  if(bite>0){ctx.globalCompositeOperation='destination-out';ctx.beginPath();ctx.arc(r*.8,-r*.5,r*.42*bite,0,7);ctx.fill();ctx.globalCompositeOperation='source-over';}
  ctx.restore();}
function popcorn(x,y,s=1){ctx.save();ctx.translate(x,y);ctx.scale(s,s);
  for(let i=0;i<9;i++)ell(-40+(i%5)*20,-96-Math.floor(i/5)*20+hash(i)*8,15,13,'#fff6dc',{lw:3.5});
  blob([[-52,-92],[52,-92],[40,0],[-40,0]],'#fffaf0',{lw:5});
  for(let i=0;i<3;i++){ctx.fillStyle='#e8484f';ctx.beginPath();ctx.moveTo(-36+i*30,-90);ctx.lineTo(-24+i*30,-90);ctx.lineTo(-18+i*26,-2);ctx.lineTo(-28+i*26,-2);ctx.closePath();ctx.fill();}
  ctx.restore();}
function snowflake(x,y,sz,a=1){if(a<=0)return;ctx.save();ctx.globalAlpha*=a;ctx.translate(x,y);ctx.strokeStyle='#bfe3ff';ctx.lineWidth=6;ctx.lineCap='round';
  for(let i=0;i<3;i++){ctx.rotate(Math.PI/3);ctx.beginPath();ctx.moveTo(-sz,0);ctx.lineTo(sz,0);ctx.stroke();}
  ctx.strokeStyle=INK;ctx.lineWidth=2;ctx.restore();}
function bedFrame(){ // side-view bed, pillow on the left
  blob(rectPts(150,G-330,70,360,18),'#b98a5e');            // headboard
  blob(rectPts(180,G-120,800,120,22),'#f3ead9');          // mattress
  blob(rectPts(200,G-170,220,70,30),'#ffffff');           // pillow
}
function bedBack(){ // front-view bed: wide headboard behind, mattress, two pillows
  blob(rectPts(150,G-520,780,440,40),'#b98a5e');blob(rectPts(190,G-480,700,360,30),'#c99b6d',{stroke:false});
  blob(rectPts(130,G-130,820,130,24),'#f3ead9');
  blob(rectPts(200,G-300,280,110,40),'#ffffff');blob(rectPts(600,G-300,280,110,40),'#ffffff');
}
function blanket(x0,x1,top,col='#7fa6cf'){blob([[x0,top+30],[x0+60,top],[x1-40,top+6],[x1,top+40],[x1+10,G-10],[x0-10,G-10]],col);
  ctx.save();ctx.globalAlpha=.25;line([[x0+120,top+40],[x0+170,G-30]],{c:'#ffffff',lw:6});line([[x0+380,top+30],[x0+420,G-30]],{c:'#ffffff',lw:6});ctx.restore();}
function bedNight(){room('#33405e','#2a3550','rgba(255,255,255,.05)');
  const lg=ctx.createRadialGradient(820,600,20,820,600,520);lg.addColorStop(0,'rgba(255,220,150,.28)');lg.addColorStop(1,'rgba(255,220,150,0)');ctx.fillStyle=lg;ctx.fillRect(0,0,W,H);
  ctx.fillStyle='#fff3c4';ctx.beginPath();ctx.arc(900,560,40,0,7);ctx.fill();ctx.fillStyle='#33405e';ctx.beginPath();ctx.arc(920,546,36,0,7);ctx.fill();}
function bigCloud(x,y,a){if(a<=0)return;ctx.save();ctx.translate(x,y);ctx.scale(2.2,2.2);raincloudSmall(0,0,a);ctx.restore();}
function couch(){blob(rectPts(130,G-260,820,150,40),'#c9806b');blob(rectPts(110,G-130,860,130,30),'#d99480');}
'''
