"""Vertical reel renderer (1080x1920, 30fps) for Testaquadrata remakes.
spec = {
  'audio': path, 'dur': seconds,
  'shots': [ {img, t0, t1, z:(z0,z1), c:((x0,y0),(x1,y1)), shake:[t..]} ],   # c = focus centre in 0..1 image coords
  'caps':  [ (t0, t1, text) ],                                               # burned captions
  'overlays': [ {type:'counter'|'card'|'notif'|'endcard', t0, t1, ...} ],
}
"""
import cv2, numpy as np, subprocess, math, os, json, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, FPS = 1080, 1920, 30
FONT = '/usr/share/fonts/truetype/google-fonts/ofl/montserrat/Montserrat[wght].ttf'
ANTON = '/usr/share/fonts/truetype/google-fonts/ofl/anton/' + [f for f in os.listdir('/usr/share/fonts/truetype/google-fonts/ofl/anton') if f.endswith('.ttf')][0]

def font(size, weight=800):
    f = ImageFont.truetype(FONT, size)
    try: f.set_variation_by_axes([weight])
    except Exception: pass
    return f

_cache = {}
def load(path):
    if path not in _cache:
        im = cv2.imread(path)
        h, w = im.shape[:2]
        s = max(W / w, H / h) * 1.0
        _cache[path] = cv2.resize(im, (int(w * s * 1.25), int(h * s * 1.25)), interpolation=cv2.INTER_CUBIC)  # oversample for zoom
    return _cache[path]

def ease(x): return 0.5 - 0.5 * math.cos(math.pi * min(max(x, 0), 1))

