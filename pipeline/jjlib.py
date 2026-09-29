#!/usr/bin/env python3
"""JJ puppy video framework.
Assembles a video HTML (engine + scenes + timing tail), voices it with Kokoro,
renders frames with headless Chromium, mixes music, muxes, and QA-checks.
Two cuts per script: 'ig' (Love Language quiz ending) and 'tt' (follow-counter ending)."""
import json, os, re, subprocess, sys, shutil
import numpy as np
import soundfile as sf

ROOT = '/home/claude/jj'
REPO = '/home/claude/viral-cartoon-video'
SRC2 = REPO + '/videos/when-she-says-im-fine/anim2.html'
SRC1 = REPO + '/videos/when-a-boy-loves-you/anim.html'
KOKORO = ('/tmp/kk/kokoro.onnx', '/tmp/kk/voices.bin')
PAD = 0.75

_l2 = open(SRC2).read().split('\n')
HEAD = '\n'.join(_l2[0:203])
COMMON = '\n'.join(_l2[204:216])          # const G, phoneMock, dishPile, raincloudSmall
TAIL = '\n'.join(_l2[292:338])             # timing/captions/grain/render code
assert 'window.render=render' in TAIL and 'const G=1180' in COMMON


def split_scenes(path):
    """Return list of scene-object strings (without d:) from an existing anim html."""
    s = open(path).read()
    a = s.index('const SCENES=[')
    b = s.index('\n];', a) if '\n];' in s[a:] else s.index('}}];', a) + 3
    body = s[a + len('const SCENES=['):b]
    parts = re.split(r'(?m)^\{d:[\d.]+,', body)[1:]
    out = []
    for p in parts:
        p = p.rstrip().rstrip(',').rstrip()
        if p.endswith('];'):
            p = p[:-2]
        out.append('{' + p.rstrip(','))
    return out


def end_ig(caps, result_label='Quality Time', callback=None):
    """Instagram ending scene: pups + phone showing a Love Language result + bio prompt."""
    capjs = json.dumps(caps)
    return '''{cap:%s,draw(u){
  room('#3d4b6c','#303b57','rgba(255,255,255,.05)');
  const lg=ctx.createRadialGradient(540,760,20,540,760,560);lg.addColorStop(0,'rgba(255,200,120,.35)');lg.addColorStop(1,'rgba(255,200,120,0)');ctx.fillStyle=lg;ctx.fillRect(-100,-100,W+200,H+200);
  pup({kind:'girl',x:340,y:G+30,s:1.1,flip:-1,eyes:'happy',mouth:'smile',blush:.4,tilt:-.06,shadow:false,wag:.3});
  pup({kind:'boy',x:600,y:G+30,s:1.1,eyes:'happy',mouth:'smile',blush:.4,tilt:.06,shadow:false,wag:.3});
  const rise=pop(u,.5,.5);
  phoneMock(770,910-rise*40,.62+.05*rise,-.04,()=>{
    const g=ctx.createLinearGradient(0,-290,0,-10);g.addColorStop(0,'#fbdfe4');g.addColorStop(1,'#fff6e8');ctx.fillStyle=g;ctx.fillRect(-70,-290,140,280);
    heart(0,-190,44,'#ec7489');ctx.font='bold 19px Poppins';ctx.fillStyle=INK;ctx.textAlign='center';ctx.fillText(%s,0,-118);
    ctx.font='15px Poppins';ctx.fillText('is your love language',0,-96);
    ctx.strokeStyle='#e0a8b4';ctx.lineWidth=3;ctx.beginPath();ctx.roundRect(-46,-70,92,26,13);ctx.stroke();ctx.font='13px Poppins';ctx.fillText('your result ✨',0,-53);
  });
  if(u>1.2){ctx.save();ctx.globalAlpha=win(u,1.2,DUR_END_IG-.4);ctx.font='bold 34px Poppins';ctx.textAlign='center';ctx.fillStyle='#fff8e8';ctx.strokeStyle=INK;ctx.lineWidth=6;ctx.lineJoin='round';ctx.strokeText('🔗 60-sec test in bio',540,1620);ctx.fillText('🔗 60-sec test in bio',540,1620);ctx.restore();}
}}''' % (capjs, json.dumps(result_label))


