#!/usr/bin/env python3
"""Two-voice dialogue builder for JJ puppy videos (no narrator).
Each spec line = (who, text). who: 'boy' | 'girl'. Boy = Kokoro am_puck pitched up,
girl = Kokoro af_heart pitched up (rubberband, formant shifted -> cute cartoon pup).
Usage: python3 dialogue.py <slug>     spec at specs/<slug>.py
Spec: TITLE, LINES=[D(...),...], END=D(...) (end card scene), optional MUSIC_N."""
import importlib, re, json, os, re, subprocess, sys, time, hashlib, base64
sys.path.insert(0, '/home/claude/jj'); sys.path.insert(0, '/home/claude/jj/specs')
import numpy as np, soundfile as sf
import jjlib as J

PAD = 0.8
J.PAD = PAD
VOICES = {
    'boy':  dict(voice='am_puck',  speed=0.9, pitch=1.36),
    'girl': dict(voice='af_heart', speed=0.9, pitch=1.24),
    'friend': dict(voice='af_sky', speed=0.95, pitch=1.36),
    'mum':    dict(voice='bf_emma', speed=0.88, pitch=1.1),
    'ex':     dict(voice='bm_lewis', speed=0.92, pitch=1.42),
}
CAPCOLS = {'boy': '#bfe3ff', 'girl': '#ffc9dc', 'friend': '#fff0a0', 'mum': '#e3ccff', 'ex': '#ffb4a8'}

