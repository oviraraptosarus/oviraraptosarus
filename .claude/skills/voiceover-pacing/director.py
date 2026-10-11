#!/usr/bin/env python3
"""Voice director: turns a marked-up performance script into a human sounding voiceover.

Kokoro reads flat and evenly. This tool does what a voice director does:
  - speaks the script one breath (phrase) at a time, each with its own speed
  - places the silences by hand (pause_ms), with small seeded human wobble
  - reshapes pitch with the WORLD vocoder: wider range, a stress lift, a falling landing on statements,
    a rise on questions, a bright start on hooks, a lower and slower voice for stakes ("gravity")
  - warms and compresses the result, and writes timings for the captions and the video kit

Usage: director.py script.json out.mp3 [--report]
Script format: see scripts/*.vo.json and SKILL.md.
"""
import json, sys, subprocess, tempfile, os
import numpy as np, soundfile as sf, pyworld as pw
from kokoro_onnx import Kokoro

SR = 24000
MODEL = "/root/.cache/hyperframes/tts/models/kokoro-v1.0.onnx"
VOICES = "/root/.cache/hyperframes/tts/voices/voices-v1.0.bin"


def voice_vec(k, spec):
    if isinstance(spec, str):
        spec = {spec: 1.0}
    tot = sum(spec.values())
    return sum(k.get_voice_style(n) * (w / tot) for n, w in spec.items())


def trim(a, thr=0.012, pad=int(0.012 * SR)):
    idx = np.where(np.abs(a) > thr)[0]
    if len(idx) == 0:
        return a
    return a[max(0, idx[0] - pad): idx[-1] + pad]


def shape(a, k=1.3, st=0.0, fall=0.0, rise=0.0, reset=0.0, gain_db=0.0, cap=(-9.0, 7.0)):
    """Reshape the pitch contour. k widens the range, st shifts the register (semitones),
    fall/rise bend the last 45% down/up (semitones), reset lifts the start and decays."""
    x = a.astype(np.float64)
    f0, t = pw.harvest(x, SR, f0_floor=70, f0_ceil=500, frame_period=5)
    sp = pw.cheaptrick(x, f0, t, SR)
    ap = pw.d4c(x, f0, t, SR)
    v = f0 > 0
    if v.sum() > 6:
        lf = np.log2(np.where(v, f0, 1.0))
        mu = np.median(lf[v])
        dev = np.clip((lf - mu) * 12, -9, 9) / 12.0          # drop octave errors
        out = mu + k * dev + st / 12.0
        vi = np.where(v)[0]
        pos = (np.arange(len(f0)) - vi[0]) / max(1, vi[-1] - vi[0])
        c = np.zeros(len(f0))
        c += -fall * np.clip((pos - 0.55) / 0.45, 0, 1) ** 1.2
        c += rise * np.clip((pos - 0.55) / 0.45, 0, 1) ** 1.2
        c += reset * np.clip(1 - pos / 0.3, 0, 1)
        out = out + c / 12.0
        out = mu + np.clip((out - mu) * 12, cap[0], cap[1]) / 12.0   # never leave a human range
        # light smoothing so the bends do not click
        kernel = np.ones(5) / 5
        out = np.where(v, np.convolve(out, kernel, mode="same"), 0)
        f0n = np.where(v, 2 ** out, 0.0)
    else:
        f0n = f0
    y = pw.synthesize(f0n, sp, ap, SR, frame_period=5)
    return y * (10 ** (gain_db / 20.0))


def fade(a, ms=8):
    n = int(ms / 1000 * SR)
    if len(a) > 2 * n:
        a = a.copy()
        a[:n] *= np.linspace(0, 1, n)
        a[-n:] *= np.linspace(1, 0, n)
    return a


def build(script, out_mp3, report=False):
    k = Kokoro(MODEL, VOICES)
    vec = voice_vec(k, script["voice"])
    rng = np.random.default_rng(script.get("seed", 7))
    wob = script.get("wobble", 0.06)
    base_k = script.get("k", 1.3)
    base_speed = script.get("base_speed", 1.05)
    lead = int(script.get("lead_ms", 60) / 1000 * SR)
    track = [np.zeros(lead)]
    t = lead / SR
    timings = []
    for p in script["phrases"]:
        sp = base_speed * p.get("speed", 1.0) * (1 + rng.uniform(-wob, wob) * 0.5)
        a, _ = k.create(p["t"], voice=vec, speed=float(np.clip(sp, 0.6, 1.5)), lang="en-us")
        a = trim(a)
        S = script.get("strength", 0.7)
        a = shape(a, k=p.get("k", base_k), st=p.get("st", 0) * S, fall=p.get("fall", 0) * S,
                  rise=p.get("rise", 0) * S, reset=p.get("reset", 0) * S, gain_db=p.get("gain", 0))
        a = fade(a)
        dur = len(a) / SR
        timings.append({"text": p["t"], "start": round(t, 3), "end": round(t + dur, 3), "e": p.get("e", 0.6)})
        track.append(a)
        pause = p.get("pause", 300) * (1 + rng.uniform(-wob, wob) * 1.5)
        track.append(np.zeros(int(pause / 1000 * SR)))
        t += dur + pause / 1000
    y = np.concatenate(track)
    tmp = tempfile.mkdtemp()
    raw = os.path.join(tmp, "raw.wav")
    sf.write(raw, y.astype(np.float32), SR)
    chain = ("highpass=f=75,bass=g=2.5:f=170:w=0.8,equalizer=f=3200:t=q:w=1.1:g=1.8,"
             "deesser=i=0.35:m=0.5:f=0.5,"
             "acompressor=threshold=0.1:ratio=3:attack=8:release=120:makeup=2.5,"
             "loudnorm=I=-16:TP=-1.5:LRA=7")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", raw, "-af", chain, "-ar", "44100",
                    "-codec:a", "libmp3lame", "-b:a", "192k", out_mp3], check=True)
    wav = out_mp3.rsplit(".", 1)[0] + ".wav"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", out_mp3, "-ar", "48000", wav], check=True)
    json.dump({"name": script.get("name"), "duration": round(t, 3), "phrases": timings},
              open(out_mp3.rsplit(".", 1)[0] + ".timings.json", "w"), indent=1)
    if report:
        report_metrics(wav, timings, script)


def report_metrics(wav, timings, script):
    x, sr = sf.read(wav)
    x = x if x.ndim == 1 else x.mean(1)
    f0, _ = pw.harvest(x.astype(np.float64), sr, f0_floor=70, f0_ceil=500, frame_period=10)
    v = f0[f0 > 0]
    stv = 12 * np.log2(v / np.median(v))
    words = sum(len(p["text"].split()) for p in timings)
    total = timings[-1]["end"]
    gaps = [round((b["start"] - a["end"]) * 1000) for a, b in zip(timings, timings[1:])]
    print(f"duration {total:.1f}s · {words} words · {words/total:.2f} words/sec incl. pauses")
    print(f"pitch median {np.median(v):.0f} Hz · std {stv.std():.2f} st · range(5-95%) {np.percentile(stv,95)-np.percentile(stv,5):.1f} st")
    print(f"pauses ms: {gaps}")
    print(f"pause time {sum(gaps)/1000/total*100:.0f}% of runtime · gaps min {min(gaps)} max {max(gaps)}")


if __name__ == "__main__":
    script = json.load(open(sys.argv[1]))
    build(script, sys.argv[2], report="--report" in sys.argv)
