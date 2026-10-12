#!/usr/bin/env python3
"""DUXIO reel kit builder. One data file in, one renderable HyperFrames project out.

  build.py reels/<id>/reel.json [--voice] [--music] [--check] [--render]

reel.json (see reels/_example-e2-draft/reel.json):
  id, theme default, voice {script: path to .vo.json, mp3: optional ready made voice}, music {track, seed},
  beats [{at: phrase index, scene, bg: paper|dark, props, cues:[{p, dt, sfx?, v?}], sfx:[{p, dt, name, v}]}]
Cue times are phrase relative (p = phrase index, dt seconds), so changing the voice moves the whole reel.
Steps: --voice renders the voice with voiceover-pacing/director.py, --music mixes the bed with music-director.
Output: out/<id>/ (index.html, assets/) then `npx hyperframes check|render` there.
"""
import json, os, sys, shutil, subprocess, glob, random

HERE = os.path.dirname(os.path.abspath(__file__))
KIT = os.path.dirname(HERE)
REPO = os.path.abspath(os.path.join(KIT, "..", ".."))
SK = os.path.join(REPO, ".claude", "skills")
SFXDIR = os.path.join(REPO, "brand", "duxio", "sfx")
LIB = os.path.join(REPO, "brand", "duxio", "music", "library")
FONTS = os.path.join(REPO, "brand", "duxio", "fonts")

def run(*a, **k):
    print("+", " ".join(map(str, a))); subprocess.run(list(map(str, a)), check=True, **k)

def dur(path):
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path]).decode().strip())

