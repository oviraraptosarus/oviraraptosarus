"""Builds reel.json for cold-call-ai-v2 from the real voice timings (run after the voice exists).
Word cues use the same length weighting as the caption engine, so a new voice retimes everything."""
import json, os
H = os.path.dirname(os.path.abspath(__file__))
tm = json.load(open(os.path.join(H, "vo", "voice.timings.json")))["phrases"]
words = [s["t"].split() for s in json.load(open(os.path.join(H, "voice.vo.json")))["phrases"]]
wt = lambda w: len(w) + 1.5
C, SFX = [], []


def dt(p, wi, off=0.0):
    ws = words[p]; tot = sum(wt(w) for w in ws); d = tm[p]["end"] - tm[p]["start"]
    return round(sum(wt(w) for w in ws[:wi]) / tot * d + off, 3)


def cue(p, wi=0, off=0.0):
    C.append({"p": p, "dt": dt(p, wi, off)}); return len(C) - 1


def endcue(p, off=0.0):
    C.append({"p": p, "dt": round(tm[p]["end"] - tm[p]["start"] + off, 3)}); return len(C) - 1


def fx(name, k, v=None, off=0.0):
    SFX.append({"p": C[k]["p"], "dt": round(C[k]["dt"] + off, 3), "name": name, **({"v": v} if v else {})})


slides = []


def slide(first, **kw):
    kw["c0"] = first; slides.append(kw)
    if len(slides) > 1: fx("whoosh", first, 0.2, -0.08)


# 0 Stop calling strangers (call screen, declined)
a, b, end = cue(0, 0), cue(0, 2), endcue(0, -0.12)
slides.append(dict(c0=a, hl=["Stop calling", "*strangers.*"], hc=[a, b], gr="red", x="call", xc=[a, end]))
fx("pulse", a, 0.25, 0.1); fx("snap", b, 0.22); fx("drop", end, 0.35); fx("snap", end, 0.22, 0.12)

# 1 The money is with the people who asked (three notifications)
h0, h1, n0, n1, n2 = cue(1, 0), cue(1, 4), cue(1, 3), cue(1, 5), cue(1, 8)
slide(h0, eye="Where the money is", hl=["The money is with", "the people who *asked.*"], hc=[h0, h1], x="notifs", xc=[n0, n1, n2])
for k in (n0, n1, n2): fx("notify", k, 0.2)
fx("plink", n2, 0.18, 0.2)

# 2 Most go quiet (the notification ages)
h0, h1 = cue(2, 0), cue(2, 3)
t = [cue(2, 0, 0.1), cue(2, 2), cue(2, 4), cue(2, 6), cue(2, 7)]
slide(h0, eye="What happens next", gr="red", hl=["Most go *quiet*", "while you coach."], hc=[h0, h1], x="age", xc=t)
fx("pop", t[0], 0.22, 0.15)
for k in t[1:]: fx("tick", k, 0.2)

# 3 AI answers under 60 seconds, in your voice (60 second ring, reply)
h0, h1 = cue(3, 0), cue(3, 5)
x0, x1, x2, x3 = cue(3, 2), cue(3, 4), cue(3, 7), cue(3, 8)
slide(h0, eye="The answer", hl=["*AI* answers in", "under *60* *seconds.*"], hc=[h0, h1], x="chat", xc=[x0, x1, x2, x3])
fx("plink", h0, 0.2, 0.1); fx("pop", x0, 0.22, 0.3)
for i in range(7): SFX.append({"p": C[x1]["p"], "dt": round(C[x1]["dt"] + i * 0.12, 3), "name": "tick", "v": 0.14})
fx("send", x2, 0.35); fx("plink", x3, 0.22)

# 4 Three questions sort the serious buyers
h0, h1 = cue(4, 0), cue(4, 5)
x = [cue(4, 0, 0.1), cue(4, 1), cue(4, 2), cue(4, 4), cue(4, 6), cue(4, 7)]
slide(h0, eye="Better calls", hl=["Three questions sort", "the serious *buyers.*"], hc=[h0, h1], x="qual", xc=x)
fx("pop", x[0], 0.2)
for k in x[1:4]: fx("pop", k, 0.18); fx("plink", k, 0.2, 0.35)
fx("plink", x[4], 0.28); fx("notify", x[5], 0.28)

# 5 Reminders get them to show up
h0, h1 = cue(5, 0), cue(5, 5)
x = [cue(5, 0, 0.05), cue(5, 1), cue(5, 3), cue(5, 5)]
slide(h0, eye="Fewer no shows", hl=["Reminders get them", "to *show* *up.*"], hc=[h0, h1], x="cal", xc=x)
fx("pop", x[0], 0.22); fx("plink", x[0], 0.2, 0.35)
for k in x[1:]: fx("notify", k, 0.2)

# 6 Objection 1: robot? (question)
h0, h1 = cue(6, 0), cue(6, 3)
slide(h0, eye="Objection 1 of 3", hl=["Does it sound", "like a *robot?*"], hc=[h0, h1], x="typing", xc=[cue(6, 0, 0.1)])
fx("pulse", h0, 0.25, 0.1)

# 7 Answer: your voice, you approve
h0, h1 = cue(7, 0), cue(7, 4)
x = [cue(7, 0, 0.15), cue(7, 8), cue(7, 4), cue(7, 5)]
slide(h0, eye="The answer", hl=["No. It writes in", "*your* *voice.*"], hc=[h0, h1], x="appr", xc=x)
fx("pop", x[0], 0.22); fx("click", x[1], 0.3); fx("send", x[2], 0.3); fx("plink", x[3], 0.2)

