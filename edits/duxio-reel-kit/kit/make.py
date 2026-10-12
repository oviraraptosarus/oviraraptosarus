#!/usr/bin/env python3
"""One command per reel: spec in, checked and rendered mp4 plus REPORT out. Run with Python 3.12.

  py -3.12 kit/make.py kit/specs/<id>.json [--no-render] [--redo-voice] [--stop-after voice|build|check|snap]

Steps: write voice script (recipe defaults + auto question lift) > voice + music > compile spec to reel.json >
build > hyperframes check > snapshots at each slide > render > ffprobe + loudness + question pitch check > REPORT.md/json.
Review out/<id>/snapshots/contact-sheet*.jpg yourself before sending the mp4 (a green check does not mean it looks right).
"""
import json, os, re, shutil, subprocess, sys, time

HERE = os.path.dirname(os.path.abspath(__file__)); KIT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from compile_ap import compile_spec

NPX = shutil.which("npx") or "npx"
VOICE_DEFAULTS = {"voice": "af_heart", "base_speed": 1.12, "seed": 21, "takes": 6, "lead_ms": 40, "pause_scale": 1.0, "pause_max": 900}


def run(cmd, cwd=None, quiet=True):
    r = subprocess.run([str(c) for c in cmd], cwd=cwd, capture_output=quiet, text=True, encoding="utf-8", errors="replace")
    return r


def voice_script(spec):
    v = {**VOICE_DEFAULTS, "name": spec["id"], **{k: x for k, x in spec["voice"].items() if k != "phrases"}}
    ph = []
    for p in spec["voice"]["phrases"]:
        p = dict(p); p.setdefault("speed", 1.1); p.setdefault("pause", 300); p.setdefault("e", 0.7)
        if p["t"].rstrip().endswith("?"):      # questions must sound like questions: rising tail, slower, short pause
            p.setdefault("q", 8); p.setdefault("q_tail", 0.45); p["speed"] = min(p["speed"], 0.98); p["pause"] = min(p["pause"], 260)
        ph.append(p)
    v["phrases"] = ph
    return v


def question_check(rdir, script):
    """f0 contour of each question phrase: semitone change from the 40 to 60 percent point to the last voiced 0.15 s."""
    try:
        import numpy as np, soundfile as sf, pyworld as pw
    except Exception as e:
        return [f"skipped ({e.__class__.__name__})"]
    tm = json.load(open(os.path.join(rdir, "vo", "voice.timings.json"), encoding="utf-8"))["phrases"]
    y, sr = sf.read(os.path.join(rdir, "vo", "voice.wav"))
    y = (y.mean(1) if y.ndim > 1 else y).astype(np.float64)
    out = []
    for i, p in enumerate(script["phrases"]):
        if not p["t"].rstrip().endswith("?"): continue
        seg = y[int(tm[i]["start"] * sr):int(tm[i]["end"] * sr)]
        f0, _ = pw.harvest(seg, sr, f0_floor=70, f0_ceil=500, frame_period=10)
        idx = np.where(f0 > 0)[0]
        if len(idx) < 12: out.append(f"{p['t']}: not enough voiced frames"); continue
        st = 12 * np.log2(f0[idx]); n = len(idx)
        mid = st[int(n * .4):int(n * .6)].mean(); low = st[int(n * .6):].min(); end = st[-12:].mean()
        out.append(f"{p['t']}: tail rise from low point {end - low:+.1f} st, end vs middle {end - mid:+.1f} st")
    return out


