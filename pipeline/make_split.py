#!/usr/bin/env python3
"""DINKLY-STYLE remakes (19 Nov 2026) - see docs/DINKLY-FORMAT.md
Silent video (song is added in the Instagram/TikTok app), exact source length.

Format "split": N panels, each = left half 'X' (alone, meh) | right half 'X WITH YOU' (both, happy),
hard cuts, then a zoom-out to a 2x2 grid of the panels that holds to the end.

Spec specs/<slug>.py defines:
  TARGET   = exact length in seconds of the source reel (frames = round(TARGET*30))
  GRID_AT  = time the grid zoom-out starts
  PANELS   = list of dict(bg, floor, ink, left_label, right_label, left=js, right=js)
             js draws with origin at the half's centre on the floor line (y=0 is the floor)
  PRELUDE  = optional extra JS (props)
Usage: python3 make_split.py <slug> [preview]
"""
import importlib, json, os, subprocess, sys, base64
sys.path.insert(0, '/home/claude/jj'); sys.path.insert(0, '/home/claude/jj/specs')
import jjlib as J
from _dk import DK_JS
from _short import SHORT_PROPS

slug = sys.argv[1]
mode = sys.argv[2] if len(sys.argv) > 2 else 'render'
spec = importlib.import_module(slug)
W = f'{J.ROOT}/work/{slug}'; os.makedirs(W, exist_ok=True)
OUT = f'{J.ROOT}/out'; os.makedirs(OUT, exist_ok=True)
FPS = 30

PROPS = r'''
const FLOOR=1250, DIVTOP=560;
function lab(txt,x,y,col){ctx.save();ctx.font='60px Neucha';ctx.textAlign='center';ctx.textBaseline='top';ctx.fillStyle=col;
  const ws=txt.split(' ');const ls=[];let c='';for(const w of ws){const t=c?c+' '+w:w;if(ctx.measureText(t).width>440&&c){ls.push(c);c=w;}else c=t;}ls.push(c);
  ls.forEach((l,i)=>ctx.fillText(l,x,y+i*62));ctx.restore();}
function half(side,fn,u){ctx.save();ctx.beginPath();ctx.rect(side?540:0,0,540,H);ctx.clip();ctx.translate(side?810:270,FLOOR);ctx.scale(1.22,1.22);fn(u);ctx.restore();}
function drawPanel(p,u){SC=0;
  ctx.fillStyle=p.bg;ctx.fillRect(0,0,W,H);
  if(SIDE){ctx.fillStyle='#ffffff';ctx.fillRect(0,0,W,H);
    for(const sd of[0,1]){ctx.save();ctx.beginPath();ctx.roundRect(sd?552:18,330,510,1060,26);ctx.clip();ctx.fillStyle=sd?(p.bg2||p.bg):p.bg;ctx.fillRect(0,0,W,H);
      if(p.floor){ctx.fillStyle=p.floor;ctx.fillRect(0,FLOOR,W,H-FLOOR);}ctx.translate(sd?807:273,FLOOR);ctx.scale(1.12,1.12);(sd?p.right:p.left)(u);ctx.restore();}
    lab(p.left_label,273,1440,p.ink);lab(p.right_label,807,1440,p.ink);return;}
  if(p.floor){ctx.fillStyle=p.floor;ctx.fillRect(0,FLOOR,W,H-FLOOR);}
  half(0,p.left,u);half(1,p.right,u);
  ctx.save();ctx.strokeStyle=p.ink;ctx.lineWidth=5;ctx.lineCap='round';ctx.beginPath();ctx.moveTo(540,DIVTOP);ctx.lineTo(540,FLOOR+40);ctx.stroke();ctx.restore();
  lab(p.left_label,270,FLOOR+110,p.ink);lab(p.right_label,810,FLOOR+110,p.ink);}
'''

TAIL = r'''
const TOTAL=TARGET;
const NP=PANELS.length;const T0S=CUTS;const pidx=t=>{let i=0;for(let k=0;k<NP;k++)if(t>=T0S[k])i=k;return i;};
const tiles=PANELS.map(()=>{const c=document.createElement('canvas');c.width=W;c.height=H;return c;});
const TW=518,TH=921,GX=[15,547],GY=[26,973];
function render(t){
  T=t;BOIL=0;
  ctx=MAIN;ctx.setTransform(1,0,0,1,0,0);ctx.globalAlpha=1;
  if(!GRID||t<GRID_AT){const i=pidx(t);drawPanel(PANELS[i],t-T0S[i]);return;}
  // grid: every tile keeps animating
  tiles.forEach((c,i)=>{ctx=c.getContext('2d');ctx.setTransform(1,0,0,1,0,0);drawPanel(PANELS[i],t-T0S[i]);});
  ctx=MAIN;ctx.fillStyle='#ffffff';ctx.fillRect(0,0,W,H);
  const k=ease((t-GRID_AT)/.7);
  tiles.forEach((c,i)=>{const gx=GX[i%2],gy=GY[Math.floor(i/2)];
    const last=i==NP-1;
    const x=last?lerp(0,gx,k):gx,y=last?lerp(0,gy,k):gy,w=last?lerp(W,TW,k):TW,h=last?lerp(H,TH,k):TH;
    if(!last){ctx.globalAlpha=k;}
    ctx.save();ctx.beginPath();ctx.roundRect(x,y,w,h,22*k);ctx.clip();ctx.drawImage(c,x,y,w,h);ctx.restore();ctx.globalAlpha=1;});
  // draw last tile on top during zoom
  const i=NP-1,c=tiles[i],gx=GX[i%2],gy=GY[Math.floor(i/2)];
  ctx.save();ctx.beginPath();ctx.roundRect(lerp(0,gx,k),lerp(0,gy,k),lerp(W,TW,k),lerp(H,TH,k),22*k);ctx.clip();
  ctx.drawImage(c,lerp(0,gx,k),lerp(0,gy,k),lerp(W,TW,k),lerp(H,TH,k));ctx.restore();
}
window.render=render;window.TOTAL=TOTAL;
'''


