"""Kitchen props for girl_always_makes_you_taste_test_her_cooking_first (9 Nov 2026 batch):
stove, pot with steam, wooden spoon, plate (empty/full), simple checklist card."""
KITCHEN_PROPS = r'''
function stove(x,y,s=1){ctx.save();ctx.translate(x,y);ctx.scale(s,s);
  blob(rectPts(-160,-40,320,110,14),'#8a8f98');
  for(const dx of[-85,85]){ctx.fillStyle='#3a3a3f';ctx.beginPath();ctx.arc(dx,-8,46,0,7);ctx.fill();ctx.strokeStyle=INK;ctx.lineWidth=3;ctx.stroke();
    ctx.strokeStyle='#5f6066';ctx.lineWidth=3;ctx.beginPath();ctx.arc(dx,-8,30,0,7);ctx.stroke();}
  ctx.restore();}
function steam(x,y,u,n=3){ctx.save();ctx.strokeStyle='rgba(255,255,255,.55)';ctx.lineWidth=7;ctx.lineCap='round';
  for(let i=0;i<n;i++){const k=fract(u*.5+i/n),yy=y-k*140,xx=x+(i-1)*30+Math.sin(k*6+i)*14;
    ctx.globalAlpha=Math.sin(k*Math.PI)*.8;ctx.beginPath();ctx.moveTo(xx,yy+26);ctx.quadraticCurveTo(xx+16,yy+8,xx,yy-18);ctx.stroke();}
  ctx.restore();}
function potOnStove(x,y,s=1,u=0){ctx.save();ctx.translate(x,y);ctx.scale(s,s);
  blob(rectPts(-78,-56,156,70,10),'#5a7a8c');
  ell(0,-58,78,16,'#3f5a68');
  blob(rectPts(-96,-72,16,22,6),'#3f5a68');blob(rectPts(80,-72,16,22,6),'#3f5a68');
  ctx.restore();
  steam(x,y-150*s,u,3);}
function spoonProp(x,y,rot=0,s=1){ctx.save();ctx.translate(x,y);ctx.rotate(rot);ctx.scale(s,s);
  ctx.strokeStyle='#b9823f';ctx.lineWidth=14;ctx.lineCap='round';ctx.beginPath();ctx.moveTo(0,60);ctx.lineTo(0,-40);ctx.stroke();
  ctx.fillStyle='#d9a05b';ctx.strokeStyle=INK;ctx.lineWidth=3.5;ctx.beginPath();ctx.ellipse(0,-66,24,34,0,0,7);ctx.fill();ctx.stroke();
  ctx.fillStyle='#8a5a2c';ctx.beginPath();ctx.ellipse(0,-70,15,22,0,0,7);ctx.fill();
  ctx.restore();}
function plateProp(x,y,s=1,full=0){ctx.save();ctx.translate(x,y);ctx.scale(s,s);
  ell(0,0,70,20,'#fbf1e2');ell(0,0,54,14,'#e9dccb');
  if(full>0){ctx.globalAlpha=full;ctx.fillStyle='#d98b4a';ctx.beginPath();ctx.ellipse(-6,-6,30,12,0,0,7);ctx.fill();
    ctx.fillStyle='#6f9a5c';ctx.beginPath();ctx.ellipse(18,-2,12,7,0,0,7);ctx.fill();ctx.globalAlpha=1;}
  ctx.restore();}
function checklistCard(x,y,rows,s=1,a=1){if(a<=0)return;ctx.save();ctx.globalAlpha*=a;ctx.translate(x,y);ctx.scale(s,s);
  const w=320,h=36*rows.length+30;
  ctx.fillStyle='#fffaf0';ctx.strokeStyle=INK;ctx.lineWidth=4;ctx.beginPath();ctx.roundRect(-w/2,-h/2,w,h,18);ctx.fill();ctx.stroke();
  ctx.textAlign='left';ctx.textBaseline='middle';ctx.font='bold 22px Poppins';
  rows.forEach((r,i)=>{const ry=-h/2+28+i*36;ctx.fillStyle=INK;ctx.fillText(r[0],-w/2+24,ry);
    ctx.fillStyle=r[1]?'#5a9e5a':'#c24b4b';ctx.font='bold 24px Poppins';ctx.fillText(r[1]?'yes':'no',w/2-70,ry);ctx.font='bold 22px Poppins';});
  ctx.restore();}
'''
