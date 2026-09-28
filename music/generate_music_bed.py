"""
Original, royalty-free background music bed for the puppy videos.

Synthesizes a warm chord pad (music-box-style) from scratch using numpy —
no samples, no licensed audio, no credits or API calls. Since Claude composes
it note-by-note in code, there's no licensing question and it costs nothing
to generate.

Usage:
    python3 generate_music_bed.py            # writes music_bed.wav, 58s
Then mix it quietly under the voiceover, e.g.:
    ffmpeg -i voice.wav -i music_bed.wav \
      -filter_complex "[1:a]volume=0.5,atrim=0:<video_len>,asetpts=PTS-STARTPTS[m];
                        [0:a][m]amix=inputs=2:duration=first:dropout_transition=0,
                        loudnorm=I=-14:TP=-1.5:LRA=8[a]" \
      -map "[a]" -ar 44100 -ac 2 voice_with_music.wav

Tune `total_dur` to match the finished video's length before the final mix.
"""
import numpy as np
import soundfile as sf

sr = 44100


def note_freq(n):  # n=0 -> C4 (261.63 Hz)
    return 261.63 * (2 ** (n / 12))


def soft_tone(freq, dur, sr=sr, vol=1.0, harm=(1, 0.5, 0.25, 0.12)):
    """A single soft, music-box/piano-like tone: harmonic stack + gentle ADSR."""
    t = np.linspace(0, dur, int(sr * dur), endpoint=False)
    wave = np.zeros_like(t)
    for i, h in enumerate(harm):
        wave += h * np.sin(2 * np.pi * freq * (i + 1) * t)
    a = int(sr * 0.02)
    d = int(sr * 0.15)
    r = len(t) - a - d
    env = np.ones_like(t)
    env[:a] = np.linspace(0, 1, a)
    env[a:a + d] = np.linspace(1, 0.55, d)
    env[a + d:] = 0.55 * np.exp(-3.2 * np.linspace(0, 1, r))
    return wave * env * vol


def chord(notes, dur, vol=0.5):
    out = np.zeros(int(sr * dur))
    for n in notes:
        w = soft_tone(note_freq(n), dur, vol=vol / len(notes) ** 0.5)
        out[:len(w)] += w
    return out


def build(total_dur=58, out_path="music_bed.wav"):
    # Warm progression: Cmaj7 - Am7 - Fmaj7(approx) - Gadd9(approx), 2.4s per chord
    prog = [
        ([0, 4, 7, 11], 2.4),   # Cmaj7
        ([-3, 0, 4, 7], 2.4),   # Am7
        ([-4, -1, 5, 9], 2.4),  # Fmaj7 (approx)
        ([-2, 2, 5, 9], 2.4),   # Gadd9 (approx)
    ]

    track = np.zeros(int(sr * total_dur))

    # sustained pad chords
    t, i = 0, 0
    while t < total_dur:
        notes, d = prog[i % len(prog)]
        c = chord(notes, d, vol=0.22)
        st = int(sr * t)
        end = min(st + len(c), len(track))
        track[st:end] += c[:end - st]
        t += d
        i += 1

    # quiet high arpeggio sparkle on top (music-box bell tone)
    t, i = 0.3, 0
    arp_pattern = [0, 4, 7, 12, 7, 4]
    while t < total_dur:
        notes, _d = prog[(i // len(arp_pattern)) % len(prog)]
        root = notes[0]
        step = arp_pattern[i % len(arp_pattern)]
        freq = note_freq(root + 12 + (step % 12))
        w = soft_tone(freq, 0.4, vol=0.06, harm=(1, 0.3, 0.1))
        st = int(sr * t)
        end = min(st + len(w), len(track))
        track[st:end] += w[:end - st]
        t += 0.4
        i += 1

    # fade in/out
    fade = int(sr * 1.5)
    track[:fade] *= np.linspace(0, 1, fade)
    track[-fade:] *= np.linspace(1, 0, fade)

    # soft limiter so the sum of chords + sparkle never clips
    track = np.tanh(track * 1.3) / 1.3

    sf.write(out_path, track, sr)
    return len(track) / sr


if __name__ == "__main__":
    dur = build()
    print(f"wrote music_bed.wav, {dur:.1f}s")
