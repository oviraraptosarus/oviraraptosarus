"""Compile a declarative reel spec (kit/specs/*.json) into reel.json for the `ap` scene, using the real voice timings.

A spec slide:
  {"p": 3, "x": "chat", "eye": "The answer", "hl": ["*AI* answers in", "under *60* *seconds.*"],
   "hw": [0, 5], "xw": [2, 4, 7, 8], "gr": "red", "sfx": [["pop", "xc0", 0.2, 0.0]]}
  p     phrase index the slide mostly belongs to (word refs below are relative to it)
  hw    word ref per headline line (when that line is revealed)
  xw    word refs for the element cues (what each element does is documented in kit/ap.js)
  ref   int = word index in phrase p | "3+0.1" word plus seconds | "end" or "end-0.12" end of phrase p | [p, w] / [p, w, off] another phrase
"""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
SFXT = json.load(open(os.path.join(HERE, "ap_sfx.json"), encoding="utf-8"))
WT = lambda w: len(w) + 1.5


def compile_spec(spec, tm):
    words = [p["t"].split() for p in spec["voice"]["phrases"]]
    C, T, SFX, cache = [], [], [], {}

    def widx(p, tok):
        """word position inside phrase p: int | first | mid | last | NN% | word:<text> (first match, punctuation and case ignored)"""
        ws = words[p]; n = len(ws)
        if isinstance(tok, int): return min(tok, n - 1)
        tok = tok.strip().lower()
        if tok == "first": return 0
        if tok == "mid": return n // 2
        if tok == "last": return n - 1
        m = re.fullmatch(r"(\d+)%", tok)
        if m: return min(n - 1, round(n * int(m.group(1)) / 100))
        if tok.startswith("word:"):
            want = re.sub(r"[^a-z0-9']", "", tok[5:])
            for i, w in enumerate(ws):
                if re.sub(r"[^a-z0-9']", "", w.lower()) == want: return i
            raise ValueError(f"word {want!r} not in phrase {p}: {' '.join(ws)}")
        raise ValueError(f"bad word ref {tok!r}")

    def parse(sp, r):
        if isinstance(r, (list, tuple)):
            w = r[1] if r[1] == "end" else widx(int(r[0]), r[1])
            return int(r[0]), w, float(r[2]) if len(r) > 2 else 0.0
        if isinstance(r, str):
            s = r.strip()
            m = re.fullmatch(r"(end|first|mid|last|\d+%|word:[^+]+?|\d+)\s*(?:([+-])\s*([0-9.]+))?", s, re.I)
            if not m: raise ValueError(f"bad ref {r!r}")
            off = float(m.group(2) + m.group(3)) if m.group(2) else 0.0
            if m.group(1).lower() == "end": return sp, "end", off
            if m.group(1).isdigit(): return sp, widx(sp, int(m.group(1))), off
            return sp, widx(sp, m.group(1)), off
        return sp, widx(sp, int(r)), 0.0

    def cue(sp, r):
        p, w, off = parse(sp, r)
        key = (p, w, off)
        if key in cache: return cache[key]
        d = tm[p]["end"] - tm[p]["start"]
        if w == "end": t = d + off
        else:
            ws = words[p]; tot = sum(WT(x) for x in ws)
            t = sum(WT(x) for x in ws[:w]) / tot * d + off
        C.append({"p": p, "dt": round(t, 3)}); T.append(round(tm[p]["start"] + t, 3)); cache[key] = len(C) - 1
        return cache[key]

    def add(name, k, v, off=0.0):
        SFX.append({"p": C[k]["p"], "dt": round(C[k]["dt"] + off, 3), "name": name, **({"v": v} if v else {})})

    def resolve(ref, hc, xc, c0):
        """ref -> list of cue indexes. c0, hcN, hc-1, xcN, each:hc, each:xc, each:xc1+, each:xc1-3"""
        if ref == "c0": return [c0]
        m = re.fullmatch(r"(each:)?(hc|xc)(-?\d+)?(?:([+])|(?:-(\d+)))?", ref)
        if not m: raise ValueError(f"bad sfx ref {ref!r}")
        arr = hc if m.group(2) == "hc" else xc
        if m.group(1):
            if m.group(3) is None: return list(arr)
            lo = int(m.group(3))
            if m.group(4): return arr[lo:]
            if m.group(5): return arr[lo:int(m.group(5)) + 1]
            return [arr[lo]]
        i = int(m.group(3)); return [arr[i]] if -len(arr) <= i < len(arr) else []

    def run_sfx(entries, hc, xc, c0):
        for e in entries:
            name, ref = e[0], e[1]
            if name == "ticks":
                o = e[2]; k = resolve(ref, hc, xc, c0)
                if not k: continue
                base = C[k[0]]["dt"] + o.get("start", 0.0)
                for i in range(o["n"]):
                    SFX.append({"p": C[k[0]]["p"], "dt": round(base + i * o["gap"] + i * i * o.get("accel", 0.0), 3), "name": "tick", "v": o.get("v", 0.14)})
            elif name == "spread":
                a, b = ref.split(":"); ka = resolve(a, hc, xc, c0); kb = resolve(b, hc, xc, c0)
                if not ka or not kb: continue
                o = e[2]; ta, tb = T[ka[0]], T[kb[0]]
                for i in range(o["n"]):
                    t = ta + i / o["n"] * (tb - ta); p = C[ka[0]]["p"]
                    SFX.append({"p": p, "dt": round(t - tm[p]["start"], 3), "name": "tick", "v": o.get("v", 0.12)})
            else:
                for k in resolve(ref, hc, xc, c0): add(name, k, e[2], e[3] if len(e) > 3 else 0.0)

    slides = []
    for si, s in enumerate(spec["slides"]):
        sp = s.get("p", 0)
        hc = [cue(sp, r) for r in s.get("hw", [])]
        xc = [cue(sp, r) for r in s.get("xw", [])]
        allk = hc + xc
        c0 = min(allk, key=lambda k: T[k])
        out = {k: s[k] for k in ("eye", "hl", "gr", "plain", "flash", "x", "top", "fs", "props") if k in s}
        out.update(hc=hc, xc=xc, c0=c0)
        slides.append(out)
        if si: run_sfx(SFXT["_slide"], hc, xc, c0)
        if hc: run_sfx(SFXT["_hl"], hc, xc, c0)
        if s.get("x"): run_sfx(SFXT.get(s["x"], []), hc, xc, c0)
        run_sfx(s.get("sfx", []), hc, xc, c0)

    look = spec.get("look", {})
    reel = {
        "id": spec["id"], "voice": {"script": "voice.vo.json"}, "music": spec.get("music", {"track": "thugs", "seed": 7}),
        "tail": spec.get("tail", 0.9), "hit": "hookhit", "capChunk": 4, "capClass": "apple",
        "vars": {"--hl": "#c9adff", "--fd": "'Inter'", "--fs": "'Instrument Serif'", "--grad": "linear-gradient(95deg,#8a3dff 0%,#b98cff 55%,#f1e8ff 100%)", "--gradr": "linear-gradient(95deg,#f1283a 0%,#ff8e6b 100%)", **look.get("vars", {})},
        "fonts": [{"family": "Inter", "file": "inter-variable.woff2", "weight": "100 900"}],
        "assets": spec.get("assets", ["brand/duxio/logo/svg/duxio-wordmark-white.svg"]),
        "beats": [{"at": 0, "scene": "ap", "bg": "dark", "props": {"slides": slides}, "cues": C, "sfx": SFX}],
    }
    sb = spec.get("silence_before")
    if sb:
        reel["silence"] = {"from": {"p": sb - 1, "dt": round(tm[sb - 1]["end"] - tm[sb - 1]["start"] + 0.02, 3)}, "to": {"p": sb, "dt": -0.04}}
    return reel, [T[s["c0"]] for s in slides]