def main():
    args = sys.argv[1:]
    reel_path = os.path.abspath(args[0]); reel = json.load(open(reel_path)); rdir = os.path.dirname(reel_path)
    rid = reel["id"]; out = os.path.join(KIT, "out", rid); assets = os.path.join(out, "assets")
    os.makedirs(os.path.join(assets, "sfx"), exist_ok=True); os.makedirs(os.path.join(assets, "fonts"), exist_ok=True)

    vo_script = os.path.join(rdir, reel["voice"]["script"])
    vo_mp3 = os.path.join(rdir, "vo", "voice.mp3"); os.makedirs(os.path.dirname(vo_mp3), exist_ok=True)
    if "--voice" in args or not os.path.exists(vo_mp3):
        run(sys.executable, os.path.join(SK, "voiceover-pacing", "director.py"), vo_script, vo_mp3)
    timings = json.load(open(vo_mp3.rsplit(".", 1)[0] + ".timings.json"))
    script = json.load(open(vo_script))
    phrases = timings["phrases"]
    for i, ph in enumerate(phrases):
        ph["cap"] = script["phrases"][i].get("cap", ph["text"])
    total = round(phrases[-1]["end"] + reel.get("tail", 0.7), 2)

    # music + premix (voice + bed, ducked)
    mix = os.path.join(rdir, "audio", "mix.mp3"); os.makedirs(os.path.dirname(mix), exist_ok=True)
    if "--music" in args or not os.path.exists(mix):
        track = os.path.join(LIB, reel.get("music", {}).get("track", "thugs") + ".mp3")
        vo_wav = vo_mp3.rsplit(".", 1)[0] + ".wav"
        run(sys.executable, os.path.join(SK, "music-director", "director.py"), track, vo_wav,
            vo_mp3.rsplit(".", 1)[0] + ".timings.json", os.path.join(rdir, "audio", "bed.wav"), "--mix", mix,
            "--seed", reel.get("music", {}).get("seed", 7))

    # resolve beats to absolute times
    beats = reel["beats"]; sfxmap = json.load(open(os.path.join(HERE, "sfx-map.json")))
    cues_out, audio = [], []
    ph_t = lambda p, dt=0: round(phrases[p]["start"] + dt, 3)
    for bi, b in enumerate(beats):
        start = 0.0 if bi == 0 else ph_t(b["at"], b.get("dt", -0.05))
        end = ph_t(beats[bi + 1]["at"], beats[bi + 1].get("dt", -0.05)) if bi + 1 < len(beats) else total
        layers = b.get("layers") or [{"scene": b["scene"], "props": b.get("props", {}), "cues": b.get("cues", [{"p": b["at"]}])}]
        lay_out = []
        for L in layers:
            lay_out.append({"scene": L["scene"], "props": L.get("props", {}), "cues": [{"t": ph_t(c["p"], c.get("dt", 0))} for c in L.get("cues", [{"p": b["at"]}])]})
            for c in L.get("cues", []):
                if c.get("sfx"): audio.append((c["sfx"], ph_t(c["p"], c.get("dt", 0)), c.get("v")))
        for s in b.get("sfx", []): audio.append((s["name"], ph_t(s["p"], s.get("dt", 0)), s.get("v")))
        if bi > 0 and b.get("cut", True): audio.append(("cut", start - 0.04, None))
        cues_out.append({"bg": b.get("bg", "paper"), "start": start, "end": end, "layers": lay_out})
    hit = reel.get("hit", True)
    if hit: audio.append((hit if isinstance(hit, str) else "hit", 0.0, None))

    # sfx files
    rnd = random.Random(3); tags = []; used = {}
    for n, (name, t, v) in enumerate(sorted(audio, key=lambda a: a[1])):
        e = sfxmap[name]; f = rnd.choice(e["files"]) if isinstance(e["files"], list) else e["files"]
        src = os.path.join(SFXDIR, f); base = os.path.basename(src)
        if not os.path.exists(os.path.join(assets, "sfx", base)): shutil.copy(src, os.path.join(assets, "sfx", base))
        d = min(dur(src), e.get("max", 1.5)); vol = round((v if v is not None else e["v"]), 3)
        tags.append(f'<audio id="sfx{n}" src="assets/sfx/{base}" data-start="{max(0,t):.3f}" data-duration="{d:.3f}" data-track-index="{20+n}" data-volume="{vol}" data-audio-group="sfx"></audio>')

    # optional hard cut to silence (a "silence beat"): {"from": {"p", "dt"}, "to": {"p", "dt"}}
    if reel.get("silence"):
        a, b = (ph_t(reel["silence"][k]["p"], reel["silence"][k].get("dt", 0)) for k in ("from", "to"))
        run("ffmpeg", "-y", "-loglevel", "error", "-i", mix, "-af",
            f"volume='if(between(t,{a},{b}),0,1)':eval=frame", "-b:a", "256k", os.path.join(assets, "mix.mp3"))
    else:
        shutil.copy(mix, os.path.join(assets, "mix.mp3"))
    for a in reel.get("assets", []): shutil.copy(os.path.join(REPO, a), os.path.join(assets, os.path.basename(a)))
    for f in glob.glob(os.path.join(FONTS, "plus-jakarta-sans-latin-*.woff2")) + [os.path.join(FONTS, "instrument-serif-latin-400-italic.woff2")]:
        shutil.copy(f, os.path.join(assets, "fonts"))
    gsap = next(p for p in [os.path.join(REPO, "kept-reel-src", "gsap.min.js")] if os.path.exists(p)); shutil.copy(gsap, os.path.join(out, "gsap.min.js"))
    shutil.copy(os.path.join(REPO, "kept-reel-src", "hyperframes.json"), os.path.join(out, "hyperframes.json"))
    json.dump({"id": rid, "name": rid}, open(os.path.join(out, "meta.json"), "w"))

    fonts = "".join(f"@font-face{{font-family:'Plus Jakarta Sans';font-weight:{w};src:url('assets/fonts/plus-jakarta-sans-latin-{w}-normal.woff2') format('woff2')}}" for w in (400, 500, 600, 700, 800))
    fonts += "@font-face{font-family:'Instrument Serif';font-style:italic;src:url('assets/fonts/instrument-serif-latin-400-italic.woff2') format('woff2')}"
    for f in reel.get("fonts", []):   # extra faces: {family, file (in brand/duxio/fonts), weight, style}
        shutil.copy(os.path.join(FONTS, f["file"]), os.path.join(assets, "fonts", f["file"]))
        fonts += f"@font-face{{font-family:'{f['family']}';font-weight:{f.get('weight', 400)};font-style:{f.get('style', 'normal')};src:url('assets/fonts/{f['file']}') format('woff2')}}"
    css = open(os.path.join(HERE, "kit.css"), encoding="utf-8").read(); js = open(os.path.join(HERE, "scenes.js"), encoding="utf-8").read()
    apjs = os.path.join(HERE, "ap.js")
    if os.path.exists(apjs): js += "\n" + open(apjs, encoding="utf-8").read()   # Apple element scenes (S.ap)
    data = {"beats": cues_out, "phrases": phrases, "total": total, "captionLight": reel.get("captionLight", False), "capChunk": reel.get("capChunk", 0), "capClass": reel.get("capClass", "")}
    html = f"""<!doctype html><html lang="en"><head><meta charset="UTF-8"/><meta name="viewport" content="width=1080, height=1920"/>
<script src="gsap.min.js"></script><style>{fonts}{css}{":root{" + ";".join(f"{k}:{v}" for k, v in reel.get("vars", {}).items()) + "}"}</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{total}" data-width="1080" data-height="1920">
<audio id="mix" src="assets/mix.mp3" data-start="0" data-duration="{total}" data-track-index="5" data-volume="1" data-audio-group="voiceover"></audio>
{chr(10).join(tags)}
</div>
<script>window.REEL={json.dumps(data)};</script>
<script>{js}
const tl=gsap.timeline({{paused:true}}); const root=document.getElementById("root"); const R=window.REEL;
R.beats.forEach((b,i)=>{{
  const el=$(root,"scene "+b.bg); tl.set(el,{{visibility:"visible"}},b.start); tl.set(el,{{visibility:"hidden"}},b.end);
  b.layers.forEach(L=>S[L.scene]({{tl,el,props:L.props,cue:(k)=>L.cues[k]?L.cues[k].t:undefined,start:b.start,end:b.end}}));
}});
buildCaptions(tl,root,R.phrases,R.captionLight,R.capChunk); if(R.capClass) document.getElementById("cap").classList.add(R.capClass);
tl.set({{}},{{}},R.total);
window.__timelines=window.__timelines||{{}}; window.__timelines["main"]=tl;
</script></body></html>"""
    open(os.path.join(out, "index.html"), "w", encoding="utf-8").write(html)
    print("built", out, "duration", total)
    if "--check" in args: run("npx", "-y", "hyperframes", "check", cwd=out)
    if "--render" in args: run("npx", "-y", "hyperframes", "render", "--output", os.path.join(out, rid + ".mp4"), cwd=out)

if __name__ == "__main__":
    main()
