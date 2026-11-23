"""Testaquadrata sound library — synthesized foley, ambiences, reverb and score elements (48 kHz mono)."""
import numpy as np
from scipy.signal import butter, sosfilt, fftconvolve
SR = 48000
_rng = np.random.default_rng(11)
def rng(seed=None): return np.random.default_rng(seed) if seed is not None else _rng
def secs(d): return int(d * SR)
def tt(n): return np.arange(n) / SR
def noise(n, seed=None): return rng(seed).standard_normal(n)
def filt(x, lo, hi, o=2):
    if lo <= 0: sos = butter(o, hi, 'low', fs=SR, output='sos')
    elif hi >= SR / 2: sos = butter(o, lo, 'high', fs=SR, output='sos')
    else: sos = butter(o, [lo, hi], 'band', fs=SR, output='sos')
    return sosfilt(sos, x)
def env(n, a=.01, r=.05):
    e = np.ones(n); na = min(n // 2, max(1, secs(a))); nr = min(n // 2, max(1, secs(r)))
    e[:na] = np.linspace(0, 1, na); e[-nr:] = np.linspace(1, 0, nr); return e
def db(d): return 10 ** (d / 20)
def norm(x, peak=1.0): m = np.max(np.abs(x)) + 1e-9; return x / m * peak

# ---------- reverb (synthetic impulse responses) ----------
def ir(rt60=1.2, pre=.01, bright=6000, seed=1, early=6):
    n = secs(rt60 * 1.3); t = tt(n); r = rng(seed)
    tail = r.standard_normal(n) * np.exp(-6.9 * t / rt60)
    tail = filt(tail, 120, bright)
    h = np.zeros(n); h[0] = 1.0
    for i in range(early): h[secs(pre + r.uniform(.003, .04))] += r.uniform(.2, .5) * (1 if r.random() > .5 else -1)
    h[secs(pre):] += tail[:n - secs(pre)] * .35
    return h
ROOMS = {'flat': ir(.45, .006, 5000, 1), 'bath': ir(.9, .004, 9000, 2, 10), 'corridor': ir(1.4, .012, 5000, 3), 'stairs': ir(2.8, .02, 4000, 4, 8), 'street': ir(1.8, .05, 3500, 5), 'out': ir(.6, .03, 4000, 6)}
def verb(x, room, wet=.3):
    y = fftconvolve(x, ROOMS[room])[:len(x) + len(ROOMS[room]) - 1]
    out = np.zeros(len(y)); out[:len(x)] += x * (1 - wet * .5); out += y * wet
    return out

# ---------- foley ----------
def tap_squeak(d=.35, seed=1):
    n = secs(d); t = tt(n); f = 1500 + 700 * np.sin(2 * np.pi * 7 * t) + 400 * t / d
    x = np.sin(2 * np.pi * np.cumsum(f) / SR) * (.5 + .5 * np.sign(np.sin(2 * np.pi * 28 * t)))
    return filt(x, 800, 5000) * env(n, .02, .08) * .6
def water_run(d, seed=2, body=1.0):
    n = secs(d); r = rng(seed); x = r.standard_normal(n)
    am = filt(r.standard_normal(n), 0, 30); am = 1 + 1.5 * am / (np.std(am) + 1e-9)
    hiss = filt(x, 1500, 9000) * .5 * am
    gurg = np.zeros(n)
    for i in r.integers(0, max(1, n - 3000), size=int(d * 45)):  # bubbles
        L = int(r.uniform(400, 1500)); f0 = r.uniform(300, 1200); tb = tt(L)
        gurg[i:i + L] += np.sin(2 * np.pi * f0 * (1 + 2 * tb) * tb) * np.exp(-tb * 60) * r.uniform(.2, .8)
    return (hiss + filt(x, 200, 900) * .6 * body + gurg * .5) * env(n, .08, .25)
def tub_fill(d, seed=3):
    """running water into a filling tub: resonant band rises as level rises."""
    n = secs(d); x = water_run(d, seed, 1.3); t = tt(n); out = np.zeros(n); blk = 2400
    for i in range(0, n, blk):
        c = 280 + 520 * (i / n); seg = x[i:i + blk]
        out[i:i + blk] = filt(np.pad(seg, (0, blk - len(seg)))[:len(seg)], c * .7, c * 1.6) * 1.4 + seg * .5
    return out
def drip(g=1.0, f=None, seed=None):
    r = rng(seed); n = secs(.14); t = tt(n); f = f or r.uniform(1100, 1800)
    fr = f + f * 1.6 * np.exp(-t * 70)
    return np.sin(2 * np.pi * np.cumsum(fr) / SR) * np.exp(-t * 38) * g
def step_wood(g=1.0, seed=None):
    r = rng(seed); n = secs(.22); t = tt(n)
    thump = np.sin(2 * np.pi * r.uniform(70, 95) * t) * np.exp(-t * 35)
    click = filt(r.standard_normal(n), 1500, 6000) * np.exp(-t * 160) * .4
    creak = filt(r.standard_normal(n), 300, 900) * np.exp(-t * 25) * .25
    return (thump + click + creak) * g
def step_concrete(g=1.0, scuff=False, seed=None):
    r = rng(seed); n = secs(.45 if scuff else .2); t = tt(n)
    x = np.sin(2 * np.pi * 60 * t) * np.exp(-t * 45) * .6 + filt(r.standard_normal(n), 400, 5000) * np.exp(-t * (7 if scuff else 60)) * (.7 if scuff else .5)
    return x * g
def door_knock(g=1.0, hard=1.0, seed=None):
    """modal wooden door: damped partials + knuckle click."""
    r = rng(seed); n = secs(.4); t = tt(n); x = np.zeros(n)
    for f, a, d in [(92, 1, 18), (171, .7, 22), (263, .5, 28), (412, .35, 35), (655, .2, 45), (1040, .12, 60)]:
        x += a * np.sin(2 * np.pi * f * r.uniform(.97, 1.03) * t) * np.exp(-t * d)
    x += filt(r.standard_normal(n), 1500, 7000) * np.exp(-t * 300) * .5 * hard
    return x * g
def wall_knock(g=1.0, seed=None):  # dull knock heard through tiles/pipes
    r = rng(seed); n = secs(.6); t = tt(n); x = np.zeros(n)
    for f, a, d in [(60, 1, 12), (118, .6, 16), (240, .4, 22), (1500, .15, 40)]: x += a * np.sin(2 * np.pi * f * t) * np.exp(-t * d)
    x += filt(r.standard_normal(n), 100, 1200) * np.exp(-t * 60) * .5
    return x * g
def handle_rattle(d=.6, seed=None):
    r = rng(seed); n = secs(d); x = np.zeros(n)
    for i in np.sort(r.integers(0, n - 800, size=int(d * 25))):
        L = 600; tb = tt(L); x[i:i + L] += np.sin(2 * np.pi * r.uniform(2500, 4200) * tb) * np.exp(-tb * 200) * r.uniform(.3, 1)
    return filt(x, 1500, 9000)
def phone_buzz(d=1.6):
    n = secs(d); t = tt(n); gate = ((t % .9) < .45).astype(float)
    m = np.sin(2 * np.pi * 172 * t) + .5 * np.sign(np.sin(2 * np.pi * 172 * t))
    rattle = filt(noise(n) * (np.sin(2 * np.pi * 172 * t) > .6), 1500, 6000) * .3
    return filt(m + rattle, 90, 4000) * filt(gate, 0, 60) * .5
def it_alert(d=4.0):
    n = secs(d); t = tt(n); gate = filt(((t % .5) < .38).astype(float), 0, 200)
    x = (np.sign(np.sin(2 * np.pi * 853 * t)) + np.sign(np.sin(2 * np.pi * 960 * t))) * .5
    return filt(x * gate, 300, 4500) * env(n, .005, .2) * .7
def mug_clink(seed=None):
    r = rng(seed); n = secs(.5); t = tt(n); x = np.zeros(n)
    for f, a in [(2150, 1), (3340, .6), (5120, .35), (6900, .2)]: x += a * np.sin(2 * np.pi * f * t) * np.exp(-t * r.uniform(9, 14))
    return x * .3
def can_clink(seed=None):
    r = rng(seed); n = secs(.18); t = tt(n); x = np.zeros(n)
    for f in [1900, 2700, 4100]: x += np.sin(2 * np.pi * f * r.uniform(.95, 1.05) * t) * np.exp(-t * 45)
    return x * .3
def pencil(d=.8, seed=None):
    r = rng(seed); n = secs(d); t = tt(n); stroke = (np.sin(2 * np.pi * 6 * t) > -.2).astype(float)
    return filt(r.standard_normal(n), 2500, 9000) * filt(stroke, 0, 40) * .35
def paper(seed=None): n = secs(.35); return filt(noise(n, seed), 800, 8000) * env(n, .01, .2) * .4
def scrape(d=1.2, f=13, seed=None):
    r = rng(seed); n = secs(d); t = tt(n)
    return filt(r.standard_normal(n), 70, 900) * (1 + .7 * np.sin(2 * np.pi * f * t + r.uniform(0, 6))) * env(n, .05, .2)
def thud(g=1.0): n = secs(.5); t = tt(n); return (np.sin(2 * np.pi * 55 * t) * np.exp(-t * 14) + filt(noise(n), 0, 300) * np.exp(-t * 25) * .5) * g
def towel_slap(seed=None):
    r = rng(seed); n = secs(.2); t = tt(n); return (filt(r.standard_normal(n), 300, 4000) * np.exp(-t * 35) + np.sin(2 * np.pi * 120 * t) * np.exp(-t * 40) * .4) * .8
def hiss(d): n = secs(d); return filt(noise(n), 3500, 12000) * env(n, .4, 1.0) * .4
def breath(d=2.4, n_breaths=1, seed=None, g=1.0):
    r = rng(seed); n = secs(d); x = np.zeros(n); per = n // n_breaths
    for b in range(n_breaths):
        L = per; t = tt(L); inh = np.sin(np.pi * np.clip(t / (L / SR * .4), 0, 1)) * (t < L / SR * .4)
        exh = np.sin(np.pi * np.clip((t - L / SR * .45) / (L / SR * .5), 0, 1)) * (t >= L / SR * .45)
        x[b * per:b * per + L] += filt(r.standard_normal(L), 400, 2500) * inh * .6 + filt(r.standard_normal(L), 200, 1600) * exh * .8
    return x * g
def heartbeat(d, bpm=64, g=1.0):
    n = secs(d); x = np.zeros(n); per = 60 / bpm; k = 0
    while k * per < d:
        for off, a in ((0, 1), (.21, .65)):
            L = secs(.16); t = tt(L); i = secs(k * per + off)
            if i + L < n: x[i:i + L] += np.sin(2 * np.pi * 46 * t) * np.exp(-t * 24) * a
        k += 1
    return x * g
def clock_tick(d, g=1.0):
    n = secs(d); x = np.zeros(n)
    for k in range(int(d)):
        L = secs(.04); t = tt(L); i = secs(k + (.5 if k % 2 else 0) * 0); x[i:i + L] += filt(noise(L), 2500, 8000) * np.exp(-t * 180) * (1 if k % 2 else .7)
    return x * g
def groan(d=1.8, f0=68, g=1.0, seed=0):
    r = rng(seed); n = secs(d); t = tt(n)
    f = f0 * (1 + .08 * np.sin(2 * np.pi * .7 * t + r.uniform(0, 6))) * (1 + .15 * np.sin(np.pi * t / d))
    ph = np.cumsum(f) / SR; saw = 2 * (ph % 1) - 1
    jit = filt(r.standard_normal(n), 0, 40); jit /= np.std(jit) + 1e-9
    rasp = filt(r.standard_normal(n), 300, 3000) * (.5 + .5 * np.sign(np.sin(2 * np.pi * ph))) * (1 + .3 * jit)
    x = saw * .7 + rasp * .6
    x = filt(x, 420, 760) * 1.3 + filt(x, 950, 1350) * .8 + filt(x, 70, 260) * .7 + filt(x, 2300, 3200) * .25
    e = np.sin(np.pi * np.clip(t / d, 0, 1)) ** 1.4 * (1 + .35 * np.sin(2 * np.pi * 2.7 * t))
    return x * e * g
def far_scream(d=1.0, seed=0):
    r = rng(seed); n = secs(d); t = tt(n); f = 650 + 320 * np.sin(np.pi * t / d) + 35 * np.sin(2 * np.pi * 6.5 * t)
    ph = np.cumsum(f) / SR; x = np.sin(2 * np.pi * ph) + .55 * np.sin(4 * np.pi * ph) + .3 * np.sin(6 * np.pi * ph) + .4 * r.standard_normal(n)
    return filt(x, 450, 2800) * np.sin(np.pi * t / d) ** 2
def siren(d, lo=700, hi=1250, period=3.2, seed=0):
    n = secs(d); t = tt(n); f = (lo + hi) / 2 + (hi - lo) / 2 * np.sin(2 * np.pi * t / period)
    return filt(np.sin(2 * np.pi * np.cumsum(f) / SR) + .3 * np.sin(4 * np.pi * np.cumsum(f) / SR), 400, 2500)
def car_alarm(d):
    n = secs(d); t = tt(n); f = np.where((t % .6) < .3, 1050, 790)
    return filt(np.sign(np.sin(2 * np.pi * np.cumsum(f) / SR)), 500, 3500) * .5
def helicopter(d, seed=0):
    n = secs(d); t = tt(n); blades = (np.sin(2 * np.pi * 11 * t) > .7).astype(float)
    x = filt(noise(n, seed), 60, 600) * (.4 + filt(blades, 0, 120) * 1.4) + np.sin(2 * np.pi * 38 * t) * .3
    return x * np.sin(np.pi * t / d) ** 2
def dog_bark(seed=0):
    r = rng(seed); n = secs(.28); t = tt(n); f = 520 * np.exp(-t * 3) + 300
    ph = np.cumsum(f) / SR; x = np.sign(np.sin(2 * np.pi * ph)) * .5 + r.standard_normal(n) * .4
    return filt(filt(x, 350, 2200), 300, 3000) * np.exp(-t * 9) * np.minimum(1, t * 80)
def room_tone(d, lo=40, hi=300, hum=50, seed=0):
    n = secs(d); t = tt(n); return (filt(noise(n, seed), lo, hi) * .6 + (np.sin(2 * np.pi * hum * t) + .3 * np.sin(4 * np.pi * hum * t)) * .05) * env(n, .5, .5)
def fridge(d): n = secs(d); t = tt(n); return (np.sin(2 * np.pi * 100 * t) * .4 + np.sin(2 * np.pi * 150 * t) * .2 + filt(noise(n), 80, 400) * .3) * env(n, .4, .4)
def city(d, seed=0):
    n = secs(d); t = tt(n); x = filt(noise(n, seed), 30, 260) * (1 + .3 * np.sin(2 * np.pi * t / 7))
    return x * env(n, 1, 1)
def wind(d, seed=0, bright=1500):
    n = secs(d); t = tt(n); r = rng(seed); g = filt(r.standard_normal(n), 0, 1.5); g = 1 + 1.4 * g / (np.std(g) + 1e-9)
    return filt(r.standard_normal(n), 150, bright) * np.clip(g, .1, 3) * env(n, 1, 1) * .5
def rain(d, seed=0, on_glass=True):
    n = secs(d); r = rng(seed); x = filt(r.standard_normal(n), 900, 11000) * .5
    if on_glass:
        for i in r.integers(0, n - 2000, size=int(d * 120)): L = 300; tb = tt(L); x[i:i + L] += np.sin(2 * np.pi * r.uniform(2500, 6000) * tb) * np.exp(-tb * 300) * r.uniform(.1, .5)
    return x * env(n, .6, .8)
def fire(d, seed=0, size=1.0):
    n = secs(d); r = rng(seed); rum = filt(r.standard_normal(n), 25, 180) * .9 * size; cr = np.zeros(n)
    for i in r.integers(0, n - 400, size=int(d * 30 * size)): L = int(r.uniform(80, 400)); cr[i:i + L] += r.standard_normal(L) * np.exp(-np.arange(L) / (L / 4)) * r.uniform(.3, 1)
    whoosh = filt(r.standard_normal(n), 200, 1500) * .3 * size
    return (rum + filt(cr, 900, 7000) * .8 + whoosh) * env(n, .5, .5)
def power_down(d=1.6):
    n = secs(d); t = tt(n); f = 240 * np.exp(-t * 2.4) + 25; ph = np.cumsum(f) / SR
    return (np.sin(2 * np.pi * ph) + .4 * np.sign(np.sin(2 * np.pi * ph))) * np.exp(-t * 1.6) * .6
def elec_hum(d, flicker=False, seed=0):
    n = secs(d); t = tt(n); x = np.sin(2 * np.pi * 100 * t) + .5 * np.sin(2 * np.pi * 200 * t) + .25 * np.sin(2 * np.pi * 300 * t)
    if flicker: x *= 1 + 1.5 * (filt(noise(n, seed), 0, 12) > 1.2)
    return filt(x, 80, 2000) * .3 * env(n, .3, .3)
def binocular_focus(): n = secs(.5); x = np.zeros(n); [x.__setitem__(slice(secs(o), secs(o) + 600), x[secs(o):secs(o) + 600] + filt(noise(600), 2500, 9000) * np.exp(-tt(600) * 250)) for o in (.05, .16, .28, .38)]; return x
def whoosh(d=.7, rev=False):
    n = secs(d); t = tt(n); x = noise(n); out = np.zeros(n)
    for i, (lo, hi) in enumerate([(200, 800), (800, 2500), (2500, 7000)]): out += filt(x, lo, hi) * np.sin(np.pi * np.clip(t / d * 1.1 - i * .05, 0, 1)) ** 2
    return out[::-1] if rev else out
# ---------- score ----------
def boom(g=1.0):
    n = secs(2.2); t = tt(n); f = 62 * np.exp(-t * 1.4) + 30
    return (np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 2.2) + filt(noise(n), 0, 300) * np.exp(-t * 5) * .5 + filt(noise(n), 2000, 9000) * np.exp(-t * 30) * .15) * g