def end_tt(count):
    caps = ["we're two little", "pups 🐾", "trying to find", "a thousand people", "who love like this 🤍",
            "if this made you", "think of someone 💭", "follow us 💌", "we'll keep making", "them for you 🤍"]
    return '''{cap:%s,draw(u){
  room('#3d4b6c','#303b57','rgba(255,255,255,.05)');
  const lg=ctx.createRadialGradient(540,760,20,540,760,560);lg.addColorStop(0,'rgba(255,200,120,.35)');lg.addColorStop(1,'rgba(255,200,120,0)');ctx.fillStyle=lg;ctx.fillRect(-100,-100,W+200,H+200);
  const wv=Math.sin(u*5);
  pup({kind:'girl',x:360,y:G+30,s:1.3,flip:-1,eyes:'happy',mouth:'smile',blush:.5,tilt:-.08,shadow:false,wag:.5});
  pup({kind:'boy',x:700,y:G+30,s:1.3,eyes:'happy',mouth:'smile',blush:.4,tilt:.08,shadow:false,wag:.5});
  const k=pop(u,.4,.5);
  ctx.save();ctx.translate(540,640);ctx.scale(k,k);
  blob(rectPts(-300,-70,600,140,50),'#fff9ee',{lw:6});
  ctx.fillStyle=INK;ctx.textAlign='center';ctx.textBaseline='middle';ctx.font='bold 54px Poppins';ctx.fillText('🐾 %d / 1,000',0,-14);
  blob(rectPts(-250,28,500,18,9),'#e8d9c3',{lw:3.5});
  const fw=Math.max(18,500*%d/1000);blob(rectPts(-250,28,fw,18,9),'#ec7489',{stroke:false});
  ctx.restore();
  floatHearts(540,860,.8,u,5,260);
}}''' % (json.dumps(caps), count, count)


def build_html(slug, title, scenes, dur, cut_end_js, end_dur, prelude=''):
    all_scenes = list(scenes) + [cut_end_js]
    scenes_js = 'const SCENES=[\n' + ',\n'.join(re.sub(r'^\{d:[\d.]+,', '{', s) for s in all_scenes) + '];\n'
    durs = list(dur) + [end_dur]
    tail = TAIL
    tail = re.sub(r'const VO=\[[^\]]*\];', 'const VO=%s;' % json.dumps([round(d - PAD, 3) for d in durs]), tail)
    tail = re.sub(r"const t=(\"[^\"]*\"|'[^']*');", lambda m: 'const t=' + json.dumps(title) + ';', tail, count=1)
    js = (HEAD + '\n' + COMMON + '\n' + prelude + '\n' + scenes_js +
          'const DUR_END_IG=%s;\n' % round(end_dur, 3) +
          'const DUR=%s;SCENES.forEach((s,i)=>s.d=DUR[i]);\n' % json.dumps([round(d, 3) for d in durs]) +
          tail + '\n</script></body></html>')
    return js


_k = None
def tts_lines(lines, outdir, prefix):
    global _k
    from kokoro_onnx import Kokoro
    if _k is None:
        _k = Kokoro(*KOKORO)
    os.makedirs(outdir, exist_ok=True)
    durs = []
    for i, t in enumerate(lines):
        a, sr = _k.create(t, voice='am_michael', speed=0.9, lang='en-us')
        idx = np.where(np.abs(a) > 0.01)[0]
        a = a[max(0, idx[0] - 400):idx[-1] + 2400]
        sf.write(f'{outdir}/{prefix}{i}.wav', a, sr)
        durs.append(round(len(a) / sr, 2))
    return durs, sr


def mix_voice(dur_list, wavs, out):
    sr = 24000
    total = sum(dur_list)
    buf = np.zeros(int(total * sr) + 5 * sr)
    t = 0
    for di, w in zip(dur_list, wavs):
        a, s2 = sf.read(w)
        assert s2 == sr
        st = int((t + 0.2) * sr)
        end = min(st + len(a), len(buf))
        buf[st:end] += a[:end - st]
        t += di
    sf.write(out, buf[:int(total * sr)], sr)
