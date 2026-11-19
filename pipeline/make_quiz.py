#!/usr/bin/env python3
"""LOVELEE-STYLE CoupleIn quiz reels (19 Nov 2026) - see docs/LOVELEE-FORMAT.md
Title card -> N question cards -> App Store card for CoupleIn. Silent (song added in-app). Exact source length.
Themes: 'flat' (pastel colour + radial light, big white text, hearts progress, pills/ABCD/open)
        'beach' (sky, palms, sand, pixel-font speech bubble, wooden sign, ABCD/pills/rate) -> night end with real Bond screens.
Spec lives in specs/lovelee_data.py as one dict per video. Usage: python3 make_quiz.py <slug> [preview]
"""
import base64, importlib, json, os, subprocess, sys
sys.path.insert(0, '/home/claude/jj'); sys.path.insert(0, '/home/claude/jj/specs')
import jjlib as J
from _dk import DK_JS
from _short import SHORT_PROPS
from lovelee_data import VIDEOS

slug = sys.argv[1]
mode = sys.argv[2] if len(sys.argv) > 2 else 'render'
spec = next(v for v in VIDEOS if v['slug'] == slug)
W = f'{J.ROOT}/work/{slug}'; os.makedirs(W, exist_ok=True)
OUT = f'{J.ROOT}/out/couplein'; os.makedirs(OUT, exist_ok=True)
FPS = 30
ASSETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets') if os.path.isdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets')) else '/home/claude/jj/assets'

def b64(p): return 'data:image/png;base64,' + base64.b64encode(open(p, 'rb').read()).decode()

n = len(spec['items'])
T = spec['target']
cuts = [0, 2.7] + [round(2.7 + 2.6 * (i + 1), 3) for i in range(n)]   # title, items..., end starts at cuts[-1]
assert cuts[-1] < T - 1.5, 'not enough room for the end card'

