#!/usr/bin/env python3
"""DINKLY-STYLE 'note' remakes (19 Nov 2026) - see docs/DINKLY-FORMAT.md
Silent video (the song is added in the Instagram/TikTok app), exact source length.
One line of soft rounded text at the top per beat, the two pups in a flat pastel scene, hard cuts.

Spec specs/<slug>.py defines:
  TARGET = exact source length in seconds (frames = round(TARGET*30))
  BEATS  = list of (text, draw_js, seconds); the LAST beat's seconds is ignored and gets the remainder
  STYLE  = 'soft' (white lowercase rounded font) or 'bold' (black caps)   [default soft]
  PRELUDE optional extra JS
Usage: python3 make_note.py <slug> [preview]
"""
import importlib, json, os, subprocess, sys, base64
sys.path.insert(0, '/home/claude/jj'); sys.path.insert(0, '/home/claude/jj/specs')
import jjlib as J
from _short import SHORT_PROPS

slug = sys.argv[1]
mode = sys.argv[2] if len(sys.argv) > 2 else 'render'
spec = importlib.import_module(slug)
W = f'{J.ROOT}/work/{slug}'; os.makedirs(W, exist_ok=True)
OUT = f'{J.ROOT}/out'; os.makedirs(OUT, exist_ok=True)
FPS = 30

durs = [b[2] for b in spec.BEATS[:-1]]
assert sum(durs) < spec.TARGET - 0.3, 'beats longer than target'
durs.append(round(spec.TARGET - sum(durs), 4))

from _dk import DK_JS as EXTRA