def shot_frame(sh, t):
    im = load(sh['img']); ih, iw = im.shape[:2]
    p = ease((t - sh['t0']) / max(sh['t1'] - sh['t0'], 1e-3))
    z0, z1 = sh.get('z', (1.0, 1.08)); z = z0 + (z1 - z0) * p
    (cx0, cy0), (cx1, cy1) = sh.get('c', ((.5, .5), (.5, .5)))
    cx = cx0 + (cx1 - cx0) * p; cy = cy0 + (cy1 - cy0) * p
    base = min(iw / W, ih / H)            # crop size at z=1 covers frame
    cw, chh = W * base / z, H * base / z
    x = np.clip(cx * iw - cw / 2, 0, iw - cw); y = np.clip(cy * ih - chh / 2, 0, ih - chh)
    sx = sy = 0
    for st in sh.get('shake', []):
        if 0 <= t - st < .45:
            a = (1 - (t - st) / .45) * 14
            sx, sy = a * math.sin(t * 90), a * math.cos(t * 70)
    M = np.float32([[W / cw, 0, -(x) * W / cw + sx], [0, H / chh, -(y) * H / chh + sy]])
    return cv2.warpAffine(im, M, (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)

def vignette():
    yy, xx = np.mgrid[0:H, 0:W]
    d = np.sqrt(((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2)
    return np.clip(1 - 0.38 * np.maximum(d - 0.55, 0) ** 1.6, 0, 1)[..., None].astype(np.float32)
VIG = vignette()

def draw_text_center(d, y, text, f, fill=(255, 255, 255), stroke=8, sc=(0, 0, 0), maxw=990):
    words, lines, cur = text.split(), [], ''
    for w_ in words:
        tst = (cur + ' ' + w_).strip()
        if d.textlength(tst, font=f) > maxw and cur: lines.append(cur); cur = w_
        else: cur = tst
    if cur: lines.append(cur)
    lh = f.size * 1.18
    for i, ln in enumerate(lines):
        tw = d.textlength(ln, font=f)
        d.text(((W - tw) / 2, y + i * lh), ln, font=f, fill=fill, stroke_width=stroke, stroke_fill=sc)
    return len(lines) * lh

def notif(img, t, ov):
    """realistic iOS-style frosted notification banner (Messages)"""
    a = min(1, (t - ov['t0']) / .25)
    bh = 270; y = int(120 - (1 - a) * 400)
    box = (36, y, W - 36, y + bh)
    if box[1] < 0: box = (36, 0, W - 36, max(1, y + bh))
    region = img.crop(box).filter(ImageFilter.GaussianBlur(30))
    region = Image.blend(region, Image.new('RGB', region.size, (245, 245, 248)), .62)
    mask = Image.new('L', region.size, 0); ImageDraw.Draw(mask).rounded_rectangle((0, 0, region.size[0] - 1, region.size[1] - 1), 52, fill=255)
    img.paste(region, box[:2], mask)
    d = ImageDraw.Draw(img); x0 = box[0] + 36; yy = y
    d.rounded_rectangle((x0, yy + 44, x0 + 104, yy + 148), 24, fill=(52, 199, 89))
    d.ellipse((x0 + 20, yy + 66, x0 + 84, yy + 116), fill=(255, 255, 255))
    d.polygon([(x0 + 30, yy + 106), (x0 + 24, yy + 128), (x0 + 46, yy + 112)], fill=(255, 255, 255))
    d.text((x0 + 134, yy + 42), ov.get('title', 'Numero sconosciuto'), font=font(44, 700), fill=(15, 15, 15))
    d.text((W - 36 - 120, yy + 48), 'ora', font=font(36, 500), fill=(120, 120, 125))
    f = font(44, 500); lines, cur = [], ''
    for w_ in ov['text'].split():
        tst = (cur + ' ' + w_).strip()
        if d.textlength(tst, font=f) > W - 36 - x0 - 170 and cur: lines.append(cur); cur = w_
        else: cur = tst
    lines.append(cur)
    for i, ln in enumerate(lines[:3]): d.text((x0 + 134, yy + 104 + i * 54), ln, font=f, fill=(30, 30, 30))

def render(spec, out):
    dur = spec['dur']; n = int(dur * FPS)
    tmp = out + '.video.mp4'
    p = subprocess.Popen(['ffmpeg', '-y', '-v', 'error', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                          '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '19', '-pix_fmt', 'yuv420p', tmp], stdin=subprocess.PIPE)
    rng = np.random.default_rng(3)
    grain = [rng.normal(0, 7, (H // 2, W // 2, 1)).astype(np.float32) for _ in range(6)]
    shots = spec['shots']
    for fi in range(n):
        t = fi / FPS
        cur = [s for s in shots if s['t0'] <= t < s['t1']] or [shots[-1]]
        fr = shot_frame(cur[-1], t).astype(np.float32)
        # crossfade from previous shot
        prev = [s for s in shots if s['t1'] <= t < s['t1'] + .35 and s is not cur[-1]]
        if prev and t - cur[-1]['t0'] < .35:
            a = (t - cur[-1]['t0']) / .35
            fr = fr * a + shot_frame(prev[-1], t).astype(np.float32) * (1 - a)
        for s in cur:
            for ft in s.get('flash', []):
                if 0 <= t - ft < .25: fr = fr + (1 - (t - ft) / .25) * 120
        g = cv2.resize(grain[fi % 6], (W, H))[..., None]
        fr = np.clip(fr * VIG + g, 0, 255).astype(np.uint8)
        img = Image.fromarray(cv2.cvtColor(fr, cv2.COLOR_BGR2RGB)); d = ImageDraw.Draw(img)
        for ov in spec.get('overlays', []):
            if not (ov['t0'] <= t < ov['t1']): continue
            k = ov['type']
            if k == 'counter':
                v = ov['to'] * ease((t - ov['t0']) / ov.get('count', .9))
                txt = ov.get('fmt', '{:,.0f} €').format(v).replace(',', '.')
                f = ImageFont.truetype(ANTON, ov.get('size', 120))
                tw = d.textlength(txt, font=f); y = ov.get('y', 260)
                d.rounded_rectangle(((W - tw) / 2 - 36, y - 10, (W + tw) / 2 + 36, y + f.size * 1.25), 22, fill=(0, 0, 0, 170))
                d.text(((W - tw) / 2, y), txt, font=f, fill=ov.get('color', (255, 214, 64)))
                if ov.get('label'): draw_text_center(d, y - 70, ov['label'], font(42, 800), stroke=6)
            elif k == 'card':
                f = ImageFont.truetype(ANTON, ov.get('size', 110))
                pop = min(1, (t - ov['t0']) / .18)
                draw_text_center(d, ov.get('y', 300), ov['text'], f, fill=ov.get('color', (255, 255, 255)), stroke=10)
            elif k == 'notif':
                notif(img, t, ov); d = ImageDraw.Draw(img)
            elif k == 'endcard':
                dim = Image.new('RGB', (W, H), (8, 8, 12)); img = Image.blend(img, dim, min(.82, (t - ov['t0']) / .5 * .82)); d = ImageDraw.Draw(img)
                draw_text_center(d, 420, 'COSA FARESTI?', ImageFont.truetype(ANTON, 110), stroke=0)
                y = 640
                for i, (lab, col) in enumerate(ov['options']):
                    if t - ov['t0'] > .5 + i * .35:
                        d.rounded_rectangle((150, y, W - 150, y + 150), 30, fill=col)
                        tw = d.textlength(lab, font=ImageFont.truetype(ANTON, 80))
                        d.text(((W - tw) / 2, y + 22), lab, font=ImageFont.truetype(ANTON, 80), fill=(255, 255, 255))
                    y += 190 if i == 0 else 0
                    if i == 0:
                        if t - ov['t0'] > .7: draw_text_center(d, y - 25, 'oppure', font(44, 600), stroke=0)
                        y += 50
                if t - ov['t0'] > 1.6:
                    draw_text_center(d, 1130, ov.get('line1', 'COMMENTA UNA PAROLA'), font(58, 900), fill=(255, 214, 64), stroke=0)
                    draw_text_center(d, 1250, ov.get('line2', 'LA PARTE 2 ESCE A 300 COMMENTI'), font(54, 800), stroke=0)
                    draw_text_center(d, 1350, ov.get('line3', 'MANDALO NEL GRUPPO'), font(54, 800), stroke=0)
        for c0, c1, txt in spec['caps']:
            if c0 <= t < c1:
                draw_text_center(d, 1330, txt, font(64, 900), fill=(255, 255, 255), stroke=9)
        p.stdin.write(cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR).tobytes())
    p.stdin.close(); p.wait()
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', tmp, '-i', spec['mix'], '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-shortest', out], check=True)
    os.remove(tmp)