QJS = r'''
const FONT='Inter';
function shade(hex,k){const n=parseInt(hex.slice(1),16);let r=n>>16,g=(n>>8)&255,b=n&255;const t=k<0?0:255,p=Math.abs(k);
  r=Math.round(r+(t-r)*p);g=Math.round(g+(t-g)*p);b=Math.round(b+(t-b)*p);return `rgb(${r},${g},${b})`;}
function flatBg(col){ctx.fillStyle=col;ctx.fillRect(0,0,W,H);const g=ctx.createRadialGradient(540,880,60,540,880,1250);
  g.addColorStop(0,shade(col,.22));g.addColorStop(.55,col);g.addColorStop(1,shade(col,-.14));ctx.fillStyle=g;ctx.fillRect(0,0,W,H);}
function cloudSoft(x,y,s,a=.95){ctx.save();ctx.globalAlpha=a;ctx.fillStyle='#ffffff';for(const [dx,dy,r] of [[0,0,90],[90,-30,110],[200,0,90],[110,30,100],[-80,20,70]]){ctx.beginPath();ctx.arc(x+dx*s,y+dy*s,r*s,0,7);ctx.fill();}ctx.restore();}
function palm(x,y,s,flip,col){ctx.save();ctx.translate(x,y);ctx.scale(s*flip,s);ctx.fillStyle=col;
  for(let i=0;i<6;i++){ctx.save();ctx.rotate(-1.2+i*.42+Math.sin(T*1.2+i)*.03);ctx.beginPath();ctx.moveTo(0,0);ctx.quadraticCurveTo(160,-70,330,10);ctx.quadraticCurveTo(170,-10,0,0);ctx.fill();ctx.restore();}ctx.restore();}
function beachBg(){const g=ctx.createLinearGradient(0,0,0,1300);g.addColorStop(0,'#58aef0');g.addColorStop(1,'#bfe6fb');ctx.fillStyle=g;ctx.fillRect(0,0,W,H);
  cloudSoft(120,260,1.1);cloudSoft(760,170,.9);cloudSoft(860,560,.8,.8);cloudSoft(60,700,.7,.7);
  palm(-40,140,1.2,1,'#2f8c5a');palm(-60,520,1.0,1,'#c46aa0');palm(1120,260,1.1,-1,'#2f8c5a');palm(1130,820,.9,-1,'#7cc46a');
  const s=ctx.createLinearGradient(0,1230,0,H);s.addColorStop(0,'#f6cf5c');s.addColorStop(1,'#efb53f');ctx.fillStyle=s;
  ctx.beginPath();ctx.moveTo(0,1260);ctx.quadraticCurveTo(540,1180,1080,1250);ctx.lineTo(1080,H);ctx.lineTo(0,H);ctx.fill();
  ctx.save();ctx.fillStyle='#ffffff';const sw=Math.sin(T*1.6)*10;
  ctx.beginPath();ctx.moveTo(-20,1700+sw);ctx.bezierCurveTo(200,1690+sw,420,1780,600,H+20);ctx.lineTo(-20,H+20);ctx.fill();
  for(let i=0;i<9;i++){const k=i/8,x=-10+k*560,y=1700+sw+k*k*230;ctx.beginPath();ctx.arc(x,y,26+8*Math.sin(i*1.7),0,7);ctx.fill();}
  ctx.fillStyle='#7fd0f0';ctx.beginPath();ctx.moveTo(-20,1760+sw);ctx.bezierCurveTo(160,1760+sw,330,1820,470,H+20);ctx.lineTo(-20,H+20);ctx.fill();
  ctx.fillStyle='#5bbfe8';ctx.beginPath();ctx.moveTo(-20,1830+sw);ctx.bezierCurveTo(100,1830+sw,220,1870,300,H+20);ctx.lineTo(-20,H+20);ctx.fill();ctx.restore();
  ell(150,1735,48,26,'#b9b2a8',{lw:4});}
function nightBg(){const g=ctx.createLinearGradient(0,0,0,H);g.addColorStop(0,'#16224f');g.addColorStop(1,'#3b4a8c');ctx.fillStyle=g;ctx.fillRect(0,0,W,H);
  for(let i=0;i<60;i++){ctx.save();ctx.globalAlpha=.35+.5*Math.abs(Math.sin(T*1.5+i));ctx.fillStyle='#fff8d8';ctx.beginPath();ctx.arc(hash(i*3.3)*W,hash(i*7.1)*1300,2+hash(i)*3,0,7);ctx.fill();ctx.restore();}
  ctx.save();ctx.fillStyle='#fff3c4';ctx.shadowColor='rgba(255,243,196,.6)';ctx.shadowBlur=60;ctx.beginPath();ctx.arc(860,230,95,0,7);ctx.fill();ctx.shadowBlur=0;ctx.fillStyle='#16224f';ctx.beginPath();ctx.arc(820,195,88,0,7);ctx.fill();ctx.restore();}
function wrapW(txt,maxw){const out=[];for(const para of txt.split('\n')){let c='';for(const w of para.split(' ')){const t=c?c+' '+w:w;if(ctx.measureText(t).width>maxw&&c){out.push(c);c=w;}else c=t;}out.push(c);}return out;}
function bigText(txt,y,size,col='#ffffff',maxw=940,weight=800){ctx.save();ctx.font=weight+' '+size+'px '+FONT;ctx.textAlign='center';ctx.textBaseline='middle';
  const ls=wrapW(txt,maxw);ctx.fillStyle=col;ctx.shadowColor='rgba(40,20,40,.38)';ctx.shadowBlur=10;ctx.shadowOffsetY=4;ctx.lineJoin='round';
  ls.forEach((l,i)=>ctx.fillText(l,540,y+i*size*1.12));ctx.restore();return y+ls.length*size*1.12;}
function hearts(y,n,k,col='#ffffff'){const gap=62,x0=540-(n-1)*gap/2;for(let i=0;i<n;i++){ctx.save();ctx.translate(x0+i*gap,y);ctx.scale(1.25,1.25);
  ctx.beginPath();ctx.moveTo(0,10);ctx.bezierCurveTo(-24,-6,-12,-22,0,-10);ctx.bezierCurveTo(12,-22,24,-6,0,10);ctx.closePath();
  if(i<k){ctx.fillStyle=col;ctx.fill();}else{ctx.strokeStyle=col;ctx.lineWidth=3;ctx.stroke();}ctx.restore();}}
function pill(x,y,w,h,letter,txt,lcol){ctx.save();ctx.fillStyle='#fffaf6';ctx.strokeStyle='rgba(60,30,50,.85)';ctx.lineWidth=4;ctx.beginPath();ctx.roundRect(x-w/2,y-h/2,w,h,h/2);ctx.fill();ctx.stroke();
  ctx.fillStyle=lcol;ctx.beginPath();ctx.arc(x-w/2+h/2+4,y,h*.3,0,7);ctx.fill();ctx.strokeStyle='rgba(60,30,50,.6)';ctx.lineWidth=2.5;ctx.stroke();
  ctx.fillStyle='#3a2a3a';ctx.font='700 '+Math.round(h*.3)+'px '+FONT;ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText(letter,x-w/2+h/2+4,y+1);
  ctx.font='700 '+Math.round(h*.36)+'px '+FONT;ctx.fillText(txt,x+h*.25,y+1);ctx.restore();}
const LCOL=['#f5a9c3','#a9c4f5','#f7c98a','#b9e3a8'];
function abcdRow(y,i,txt,beach){const w=900,h=88,x=540;ctx.save();ctx.fillStyle='#ffffff';ctx.strokeStyle=beach?'#24324a':'rgba(60,30,50,.85)';ctx.lineWidth=beach?6:4;
  ctx.beginPath();ctx.roundRect(x-w/2,y-h/2,w,h,22);ctx.fill();ctx.stroke();
  ctx.fillStyle=['#ef6fa0','#9b7be0','#f39a4d','#4fa7e0'][i];ctx.beginPath();ctx.arc(x-w/2+50,y,28,0,7);ctx.fill();
  ctx.fillStyle='#ffffff';ctx.font='800 32px '+FONT;ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText('ABCD'[i],x-w/2+50,y+1);
  ctx.fillStyle='#24324a';ctx.font='600 40px '+FONT;ctx.textAlign='left';ctx.fillText(txt,x-w/2+100,y+2);ctx.restore();}
function bubble2(txt,cy,size=74,maxw=820){ctx.save();ctx.font='600 '+size+'px "Pixelify Sans"';const ls=wrapW(txt,maxw);const lh=size*1.18;const h=ls.length*lh+80;const w=Math.min(960,Math.max(...ls.map(l=>ctx.measureText(l).width))+110);
  const x=540-w/2,y=cy-h/2;ctx.fillStyle='#ffffff';ctx.strokeStyle='#24324a';ctx.lineWidth=8;ctx.lineJoin='round';
  ctx.beginPath();ctx.roundRect(x,y,w,h,36);ctx.fill();ctx.stroke();ctx.beginPath();ctx.moveTo(500,y+h-4);ctx.lineTo(540,y+h+46);ctx.lineTo(580,y+h-4);ctx.fill();
  ctx.beginPath();ctx.moveTo(500,y+h);ctx.lineTo(540,y+h+46);ctx.lineTo(580,y+h);ctx.stroke();
  ctx.fillStyle='#24324a';ctx.textAlign='center';ctx.textBaseline='middle';ls.forEach((l,i)=>ctx.fillText(l,540,y+40+lh/2+i*lh));ctx.restore();return y+h+46;}
function outlined(txt,y,size){ctx.save();ctx.font='800 '+size+'px '+FONT;ctx.textAlign='center';ctx.textBaseline='middle';ctx.lineJoin='round';ctx.strokeStyle='#24324a';ctx.lineWidth=10;ctx.strokeText(txt,540,y);ctx.fillStyle='#ffffff';ctx.fillText(txt,540,y);ctx.restore();}
function sign(txt,y){ctx.save();ctx.font='600 46px "Pixelify Sans"';const w=ctx.measureText(txt).width+120;ctx.fillStyle='#8a5530';ctx.strokeStyle='#5a3418';ctx.lineWidth=6;
  ctx.beginPath();ctx.roundRect(540-w/2,y-42,w,84,16);ctx.fill();ctx.stroke();ctx.strokeStyle='#c98a50';ctx.lineWidth=3;ctx.beginPath();ctx.roundRect(540-w/2+10,y-32,w-20,64,10);ctx.stroke();
  ctx.fillStyle='#fff3dc';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText(txt,540,y+2);ctx.restore();}
function rateGrid(y,beach){ctx.save();for(let i=0;i<10;i++){const x=540+((i%5)-2)*150,yy=y+Math.floor(i/5)*150;ctx.save();ctx.translate(x,yy);ctx.scale(2.9,2.9);
  ctx.beginPath();ctx.moveTo(0,16);ctx.bezierCurveTo(-30,-4,-16,-26,0,-12);ctx.bezierCurveTo(16,-26,30,-4,0,16);ctx.closePath();ctx.fillStyle='#ffffff';ctx.fill();ctx.lineWidth=2.4;ctx.strokeStyle='#24324a';ctx.stroke();ctx.restore();
  ctx.fillStyle='#24324a';ctx.font='600 50px "Pixelify Sans"';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText(String(i+1),x,yy-6);}ctx.restore();}
/* reactions near the pups */
function drop(x,y){ctx.save();ctx.fillStyle='#7cc4f2';ctx.strokeStyle='#24324a';ctx.lineWidth=3;ctx.beginPath();ctx.moveTo(x,y-26);ctx.quadraticCurveTo(x+18,y,x,y+10);ctx.quadraticCurveTo(x-18,y,x,y-26);ctx.fill();ctx.stroke();ctx.restore();}
function glyph(ch,x,y,col='#ffffff'){ctx.save();ctx.font='900 64px '+FONT;ctx.textAlign='center';ctx.lineJoin='round';ctx.strokeStyle='#24324a';ctx.lineWidth=8;ctx.strokeText(ch,x,y);ctx.fillStyle=col;ctx.fillText(ch,x,y);ctx.restore();}
const MOODS=[
 {b:{eyes:'open',mouth:'flat'},g:{eyes:'squint',mouth:'pout'},fx:(u)=>{drop(330,1180);glyph('?',820,1150);}},
 {b:{eyes:'happy',mouth:'smile',blush:.9},g:{eyes:'closed',mouth:'smile',blush:.9},fx:(u)=>{heart(540,1150-u*30,26,'#ec7489');heart(500,1190-u*20,18,'#f29bb3');}},
 {b:{eyes:'open',mouth:'o'},g:{eyes:'happy',mouth:'open'},fx:(u)=>{glyph('!',290,1150);sparkle(800,1160,30);}},
 {b:{eyes:'closed',mouth:'smile'},g:{eyes:'open',mouth:'smile'},fx:(u)=>{note(260,1170,1,1);note(830,1130,.9,1);}},
 {b:{eyes:'happy',mouth:'open'},g:{eyes:'squint',mouth:'flat'},fx:(u)=>{popcorn(520,1500,.9);}},
 {b:{eyes:'open',mouth:'smile'},g:{eyes:'wide',mouth:'o',blush:1},fx:(u)=>{drop(820,1170);glyph('!',860,1120);}},
 {b:{eyes:'squint',mouth:'smile'},g:{eyes:'happy',mouth:'smile'},fx:(u)=>{sparkle(260,1150,34);sparkle(820,1180,26);}},
 {b:{eyes:'wide',mouth:'o'},g:{eyes:'closed',mouth:'smile',blush:.8},fx:(u)=>{phoneS(820,1450,1.1,0);heart(760,1200,20,'#ec7489');}},
];
function pups(m,u,y,solo){const bob=Math.sin(T*3)*6;
  if(solo){pup(Object.assign({kind:'girl',x:540,y:y+bob*.5,s:1.35,shadow:true},m.g));phoneS(700,y-10,1.0,0);if(m.fx){ctx.save();ctx.translate(0,y-1520);m.fx(u);ctx.restore();}return;}
  pup(Object.assign({kind:'boy',x:320,y:y,s:1.15,shadow:true},m.b));pup(Object.assign({kind:'girl',x:760,y:y,s:1.15,flip:-1,shadow:true},m.g));if(m.fx){ctx.save();ctx.translate(0,y-1520);m.fx(u);ctx.restore();}}
function appCard(cy,u){const w=920,h=330,x=540-w/2,y=cy-h/2;ctx.save();ctx.shadowColor='rgba(0,0,0,.18)';ctx.shadowBlur=30;ctx.shadowOffsetY=10;ctx.fillStyle='#ffffff';
  ctx.beginPath();ctx.roundRect(x,y,w,h,44);ctx.fill();ctx.restore();
  ctx.save();ctx.fillStyle='#eeeef1';ctx.beginPath();ctx.roundRect(x+36,y+32,w-72,84,24);ctx.fill();
  ctx.strokeStyle='#8e8e93';ctx.lineWidth=5;ctx.beginPath();ctx.arc(x+84,y+70,14,0,7);ctx.stroke();ctx.beginPath();ctx.moveTo(x+94,y+80);ctx.lineTo(x+106,y+92);ctx.stroke();
  const q='couplein'.slice(0,Math.max(0,Math.min(8,Math.floor(u*14))));ctx.fillStyle='#1c1c1e';ctx.font='400 40px '+FONT;ctx.textBaseline='middle';ctx.fillText(q,x+124,y+75);
  if(Math.floor(T*2)%2==0){const tw=ctx.measureText(q).width;ctx.fillStyle='#0a84ff';ctx.fillRect(x+128+tw,y+52,4,46);}
  appIcon(x+40,y+148,150);ctx.fillStyle='#1c1c1e';ctx.font='700 46px '+FONT;ctx.textBaseline='alphabetic';ctx.fillText('CoupleIn',x+220,y+200);
  ctx.fillStyle='#8e8e93';ctx.font='400 32px '+FONT;ctx.fillText('Two selfies. One reveal.',x+220,y+244);ctx.font='400 28px '+FONT;ctx.fillText('★★★★★  Lifestyle',x+220,y+286);
  ctx.fillStyle='#0a84ff';ctx.beginPath();ctx.roundRect(x+w-200,y+186,150,70,35);ctx.fill();ctx.fillStyle='#ffffff';ctx.font='700 36px '+FONT;ctx.textAlign='center';ctx.fillText('GET',x+w-125,y+234);ctx.restore();
  for(let i=0;i<4;i++){const a=.5+.5*Math.sin(T*4+i*1.7);sparkle([x+w-30,x+w-70,x+20,x+w-20][i],[y+150,y+300,y+20,y-20][i],28+i*4,a,'#ffd75e');}}
function appIcon(x,y,s){ctx.save();ctx.translate(x,y);ctx.beginPath();ctx.roundRect(0,0,s,s,s*.23);ctx.save();ctx.clip();
  if(typeof ICONIMG!=='undefined'&&ICONIMG.complete&&ICONIMG.naturalWidth){ctx.drawImage(ICONIMG,0,0,s,s);}else{ctx.fillStyle='#ffffff';ctx.fillRect(0,0,s,s);}ctx.restore();
  ctx.strokeStyle='rgba(0,0,0,.12)';ctx.lineWidth=2;ctx.stroke();ctx.restore();}
function phoneShot(img,x,y,w){const h=w*img.height/img.width;ctx.save();ctx.shadowColor='rgba(0,0,0,.35)';ctx.shadowBlur=24;ctx.fillStyle='#111';ctx.beginPath();ctx.roundRect(x-8,y-8,w+16,h+16,w*.13);ctx.fill();ctx.restore();
  ctx.save();ctx.beginPath();ctx.roundRect(x,y,w,h,w*.11);ctx.clip();ctx.drawImage(img,x,y,w,h);ctx.restore();}
'''