def riser(d=3.0):
    n = secs(d); t = tt(n); x = filt(noise(n), 300, 8000) * (t / d) ** 2 * .5
    f = 80 + 300 * (t / d) ** 2; x += np.sin(2 * np.pi * np.cumsum(f) / SR) * (t / d) ** 2 * .4
    return x
def sub_drop(): n = secs(1.6); t = tt(n); f = 70 * np.exp(-t * 1.2) + 25; return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 1.8)
def drone(d, root=55, seed=0):
    n = secs(d); t = tt(n); r = rng(seed); x = np.zeros(n)
    for m, a in [(1, .8), (1.5, .35), (2, .3), (2.38, .15), (3, .12)]:
        x += a * np.sin(2 * np.pi * root * m * (1 + .002 * r.standard_normal()) * t + r.uniform(0, 6))
    x = x * (.7 + .3 * np.sin(2 * np.pi * t / 9)) + filt(noise(n), 60, 400) * .15
    return x * env(n, 2, 2)
def pad(d, chord, seed=0):
    n = secs(d); t = tt(n); x = np.zeros(n)
    for f in chord:
        for det in (-.7, 0, .7):
            ph = 2 * np.pi * (f + det) * t; x += np.sin(ph) + .3 * np.sin(2 * ph) + .12 * np.sin(3 * ph)
    return filt(x, 0, 1100) * env(n, 2.5, 2.5) / (len(chord) * 3)
def piano_note(f, d=3.0, g=1.0):
    n = secs(d); t = tt(n); x = np.zeros(n)
    for k, a in [(1, 1), (2, .45), (3, .25), (4, .12), (5, .06)]: x += a * np.sin(2 * np.pi * f * k * t) * np.exp(-t * (1.1 + k * .6))
    return x * np.minimum(1, t * 400) * g
def tension_strings(d, f=220, seed=0):
    n = secs(d); t = tt(n); r = rng(seed); x = np.zeros(n)
    for i in range(6):
        fr = f * (1 + r.uniform(-.004, .004)) * (2 if i % 3 == 2 else 1); ph = np.cumsum(fr * (1 + .004 * np.sin(2 * np.pi * 5.2 * t + i))) / SR
        x += 2 * (ph % 1) - 1
    return filt(x, 150, 3000) * env(n, 1.5, 1) * (t / d) * .15