def build():
    panels = []
    for p in spec.PANELS:
        panels.append('{bg2:%s,bg:%s,floor:%s,ink:%s,left_label:%s,right_label:%s,left(u){\n%s\n},right(u){\n%s\n}}' % (
            json.dumps(p.get('bg2')), json.dumps(p['bg']), json.dumps(p.get('floor')), json.dumps(p.get('ink', '#2b2b2b')),
            json.dumps(p['left_label']), json.dumps(p['right_label']), p['left'], p['right']))
    js = (J.HEAD.replace('amp=o.amp??2.4','amp=o.amp??0.7').replace('jit(pts,o.j??1.2)','jit(pts,o.j??0.3)').replace('jit(pts,o.j??1.8)','jit(pts,o.j??0.4)') + '\n' + J.COMMON + '\n' + SHORT_PROPS + '\n' + DK_JS + '\n' + PROPS + '\n' + getattr(spec, 'PRELUDE', '') + '\n' +
          'const TARGET=%r, GRID_AT=%r, GRID=%s, SIDE=%s, CUTS=%s;\n' % (spec.TARGET, getattr(spec,'GRID_AT',spec.TARGET), 'true' if getattr(spec,'GRID',True) else 'false', 'true' if getattr(spec,'SIDE',False) else 'false', json.dumps(spec.CUTS)) +
          'const PANELS=[\n' + ',\n'.join(panels) + '];\n' + TAIL + '\n</script></body></html>')
    p = f'{W}/split.html'
    open(p, 'w').write(js)
    return p


def page(p, html):
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
    pg = b.new_page(viewport={'width': 1080, 'height': 1920}); errs = []
    pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto('file://' + html)
    pg.evaluate("async()=>{await document.fonts.load('bold 80px Poppins');await document.fonts.load('70px \"Noto Color Emoji\"');await document.fonts.load('60px Neucha');}")
    return b, pg, errs


def frames_at(times, prefix):
    from playwright.sync_api import sync_playwright
    out = []
    with sync_playwright() as p:
        b, pg, errs = page(p, html)
        for k, t in enumerate(times):
            pg.evaluate('t=>render(t)', t)
            f = f'{W}/{prefix}{k}.png'; pg.locator('#c').screenshot(path=f); out.append(f)
        b.close()
    if errs: print('PAGE ERRORS', errs[:3])
    return out


def sheet(files, path, cols=4):
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error'] + sum([['-i', f] for f in files], []) +
                   ['-filter_complex', ''.join(f'[{k}:v]scale=270:-1[v{k}];' for k in range(len(files))) +
                    ''.join(f'[v{k}]' for k in range(len(files))) + f'xstack=inputs={len(files)}:layout=' +
                    '|'.join(f'{(k % cols) * 270}_{(k // cols) * 480}' for k in range(len(files))) + '[o]', '-map', '[o]', path], check=True)
    print(path)


def render():
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
          'size_mb': round(os.path.getsize(final) / 1e6, 1), 'audio': 'none - add the song in-app'}
    qa['length_ok'] = abs(dur - spec.TARGET) <= 1 / FPS
    json.dump(qa, open(os.path.splitext(final)[0] + '.qa.json', 'w'))
    print(json.dumps(qa)); print(final)
    if not qa['length_ok']:
        sys.exit('LENGTH MISMATCH')


html = build()
if mode == 'preview':
    c = spec.CUTS + [getattr(spec, 'GRID_AT', spec.TARGET)]
    ts = [(c[i] + c[i + 1]) / 2 for i in range(len(spec.PANELS))] + ([getattr(spec, 'GRID_AT', 0) + .35, spec.TARGET - .1] if getattr(spec, 'GRID', True) else [])
    sheet(frames_at(ts, 'pv_'), f'{W}/sheet.png', cols=min(len(ts), 4))
else:
    render()
