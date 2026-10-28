"""Original, synthesized music beds for every JJ video (added 28 Oct 2026).

WHY: on 28 Oct the short-format video `short_fries` published MUTE. Its file had sound; the only audio
was one of the three phone-recorded clips in music/sound1-3.m4a, at full volume with no narrator. Those
clips are most likely commercial songs, which Instagram/Facebook/TikTok detect and mute. Every JJ video
must therefore use music generated here, note by note, which no platform can match to a song.

The old clips stay in the repo for reference only. make_video.py and make_short.py call ensure(n),
never music/sound*.wav.

    from original_music import ensure
    path = ensure(n)   # n in 1..3, returns a 90 s 44.1 kHz stereo wav, generated once and cached
"""
import os
import numpy as np
import soundfile as sf

SR = 44100
HERE = os.path.dirname(os.path.abspath(__file__))

# three different warm progressions so consecutive videos don't sound identical
PROGS = {
    1: [([0, 4, 7, 11], 2.4), ([-3, 0, 4, 7], 2.4), ([-4, -1, 5, 9], 2.4), ([-2, 2, 5, 9], 2.4)],   # Cmaj7 Am7 Fmaj7 G
    2: [([2, 5, 9, 12], 2.0), ([-1, 2, 7, 11], 2.0), ([0, 4, 7, 12], 2.0), ([-3, 0, 4, 9], 2.0)],    # Dm7 G C Am
    3: [([-5, -1, 2, 7], 2.8), ([-3, 0, 4, 7], 2.8), ([-7, -3, 0, 5], 2.8), ([-5, -1, 2, 9], 2.8)],  # G Am F G6
}
ARP = {1: [0, 4, 7, 12, 7, 4], 2: [0, 7, 12, 7], 3: [0, 4, 7, 4]}
STEP = {1: 0.4, 2: 0.3, 3: 0.35}


def _f(n):
    return 261.63 * (2 ** (n / 12))


def _tone(freq, dur, vol=1.0, harm=(1, 0.5, 0.25, 0.12)):
    t = np.linspace(0, dur, int(SR * dur), endpoint=False)
    w = sum(h * np.sin(2 * np.pi * freq * (i + 1) * t) for i, h in enumerate(harm))
    a, d = int(SR * 0.02), int(SR * 0.15)
    env = np.ones_like(t)
    env[:a] = np.linspace(0, 1, a)
    env[a:a + d] = np.linspace(1, 0.55, d)
    env[a + d:] = 0.55 * np.exp(-3.2 * np.linspace(0, 1, len(t) - a - d))
    return w * env * vol


def build(n, total=90.0, path=None):
    prog, arp, step = PROGS[n], ARP[n], STEP[n]
    tr = np.zeros(int(SR * total))
    t, i = 0.0, 0
    while t < total:
        notes, d = prog[i % len(prog)]
        c = sum(_tone(_f(x), d, vol=0.22 / len(notes) ** 0.5) for x in notes)
        s = int(SR * t); e = min(s + len(c), len(tr)); tr[s:e] += c[:e - s]
        t += d; i += 1
    t, i = 0.3, 0
    while t < total:
        notes, d = prog[int(t // prog[0][1]) % len(prog)]
        w = _tone(_f(notes[0] + 12 + arp[i % len(arp)] % 12), 0.4, vol=0.06, harm=(1, 0.3, 0.1))
        s = int(SR * t); e = min(s + len(w), len(tr)); tr[s:e] += w[:e - s]
        t += step; i += 1
    tr = np.tanh(tr * 1.3) / 1.3
    path = path or os.path.join(HERE, 'music', f'original{n}.wav')
    sf.write(path, np.stack([tr, tr], axis=1), SR)
    return path


def ensure(n):
    n = int(n) if n in (1, 2, 3, '1', '2', '3') else 1
    p = os.path.join(HERE, 'music', f'original{n}.wav')
    if not os.path.exists(p):
        build(n, path=p)
    return p


if __name__ == '__main__':
    for k in (1, 2, 3):
        print(ensure(k))
