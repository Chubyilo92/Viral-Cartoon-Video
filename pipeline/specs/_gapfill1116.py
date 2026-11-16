"""Shared props for the 16 Nov 2026 gap-fill batch (chair+jacket, street/road, car warm-up,
recipe card, camera framing, phone face-down, foil-covered plate, card/board game).
Built from the same primitives as _r3props.py / _kitchenprops.py (room, blob, ell, line, tube,
rectPts, ctx save/restore, INK outline) so new props render consistently with the rest of the
engine. Kept in one file since all 8 of this batch's scripts are built in the same run."""
GAPFILL_PROPS = r'''
function labelCard(x,y,txt,s=1,a=1,fs=24){if(a<=0)return;ctx.save();ctx.globalAlpha*=a;ctx.translate(x,y);ctx.scale(s,s);
  ctx.font='bold '+fs+'px Poppins';const w=ctx.measureText(txt).width+40;
  blob(rectPts(-w/2,-30,w,56,16),'#fffaf0',{lw:4});
  ctx.fillStyle=INK;ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText(txt,0,0);ctx.restore();}

function chairJacket(x,y,s=1,draped=1){ctx.save();ctx.translate(x,y);ctx.scale(s,s);
  // simple front-view chair: tall back rail (two posts + top bar), seat slab, four legs
  blob(rectPts(-78,-260,20,230,6),'#b98a5e');blob(rectPts(58,-260,20,230,6),'#b98a5e');
  blob(rectPts(-84,-270,188,24,8),'#caa070');
  blob(rectPts(-90,-40,200,34,8),'#caa070');
  blob(rectPts(-76,-6,18,120,4),'#9c7148');blob(rectPts(58,-6,18,120,4),'#9c7148');
  if(draped>0){ctx.save();ctx.globalAlpha=draped;ctx.translate(10,-160);
    // jacket draped over the back rail: collar notch up top, two sleeves hanging either side, hem below
    ctx.fillStyle='#4a6fa5';ctx.strokeStyle='#2e4a72';ctx.lineWidth=5;ctx.lineJoin='round';
    ctx.beginPath();
    ctx.moveTo(-20,-96);ctx.lineTo(0,-82);ctx.lineTo(20,-96);           // collar notch
    ctx.lineTo(96,-70);ctx.lineTo(112,0);ctx.lineTo(80,40);             // right shoulder -> right sleeve hanging
    ctx.lineTo(60,-10);ctx.lineTo(30,30);ctx.lineTo(0,10);ctx.lineTo(-30,30);ctx.lineTo(-60,-10);  // hem wobble
    ctx.lineTo(-80,40);ctx.lineTo(-112,0);ctx.lineTo(-96,-70);          // left sleeve hanging -> left shoulder
    ctx.closePath();ctx.fill();ctx.stroke();
    ctx.strokeStyle='#2e4a72';ctx.lineWidth=3;line([[0,-70],[0,24]],{c:'#2e4a72',lw:3});   // zip line
    for(const sx of[-1,1]){ctx.beginPath();ctx.arc(sx*8,-40,4,0,7);ctx.fillStyle='#8fb0d8';ctx.fill();}  // buttons
    ctx.restore();}
  ctx.restore();}

function curbRoad(fy){ // thin road band just past the pavement edge, with dashed centre line
  ctx.save();blob(rectPts(-200,fy-26,W+400,70,0),'#5c6066',{stroke:false});
  ctx.strokeStyle='#e8d9a0';ctx.lineWidth=8;ctx.setLineDash([34,26]);
  ctx.beginPath();ctx.moveTo(-60,fy+6);ctx.lineTo(W+60,fy+6);ctx.stroke();ctx.setLineDash([]);
  ctx.restore();}
function carPass(x,y,s,a=1){if(a<=0)return;ctx.save();ctx.globalAlpha*=a;ctx.translate(x,y);ctx.scale(s,s);
  blob([[-150,0],[-150,-50],[-100,-96],[-20,-104],[60,-70],[150,-50],[150,0]],'#c0574f');
  ell(-90,6,30,30,'#2b2830');ell(80,6,30,30,'#2b2830');
  blob(rectPts(-80,-96,110,46,10),'#dff0f7',{lw:3});
  ctx.restore();}

function carFront(x,y,s=1){ctx.save();ctx.translate(x,y);ctx.scale(s,s);
  // big front-on car body, filling roughly the same visual weight as a sitting puppy
  blob([[-270,120],[-255,-50],[-170,-140],[170,-140],[255,-50],[270,120],[220,170],[-220,170]],'#8fb0c6');
  blob(rectPts(-175,-118,180,118,20),'#dff0f7',{lw:4});          // her (left) windscreen pane
  blob(rectPts(5,-118,180,118,20),'#dff0f7',{lw:4});             // his (right) windscreen pane
  blob(rectPts(-6,-118,12,118,2),'#6f8ea0',{stroke:false});      // centre pillar
  ell(-190,168,54,54,'#2b2830');ell(190,168,54,54,'#2b2830');
  ell(-190,168,22,22,'#8a8f98');ell(190,168,22,22,'#8a8f98');
  blob(rectPts(-30,90,60,26,6),'#f3ead9',{lw:4});                // grille
  ell(-230,-10,16,10,'#fff3c4');ell(230,-10,16,10,'#fff3c4');     // headlights
  ctx.restore();}
function frostGlass(x,y,w,h,a=1){if(a<=0)return;ctx.save();ctx.globalAlpha=a;
  ctx.fillStyle='rgba(255,255,255,.82)';ctx.fillRect(x-w/2,y-h/2,w,h);
  ctx.strokeStyle='#bcdcef';ctx.lineWidth=3;
  for(let i=0;i<14;i++){const fx=x-w/2+12+((i*41)%(w-24)),fy=y-h/2+14+((i*53)%(h-28));
    ctx.save();ctx.translate(fx,fy);ctx.rotate(i*.9);
    for(let k=0;k<3;k++){ctx.rotate(Math.PI/3);ctx.beginPath();ctx.moveTo(-9,0);ctx.lineTo(9,0);ctx.stroke();}
    ctx.restore();}
  ctx.restore();}
function scraperProp(x,y,rot=0,s=1){ctx.save();ctx.translate(x,y);ctx.rotate(rot);ctx.scale(s,s);
  ctx.strokeStyle='#b9823f';ctx.lineWidth=12;ctx.lineCap='round';ctx.beginPath();ctx.moveTo(0,40);ctx.lineTo(0,-30);ctx.stroke();
  ctx.fillStyle='#e8484f';ctx.strokeStyle=INK;ctx.lineWidth=3;ctx.beginPath();ctx.roundRect(-26,-56,52,30,6);ctx.fill();ctx.stroke();
  ctx.restore();}
function heatWave(x,y,u,n=3,a=1){ctx.save();ctx.globalAlpha=a;ctx.strokeStyle='#e8a04a';ctx.lineWidth=5;ctx.lineCap='round';
  for(let i=0;i<n;i++){const k=fract(u*.6+i/n),yy=y-k*70,xx=x+i*24;ctx.beginPath();ctx.moveTo(xx-10,yy+16);ctx.quadraticCurveTo(xx+8,yy,xx-10,yy-16);ctx.stroke();}
  ctx.restore();}

function recipeCard(x,y,s=1,a=1){if(a<=0)return;ctx.save();ctx.globalAlpha*=a;ctx.translate(x,y);ctx.scale(s,s);
  blob(rectPts(-150,-190,300,380,18),'#fffaf0',{lw:4});
  ctx.strokeStyle='#e0c9a0';ctx.lineWidth=2;for(let i=0;i<7;i++)line([[-126,-150+i*44],[126,-150+i*44]],{c:'#e0c9a0',lw:2});
  ctx.fillStyle='#c0574f';ctx.font='bold 24px Poppins';ctx.textAlign='center';ctx.fillText("mum's recipe",0,-168);
  ctx.strokeStyle=INK;ctx.lineWidth=3;ctx.beginPath();ctx.moveTo(-90,-108);ctx.lineTo(10,-108);ctx.stroke();
  ctx.beginPath();ctx.moveTo(-90,-64);ctx.lineTo(60,-64);ctx.stroke();
  ctx.beginPath();ctx.moveTo(-90,-20);ctx.lineTo(-10,-20);ctx.stroke();
  ctx.restore();}

function cameraFraming(x,y,w,h,a=1){if(a<=0)return;ctx.save();ctx.globalAlpha=a;ctx.strokeStyle='#fff8e8';ctx.lineWidth=6;ctx.lineCap='round';
  const cl=28;
  for(const [sx,sy] of [[-1,-1],[1,-1],[-1,1],[1,1]]){ctx.save();ctx.translate(x+sx*w/2,y+sy*h/2);
    ctx.beginPath();ctx.moveTo(0,sy*cl);ctx.lineTo(0,0);ctx.lineTo(sx*cl,0);ctx.stroke();ctx.restore();}
  ctx.restore();}
function cameraProp(x,y,s=1,rot=0){ctx.save();ctx.translate(x,y);ctx.rotate(rot);ctx.scale(s,s);
  blob(rectPts(-56,-34,112,68,10),'#3a3a3f');
  ctx.fillStyle='#1f1a1a';ctx.strokeStyle=INK;ctx.lineWidth=4;ctx.beginPath();ctx.arc(0,2,30,0,7);ctx.fill();ctx.stroke();
  ctx.fillStyle='#8fc8f0';ctx.beginPath();ctx.arc(0,2,16,0,7);ctx.fill();
  blob(rectPts(-20,-46,30,16,4),'#3a3a3f');
  ctx.restore();}

function phoneFaceDown(x,y,s=1,buzz=0){ctx.save();ctx.translate(x,y);ctx.scale(s,s);
  if(buzz>0){ctx.save();ctx.translate(Math.sin(T*40)*3*buzz,0);}
  ell(4,10,78,30,'#00000022',{stroke:false});                      // flat shadow on the table
  ctx.save();ctx.rotate(-.08);
  blob(rectPts(-54,-92,108,184,16),'#3a3a3f');                      // phone body, viewed from above lying flat
  blob(rectPts(-44,-80,88,160,10),'#1f1a1a',{stroke:false});        // dark screen-side-down panel
  ctx.fillStyle='#55575e';ctx.beginPath();ctx.arc(0,70,7,0,7);ctx.fill();  // camera bump
  ctx.restore();
  if(buzz>0)ctx.restore();
  if(buzz>0){ctx.save();ctx.strokeStyle='#e8a04a';ctx.lineWidth=4;ctx.globalAlpha=.6+Math.sin(T*8)*.3;
    ctx.beginPath();ctx.ellipse(0,0,100,66,0,0,7);ctx.stroke();ctx.restore();}
  ctx.restore();}

function foilPlate(x,y,s=1,covered=1){ctx.save();ctx.translate(x,y);ctx.scale(s,s);
  ell(0,0,70,20,'#fbf1e2');ell(0,0,54,14,'#e9dccb');
  if(covered>0){ctx.save();ctx.globalAlpha=covered;
    ell(0,-10,50,22,'#cfd3d8');
    ctx.strokeStyle='#aab0b8';ctx.lineWidth=2;for(const dx of[-24,0,24])line([[dx,-26],[dx,6]],{c:'#aab0b8',lw:2});
    ctx.restore();}
  ctx.restore();}

function boardGrid(x,y,s=1){ctx.save();ctx.translate(x,y);ctx.scale(s,s);
  blob(rectPts(-170,-170,340,340,16),'#efe0c0',{lw:5});
  ctx.strokeStyle='#cbb482';ctx.lineWidth=3;
  for(let i=1;i<6;i++){line([[-170+i*340/6,-170],[-170+i*340/6,170]],{c:'#cbb482',lw:3});
    line([[-170,-170+i*340/6],[170,-170+i*340/6]],{c:'#cbb482',lw:3});}
  ctx.restore();}
function pawnProp(x,y,col,s=1){ctx.save();ctx.translate(x,y);ctx.scale(s,s);
  ctx.fillStyle=col;ctx.strokeStyle=INK;ctx.lineWidth=3;ctx.beginPath();ctx.moveTo(-14,18);ctx.lineTo(14,18);ctx.lineTo(7,-20);ctx.lineTo(-7,-20);ctx.closePath();ctx.fill();ctx.stroke();
  ctx.beginPath();ctx.arc(0,-26,9,0,7);ctx.fill();ctx.stroke();ctx.restore();}
function diceProp(x,y,s=1,rot=0){ctx.save();ctx.translate(x,y);ctx.rotate(rot);ctx.scale(s,s);
  blob(rectPts(-24,-24,48,48,8),'#fffaf0',{lw:3});
  ctx.fillStyle=INK;for(const [dx,dy] of [[0,0],[-11,-11],[11,11],[-11,11],[11,-11]])ctx.beginPath(),ctx.arc(dx,dy,3.5,0,7),ctx.fill();
  ctx.restore();}
'''