TAIL = r'''
const DURS=%s;let acc=0;const T0=DURS.map(d=>{const a=acc;acc+=d;return a;});
const TOTAL=TARGET;const ZOOM=%s;let RAWB=false;{const _p=pup;pup=function(o){if(RAWB)return _p(o);o=Object.assign({},o);o.x=540+(o.x-540)*.92;return _p(o);};}
function wrapT(txt,maxw){const out=[];for(const para of txt.split('\n')){const ws=para.split(' ');let c='';for(const w of ws){const t=c?c+' '+w:w;if(ctx.measureText(t).width>maxw&&c){out.push(c);c=w;}else c=t;}out.push(c);}return out;}
function fit(s,sz,face,maxw){if(!s.includes('\n'))return sz;ctx.font=sz+'px '+face;while(sz>70&&Math.max(...s.split('\n').map(l=>ctx.measureText(l).width))>maxw){sz-=4;ctx.font=sz+'px '+face;}return sz;}
function text(s,o){if(!s)return;o=o||{};const st=o.style||STYLE;ctx.save();ctx.textAlign='center';ctx.textBaseline='middle';
  const y=o.y||(st=='bold'?250:400);
  if(st=='bold'||st=='bigcaps'){const sz=o.size||98;ctx.font='900 '+sz+'px Nunito';ctx.fillStyle=o.col||'#1d1d1d';const ls=wrapT(s.toUpperCase(),o.w||900);ls.forEach((l,i)=>ctx.fillText(l,540,y+i*sz*1.16));}
  else if(st=='outline'){const sz=o.size||86;ctx.font='900 '+sz+'px Nunito';ctx.lineJoin='round';const ls=wrapT(s.toUpperCase(),o.w||900);ls.forEach((l,i)=>{ctx.strokeStyle='#2b1d13';ctx.lineWidth=16;ctx.strokeText(l,540,y+i*sz*1.15);ctx.fillStyle='#ffffff';ctx.fillText(l,540,y+i*sz*1.15);});}
  else if(st=='caps'){const sz=o.size||(s.length>45?104:124);ctx.font=sz+'px Neucha';ctx.fillStyle=o.col||'#2b2b2b';const ls=wrapT(s.toUpperCase(),o.w||940);const y0=y-(ls.length-1)*sz*.53;ls.forEach((l,i)=>ctx.fillText(l,540,y0+i*sz*1.06));}
  else if(st=='dark'){const sz=o.size||134;ctx.font=sz+'px Neucha';ctx.fillStyle=o.col||'#2b2b2b';const ls=wrapT(s,o.w||800);const y0=y-(ls.length-1)*sz*.53;ls.forEach((l,i)=>ctx.fillText(l,540,y0+i*sz*1.06));}
  else{const sz=fit(s,o.size?o.size*1.6:(s.length>90?100:s.length>50?118:140),'Neucha',890);ctx.font=sz+'px Neucha';ctx.fillStyle=o.col||'#fffdf7';ctx.shadowColor='rgba(0,0,0,.18)';ctx.shadowBlur=8;
    const ls=wrapT(s,o.w||920);const y0=y-(ls.length-1)*sz*.52;ls.forEach((l,i)=>ctx.fillText(l,540,y0+i*sz*1.04));}
  ctx.restore();}

function appIcon(x,y,s){ctx.save();ctx.translate(x,y);ctx.fillStyle='#FF6B9D';ctx.beginPath();ctx.roundRect(0,0,s,s,s*.24);ctx.fill();
  ctx.fillStyle='#ffffff';const h=(cx,cy,r)=>{ctx.beginPath();ctx.moveTo(cx,cy+r*.9);ctx.bezierCurveTo(cx-r*1.3,cy-r*.1,cx-r*.6,cy-r*1.1,cx,cy-r*.45);ctx.bezierCurveTo(cx+r*.6,cy-r*1.1,cx+r*1.3,cy-r*.1,cx,cy+r*.9);ctx.fill();};
  h(s*.42,s*.56,s*.26);ctx.globalAlpha=.75;h(s*.62,s*.46,s*.18);ctx.restore();}
function wrapF(txt,maxw){const ws=txt.split(' ');const out=[];let c='';for(const w of ws){const t=c?c+' '+w:w;if(ctx.measureText(t).width>maxw&&c){out.push(c);c=w;}else c=t;}out.push(c);return out;}
function notif(n,u){const d=n.at||0.25;if(u<d)return;const k=ease((u-d)/.35);
  const x=40,w=1000,y=lerp(540,600,k);ctx.save();ctx.font='40px Inter';const lines=wrapF(n.body,w-190);const h=100+lines.length*50;
  ctx.globalAlpha=k;ctx.save();ctx.beginPath();ctx.roundRect(x,y,w,h,44);ctx.clip();ctx.filter='blur(22px)';ctx.drawImage(cv,0,0);ctx.filter='none';
  ctx.fillStyle='rgba(40,38,48,.42)';ctx.fillRect(x,y,w,h);ctx.fillStyle='rgba(255,255,255,.10)';ctx.fillRect(x,y,w,h);ctx.restore();
  ctx.strokeStyle='rgba(255,255,255,.18)';ctx.lineWidth=2;ctx.beginPath();ctx.roundRect(x,y,w,h,44);ctx.stroke();
  appIcon(x+32,y+30,92);ctx.fillStyle='#ffffff';ctx.textBaseline='top';ctx.textAlign='left';
  ctx.font='600 40px Inter';ctx.fillText(n.title,x+150,y+28);ctx.font='30px Inter';ctx.fillStyle='rgba(255,255,255,.7)';ctx.textAlign='right';ctx.fillText('now',x+w-36,y+32);
  ctx.textAlign='left';ctx.fillStyle='#ffffff';ctx.font='40px Inter';lines.forEach((l,i)=>ctx.fillText(l,x+150,y+78+i*50));ctx.restore();}
function render(t){
  T=t;BOIL=0;
  let i=T0.findIndex((a,k)=>t<a+DURS[k]);if(i<0)i=DURS.length-1;
  ctx=MAIN;ctx.setTransform(1,0,0,1,0,0);ctx.globalAlpha=1;SC=0;
  const B=BEATS[i];RAWB=!!B.o.raw;ctx.save();if(!B.o.raw){const z=B.o.zoom||ZOOM;ctx.translate(540,1500);ctx.scale(z,z);ctx.translate(-540,-1180);}B.draw(t-T0[i]);ctx.restore();
  text(B.text,B.o);
  if(B.o.notif){ctx.setTransform(1,0,0,1,0,0);notif(B.o.notif,t-T0[i]);}
}
window.render=render;window.TOTAL=TOTAL;
'''