PRELUDE = r'''
let CURVO=3,CURLEAD=0,CAPCOL='#fffaf0';
function talking(u){return u>.22+CURLEAD&&u<.12+CURLEAD+CURVO;}
function tm(u,rest){if(!talking(u))return rest;const seq=['open','o','w','open','smile','o','open','w','o'];return seq[(Math.floor(u*9)*7+3)%seq.length];}
function SP(kind,u,o){const b=Object.assign({kind,y:G+10,s:1.3},o);if(o.talk&&talking(u)){b.mouth=tm(u,o.mouth||'smile');b.bob=(b.bob||0)-Math.abs(Math.sin(u*9))*6;}pup(b);}
function chip(txt,a){if(a<=0)return;ctx.save();ctx.setTransform(1,0,0,1,0,0);ctx.globalAlpha=clamp(a);ctx.font='bold 46px Poppins, "Noto Color Emoji"';const w=ctx.measureText(txt).width+70;ctx.translate(540,440);ctx.fillStyle='#2c1d13';ctx.beginPath();ctx.roundRect(-w/2,-38,w,76,38);ctx.fill();ctx.fillStyle='#fff3c4';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText(txt,0,3);ctx.restore();}
function fridge(x,y,open,full){ctx.save();ctx.translate(x,y);
  blob(rectPts(-110,-430,220,430,22),'#eef3f6',{lw:6});line([[-110,-290],[110,-290]],{lw:5});
  if(open>0){blob(rectPts(-96,-276,192,262,10),'#fdfbe9',{lw:4});
    const lg=ctx.createRadialGradient(0,-160,10,0,-160,160);lg.addColorStop(0,'rgba(255,250,200,'+(.55*open)+')');lg.addColorStop(1,'rgba(255,250,200,0)');ctx.fillStyle=lg;ctx.fillRect(-160,-330,320,330);
    line([[-96,-190],[96,-190]],{lw:4});line([[-96,-100],[96,-100]],{lw:4});
    if(full)milk(-30,-104,.62);else{ctx.save();ctx.globalAlpha=.5;ell(-40,-108,22,6,'#d8d2bf',{stroke:false});ctx.restore();}
    ell(40,-118,26,16,'#f2c55c');
    ctx.save();ctx.translate(-110,-140);ctx.scale(1-open*.85,1);blob(rectPts(-200,-136,200,272,18),'#e3eaee',{lw:5});ctx.restore();}
  else{line([[78,-250],[78,-170]],{lw:9});}
  line([[78,-400],[78,-330]],{lw:9});ctx.restore();}
function milk(x,y,s,rot=0){ctx.save();ctx.translate(x,y);ctx.rotate(rot);ctx.scale(s,s);
  blob([[-46,-110],[46,-110],[46,0],[-46,0]],'#fbfbf6',{lw:6});blob([[-46,-110],[0,-152],[46,-110]],'#5aa0d8',{lw:6});
  blob(rectPts(-9,-168,18,18,4),'#5aa0d8',{lw:4});blob(rectPts(-46,-78,92,46,6),'#5aa0d8',{lw:4});
  ctx.fillStyle='#fff';ctx.font='bold 26px Poppins';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText('MILK',0,-54);ctx.restore();}
function cereal(x,y,s,wet){ctx.save();ctx.translate(x,y);ctx.scale(s,s);
  ell(0,-58,92,18,wet?'#fbf6ea':'#e7c98c');for(let i=0;i<9;i++){const a=i*1.9;ell(Math.cos(a)*55*(i%3)/2,-60+Math.sin(a)*8,12,7,'#e2a54b',{lw:3});}
  blob([[-96,-58],[96,-58],[80,-4],[0,4],[-80,-4]],'#7fb3d9');ell(0,-58,96,17,'none',{lw:5});ctx.restore();}
function brownies(x,y,s,steam){ctx.save();ctx.translate(x,y);ctx.scale(s,s);
  if(steam>0){for(let i=0;i<3;i++){const ph=T*2+i*2;ctx.save();ctx.globalAlpha=.6*steam;line([[-50+i*50,-70],[-58+i*50+Math.sin(ph)*8,-110],[-46+i*50,-150],[-54+i*50+Math.sin(ph+1)*8,-180]],{lw:6,c:'#fff'});ctx.restore();}}
  blob(rectPts(-150,-46,300,52,14),'#b9b4ad',{lw:6});
  for(let r=0;r<2;r++)for(let c=0;c<4;c++){blob(rectPts(-138+c*70,-70+r*26,62,36,7),r?'#5b3420':'#6d3f27',{lw:4});}
  ctx.restore();}
function cityOut(sky){ctx.save();const g=ctx.createLinearGradient(0,0,0,1180);g.addColorStop(0,sky[0]);g.addColorStop(1,sky[1]);ctx.fillStyle=g;ctx.fillRect(-200,-200,W+400,1400);
  const bs=[[60,520,180],[250,420,150],[420,600,170],[620,460,190],[830,560,170]];for(const[bx,by,bw]of bs){blob(rectPts(bx-40,by,bw,1180-by,6),'#8c7d9e',{lw:5});
    for(let yy=by+40;yy<1120;yy+=70)for(let xx=bx-20;xx<bx-40+bw-30;xx+=50)blob(rectPts(xx,yy,26,34,4),'#ffd98a',{lw:3});}
  ctx.fillStyle='#b9a6a0';ctx.fillRect(-200,1180,W+400,800);line([[-200,1180],[W+200,1180]],{lw:6});ctx.restore();}
function bag(x,y){ctx.save();ctx.translate(x,y);blob(rectPts(-46,-70,92,70,10),'#7a5a43',{lw:5});ell(0,-74,26,18,'none',{lw:7});ctx.restore();}
function appUI(head){const g=ctx.createLinearGradient(0,-290,0,-10);g.addColorStop(0,'#fff5f8');g.addColorStop(1,'#ffe3ec');ctx.fillStyle=g;ctx.fillRect(-70,-290,140,280);
  heart(-42,-258,12,'#ff6b9d');ctx.font='bold 13px Poppins';ctx.fillStyle=INK;ctx.textAlign='left';ctx.textBaseline='alphabetic';ctx.fillText('CoupleIn',-26,-254);
  if(head){ctx.font='bold 11px Poppins';ctx.fillStyle='#ff6b9d';ctx.textAlign='center';ctx.fillText(head,0,-232);}}
function pill(y,txt,on,col){ctx.save();ctx.strokeStyle=col||'#ff6b9d';ctx.lineWidth=2.5;ctx.fillStyle=on?(col||'#ff6b9d'):'rgba(255,255,255,.7)';ctx.beginPath();ctx.roundRect(-58,y,116,30,15);ctx.fill();ctx.stroke();
  ctx.fillStyle=on?'#fff':INK;ctx.font=(on?'bold ':'')+'12px Poppins, "Noto Color Emoji"';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText(txt,0,y+16);ctx.restore();}
function appBadge(x,y,w,sub,label){ctx.save();blob(rectPts(x,y,w,66,14),'#232025',{stroke:false});ctx.fillStyle='#fff';ctx.textAlign='left';ctx.textBaseline='alphabetic';ctx.font='11px Poppins';ctx.fillText(sub,x+16,y+24);ctx.font='bold 20px Poppins';ctx.fillText(label,x+16,y+48);ctx.restore();}
'''


