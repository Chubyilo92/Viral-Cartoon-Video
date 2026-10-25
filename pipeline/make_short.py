#!/usr/bin/env python3
"""SHORT FORMAT (test, 26 Oct 2026) - see docs/SHORT-FORMAT.md
~18-22s, no narrator (music only), one persistent hook line on top for the whole video,
one plain sentence per beat, a twist beat, ends on the peak (no quiz/follow end card).

Spec file specs/<slug>.py must define:
  HOOK   = persistent top line (str)
  BEATS  = list of (caption_str, draw_js_body, seconds)
  PRELUDE (optional) extra JS (props); SHORT_PROPS from _short.py is always included
  MUSIC_N (optional) 1-3
Usage: python3 make_short.py <slug> [preview]
"""
import importlib, json, os, subprocess, sys, hashlib, base64
sys.path.insert(0, '/home/claude/jj'); sys.path.insert(0, '/home/claude/jj/specs')
import jjlib as J
from _short import SHORT_PROPS

slug = sys.argv[1]
mode = sys.argv[2] if len(sys.argv) > 2 else 'render'
spec = importlib.import_module(slug)
W = f'{J.ROOT}/work/{slug}'; os.makedirs(W, exist_ok=True)
OUT = f'{J.ROOT}/out'; os.makedirs(OUT, exist_ok=True)

TAIL = r'''
let acc=0;for(const s of SCENES){s.t0=acc;acc+=s.d;}
const TOTAL=acc;
const grain=document.createElement('canvas');grain.width=W;grain.height=H;
(function(){const g=grain.getContext('2d');g.fillStyle='#fff';g.fillRect(0,0,W,H);const id=g.getImageData(0,0,W,H),d=id.data;
  for(let i=0;i<d.length;i+=4){const r=Math.random();const v=255-Math.pow(r,3)*38;d[i]=v;d[i+1]=v-2;d[i+2]=v-6;}g.putImageData(id,0,0);
  const v=g.createRadialGradient(W/2,H*.48,H*.28,W/2,H*.5,H*.75);v.addColorStop(0,'rgba(255,255,255,0)');v.addColorStop(1,'rgba(150,100,60,.40)');g.fillStyle=v;g.fillRect(0,0,W,H);})();
function drawScene(i,t){const s=SCENES[i],u=t-s.t0;SC=0;
  ctx.save();const z=1+.04*clamp(u/s.d);ctx.translate(540,1000);ctx.scale(z,z);ctx.translate(-540,-1000);ctx.translate(540,1300);ctx.scale(1.2,1.2);ctx.translate(-540,-1180);s.draw(u);ctx.restore();}
function wrap(txt,maxw){const ws=txt.split(' ');const lines=[];let cur='';
  for(const w of ws){const tst=cur?cur+' '+w:w;if(ctx.measureText(tst).width>maxw&&cur){lines.push(cur);cur=w;}else cur=tst;}if(cur)lines.push(cur);return lines;}
function outlined(lines,y,size,lh,fill,strokeW){ctx.font='bold '+size+'px Poppins, "Noto Color Emoji"';ctx.textAlign='center';ctx.textBaseline='middle';ctx.lineJoin='round';
  lines.forEach((l,i)=>{const yy=y+i*lh;ctx.strokeStyle='#2c1d13';ctx.lineWidth=strokeW;ctx.strokeText(l,540,yy);ctx.fillStyle=fill;ctx.fillText(l,540,yy);});}
function hook(){ctx.save();ctx.font='bold 62px Poppins, "Noto Color Emoji"';const ls=wrap(HOOK,920);outlined(ls,300,62,78,'#ffffff',14);ctx.restore();}
function beatCap(s,u){if(!s.cap)return;ctx.save();const k=pop(u,.12,.35);ctx.globalAlpha=clamp((u-.12)/.12)*clamp((s.d-u)/.15);
  ctx.translate(540,1440);ctx.scale(.85+.15*k,.85+.15*k);ctx.translate(-540,-1440);
  ctx.font='bold 72px Poppins, "Noto Color Emoji"';const ls=wrap(s.cap,930);const y0=1440-(ls.length-1)*24;outlined(ls,y0,72,88,'#fffaf0',16);ctx.restore();}
function render(t,withCap=true){
  T=t;BOIL=Math.floor(t*8);
  let i=SCENES.findIndex(s=>t<s.t0+s.d);if(i<0)i=SCENES.length-1;
  ctx=MAIN;ctx.setTransform(1,0,0,1,0,0);ctx.globalAlpha=1;ctx.globalCompositeOperation='source-over';
  drawScene(i,t);
  const FD=.25,s=SCENES[i];
  if(i<SCENES.length-1&&s.t0+s.d-t<FD){ctx=OFF;ctx.setTransform(1,0,0,1,0,0);ctx.clearRect(0,0,W,H);drawScene(i+1,s.t0+s.d);ctx=MAIN;
    ctx.globalAlpha=1-(s.t0+s.d-t)/FD;ctx.drawImage(off,0,0);ctx.globalAlpha=1;}
  ctx.globalCompositeOperation='multiply';ctx.drawImage(grain,0,0);ctx.globalCompositeOperation='source-over';
  if(withCap){hook();beatCap(s,t-s.t0);}
}
window.render=render;window.TOTAL=TOTAL;window.SCENES=SCENES;
'''


