#!/usr/bin/env python3
"""Render a .vo.json performance script with ElevenLabs instead of Kokoro, same pauses, same timings output.

Usage: ELEVENLABS_API_KEY=... eleven.py script.vo.json out.mp3 [male|female_reel]
Needs: network access to api.elevenlabs.io and the key in the environment. Looks the voice up by name in
the account, then in the shared voice library (and adds it to the account). Settings: elevenlabs.json.
UNTESTED from the cloud session (host blocked). Run it where the key and network exist.
"""
import os, sys, json, io, subprocess, tempfile, urllib.request, urllib.parse
import numpy as np, soundfile as sf

API = "https://api.elevenlabs.io/v1"
KEY = os.environ.get("ELEVENLABS_API_KEY")
HERE = os.path.dirname(__file__)


def call(path, data=None, method=None, raw=False):
    req = urllib.request.Request(API + path, data=json.dumps(data).encode() if data is not None else None,
                                 headers={"xi-api-key": KEY, "Content-Type": "application/json"}, method=method)
    r = urllib.request.urlopen(req, timeout=120).read()
    return r if raw else json.loads(r)


def resolve_voice(names):
    mine = {v["name"].lower(): v["voice_id"] for v in call("/voices")["voices"]}
    for n in names:
        for k, vid in mine.items():
            if n.lower() in k:
                return vid, n
    for n in names:
        res = call("/shared-voices?search=" + urllib.parse.quote(n) + "&page_size=5").get("voices", [])
        if res:
            v = res[0]
            call(f"/voices/add/{v['public_owner_id']}/{v['voice_id']}", {"new_name": v["name"]}, method="POST")
            return v["voice_id"], n
    raise SystemExit("no voice found for " + ", ".join(names))


def main():
    if not KEY:
        raise SystemExit("Set ELEVENLABS_API_KEY")
    script = json.load(open(sys.argv[1]))
    out = sys.argv[2]
    kind = sys.argv[3] if len(sys.argv) > 3 else "female_reel"
    cfg = json.load(open(os.path.join(HERE, "elevenlabs.json")))[kind]
    vid, name = resolve_voice(cfg["search"])
    print("voice:", name, vid)
    sr = 44100
    track, timings, t = [np.zeros(int(0.06 * sr))], [], 0.06
    texts = [p["t"] for p in script["phrases"]]
    for i, p in enumerate(script["phrases"]):
        body = {"text": p["t"], "model_id": cfg["model"], "voice_settings": cfg["settings"],
                "previous_text": " ".join(texts[max(0, i - 2):i]) or None, "next_text": " ".join(texts[i + 1:i + 3]) or None}
        body = {k: v for k, v in body.items() if v is not None}
        mp3 = call(f"/text-to-speech/{vid}?output_format=mp3_44100_128", body, method="POST", raw=True)
        a, _ = sf.read(io.BytesIO(mp3))
        a = a if a.ndim == 1 else a.mean(1)
        idx = np.where(np.abs(a) > 0.01)[0]
        if len(idx):
            a = a[max(0, idx[0] - 300): idx[-1] + 300]
        dur = len(a) / sr
        pause = min(p.get("pause", 300) * script.get("pause_scale", 0.6), script.get("pause_max", 480)) / 1000
        timings.append({"text": p["t"], "start": round(t, 3), "end": round(t + dur, 3), "e": p.get("e", 0.6)})
        track += [a, np.zeros(int(pause * sr))]
        t += dur + pause
    y = np.concatenate(track)
    tmp = tempfile.mkdtemp(); raw = os.path.join(tmp, "r.wav"); sf.write(raw, y.astype(np.float32), sr)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", raw, "-af", "highpass=f=80,loudnorm=I=-16:TP=-1.5:LRA=9",
                    "-codec:a", "libmp3lame", "-b:a", "192k", out], check=True)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", out, "-ar", "48000", out.rsplit(".", 1)[0] + ".wav"], check=True)
    json.dump({"name": script.get("name"), "duration": round(t, 3), "voice": name, "phrases": timings},
              open(out.rsplit(".", 1)[0] + ".timings.json", "w"), indent=1)
    print("done", out)


if __name__ == "__main__":
    main()