def chunks(text, emoji=None, maxc=15):
    words = text.replace('…', '...').split()
    out, cur = [], ''
    for w in words:
        cand = (cur + ' ' + w).strip()
        if cur and (len(cand) > maxc or len(cand.split()) > 3):
            out.append(cur); cur = w
        else:
            cur = cand
    if cur: out.append(cur)
    if emoji: out[-1] += ' ' + emoji
    return out


def D(who, text, body, emoji=None, cap=None):
    """A dialogue scene: one spoken line by `who`."""
    return {'who': who, 'text': text,
            'js': '{who:%s,cap:%s,draw(u){\n%s\n}}' % (json.dumps(who), json.dumps(cap or chunks(text, emoji), ensure_ascii=False), body)}


def ENDCARD(tagline, extra='', speaker='girl'):
    other = 'boy' if speaker == 'girl' else 'girl'
    return """  room('#fbdfe4','#f3b8c6',1180,'rgba(255,255,255,.18)');
  SP('girl',u,{x:250,y:G+10,s:1.1,flip:-1,eyes:'happy',mouth:'smile',blush:.4,tilt:-.05,wag:.3,talk:%s});
  SP('boy',u,{x:520,y:G+10,s:1.1,eyes:'happy',mouth:'smile',blush:.3,tilt:.05,wag:.3,talk:%s});
  %s
  const rise=pop(u,.3,.5);
  phoneMock(820,1060-rise*30,1.25+.08*rise,-.04,()=>{appUI('');
    heart(0,-212,34,'#ff6b9d');ctx.font='bold 20px Poppins';ctx.fillStyle=INK;ctx.textAlign='center';ctx.fillText('CoupleIn',0,-152);
    ctx.font='12px Poppins';ctx.fillText(%s,0,-130);pill(-106,'start free ✨',true);
    ctx.font='bold 10px Poppins';ctx.fillStyle='#8a7b80';ctx.fillText('App Store · Google Play',0,-50);});
  const k=pop(u,.6,.5);ctx.save();ctx.translate(540,470);ctx.scale(k,k);ctx.font='bold 46px Poppins, \"Noto Color Emoji\"';const tw=ctx.measureText('🔗 CoupleIn · link in bio').width+70;
  ctx.fillStyle='#ff6b9d';ctx.strokeStyle=INK;ctx.lineWidth=6;ctx.beginPath();ctx.roundRect(-tw/2,-44,tw,88,44);ctx.fill();ctx.stroke();
  ctx.fillStyle='#fff';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText('🔗 CoupleIn · link in bio',0,4);ctx.restore();
  if(u>1)floatHearts(400,860,1,u,4,160);""" % (1 if speaker == 'girl' else 0, 1 if speaker == 'boy' else 0, extra, json.dumps(tagline))


def tts(lines, outdir):
    from kokoro_onnx import Kokoro
    k = Kokoro(*J.KOKORO)
    durs = []
    for i, (who, text) in enumerate(lines):
        v = VOICES[who]
        a, sr = k.create(text, voice=v['voice'], speed=v['speed'], lang='en-us')
        raw = f'{outdir}/r{i}.wav'; sf.write(raw, a, sr)
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', raw, '-af', f"rubberband=pitch={v['pitch']}:formant=shifted:pitchq=quality",
                        '-ar', str(sr), '-ac', '1', f'{outdir}/p{i}.wav'], check=True)
        a, _ = sf.read(f'{outdir}/p{i}.wav')
        idx = np.where(np.abs(a) > 0.01)[0]
        a = a[max(0, idx[0] - 400):idx[-1] + 2400]
        sf.write(f'{outdir}/b{i}.wav', a, sr)
        durs.append(round(len(a) / sr, 2))
    return durs