TAIL = r'''
const IMGS=BOND.map(s=>{const i=new Image();i.src=s;return i;});
const CUTS=%s, TOTAL=%r;
function render(t){T=t;BOIL=0;ctx=MAIN;ctx.setTransform(1,0,0,1,0,0);ctx.globalAlpha=1;SC=0;
  let i=0;for(let k=0;k<CUTS.length;k++)if(t>=CUTS[k])i=k;const u=t-CUTS[i];
  const beach=S.theme=='beach';
  if(i==0){ // title
    if(beach){beachBg();const yb=bubble2(S.title,560);outlined(S.sub||'',yb+60,40);}
    else{flatBg(S.title_bg);const yb=bigText(S.title,560,96);ctx.save();ctx.font='700 40px '+FONT;ctx.fillStyle='#ffffff';ctx.textAlign='center';ctx.shadowColor='rgba(40,20,40,.3)';ctx.shadowBlur=6;ctx.fillText(S.sub||'',540,yb+50);ctx.restore();}
    pups(MOODS[0],u,beach?1600:1560,S.solo);return;}
  if(i==CUTS.length-1){ // end card
    if(beach){nightBg();bigText('search CoupleIn on the\napp store for more questions',360,64);appCard(720,u);
      if(IMGS.every(m=>m.complete)){phoneShot(IMGS[0],60,1020,300);phoneShot(IMGS[1],390,1000,300);phoneShot(IMGS[2],720,1020,300);}}
    else{flatBg('#f4a3bd');const ye=bigText('find more questions for\nyou two on CoupleIn',600,80,'#ffffff',1000);ctx.save();ctx.font='700 42px '+FONT;ctx.fillStyle='#ffffff';ctx.textAlign='center';ctx.shadowColor='rgba(40,20,40,.3)';ctx.shadowBlur=6;ctx.fillText('free on the app store',540,ye+30);ctx.restore();appCard(ye+330,u);}
    return;}
  const it=S.items[i-1],k=i,m=MOODS[(i+S.seed)%%MOODS.length];
  if(beach){beachBg();if(S.sign)sign(S.sign,240);if(S.kind=='rate')hearts(330,S.items.length,k,'#ffffff');
    const yb=bubble2((S.numbered?k+'. ':'')+it.q,S.kind=='rate'?520:(it.opts&&it.opts.length>2?520:560),S.kind=='rate'?60:(it.q.length>40?62:70),S.kind=='rate'?900:820);
    if(S.kind=='rate')rateGrid(yb+90,true);
    else if(it.opts&&it.opts.length>2)it.opts.forEach((o,j)=>abcdRow(yb+70+j*104,j,o,true));
    else if(it.opts){pill(300,yb+90,400,96,'a',it.opts[0],LCOL[0]);pill(780,yb+90,400,96,'b',it.opts[1],LCOL[1]);}
  } else {flatBg(S.colors[(i-1)%%S.colors.length]);
    ctx.save();ctx.font='700 40px '+FONT;ctx.fillStyle='#ffffff';ctx.textAlign='center';ctx.globalAlpha=.92;ctx.shadowColor='rgba(40,20,40,.3)';ctx.shadowBlur=6;ctx.fillText(S.label,540,330);ctx.restore();
    hearts(395,S.items.length,k);
    const yq=bigText((S.numbered?k+'. ':'')+it.q,520,it.q.length>55?72:84);
    if(it.opts&&it.opts.length>2)it.opts.forEach((o,j)=>abcdRow(yq+40+j*104,j,o,false));
    else if(it.opts){pill(300,yq+70,400,96,'a',it.opts[0],LCOL[0]);pill(780,yq+70,400,96,'b',it.opts[1],LCOL[1]);}
  }
  pups(m,u,beach?1620:1580,S.solo);
}
window.render=render;window.TOTAL=TOTAL;
'''