def main():
    a = sys.argv[1:]
    if not a or a[0].startswith("-"): sys.exit(__doc__)
    spec_path = os.path.abspath(a[0]); spec = json.load(open(spec_path, encoding="utf-8"))
    stop = a[a.index("--stop-after") + 1] if "--stop-after" in a else None
    rid = spec["id"]; rdir = os.path.join(KIT, "reels", rid); out = os.path.join(KIT, "out", rid)
    os.makedirs(rdir, exist_ok=True)
    rep = {"id": rid, "started": time.strftime("%Y-%m-%d %H:%M:%S"), "problems": []}
    t0 = time.time()

    # 1 voice + music
    script = voice_script(spec)
    json.dump(script, open(os.path.join(rdir, "voice.vo.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    reel_json = os.path.join(rdir, "reel.json")
    import hashlib
    sig = hashlib.sha1(json.dumps(script, sort_keys=True, ensure_ascii=False).encode("utf-8")).hexdigest()
    sigf = os.path.join(rdir, "vo", ".script.sha")
    same = os.path.exists(sigf) and open(sigf).read().strip() == sig        # voice is re-rendered whenever the spoken script changes
    have_voice = os.path.exists(os.path.join(rdir, "vo", "voice.timings.json")) and same and "--redo-voice" not in a
    if not have_voice:
        json.dump({"id": rid, "voice": {"script": "voice.vo.json"}, "music": spec.get("music", {"track": "thugs", "seed": 7}), "tail": 0.9,
                   "beats": [{"at": 0, "scene": "statement", "bg": "dark", "props": {"lines": ["stub"]}}]}, open(reel_json, "w"))
        mix = os.path.join(rdir, "audio", "mix.mp3")
        if os.path.exists(mix): os.remove(mix)
        r = run([sys.executable, os.path.join(HERE, "build.py"), reel_json, "--voice", "--music"])
        if r.returncode: rep["problems"].append("voice/music failed: " + r.stderr[-600:]); return finish(rep, rdir, out, 1)
    os.makedirs(os.path.join(rdir, "vo"), exist_ok=True); open(sigf, "w").write(sig)
    rep["voice_questions"] = question_check(rdir, script)
    print(f"[{rid}] voice ok ({time.time() - t0:.0f}s)")
    if stop == "voice": return finish(rep, rdir, out, 0)

    # 2 compile + build
    tm = json.load(open(os.path.join(rdir, "vo", "voice.timings.json"), encoding="utf-8"))["phrases"]
    reel, starts = compile_spec({**spec, "voice": {"phrases": script["phrases"]}}, tm)
    json.dump(reel, open(reel_json, "w", encoding="utf-8"), indent=1)
    r = run([sys.executable, os.path.join(HERE, "build.py"), reel_json])
    if r.returncode: rep["problems"].append("build failed: " + r.stderr[-800:]); return finish(rep, rdir, out, 1)
    rep["duration"] = float(re.search(r"duration ([0-9.]+)", r.stdout).group(1))
    print(f"[{rid}] built {rep['duration']}s ({time.time() - t0:.0f}s)")
    if stop == "build": return finish(rep, rdir, out, 0)

    # 3 check
    r = run([NPX, "-y", "hyperframes", "check"], cwd=out)
    text = r.stdout + r.stderr
    errs = [l.strip() for l in text.splitlines() if "✗" in l]
    rep["check_errors"] = errs
    if errs: rep["problems"] += [f"check: {e[:200]}" for e in errs]
    print(f"[{rid}] check: {len(errs)} error(s) ({time.time() - t0:.0f}s)")
    if stop == "check" or errs: return finish(rep, rdir, out, 1 if errs else 0)

    # 4 snapshots, one per slide, a beat after it starts
    snaps = os.path.join(out, "snapshots"); shutil.rmtree(snaps, ignore_errors=True)
    at = ",".join(f"{min(t + 1.0, rep['duration'] - 0.2):.2f}" for t in starts)
    r = run([NPX, "-y", "hyperframes", "snapshot", "--at", at, "--no-end", "--describe", "false"], cwd=out)
    rep["contact_sheets"] = sorted(os.path.join(snaps, f) for f in os.listdir(snaps) if f.startswith("contact-sheet")) if os.path.isdir(snaps) else []
    print(f"[{rid}] snapshots {len(rep['contact_sheets'])} sheet(s) ({time.time() - t0:.0f}s)")
    if stop == "snap" or "--no-render" in a: return finish(rep, rdir, out, 0)

    # 5 render + measure
    mp4 = os.path.join(out, rid + ".mp4")
    r = run([NPX, "-y", "hyperframes", "render", "--output", mp4], cwd=out)
    if r.returncode or not os.path.exists(mp4): rep["problems"].append("render failed: " + (r.stderr or r.stdout)[-600:]); return finish(rep, rdir, out, 1)
    pr = run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height,r_frame_rate,duration", "-of", "csv=p=0", mp4]).stdout.strip()
    ln = run(["ffmpeg", "-i", mp4, "-af", "ebur128=peak=true", "-f", "null", "-"]).stderr
    lufs = re.findall(r"I:\s+(-?[0-9.]+) LUFS", ln); peak = re.findall(r"Peak:\s+(-?[0-9.]+) dBFS", ln)
    rep.update(mp4=mp4, video=pr, lufs=float(lufs[-1]) if lufs else None, peak_dbfs=float(peak[-1]) if peak else None)
    if rep["lufs"] is not None and not -16.5 <= rep["lufs"] <= -12.5: rep["problems"].append(f"loudness {rep['lufs']} LUFS outside -16.5..-12.5")
    if rep["peak_dbfs"] is not None and rep["peak_dbfs"] > -1.0: rep["problems"].append(f"true peak {rep['peak_dbfs']} dBFS above -1")
    print(f"[{rid}] rendered {pr} {rep['lufs']} LUFS ({time.time() - t0:.0f}s)")
    return finish(rep, rdir, out, 0)


def finish(rep, rdir, out, code):
    os.makedirs(out, exist_ok=True)
    json.dump(rep, open(os.path.join(out, "REPORT.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    md = [f"# {rep['id']} build report", ""] + [f"- {k}: {v}" for k, v in rep.items() if k not in ("voice_questions", "problems", "check_errors", "contact_sheets", "id")]
    md += ["", "## Question pitch (rise should be clearly positive)"] + [f"- {q}" for q in rep.get("voice_questions", [])]
    md += ["", "## Contact sheets (review these)"] + [f"- {c}" for c in rep.get("contact_sheets", [])]
    md += ["", "## Problems"] + ([f"- {p}" for p in rep["problems"]] or ["- none"])
    open(os.path.join(out, "REPORT.md"), "w", encoding="utf-8").write("\n".join(md) + "\n")
    if rep["problems"]: print(f"[{rep['id']}] PROBLEMS: " + " | ".join(p[:160] for p in rep["problems"]))
    return code


if __name__ == "__main__":
    sys.exit(main())