def render(html_path, mp4):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1080, 'height': 1920}); errs = []
        pg.on('pageerror', lambda e: errs.append(str(e)))
        pg.goto('file://' + html_path)
        pg.evaluate("async()=>{await document.fonts.load('bold 80px Poppins');await document.fonts.load('70px \"Noto Color Emoji\"');}")
        total = pg.evaluate('TOTAL'); n = round(total * 30)
        f = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', '30', '-c:v', 'mjpeg', '-i', '-',
                              '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '24', '-preset', 'veryfast', '-movflags', '+faststart', mp4],
                             stdin=subprocess.PIPE)
        for i in range(n):
            u = pg.evaluate("t=>{render(t,true);return document.getElementById('c').toDataURL('image/jpeg',.92)}", i / 30)
            f.stdin.write(base64.b64decode(u.split(',', 1)[1]))
        f.stdin.close(); f.wait(); b.close()
        if errs: print('PAGE ERRORS', errs[:3])
        return total


def build_html(spec, durs, vo=None, lead=None):
    scenes = [s['js'] for s in spec.LINES]
    n = len(durs)
    lead = lead or [0] * n
    html = J.build_html(spec.SLUG, spec.TITLE, scenes, durs[:-1], spec.END['js'], durs[-1],
                        PRELUDE + 'const LEAD=%s;\n' % json.dumps(lead) + getattr(spec, 'PRELUDE', ''))
    if vo is not None:
        html = re.sub(r'const VO=\[[^\]]*\];', 'const VO=%s;' % json.dumps([round(v, 3) for v in vo]), html, count=1)
    for a, b in [("SC=0;", "SC=0;CURVO=VO[i];CURLEAD=LEAD[i];"),
                 ("const endT=.2+VO[si];let t=.2;", "const endT=.2+LEAD[si]+VO[si];let t=.2+LEAD[si];"),
                 ("t+=w/tot*(endT-.2)", "t+=w/tot*VO[si]"),
                 ("ctx.fillStyle='#fffaf0';ctx.fillText(tx,x0,0);", "ctx.fillStyle=CAPCOL;ctx.fillText(tx,x0,0);"),
                 ("if(withCap){title();", "if(withCap){title();CAPCOL=(%s)[s.who]||'#fffaf0';" % json.dumps(CAPCOLS)),
                 ("const c=PAL[o.kind];", "const c=o.pal||PAL[o.kind];"),
                 ("if(o.kind=='boy'&&o.bandana)blob([[-68,-160],[0,-150],[68,-160],[42,-126],[0,-100],[-42,-126]],'#6f95ba');",
                  "if((o.kind=='boy'||o.collar)&&o.bandana)blob([[-68,-160],[0,-150],[68,-160],[42,-126],[0,-100],[-42,-126]],o.bandCol||'#6f95ba');"),
                 ("blob([[0,0],[-44,-26],[-50,4],[-40,28]],'#ee8fa2');blob([[0,0],[44,-26],[50,4],[40,28]],'#ee8fa2');ell(0,0,14,13,'#f4a9b8');",
                  "blob([[0,0],[-44,-26],[-50,4],[-40,28]],o.bowCol||'#ee8fa2');blob([[0,0],[44,-26],[50,4],[40,28]],o.bowCol||'#ee8fa2');ell(0,0,14,13,o.bowCol2||'#f4a9b8');")]:
        assert html.count(a) >= 1, a
        html = html.replace(a, b, 1)
    return html