def build():
    head = (J.HEAD.replace('amp=o.amp??2.4', 'amp=o.amp??0.7').replace('jit(pts,o.j??1.2)', 'jit(pts,o.j??0.3)')
            .replace('jit(pts,o.j??1.8)', 'jit(pts,o.j??0.4)'))
    S = {k: spec[k] for k in ('theme', 'title', 'sub', 'label', 'items', 'kind', 'sign', 'solo', 'numbered', 'colors', 'title_bg', 'seed') if k in spec}
    S.setdefault('label', ''); S['seed'] = spec['n'] * 3; S.setdefault('colors', ['#c4677e', '#5d68b3', '#d8893a', '#6b7f3f', '#8a62b8', '#3f8a8a'])
    S.setdefault('title_bg', '#3f7f86'); S.setdefault('kind', 'open'); S.setdefault('solo', False); S.setdefault('numbered', False); S.setdefault('sign', '')
    js = (head + '\n' + J.COMMON + '\n' + SHORT_PROPS + '\n' + DK_JS + '\n' + QJS + '\n' +
          'const S=%s;\nconst BOND=%s;\nconst ICONIMG=new Image();ICONIMG.src=%s;\n' % (json.dumps(S, ensure_ascii=False), json.dumps([b64(f'{ASSETS}/bond{i}.png') for i in (1, 2, 3)]), json.dumps(b64(f'{ASSETS}/couplein_icon.png'))) +
          TAIL % (json.dumps(cuts), T) + '\n</script></body></html>')
    p = f'{W}/quiz.html'; open(p, 'w').write(js); return p


