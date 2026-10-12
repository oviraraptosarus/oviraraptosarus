#!/usr/bin/env python3
"""Music director: turns a flat music bed into a reel soundtrack with a shape.

A track on its own sits at one energy. Reels need an arc: a hit at frame 0, a drop-out for the sting,
a build into the reveal, a full drive for the CTA. This tool does that:
  - finds the most energetic stretch of the track and cuts it on a bar line, locked to the beat grid
  - synthesizes a drum layer (kick, clap, hats) on that grid, whose density follows the energy curve
  - adds a riser into every build and an impact on every drop, and a hit at frame 0
  - sweeps a low pass so the music opens up with the energy and tucks away under gravity lines
  - ducks the music under the voice with a sidechain, then mixes and masters

Usage: director.py track.mp3 voice.wav timings.json out.wav [--mix out_mix.mp3] [--seed N]
timings.json comes from voiceover-pacing/director.py (each phrase has start, end and e, energy 0..1).
"""
import sys, json, subprocess, tempfile, os
import numpy as np, soundfile as sf, librosa
from scipy import signal

SR = 44100


def energy_curve(timings, T, hz=50):
    ts = [0.0] + [(p["start"] + p["end"]) / 2 for p in timings] + [T]
    es = [timings[0]["e"]] + [p["e"] for p in timings] + [timings[-1]["e"]]
    x = np.arange(0, T, 1 / hz)
    e = np.interp(x, ts, es)
    k = int(0.35 * hz)
    e = np.convolve(np.pad(e, (k, k), mode="edge"), np.ones(2 * k + 1) / (2 * k + 1), mode="valid")
    return x, e[: len(x)]


def pick_segment(y, sr, T):
    tempo, beats = librosa.beat.beat_track(y=y, sr=sr, units="time")
    tempo = float(np.atleast_1d(tempo)[0])
    if tempo > 150:
        tempo /= 2          # half time reading of a fast track
    bar = 4 * 60 / tempo
    rms = librosa.feature.rms(y=y, frame_length=2048, hop_length=512)[0]
    hop = 512 / sr
    n = int(T / hop)
    best, bi = -1, 0
    for i in range(0, max(1, len(rms) - n), int(0.5 / hop)):
        v = rms[i:i + n].mean()
        if v > best:
            best, bi = v, i
    start_t = bi * hop
    on = beats[beats >= start_t - 0.01]
    start_t = on[0] if len(on) else start_t
    # snap to a bar: pick a beat whose index is a multiple of 4 from the first beat
    if len(beats):
        idx = np.argmin(np.abs(beats - start_t))
        idx -= idx % 4
        start_t = beats[idx]
    return start_t, tempo, bar, beats


def kick(n):
    t = np.arange(int(0.28 * SR)) / SR
    f = 45 + 110 * np.exp(-t * 28)
    ph = 2 * np.pi * np.cumsum(f) / SR
    return np.sin(ph) * np.exp(-t * 11) * 0.95 + np.random.randn(len(t)) * np.exp(-t * 90) * 0.12


def clap(rng):
    t = np.arange(int(0.22 * SR)) / SR
    n = rng.standard_normal(len(t))
    b, a = signal.butter(2, [1000 / (SR / 2), 3200 / (SR / 2)], "band")
    n = signal.lfilter(b, a, n)
    env = np.exp(-t * 22) + 0.7 * np.exp(-((t - 0.012) ** 2) / 1e-5) + 0.5 * np.exp(-((t - 0.024) ** 2) / 1e-5)
    return n * env * 0.7


def hat(rng, open_=False):
    d = 0.09 if open_ else 0.035
    t = np.arange(int(d * 3 * SR)) / SR
    n = rng.standard_normal(len(t))
    b, a = signal.butter(2, 7000 / (SR / 2), "high")
    return signal.lfilter(b, a, n) * np.exp(-t / d) * 0.28


def riser(dur, rng):
    n = int(dur * SR)
    x = rng.standard_normal(n)
    f, t, Z = signal.stft(x, SR, nperseg=2048)
    fc = np.geomspace(300, 9000, Z.shape[1])
    lf = np.log(f[:, None] + 1)
    mask = np.exp(-((lf - np.log(fc)[None, :]) ** 2) / (2 * 0.55 ** 2))
    _, y = signal.istft(Z * mask, SR, nperseg=2048)
    y = y[:n]
    env = np.linspace(0.05, 1, len(y)) ** 2.2
    sw = np.sin(2 * np.pi * np.cumsum(np.geomspace(180, 1800, len(y))) / SR) * 0.15
    y = (y / (np.abs(y).max() + 1e-9) * 0.8 + sw) * env
    y[-int(0.02 * SR):] *= np.linspace(1, 0, int(0.02 * SR))
    return y


def impact(rng):
    t = np.arange(int(1.4 * SR)) / SR
    sub = np.sin(2 * np.pi * (48 + 60 * np.exp(-t * 9)) * t) * np.exp(-t * 3.0)
    n = rng.standard_normal(len(t))
    b, a = signal.butter(2, 2500 / (SR / 2), "low")
    nz = signal.lfilter(b, a, n) * np.exp(-t * 7) * 0.5
    return (sub * 0.95 + nz)