# --- sound effects -----------------------------------------------------------------
# spec.SFX = [(line_index, 'end'|'start', 'faaak'|'text'), ...]; -1 = END scene.
# 'end'  : sound plays right after that line's voice, scene gets FAAAK_TAIL extra seconds so nothing talks over it.
# 'start': sound plays at the top of the scene (text arrives), voice is delayed by START_LEAD.
FAAAK_TAIL = 1.45
START_LEAD = {'faaak': 1.75, 'text': 0.6, 'text+faaak': 2.0}
SFX_DIR = '/home/claude/jj/sfx'

def _sfx(name, sr):
    a, s2 = sf.read(f'{SFX_DIR}/{name}.wav')
    if a.ndim > 1: a = a.mean(1)
    if s2 != sr:
        x = np.linspace(0, len(a) - 1, int(len(a) * sr / s2)); a = np.interp(x, np.arange(len(a)), a)
    return a

def sfx_plan(spec, n):
    lead = [0.0] * n; tail = [0.0] * n; events = []   # (line, kind, name, offset_from_voice_or_scene)
    for idx, where, name in getattr(spec, 'SFX', []):
        i = idx % n
        if where == 'end':
            tail[i] += FAAAK_TAIL; events.append((i, 'end', name))
        else:
            lead[i] += START_LEAD[name]; events.append((i, 'start', name))
    return lead, tail, events

def mix_lines(durs, lead, wavs, out, sr=24000):
    buf = np.zeros(int(sum(durs) * sr) + 5 * sr); t = 0; starts = []
    for di, li, w in zip(durs, lead, wavs):
        a, _ = sf.read(w); st = int((t + 0.2 + li) * sr); starts.append(t + 0.2 + li)
        buf[st:st + len(a)] += a[:len(buf) - st]; t += di
    sf.write(out, buf[:int(sum(durs) * sr)], sr)
    return starts

def sfx_track(durs, starts, vo, events, total, out, sr=44100):
    buf = np.zeros(int((total + 1) * sr)); t0 = np.cumsum([0] + durs[:-1])
    fa = _sfx('faaaack_once', sr); k = int(1.0 * sr); m = int(1.45 * sr)
    fa = fa[:m].copy(); fa[k:] *= np.linspace(1, 0, m - k)
    tx = _sfx('text_ding', sr)
    def put(t, sig, g):
        i = int(t * sr); buf[i:i + len(sig)] += g * sig[:len(buf) - i]
    for i, kind, name in events:
        if kind == 'end':
            put(starts[i] + vo[i] + 0.08, fa, 1.0)
        else:
            if 'text' in name: put(t0[i] + 0.05, tx, 0.7)
            if 'faaak' in name: put(t0[i] + (0.45 if 'text' in name else 0.1), fa, 1.0)
    sf.write(out, np.clip(buf[:int(total * sr)], -1, 1), sr)


