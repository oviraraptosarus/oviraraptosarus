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
MODEL = os.path.expanduser("~/.cache/hyperframes/tts/models/kokoro-v1.0.onnx")
VOICES = os.path.expanduser("~/.cache/hyperframes/tts/voices/voices-v1.0.bin")


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


def nudge(a, st, gain_db):
    """Small register shift with rubberband (formants preserved), no resynthesis, so no buzz."""
    if abs(st) >= 0.4:
        tmp = tempfile.mkdtemp()
        i, o = os.path.join(tmp, "i.wav"), os.path.join(tmp, "o.wav")
        sf.write(i, a.astype(np.float32), SR)
        r = 2 ** (st / 12.0)
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", i, "-af",
                        f"rubberband=pitch={r:.4f}:formant=preserved:pitchq=quality", o], check=True)
        a, _ = sf.read(o)
    return a * (10 ** (gain_db / 20.0))


def lift(a, st, tail=0.45, xf=0.02):
    """Question intonation. Only the last `tail` seconds are re-synthesised (WORLD): the voiced contour is replaced by a glide
    from the tail's low point up `st` semitones, so the phrase ends on a rise even when the TTS falls. The head stays untouched."""
    x = a.astype(np.float64)
    f0, t = pw.harvest(x, SR, f0_floor=70, f0_ceil=500, frame_period=5)
    sp = pw.cheaptrick(x, f0, t, SR)
    ap = pw.d4c(x, f0, t, SR)
    k0 = int(np.searchsorted(t, len(x) / SR - tail))
    v = np.where(f0[k0:] > 0)[0] + k0
    if len(v) < 8:
        return a
    base = np.percentile(f0[v], 25)
    ramp = np.clip((np.arange(len(f0)) - v[0]) / max(1, v[-1] - v[0]), 0, 1) ** 1.4
    new = f0.copy()
    new[v] = base * 2 ** (st * ramp[v] / 12.0)
    for k in range(v[0], v[-1]):                      # bridge gaps of up to 3 frames so the glide stays continuous
        if new[k] == 0 and (new[max(k - 3, 0):k] > 0).any() and (new[k:k + 4] > 0).any():
            new[k] = base * 2 ** (st * ramp[k] / 12.0)
    y = pw.synthesize(new[k0:], sp[k0:], ap[k0:], SR, frame_period=5)
    s0 = int(round(t[k0] * SR))
    y = y[: len(x) - s0]
    ref = np.sqrt(np.mean(x[s0:] ** 2)) + 1e-9
    y = y * (ref / (np.sqrt(np.mean(y ** 2)) + 1e-9))
    c = min(int(xf * SR), len(y) // 2, s0)
    w = np.linspace(0, 1, c)
    return np.concatenate([x[: s0 - c], x[s0 - c: s0] * (1 - w) + y[:c] * w, y[c:]])


def roughness(a):
    """Lower is cleaner. Counts pitch jumps and breathy/noisy voiced frames (the raspy glitches)."""
    x = a.astype(np.float64)
    f0, t = pw.harvest(x, SR, f0_floor=70, f0_ceil=500, frame_period=5)
    v = f0 > 0
    if v.sum() < 8:
        return 9.0
    st = 12 * np.log2(np.where(v, f0, 1))
    both = v[1:] & v[:-1]
    jumps = (np.abs(np.diff(st))[both] > 3.0).mean()
    ap = pw.d4c(x, f0, t, SR)
    hf = ap[:, 40:][v].mean()              # aperiodicity in the upper band while voiced
    env = np.abs(x[::int(0.005 * SR)])[:len(v)]
    unv = (~v[:len(env)] & (env > 0.05)).mean()
    return float(jumps * 10 + hf * 2 + unv * 3)


def clean_take(k, text, vec, speed, rng, tries):
    best = None
    for i in range(tries):
        sp = float(np.clip(speed * (1 + (0 if i == 0 else rng.uniform(-0.05, 0.05))), 0.6, 1.5))
        a, _ = k.create(text, voice=vec, speed=sp, lang="en-us")
        a = trim(a)
        r = roughness(a)
        if best is None or r < best[0]:
            best = (r, a)
    return best


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
        r, a = clean_take(k, p["t"], vec, sp, rng, script.get("takes", 6))
        if report: print(f"  rough {r:.2f}  {p['t']}")
        S = script.get("strength", 0.7)
        if script.get("shape", False):      # WORLD vocoder contour shaping: expressive but can sound raspy
            a = shape(a, k=p.get("k", base_k), st=p.get("st", 0) * S, fall=p.get("fall", 0) * S,
                      rise=p.get("rise", 0) * S, reset=p.get("reset", 0) * S, gain_db=p.get("gain", 0))
        else:                                # clean path: best of N takes, no resynthesis, no pitch shifting
            a = a * (10 ** (p.get("gain", 0) / 20.0))
        if p.get("q"):                       # question: end the phrase on a rising pitch (semitones)
            a = lift(a, p["q"], tail=p.get("q_tail", 0.42))
        a = fade(a)
        dur = len(a) / SR
        timings.append({"text": p["t"], "start": round(t, 3), "end": round(t + dur, 3), "e": p.get("e", 0.6)})
        track.append(a)
        pause = min(p.get("pause", 300) * script.get("pause_scale", 0.6), script.get("pause_max", 480)) * (1 + rng.uniform(-wob, wob) * 1.5)
        track.append(np.zeros(int(pause / 1000 * SR)))
        t += dur + pause / 1000
    y = np.concatenate(track)
    if script.get("global_st"):           # one formant-safe shift over the whole read, never per phrase
        y = nudge(y, script["global_st"], 0)
    tmp = tempfile.mkdtemp()
    raw = os.path.join(tmp, "raw.wav")
    sf.write(raw, y.astype(np.float32), SR)
    chain = script.get("chain") or ("highpass=f=80,bass=g=1.5:f=170:w=0.8,"
             "deesser=i=0.5:m=0.5:f=0.5,equalizer=f=7500:t=h:w=0.7:g=-2.5,"
             "acompressor=threshold=0.14:ratio=2.2:attack=10:release=160:makeup=1.5,"
             "loudnorm=I=-16:TP=-1.5:LRA=9")
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
