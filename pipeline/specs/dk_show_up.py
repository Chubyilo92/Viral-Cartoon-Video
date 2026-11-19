"""Remake of @dinklygame DX6utmKhMoC (2.4M, 12.31s, Phury - Grateful (Instrumental)). Comic strip: 'you don't have to...' / 'I know.' x3, then the why, then a 2x2 recap."""
TARGET = 12.305
SONG = 'Phury - Grateful (Instrumental)'
CAPTION = "when you choose to show up each and every day 🤍\n\n#couples #loveadvice #relationshipgoals"
PRELUDE = r'''
function cscene(i,u){
 if(i==0){room('#c9d6e6','#b9c6d6','rgba(255,255,255,.12)');frame(820,640,140,120,(x,y)=>heart(x,y,20,'#ec7489'));sofa('#8fa8c9','#9fb8d9');
   pup({kind:'girl',x:420,y:G-150,s:.95,eyes:'open',mouth:'flat',brows:'sad',blush:.9});blanket(260,600,G-230,'#fbf5ec');pup({kind:'boy',x:700,y:G-150,s:.95,flip:-1,eyes:'happy',mouth:'smile'});mug(800,G-200,.5);}
 if(i==1){ctx.fillStyle='#4d5d84';ctx.fillRect(0,0,540,1920);ctx.fillStyle='#8fa8c9';ctx.fillRect(540,0,540,1920);
   ctx.save();ctx.beginPath();ctx.rect(0,0,540,1920);ctx.clip();bed(260,G+40,420);pup({kind:'girl',x:250,y:G-80,s:.8,eyes:'happy',mouth:'smile',shadow:false});quilt(260,G+140,420,'#c9b8e6');phoneS(340,G-120,.8);ctx.restore();
   ctx.save();ctx.beginPath();ctx.rect(540,0,540,1920);ctx.clip();pup({kind:'boy',x:800,y:G+20,s:.85,eyes:'open',look:[-1,.5],mouth:'smile'});phoneS(660,G-60,.8);ctx.restore();line([[540,0],[540,1920]],{lw:6});}
 if(i==2){room('#e8d2b8','#d8c2a8','rgba(255,255,255,.12)');pup({kind:'girl',x:200,y:G-40,s:.8,eyes:'happy',mouth:'smile',old:1});pup({kind:'boy',x:880,y:G-40,s:.8,flip:-1,eyes:'happy',mouth:'open',old:1});
   pup({kind:'girl',x:430,y:G-40,s:.85,eyes:'open',mouth:'smile'});pup({kind:'boy',x:650,y:G-40,s:.85,flip:-1,eyes:'happy',mouth:'smile'});table(540,G+80,900,'#a07a5a');
   plate(300,G-72,.7,'#e8b04a');plate(470,G-72,.7,'#7fbf6a');plate(620,G-72,.7,'#e8484f');plate(790,G-72,.7,'#e8b04a');}
}
function closeup(kind,x,y,w,h,bg){ctx.save();ctx.beginPath();ctx.rect(x,y,w,h);ctx.clip();ctx.fillStyle=bg;ctx.fillRect(x,y,w,h);ctx.translate(x+w*.5,y+h+260*(w/1000));ctx.scale(w/520,w/520);
  pup({kind,x:0,y:0,s:1,eyes:kind=='girl'?'open':'happy',mouth:'smile',blush:.8,shadow:false});ctx.restore();ctx.save();ctx.strokeStyle=INK;ctx.lineWidth=5;ctx.strokeRect(x,y,w,h);ctx.restore();}
const BUB=[[["You don't have to stay with me.",.22,.3,.38,1],["I know.",.82,.3,.2,-1]],
           [["You don't have to text me goodnight.",.25,.3,.42,1],["I know.",.78,.3,.2,-1]],
           [["You don't have to come to these dinners.",.3,.33,.46,1],["I know.",.8,.33,.2,-1]]];
function comic(i,x,y,w,h,u){const k=w/1000;
  if(i<3){panelRect(x,y,w,h,cscene.bind(null,i),u,540,940,w/1080*1.0);
    BUB[i].forEach(b=>{ctx.save();ctx.translate(x+w*b[1],y+h*b[2]);ctx.scale(k,k);bubble(0,0,b[0],1000*b[3]*1.15,b[4],52);ctx.restore();});}
  else{const hh=h/2;closeup('girl',x,y,w,hh,'#f6e3c0');closeup('boy',x,y+hh,w,hh,'#f6d6c0');
    ctx.save();ctx.translate(x+w*.26,y+hh*.55);ctx.scale(k,k);bubble(0,0,'So why do you do all of it?',440,1,54);ctx.restore();
    ctx.save();ctx.translate(x+w*.26,y+hh+hh*.55);ctx.scale(k,k);bubble(0,0,'Because I want to.',380,1,54);ctx.restore();}}
'''
PW, PH, PX, PY = 1040, 680, 20, 620
def one(i):
    return "ctx.fillStyle='#ffffff';ctx.fillRect(0,0,W,H);comic(%d,%d,%d,%d,%d,u);" % (i, PX, PY, PW, PH)
GRID = ("ctx.fillStyle='#ffffff';ctx.fillRect(0,0,W,H);"
        "for(let i=0;i<4;i++)comic(i,30+(i%2)*525,560+Math.floor(i/2)*345,495,307,u+i);")
BEATS = [("", one(0), 2.5, {'raw': True}), ("", one(1), 2.3, {'raw': True}), ("", one(2), 2.3, {'raw': True}),
         ("", one(3), 2.4, {'raw': True}), ("", GRID, 0, {'raw': True})]
