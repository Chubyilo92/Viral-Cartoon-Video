"""Extra props for the 1 Nov 2026 batch (phones with chat bubbles, video cards, water glass, pyjamas, face mask)."""
import sys; sys.path.insert(0, '/home/claude/jj/specs')
from _short import SHORT_PROPS
R3_PROPS = SHORT_PROPS + r'''
function tears(x,y,u){ctx.save();ctx.fillStyle='#8fc8f0';ctx.strokeStyle=INK;ctx.lineWidth=3;for(const sd of[-1,1]){const yy=y+fract(u*.9+(sd>0?.5:0))*60;ctx.beginPath();ctx.ellipse(x+sd*56,yy,8,12,0,0,7);ctx.fill();ctx.stroke();}ctx.restore();}
function bigPhone(x,y,s,draw){ctx.save();ctx.translate(x,y);ctx.scale(s,s);ctx.lineWidth=6;ctx.strokeStyle=INK;
 ctx.fillStyle='#2b2830';ctx.beginPath();ctx.roundRect(-130,-250,260,500,34);ctx.fill();ctx.stroke();
 ctx.fillStyle='#f4f1ec';ctx.beginPath();ctx.roundRect(-112,-222,224,444,20);ctx.fill();
 ctx.save();ctx.beginPath();ctx.rect(-112,-222,224,444);ctx.clip();draw();ctx.restore();ctx.restore();}
function chatBub(x,y,w,h,mine){ctx.fillStyle=mine?'#7fa6cf':'#dcd6cf';ctx.beginPath();ctx.roundRect(x,y,w,h,14);ctx.fill();
 ctx.fillStyle=mine?'#ffffffaa':'#8f8780';for(let i=0;i<Math.floor((h-12)/20);i++)ctx.fillRect(x+12,y+12+i*20,w-24-(i%2)*20,8);}
function chatTxt(x,y,t,mine){ctx.font='bold 26px Poppins';const w=ctx.measureText(t).width+30;ctx.fillStyle=mine?'#7fa6cf':'#dcd6cf';
 ctx.beginPath();ctx.roundRect(mine?x-w:x,y,w,46,14);ctx.fill();ctx.fillStyle=mine?'#fff':'#3a3330';ctx.textBaseline='middle';ctx.textAlign='left';ctx.fillText(t,(mine?x-w:x)+15,y+24);}
function playCard(x,y,s,a=1){if(a<=0)return;ctx.save();ctx.globalAlpha*=a;ctx.translate(x,y);ctx.scale(s,s);ctx.lineWidth=4;ctx.strokeStyle=INK;
 ctx.fillStyle='#2b2830';ctx.beginPath();ctx.roundRect(-34,-56,68,112,12);ctx.fill();ctx.stroke();
 ctx.fillStyle='#ffffff';ctx.beginPath();ctx.moveTo(-10,-18);ctx.lineTo(16,0);ctx.lineTo(-10,18);ctx.closePath();ctx.fill();
 ctx.fillStyle='#ec7489';ctx.fillRect(-26,40,30,6);ctx.restore();}
function glassWater(x,y,s=1){ctx.save();ctx.translate(x,y);ctx.scale(s,s);ctx.lineWidth=4;ctx.strokeStyle=INK;
 ctx.fillStyle='#bfe3ffcc';ctx.beginPath();ctx.moveTo(-34,-90);ctx.lineTo(34,-90);ctx.lineTo(26,0);ctx.lineTo(-26,0);ctx.closePath();ctx.fill();
 ctx.fillStyle='#8fc8f0';ctx.beginPath();ctx.moveTo(-31,-60);ctx.lineTo(31,-60);ctx.lineTo(26,0);ctx.lineTo(-26,0);ctx.closePath();ctx.fill();
 ctx.beginPath();ctx.moveTo(-34,-90);ctx.lineTo(34,-90);ctx.lineTo(26,0);ctx.lineTo(-26,0);ctx.closePath();ctx.stroke();ctx.restore();}
function pjTop(x,s,flip,y){ctx.save();ctx.translate(x,(y===undefined?G+10:y));ctx.scale(s*(flip||1),s);
 ctx.lineWidth=4/s;ctx.strokeStyle=INK;ctx.fillStyle='#f2b8c6';
 ctx.beginPath();ctx.moveTo(-62,-150);ctx.quadraticCurveTo(-92,-120,-96,-40);ctx.lineTo(-92,-4);ctx.lineTo(92,-4);ctx.lineTo(96,-40);ctx.quadraticCurveTo(92,-120,62,-150);ctx.quadraticCurveTo(0,-128,-62,-150);ctx.closePath();ctx.fill();ctx.stroke();
 ctx.fillStyle='#ffffff';for(const [a,b] of [[-50,-110],[30,-95],[-20,-60],[55,-40],[-60,-30],[10,-130]]){ctx.beginPath();ctx.arc(a,b,7,0,7);ctx.fill();}
 ctx.restore();}
function chinSpot(x,y,s){ctx.save();ctx.fillStyle='#ffffff';ctx.strokeStyle=INK;ctx.lineWidth=2.5;ctx.beginPath();ctx.arc(x+6*s,y-150*s,8*s,0,7);ctx.fill();ctx.stroke();ctx.restore();}
function faceMask(x,y,s){ctx.save();ctx.globalAlpha=.72;ctx.fillStyle='#bfe8c4';ctx.beginPath();ctx.ellipse(x,y-205*s,64*s,58*s,0,0,7);ctx.fill();ctx.restore();}
function doorFrame(x){blob(rectPts(x,G-560,230,560,6),'#b98a5e');blob(rectPts(x+18,G-540,194,540,4),'#e9dccb',{stroke:false});}
'''
