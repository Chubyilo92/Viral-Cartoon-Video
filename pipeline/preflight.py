#!/usr/bin/env python3
"""PREFLIGHT GATE — must exit 0 before any JJ video is scheduled (added 28 Oct 2026).

Earlier QA only checked that an audio *stream* existed, so a video whose music the platforms muted
still "passed"; banned hashtags (#fyp) reached captions because nothing checked them; and nothing
proved the scheduled URL was the exact file that passed QA. This script checks all of that and exits
non-zero on any failure. Do not schedule on a non-zero exit. Do not edit thresholds to make a video pass.

Usage (one call per post):
  python3 preflight.py --file out/x-instagram.mp4 --platform instagram --format long \
      --caption-file work/x/caption_ig.txt [--url https://raw.githubusercontent.com/.../x-instagram.mp4]
  --platform: instagram | tiktok   (instagram covers the IG+FB post)
  --format:   long (narrated, 35-75 s) | short (music only, 15-25 s)
  --url:      after pushing, pass the commit-pinned raw URL; the script downloads it and checks the
              sha256 matches the local file that passed. Run this second pass right before scheduling.
Prints one JSON line with every check. Exit 0 = all passed.
"""
import argparse, hashlib, json, os, re, subprocess, sys, tempfile, urllib.request

BANNED_TAGS = {'#fyp', '#foryou', '#foryoupage', '#viral', '#trending', '#fypシ', '#xyzbca', '#explore'}
DUR = {'long': (35, 75), 'short': (15, 25)}


def sh(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)


def sha(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--file', required=True)
    ap.add_argument('--platform', required=True, choices=['instagram', 'tiktok'])
    ap.add_argument('--format', required=True, choices=['long', 'short'])
    ap.add_argument('--caption-file', required=True)
    ap.add_argument('--url')
    a = ap.parse_args()
    r, fails = {'file': a.file}, []

    # streams + duration
    pr = json.loads(sh(['ffprobe', '-v', 'error', '-show_entries', 'stream=codec_type,duration:format=duration',
                        '-of', 'json', a.file]).stdout or '{}')
    st = {s['codec_type']: float(s.get('duration') or 0) for s in pr.get('streams', [])}
    dur = float(pr.get('format', {}).get('duration') or 0)
    r['duration'] = round(dur, 1)
    if 'video' not in st: fails.append('no video stream')
    if 'audio' not in st: fails.append('no audio stream')
    lo, hi = DUR[a.format]
    if not lo <= dur <= hi: fails.append(f'duration {dur:.1f}s outside {lo}-{hi}s for {a.format}')
    if 'audio' in st and abs(st['audio'] - st.get('video', 0)) > 1.0: fails.append('audio shorter/longer than video by >1s')

    # loudness: catches silent or near-silent tracks
    vd = sh(['ffmpeg', '-nostats', '-i', a.file, '-af', 'volumedetect', '-vn', '-f', 'null', '-']).stderr
    m = re.search(r'mean_volume: (-?[\d.]+) dB', vd); mx = re.search(r'max_volume: (-?[\d.]+) dB', vd)
    mean = float(m.group(1)) if m else -99.0
    r['mean_db'] = mean; r['max_db'] = float(mx.group(1)) if mx else None
    if mean < -30: fails.append(f'audio too quiet / silent (mean {mean} dB, need >= -30)')
    if mean > -8: fails.append(f'audio too loud (mean {mean} dB)')

    # silent stretches: music should never drop out for >1.5 s
    sd = sh(['ffmpeg', '-nostats', '-i', a.file, '-af', 'silencedetect=noise=-45dB:d=1.5', '-vn', '-f', 'null', '-']).stderr
    gaps = len(re.findall(r'silence_start', sd))
    r['silent_gaps'] = gaps
    if gaps: fails.append(f'{gaps} silent stretch(es) > 1.5 s')

    # music source: refuse the phone clips (copyright-muting risk)
    side = os.path.splitext(a.file)[0] + '.music.json'
    if os.path.exists(side):
        src = json.load(open(side)).get('source', '')
        r['music_source'] = src
        if 'sound' in os.path.basename(src) and 'original' not in src:
            fails.append(f'music is a user-supplied clip ({src}); must be original_music.py')

    # size
    mb = os.path.getsize(a.file) / 1e6
    r['size_mb'] = round(mb, 1)
    if mb > 25: fails.append(f'file {mb:.1f} MB > 25 MB')

    # caption
    cap = open(a.caption_file, encoding='utf-8').read().strip()
    tags = re.findall(r'#\w+', cap.lower())
    r['hashtags'] = tags
    bad = sorted(set(tags) & BANNED_TAGS)
    if bad: fails.append(f'banned hashtags {bad}')
    if len(tags) > 5: fails.append(f'{len(tags)} hashtags (max 5)')
    if len(set(tags)) != len(tags): fails.append('duplicate hashtag')
    if not cap: fails.append('empty caption')
    if a.platform == 'tiktok' and re.search(r'https?://|link in bio|\bbio\b', cap.lower()):
        fails.append('TikTok caption contains a link / bio mention')
    if a.platform == 'instagram' and a.format == 'long' and 'bio' not in cap.lower():
        fails.append('IG long-format caption must mention the 60-sec test in bio')

    # file identity
    r['sha256'] = sha(a.file)
    if a.url:
        if 'raw.githubusercontent.com' in a.url and not re.search(r'/[0-9a-f]{40}/', a.url):
            fails.append('URL is not commit-pinned (needs the 40-char commit sha, not a branch name)')
        try:
            with tempfile.NamedTemporaryFile(suffix='.mp4') as t:
                urllib.request.urlretrieve(a.url, t.name)
                rs = sha(t.name)
            r['url_sha256'] = rs
            if rs != r['sha256']: fails.append('file at URL is NOT the file that passed QA (sha256 mismatch)')
        except Exception as e:
            fails.append(f'could not download URL: {e}')

    r['fails'] = fails
    r['pass'] = not fails
    print(json.dumps(r, ensure_ascii=False))
    sys.exit(0 if not fails else 1)


if __name__ == '__main__':
    main()