def place(buf, clip, at, gain=1.0):
    i = int(at * SR)
    if i < 0 or i >= len(buf):
        return
    j = min(len(buf), i + len(clip))
    buf[i:j] += clip[: j - i] * gain


def main():
    a = sys.argv
    track, voice, tj, out = a[1], a[2], a[3], a[4]
    mix_out = a[a.index("--mix") + 1] if "--mix" in a else None
    seed = int(a[a.index("--seed") + 1]) if "--seed" in a else 5
    rng = np.random.default_rng(seed)
    timings = json.load(open(tj))["phrases"]
    v, vsr = sf.read(voice)
    v = v if v.ndim == 1 else v.mean(1)
    T = len(v) / vsr + 1.0
    y, sr = librosa.load(track, sr=SR, mono=True)
    start, tempo, bar, beats = pick_segment(y, SR, T + bar_pad(T))
    seg = y[int(start * SR): int(start * SR) + int(T * SR)]
    if len(seg) < int(T * SR):
        seg = np.pad(seg, (0, int(T * SR) - len(seg)))
    # beat grid inside the segment
    beat = 60 / tempo
    sb = beats[beats >= start]
    first = (sb[0] - start) if len(sb) else 0.0
    grid = np.arange(first, T, beat)
    xs, e = energy_curve(timings, T)
    env = lambda t: float(np.interp(t, xs, e))
    # music with an energy shaped filter: closed under gravity, open on drive
    seg = seg / (np.abs(seg).max() + 1e-9)
    blocks = []
    hop = int(0.1 * SR)
    prev = None
    out_seg = np.zeros_like(seg)
    for i in range(0, len(seg), hop):
        t0 = i / SR
        fc = 900 + 14000 * env(t0) ** 1.4
        b, aa = signal.butter(2, min(fc, 20000) / (SR / 2), "low")
        chunk = seg[i:i + hop + 2048]
        zi = signal.lfilter_zi(b, aa) * (prev if prev is not None else 0)
        # block filtering with continuity via overlap discard
        yb = signal.lfilter(b, aa, seg[max(0, i - 2048):i + hop])[min(i, 2048):]
        out_seg[i:i + len(yb)] = yb[: len(out_seg[i:i + len(yb)])]
    seg = out_seg
    gain = np.array([0.45 + 0.55 * env(t) for t in np.arange(len(seg)) / SR])
    seg = seg * gain
    # drums on the grid
    drums = np.zeros(len(seg))
    K, C = kick(0), clap(rng)
    for k_, t in enumerate(grid):
        en = env(t)
        step = k_ % 4
        if en > 0.30 and step in (0, 2) or (en > 0.8 and step == 3 and k_ % 8 == 7):
            place(drums, K, t, 0.85 * min(1, en + 0.2))
        if en > 0.52 and step in (1, 3):
            place(drums, C, t, 0.55 * en)
        if en > 0.42:
            place(drums, hat(rng), t + beat / 2, 0.8 * en)
        if en > 0.78:
            place(drums, hat(rng), t + beat / 4, 0.55 * en)
            place(drums, hat(rng), t + 3 * beat / 4, 0.55 * en)
    # risers and impacts at energy jumps and after long pauses
    fx = np.zeros(len(seg))
    place(fx, impact(rng), 0.0, 0.9)
    for p, q in zip(timings, timings[1:]):
        gap = q["start"] - p["end"]
        if gap >= 0.55 or q["e"] - p["e"] >= 0.3:
            at = q["start"]
            rl = min(1.6, max(0.8, gap + 0.6))
            place(fx, riser(rl, rng), max(0, at - rl + 0.05), 0.55)
            place(fx, impact(rng), at - 0.02, 0.6 if q["e"] > 0.6 else 0.35)
    # a short drop out: dip the bed for the sting lines
    bed = seg + drums * 0.9
    bed = bed / (np.abs(bed).max() + 1e-9) * 0.7
    stem = bed + fx * 0.8
    stem = np.tanh(stem * 1.2) / np.tanh(1.2)
    sf.write(out, stem.astype(np.float32), SR)
    print(f"track tempo {tempo:.0f} bpm · start {start:.1f}s · segment {T:.1f}s · beats in grid {len(grid)}")
    if mix_out:
        # sidechain: duck the music under the voice, then master the pair
        vd = voice
        fc = (f"[1:a]asplit=2[sc][vv];[0:a]volume=-9dB[m];[m][sc]sidechaincompress=threshold=0.02:ratio=7:attack=6:release=320:makeup=1[md];"
              f"[md][vv]amix=inputs=2:duration=longest:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=9[o]")
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", out, "-i", vd, "-filter_complex", fc, "-map", "[o]",
                        "-codec:a", "libmp3lame", "-b:a", "192k", mix_out], check=True)
        print("mixed ->", mix_out)


def bar_pad(T):
    return 2.0


if __name__ == "__main__":
    main()