def build():
    beats = ['{text:%s,o:%s,draw(u){\n%s\n}}' % (json.dumps(b[0], ensure_ascii=False), json.dumps(b[3] if len(b) > 3 else {}), b[1]) for b in spec.BEATS]
    js = (J.HEAD.replace('amp=o.amp??2.4','amp=o.amp??0.7').replace('jit(pts,o.j??1.2)','jit(pts,o.j??0.3)').replace('jit(pts,o.j??1.8)','jit(pts,o.j??0.4)') + '\n' + J.COMMON + '\n' + SHORT_PROPS + '\n' + EXTRA + '\n' + getattr(spec, 'PRELUDE', '') + '\n' +
          'const TARGET=%r, STYLE=%s;\n' % (spec.TARGET, json.dumps(getattr(spec, 'STYLE', 'soft'))) +
          'const BEATS=[\n' + ',\n'.join(beats) + '];\n' + TAIL % (json.dumps(durs), getattr(spec,'ZOOM',1.48)) + '\n</script></body></html>')
    p = f'{W}/note.html'
    open(p, 'w').write(js)
    return p


def page(p, html):
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
    pg = b.new_page(viewport={'width': 1080, 'height': 1920}); errs = []
    pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto('file://' + html)
    pg.evaluate("async()=>{await document.fonts.load('bold 80px Poppins');await document.fonts.load('64px Itim');await document.fonts.load('100px \"Patrick Hand\"');await document.fonts.load('100px Neucha');await document.fonts.load('600 36px Inter');await document.fonts.load('34px Inter');await document.fonts.load('900 74px Nunito');}")
    return b, pg, errs


def preview(html):
    from playwright.sync_api import sync_playwright
    files = []
    with sync_playwright() as p:
        b, pg, errs = page(p, html)
        t0 = 0
        for i, d in enumerate(durs):
            pg.evaluate('t=>render(t)', t0 + d * .6)
            f = f'{W}/pv_{i}.png'; pg.locator('#c').screenshot(path=f); files.append(f)
            t0 += d
        b.close()
    if errs: print('PAGE ERRORS', errs[:3])
    n = len(files)
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error'] + sum([['-i', f] for f in files], []) +
                   ['-filter_complex', ''.join(f'[{k}:v]scale=360:-1[v{k}];' for k in range(n)) +
                    ''.join(f'[v{k}]' for k in range(n)) + f'xstack=inputs={n}:layout=' +
                    '|'.join(f'{(k % 3) * 360}_{(k // 3) * 640}' for k in range(n)) + '[o]', '-map', '[o]', f'{W}/sheet.png'], check=True)
    print(f'{W}/sheet.png', durs)


def render(html):
    from playwright.sync_api import sync_playwright
    n = round(spec.TARGET * FPS)
    final = f'{OUT}/{slug.replace("_", "-")}.mp4'
    with sync_playwright() as p:
        b, pg, errs = page(p, html)
        f = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', str(FPS), '-c:v', 'mjpeg', '-i', '-',
                              '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '20', '-preset', 'veryfast', '-movflags', '+faststart', final],
                             stdin=subprocess.PIPE)
        for i in range(n):
            u = pg.evaluate("t=>{render(t);return document.getElementById('c').toDataURL('image/jpeg',.93)}", i / FPS)
            f.stdin.write(base64.b64decode(u.split(',', 1)[1]))
        f.stdin.close(); f.wait(); b.close()
        if errs: print('PAGE ERRORS', errs[:3])
    dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', final],
                               capture_output=True, text=True).stdout)
    qa = {'target_s': spec.TARGET, 'actual_s': round(dur, 3), 'frames': n, 'off_by_s': round(dur - spec.TARGET, 3),
          'size_mb': round(os.path.getsize(final) / 1e6, 1), 'audio': 'none - song added in-app'}
    qa['length_ok'] = abs(dur - spec.TARGET) <= 1 / FPS
    json.dump(qa, open(os.path.splitext(final)[0] + '.qa.json', 'w'))
    print(json.dumps(qa)); print(final)
    if not qa['length_ok']:
        sys.exit('LENGTH MISMATCH')


html = build()
preview(html) if mode == 'preview' else render(html)