if __name__ == '__main__':
    slug = sys.argv[1]
    mode = sys.argv[2] if len(sys.argv) > 2 else 'full'
    spec = importlib.import_module(slug); spec.SLUG = slug
    W = f'{J.ROOT}/work/{slug}'; os.makedirs(W, exist_ok=True)
    OUT = f'{J.ROOT}/out'; os.makedirs(OUT, exist_ok=True)
    lines = [(s['who'], s['text']) for s in spec.LINES] + [(spec.END['who'], spec.END['text'])]
    key = hashlib.md5(json.dumps([lines, VOICES]).encode()).hexdigest()
    meta = f'{W}/meta.json'
    if os.path.exists(meta) and json.load(open(meta))['key'] == key:
        vo = json.load(open(meta))['durs']
    else:
        vo = tts(lines, W); json.dump({'key': key, 'durs': vo}, open(meta, 'w'))
    n = len(lines)
    lead, tail, events = sfx_plan(spec, n)
    durs = [round(d + PAD + lead[i] + tail[i], 2) for i, d in enumerate(vo)]
    durs[-1] = round(durs[-1] + 1.2 + getattr(spec, 'END_TAIL', 0), 2)          # let the end card breathe (+ outro)
    hp = f'{W}/v.html'; open(hp, 'w').write(build_html(spec, durs, vo, lead))
    print('lines', len(lines), 'est total', round(sum(durs), 1))
    if mode == 'preview':
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1080, 'height': 1920}); errs = []
            pg.on('pageerror', lambda e: errs.append(str(e))); pg.goto('file://' + hp)
            pg.evaluate("async()=>{await document.fonts.load('bold 80px Poppins');await document.fonts.load('70px \"Noto Color Emoji\"');}")
            t = 0
            for i, d in enumerate(durs):
                pg.evaluate("t=>render(t,true)", t + min(lead[i] + vo[i] * .5 + .2, d - .1)); pg.locator('#c').screenshot(path=f'{W}/pv_{i:02d}.png'); t += d
            pg.evaluate("t=>render(t,true)", sum(durs) - .3); pg.locator('#c').screenshot(path=f'{W}/pv_last.png')
            b.close(); print('errs', errs[:3])
        sys.exit()
    silent = f'{W}/silent.mp4'; t0 = time.time(); total = render(hp, silent)
    wavs = [f'{W}/b{i}.wav' for i in range(len(lines))]
    starts = mix_lines(durs, lead, wavs, f'{W}/vo_raw.wav')
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', f'{W}/vo_raw.wav', '-af',
                    'highpass=f=90,acompressor=threshold=-20dB:ratio=3:attack=5:release=120,aecho=0.8:0.4:30:0.08,loudnorm=I=-14:TP=-1.5:LRA=7',
                    '-ar', '44100', '-ac', '2', f'{W}/vo.wav'], check=True)
    music = J.ROOT + '/music/sound%d.wav' % getattr(spec, 'MUSIC_N', 1)
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', f'{W}/vo.wav', '-i', music, '-filter_complex',
                    f'[1:a]volume=0.4,aloop=loop=-1:size=2e9,atrim=0:{total:.2f},asetpts=PTS-STARTPTS,afade=t=in:d=1,afade=t=out:st={total-2:.2f}:d=2[m];[0:a][m]amix=inputs=2:duration=first:dropout_transition=0,loudnorm=I=-14:TP=-1.5:LRA=8[a]',
                    '-map', '[a]', '-ar', '44100', '-ac', '2', f'{W}/mix0.wav'], check=True)
    if events:
        sfx_track(durs, starts, vo, events, total, f'{W}/sfx.wav')
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', f'{W}/mix0.wav', '-i', f'{W}/sfx.wav', '-filter_complex',
                        '[1:a]aformat=channel_layouts=stereo,volume=1.6[s];[0:a][s]amix=inputs=2:duration=first:normalize=0,alimiter=limit=0.95[a]',
                        '-map', '[a]', '-ar', '44100', '-ac', '2', f'{W}/mix.wav'], check=True)
    else:
        os.replace(f'{W}/mix0.wav', f'{W}/mix.wav')
    final = f'{OUT}/{slug.replace("_", "-")}.mp4'
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', silent, '-i', f'{W}/mix.wav', '-map', '0:v', '-map', '1:a',
                    '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-shortest', '-movflags', '+faststart', final], check=True)
    qa = {'total_s': round(total, 1), 'render_s': round(time.time() - t0)}
    gaps = []; t = 0
    for di, w in zip(durs, wavs):
        a, sr = sf.read(w); gaps.append(round(t + di - (starts[len(gaps)] + len(a) / sr), 2)); t += di
    qa['min_gap'] = min(gaps); qa['overlap_ok'] = min(gaps) > 0; qa['duration_ok'] = 25 <= total <= 75
    st = json.loads(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'stream=codec_type,duration', '-of', 'json', final],
                                   capture_output=True, text=True).stdout)['streams']
    qa['streams'] = {s['codec_type']: float(s.get('duration', 0)) for s in st}
    qa['audio_ok'] = 'audio' in qa['streams'] and abs(qa['streams']['audio'] - qa['streams']['video']) < 1.5
    qa['size_mb'] = round(os.path.getsize(final) / 1e6, 1); qa['size_ok'] = qa['size_mb'] < 25
    json.dump(qa, open(f'{W}/qa.json', 'w')); print(json.dumps(qa))