def page(p, html):
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
    pg = b.new_page(viewport={'width': 1080, 'height': 1920}); errs = []
    pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto('file://' + html)
    pg.evaluate("async()=>{await document.fonts.load('800 80px Inter');await document.fonts.load('600 70px \"Pixelify Sans\"');await document.fonts.load('700 40px Inter');await document.fonts.load('400 40px Inter');await new Promise(r=>setTimeout(r,300));}")
    pg.evaluate("async()=>{if(typeof ICONIMG!=='undefined'){await ICONIMG.decode().catch(()=>{});} if(typeof IMGS!=='undefined'){await Promise.all(IMGS.map(i=>i.decode().catch(()=>{})));}}")
    return b, pg, errs


def preview(html):
    from playwright.sync_api import sync_playwright
    ts = [(cuts[i] + (cuts[i + 1] if i + 1 < len(cuts) else T)) / 2 for i in range(len(cuts))]
    files = []
    with sync_playwright() as p:
        b, pg, errs = page(p, html)
        for k, t in enumerate(ts):
            pg.evaluate('t=>render(t)', t); f = f'{W}/pv_{k}.png'; pg.locator('#c').screenshot(path=f); files.append(f)
        b.close()
    if errs: print('PAGE ERRORS', errs[:3])
    nn = len(files); cols = min(nn, 4)
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error'] + sum([['-i', f] for f in files], []) +
                   ['-filter_complex', ''.join(f'[{k}:v]scale=270:-1[v{k}];' for k in range(nn)) + ''.join(f'[v{k}]' for k in range(nn)) +
                    f'xstack=inputs={nn}:layout=' + '|'.join(f'{(k % cols) * 270}_{(k // cols) * 480}' for k in range(nn)) + '[o]', '-map', '[o]', f'{W}/sheet.png'], check=True)
    print(f'{W}/sheet.png')


def render(html):
    from playwright.sync_api import sync_playwright
    nf = round(T * FPS); final = f'{OUT}/{slug}.mp4'
    with sync_playwright() as p:
        b, pg, errs = page(p, html)
        f = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', str(FPS), '-c:v', 'mjpeg', '-i', '-',
                              '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '20', '-preset', 'veryfast', '-movflags', '+faststart', final], stdin=subprocess.PIPE)
        for i in range(nf):
            u = pg.evaluate("t=>{render(t);return document.getElementById('c').toDataURL('image/jpeg',.93)}", i / FPS)
            f.stdin.write(base64.b64decode(u.split(',', 1)[1]))
        f.stdin.close(); f.wait(); b.close()
        if errs: print('PAGE ERRORS', errs[:3])
    dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', final], capture_output=True, text=True).stdout)
    ok = abs(dur - T) <= 1 / FPS
    print(json.dumps({'slug': slug, 'target': T, 'actual': round(dur, 3), 'ok': ok}))
    if not ok: sys.exit('LENGTH MISMATCH')


html = build()
preview(html) if mode == 'preview' else render(html)
