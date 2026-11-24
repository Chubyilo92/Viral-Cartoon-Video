import sys, json, subprocess, numpy as np, soundfile as sf
sys.path.insert(0, '/home/claude/viral-cartoon-video/testaquadrata/code/audio')
import sfxlib as S
SR = S.SR

def load_voice(path):
    pcm = subprocess.run(['ffmpeg', '-v', 'error', '-i', path, '-ac', '1', '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True).stdout
    return np.frombuffer(pcm, np.float32).copy()

def place(bus, x, t, gain_db):
    i = int(t * SR); x = x * S.db(gain_db); j = min(len(bus), i + len(x))
    if i < len(bus): bus[i:j] += x[:j - i]

def bed(d, seed=0):
    n = S.secs(d); t = S.tt(n)
    drone = np.sin(2 * np.pi * 55 * t) * .5 + np.sin(2 * np.pi * 82.4 * t) * .25
    drone *= .6 + .4 * np.sin(2 * np.pi * t / 9)
    return drone + S.filt(S.noise(n, seed), 60, 400) * .6

def riser(d=2.5):
    n = S.secs(d); t = S.tt(n); f = 200 + 1800 * (t / d) ** 2
    return (S.filt(S.noise(n, 7), 800, 9000) * (t / d) ** 2 * .7 + np.sin(2 * np.pi * np.cumsum(f) / SR) * (t / d) ** 2 * .3)

def sub_drop(d=2.0):
    n = S.secs(d); t = S.tt(n); f = 90 * np.exp(-t * 1.2) + 30
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 1.3)

def beep(f=2400, d=.12):
    n = S.secs(d); t = S.tt(n); return np.sin(2 * np.pi * f * t) * S.env(n, .005, .04) * .6

def whistle(d=1.2):
    n = S.secs(d); t = S.tt(n); f = 2900 + 120 * np.sin(2 * np.pi * 35 * t)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * S.env(n, .02, .2) * .5

def crowd(d, seed=4):
    n = S.secs(d); return S.filt(S.noise(n, seed), 250, 2500) * (.8 + .2 * np.sin(2 * np.pi * S.tt(n) / 3))

def mix(voice_path, cues, out, bed_db=-34, duck_db=12):
    v = load_voice(voice_path); dur = len(v) / SR + .2
    bus = np.zeros(int(dur * SR), np.float32)
    # speech envelope for ducking
    win = int(.05 * SR); e = np.convolve(np.abs(v), np.ones(win) / win, 'same')
    sp = (e > .01).astype(np.float32); sp = np.convolve(sp, np.ones(int(.3 * SR)) / int(.3 * SR), 'same')
    sp = np.pad(sp, (0, len(bus) - len(sp)))
    fx = np.zeros_like(bus)
    for c in cues:
        kind, t, g = c[0], c[1], c[2]
        if kind == 'bed':   place(fx, S.norm(bed(c[3] - t, int(t))), t, bed_db)
        elif kind == 'crowd': place(fx, S.norm(crowd(c[3] - t)), t, g)
        elif kind == 'heartbeat': place(fx, S.norm(S.heartbeat(c[3] - t)), t, g)
        elif kind == 'tick': place(fx, S.norm(S.clock_tick(c[3] - t)), t, g)
        elif kind == 'buzz': place(fx, S.norm(S.phone_buzz()), t, g)
        elif kind == 'beep': place(fx, S.norm(beep()), t, g)
        elif kind == 'riser': place(fx, S.norm(riser()), t, g)
        elif kind == 'drop': place(fx, S.norm(sub_drop()), t, g)
        elif kind == 'thud': place(fx, S.norm(S.thud()), t, g)
        elif kind == 'whistle': place(fx, S.norm(whistle()), t, g)
        elif kind == 'knock': place(fx, S.norm(S.door_knock()), t, g)
        elif kind == 'step': place(fx, S.norm(S.step_concrete()), t, g)
        elif kind == 'paper': place(fx, S.norm(S.paper()), t, g)
    duck = 1 - sp * (1 - S.db(-duck_db))
    bus += fx * duck
    bus[:len(v)] += v * 1.0
    bus = np.tanh(bus * 1.1) / 1.1
    sf.write(out + '.wav', bus, SR)
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', out + '.wav', '-af', 'loudnorm=I=-15:TP=-1.5', '-ar', '48000', out], check=True)
    return dur
