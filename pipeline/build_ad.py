#!/usr/bin/env python3
"""Build a one-off ad video (custom end card, not the quiz/follow-counter
endings from make_video.py). Usage: python3 build_ad.py <slug>
Spec needs: TITLE, BODY_LINES, SCENES, END_LINE, END_SCENE_JS, optional
PRELUDE, optional MUSIC_N. Produces <slug>-instagram.mp4 and
<slug>-tiktok.mp4 in out/ (identical -- ads share one body/end card across
platforms; only the Metricool post copy differs per platform)."""
import importlib, json, os, subprocess, sys, time, hashlib
sys.path.insert(0, '/home/claude/jj')
import soundfile as sf
import jjlib as J

slug = sys.argv[1]
sys.path.insert(0, J.ROOT + '/specs')
spec = importlib.import_module(slug)
W = f'{J.ROOT}/work/{slug}'
os.makedirs(W, exist_ok=True)
OUT = f'{J.ROOT}/out'
os.makedirs(OUT, exist_ok=True)

lines = list(spec.BODY_LINES) + [spec.END_LINE]
key = hashlib.md5(json.dumps(lines).encode()).hexdigest()
meta = f'{W}/b_meta.json'
if os.path.exists(meta) and json.load(open(meta))['key'] == key:
    durs = json.load(open(meta))['durs']
else:
    durs, sr = J.tts_lines(lines, W, 'b')
    json.dump({'key': key, 'durs': durs}, open(meta, 'w'))

assert len(spec.SCENES) == len(spec.BODY_LINES), (len(spec.SCENES), len(spec.BODY_LINES))
body_dur = [round(d + J.PAD, 2) for d in durs[:-1]]
end_dur = round(durs[-1] + J.PAD + 0.7, 2)

html = J.build_html(slug, spec.TITLE, spec.SCENES, body_dur, spec.END_SCENE_JS, end_dur, getattr(spec, 'PRELUDE', ''))
hp = f'{W}/ad.html'
open(hp, 'w').write(html)


def render(html_path, mp4):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={'width': 1080, 'height': 1920})
        errs = []
        pg.on('pageerror', lambda e: errs.append(str(e)))
        pg.goto('file://' + html_path)
        pg.evaluate("async()=>{await document.fonts.load('bold 80px Poppins');await document.fonts.load('70px \"Noto Color Emoji\"');}")
        total = pg.evaluate('TOTAL')
        n = round(total * 30)
        f = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', '30', '-c:v', 'mjpeg',
                              '-i', '-', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '24', '-preset', 'veryfast',
                              '-movflags', '+faststart', mp4], stdin=subprocess.PIPE)
        import base64
        for i in range(n):
            u = pg.evaluate("t=>{render(t,true);return document.getElementById('c').toDataURL('image/jpeg',.92)}", i / 30)
            f.stdin.write(base64.b64decode(u.split(',', 1)[1]))
        f.stdin.close(); f.wait(); b.close()
        if errs:
            print('PAGE ERRORS', errs[:3])
        return total


MUSIC = J.ROOT + '/music/sound%d.wav' % getattr(spec, 'MUSIC_N', 2)

silent = f'{W}/ad_silent.mp4'
t0 = time.time()
total = render(hp, silent)

all_durs = body_dur + [end_dur]
wavs = [f'{W}/b{i}.wav' for i in range(len(body_dur))] + [f'{W}/b{len(body_dur)}.wav']
J.mix_voice(all_durs, wavs, f'{W}/ad_vo_raw.wav')
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', f'{W}/ad_vo_raw.wav', '-af',
                'highpass=f=70,acompressor=threshold=-20dB:ratio=3:attack=5:release=120,aecho=0.8:0.5:40:0.12,loudnorm=I=-14:TP=-1.5:LRA=7',
                '-ar', '44100', '-ac', '2', f'{W}/ad_vo.wav'], check=True)
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', f'{W}/ad_vo.wav', '-i', MUSIC,
                '-filter_complex', f'[1:a]volume=0.5,aloop=loop=-1:size=2e9,atrim=0:{total:.2f},asetpts=PTS-STARTPTS,afade=t=in:d=1,afade=t=out:st={total-2:.2f}:d=2[m];[0:a][m]amix=inputs=2:duration=first:dropout_transition=0,loudnorm=I=-14:TP=-1.5:LRA=8[a]',
                '-map', '[a]', '-ar', '44100', '-ac', '2', f'{W}/ad_mix.wav'], check=True)
canonical = f'{OUT}/{slug.replace("_","-")}.mp4'
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', silent, '-i', f'{W}/ad_mix.wav', '-map', '0:v', '-map', '1:a',
                '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-shortest', '-movflags', '+faststart', canonical], check=True)

# QA
qa = {'total_s': round(total, 1), 'render_s': round(time.time() - t0)}
gaps = []
t = 0
for di, w in zip(all_durs, wavs):
    a, sr = sf.read(w)
    gaps.append(round(t + di - (t + 0.2 + len(a) / sr), 2)); t += di
qa['min_gap'] = min(gaps)
qa['overlap_ok'] = min(gaps) > 0
qa['duration_ok'] = 35 <= total <= 75
pr = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'stream=codec_type,duration', '-of', 'json', canonical],
                    capture_output=True, text=True)
st = json.loads(pr.stdout)['streams']
qa['streams'] = {s['codec_type']: float(s.get('duration', 0)) for s in st}
qa['audio_ok'] = 'audio' in qa['streams'] and abs(qa['streams']['audio'] - qa['streams']['video']) < 1.5
qa['size_mb'] = round(os.path.getsize(canonical) / 1e6, 1)
qa['size_ok'] = qa['size_mb'] < 25
json.dump(qa, open(f'{W}/ad_qa.json', 'w'))

# two platform copies (same creative for both -- ad CTA doesn't differ)
for name in ('instagram', 'tiktok'):
    dest = f'{OUT}/{slug.replace("_","-")}-{name}.mp4'
    subprocess.run(['cp', canonical, dest])

# sample frames
pts = [1.5, sum(all_durs[:2]) + 1.5, sum(all_durs[:len(all_durs) // 2]) + 1.5, sum(all_durs[:-2]) + 1.5, sum(all_durs[:-1]) + 1.2, total - 1.0]
for k, ts in enumerate(pts):
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-ss', f'{ts:.2f}', '-i', canonical, '-frames:v', '1', '-vf', 'scale=360:-1',
                    f'{W}/ad_f{k}.png'])

print(json.dumps(qa))