def build():
    scenes = []
    for cap, body, d in spec.BEATS:
        scenes.append('{cap:%s,d:%s,draw(u){\n%s\n}}' % (json.dumps(cap, ensure_ascii=False), d, body))
    js = (J.HEAD + '\n' + J.COMMON + '\n' + SHORT_PROPS + '\n' + getattr(spec, 'PRELUDE', '') + '\n' +
          'const HOOK=%s;\n' % json.dumps(spec.HOOK, ensure_ascii=False) +
          'const SCENES=[\n' + ',\n'.join(scenes) + '];\n' + TAIL + '\n</script></body></html>')
    p = f'{W}/short.html'
    open(p, 'w').write(js)
    return p


def page(p, html):
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1080, 'height': 1920}); errs = []
    pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto('file://' + html)
    pg.evaluate("async()=>{await document.fonts.load('bold 80px Poppins');await document.fonts.load('70px \"Noto Color Emoji\"');}")
    return b, pg, errs


def preview(html):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b, pg, errs = page(p, html)
        t0 = 0
        for i, (_, _, d) in enumerate(spec.BEATS):
            for j, f in enumerate((.35, .9)):
                pg.evaluate('t=>render(t,true)', t0 + d * f)
                pg.locator('#c').screenshot(path=f'{W}/pv_{i}_{j}.png')
            t0 += d
        print('errors', errs[:3])
        b.close()
    # contact sheet
    files = [f'{W}/pv_{i}_{j}.png' for i in range(len(spec.BEATS)) for j in (0, 1)]
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error'] + sum([['-i', f] for f in files], []) +
                   ['-filter_complex', ''.join(f'[{k}:v]scale=270:-1[v{k}];' for k in range(len(files))) +
                    ''.join(f'[v{k}]' for k in range(len(files))) + f'xstack=inputs={len(files)}:layout=' +
                    '|'.join(f'{(k % 4) * 270}_{(k // 4) * 480}' for k in range(len(files))) + '[o]', '-map', '[o]',
                    f'{W}/sheet.png'], check=True)
    print(f'{W}/sheet.png')


def render(html):
    from playwright.sync_api import sync_playwright
    silent = f'{W}/silent.mp4'
    with sync_playwright() as p:
        b, pg, errs = page(p, html)
        total = pg.evaluate('TOTAL'); n = round(total * 30)
        f = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', '30', '-c:v', 'mjpeg', '-i', '-',
                              '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '22', '-preset', 'veryfast', '-movflags', '+faststart', silent],
                             stdin=subprocess.PIPE)
        for i in range(n):
            u = pg.evaluate("t=>{render(t,true);return document.getElementById('c').toDataURL('image/jpeg',.92)}", i / 30)
            f.stdin.write(base64.b64decode(u.split(',', 1)[1]))
        f.stdin.close(); f.wait(); b.close()
        if errs: print('PAGE ERRORS', errs[:3])
    mn = getattr(spec, 'MUSIC_N', None) or (int(hashlib.md5(slug.encode()).hexdigest(), 16) % 3 + 1)
    music = f'{J.ROOT}/music/sound{mn}.wav'
    final = f'{OUT}/{slug.replace("_", "-")}.mp4'
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', silent, '-i', music, '-filter_complex',
                    f'[1:a]atrim=0:{total:.2f},asetpts=PTS-STARTPTS,afade=t=in:d=0.3,afade=t=out:st={total-1.2:.2f}:d=1.2,loudnorm=I=-14:TP=-1.5:LRA=8[a]',
                    '-map', '0:v', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-shortest', '-movflags', '+faststart', final], check=True)
    pr = json.loads(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'stream=codec_type,duration', '-of', 'json', final],
                                   capture_output=True, text=True).stdout)['streams']
    qa = {'total_s': round(total, 1), 'streams': {s['codec_type']: float(s.get('duration', 0)) for s in pr},
          'size_mb': round(os.path.getsize(final) / 1e6, 1), 'music': mn}
    qa['duration_ok'] = 15 <= total <= 24
    qa['audio_ok'] = abs(qa['streams'].get('audio', 0) - qa['streams'].get('video', 0)) < 1
    print(json.dumps(qa)); print(final)


html = build()
if mode == 'preview':
    preview(html)
else:
    render(html)