# 8 Objection 2: follow up myself? (question)
h0, h1 = cue(8, 0), cue(8, 3)
x = [cue(8, 0, 0.1), cue(8, 2), endcue(8, -0.05)]
slide(h0, eye="Objection 2 of 3", hl=["Can't I just", "follow up *myself?*"], hc=[h0, h1], x="badge", xc=x)
fx("pop", x[0], 0.22, 0.2); fx("notify", x[1], 0.18)
for i in range(14): SFX.append({"p": C[x[0]]["p"], "dt": round(C[x[0]]["dt"] + 0.5 + i * 0.07 + i * i * 0.004, 3), "name": "tick", "v": 0.13})

# 9 Answer: not at 2 AM, 21 days (lock screen + 21 dots)
h0, h1 = cue(9, 2), cue(9, 5)
x = [cue(9, 0, 0.05), cue(9, 4), cue(9, 8), endcue(9, -0.05)]
slide(h0, eye="The answer", hl=["Not at two in", "the *morning.*"], hc=[h0, h1], x="lock", xc=x)
fx("sub", x[0], 0.25, 0.05); fx("notify", x[1], 0.25)
for i in range(21): SFX.append({"p": 9, "dt": round(C[x[2]]["dt"] + i / 21 * (C[x[3]]["dt"] - C[x[2]]["dt"]), 3), "name": "tick", "v": 0.12})

# 10 Objection 3: not ready? (question)
h0, h1 = cue(10, 0), cue(10, 3)
slide(h0, eye="Objection 3 of 3", hl=["What if they", "are *not* *ready?*"], hc=[h0, h1], x="notready", xc=[cue(10, 0, 0.1), cue(10, 4)])
fx("pulse", h0, 0.25, 0.1); fx("pop", len(C) - 1, 0.2)

# 11 Answer: content, then a check in
h0, h1 = cue(11, 4), cue(11, 10)
x = [cue(11, 2), cue(11, 6)]
slide(h0, eye="The answer", hl=["Your *content,*", "then a *check* *in.*"], hc=[h0, h1], x="route", xc=x)
fx("pop", x[0], 0.22); fx("pop", x[1], 0.22); fx("plink", x[1], 0.22, 0.35)

# 12 Outcome: more paying clients, calls worth taking
h0, h1 = cue(12, 0), cue(12, 3)
x = [cue(12, 0, 0.2), cue(12, 2)]
slide(h0, eye="What you get", hl=["More paying *clients.*", "Calls worth *taking.*"], hc=[h0, h1], x="report", xc=x)
fx("pop", x[0], 0.22); fx("whoosh", x[1], 0.18)
for i in range(4): fx("tick", x[1], 0.16, 0.1 + i * 0.18)

# 13 Cold calling chases (the red handset, struck)
h0, h1, e = cue(13, 0), cue(13, 2), endcue(13, -0.1)
slide(h0, gr="red", hl=["Cold calling", "*chases.*"], hc=[h0, h1], x="handset", xc=[h0, e])
fx("pulse", h0, 0.25, 0.1); fx("drop", e, 0.35); fx("snap", e, 0.25, 0.1)

# 14 DUXIO answers (violet flash, wordmark)
a, b = cue(14, 0), cue(14, 1)
slide(a, flash=True, plain=True, hl=[], hc=[], x="logo", xc=[a, b])
fx("stamp", a, 0.4, 0.05); fx("snap", b, 0.28)

# 15 Book a Strategy Call
h0, h1 = cue(15, 0), cue(15, 2)
x = [cue(15, 0, 0.3), endcue(15, -0.35)]
slide(h0, hl=["Book a", "*Strategy* *Call.*"], hc=[h0, h1], x="cta", xc=x)
fx("snap", h0, 0.22); fx("pop", x[0], 0.22); fx("click", x[1], 0.3); fx("send", x[1], 0.3, 0.1)

reel = {
    "id": "cold-call-ai-v2", "voice": {"script": "voice.vo.json"}, "music": {"track": "thugs", "seed": 7},
    "tail": 0.9, "hit": "hookhit", "capChunk": 4, "capClass": "apple", "vars": {"--hl": "#c9adff", "--fd": "'Inter'", "--fs": "'Instrument Serif'", "--grad": "linear-gradient(95deg,#8a3dff 0%,#b98cff 55%,#f1e8ff 100%)", "--gradr": "linear-gradient(95deg,#f1283a 0%,#ff8e6b 100%)"},
    "fonts": [{"family": "Inter", "file": "inter-variable.woff2", "weight": "100 900"}],
    "assets": ["brand/duxio/logo/svg/duxio-wordmark-white.svg"],
    "silence": {"from": {"p": 14, "dt": round(tm[14]["end"] - tm[14]["start"] + 0.02, 3)}, "to": {"p": 15, "dt": -0.04}},
    "beats": [{"at": 0, "scene": "ap", "bg": "dark", "props": {"slides": slides}, "cues": C, "sfx": SFX}],
}
json.dump(reel, open(os.path.join(H, "reel.json"), "w"), indent=1)
print("reel.json:", len(C), "cues,", len(SFX), "sfx,", len(slides), "slides")
