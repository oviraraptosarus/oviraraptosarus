"""Builds reel.json for cold-call-ai from the real voice timings (run after the voice exists).
Word cues are placed by the same length weighting the caption engine uses, so a new voice retimes everything."""
import json, os
H = os.path.dirname(os.path.abspath(__file__))
tm = json.load(open(os.path.join(H, "vo", "voice.timings.json")))["phrases"]
words = [s["t"].split() for s in json.load(open(os.path.join(H, "voice.vo.json")))["phrases"]]
wt = lambda w: len(w) + 1.5
C, SFX = [], []

def dt(p, wi, off=0):
    ws = words[p]; tot = sum(wt(w) for w in ws); d = tm[p]["end"] - tm[p]["start"]
    return round(sum(wt(w) for w in ws[:wi]) / tot * d + off, 3)

def cue(p, wi=0, off=0):
    C.append({"p": p, "dt": dt(p, wi, off)}); return len(C) - 1

def endcue(p, off=0):
    C.append({"p": p, "dt": round(tm[p]["end"] - tm[p]["start"] + off, 3)}); return len(C) - 1

def fx(name, k, v=None, off=0):
    SFX.append({"p": C[k]["p"], "dt": round(C[k]["dt"] + off, 3), "name": name, **({"v": v} if v else {})})

GRAY, VIO, RED = "#9A9AA5", "#B794FF", "#F1283A"
slides = []

# 0 Stop calling strangers
a, b, c, d = cue(0, 0), cue(0, 1), cue(0, 2), endcue(0, -0.12)
slides.append(dict(c0=a, ghost="COLD", gs=1000, top=540, acc=RED, x="phone", xc=[a, d], lines=[
    dict(t="STOP", size=380, c=a, slam=True), dict(t="CALLING", size=196, c=b), dict(t="STRANGERS.", size=148, c=c, strike=d)]))
fx("ping", a, 0.25); fx("snap", a, 0.3); fx("tap", b); fx("snap", c, 0.3); fx("drop", d, 0.4); fx("snap", d, 0.3, 0.02)

# 1 They never asked
a, b, c = cue(1, 0), cue(1, 1), cue(1, 2)
slides.append(dict(c0=a, ghost="ASKED", gs=1000, top=400, acc=RED, lines=[
    dict(t="THEY", size=340, c=a, slam=True), dict(t="*never*", size=320, c=b), dict(t="ASKED.", size=245, c=c)]))
fx("whoosh", a, 0.22, -0.06); fx("snap", a, 0.3); fx("plink", b, 0.22); fx("snap", c, 0.3)

# 2 The people who did are in your inbox
a, b, c, p1, p2, p3 = cue(2, 1), cue(2, 2), cue(2, 3), cue(2, 5), cue(2, 7), cue(2, 8)
slides.append(dict(c0=a, ghost="INBOX", gs=1000, top=220, x="inbox", xc=[p1, p2, p3], pills=["New Instagram DM", "New form", "New email"], pillTop=1010, lines=[
    dict(t="THOSE", size=230, c=a), dict(t="WHO", size=230, c=b), dict(t="*did.*", size=300, c=c)]))
fx("whoosh", a, 0.22, -0.06); fx("tap", a); fx("tap", b); fx("plink", c, 0.25)
for k in (p1, p2, p3): fx("notify", k, 0.18)

# 3 AI answers them in under sixty seconds
a, b, c, d, e, f = cue(3, 0), cue(3, 4), cue(3, 5), cue(3, 6), cue(3, 4), endcue(3, 0.0)
slides.append(dict(c0=a, ghost="60", gs=1700, top=240, acc=VIO, x="bar", xc=[e, f], lines=[
    dict(t="*AI* ANSWERS", size=150, c=a), dict(t="UNDER", size=100, c=b, color=GRAY), dict(t="60", size=620, c=c, slam=True), dict(t="SECONDS", size=190, c=d)]))
fx("whoosh", a, 0.22, -0.06); fx("snap", a, 0.3); fx("tap", b); fx("stamp", c, 0.4); fx("snap", d, 0.25)
t = 0.0
while t < tm[3]["end"] - tm[3]["start"] - dt(3, 4) - 0.1:
    SFX.append({"p": 3, "dt": round(dt(3, 4) + t, 3), "name": "tick", "v": 0.16}); t += 0.11
fx("send", f, 0.35, 0.02)

# 4 Objection 1: robot
a, b = cue(4, 0), cue(4, 5)
slides.append(dict(c0=a, ghost="?", gs=1700, top=600, eyebrow="Objection 1 of 3", lines=[
    dict(t="Will it sound like a", size=104, c=a, lc=True, color=GRAY), dict(t="ROBOT?", size=240, c=b, outline=True)]))
fx("whoosh", a, 0.22, -0.06); fx("plink", a, 0.22); fx("glitch", b, 0.22)

# 5 Answer: your voice
a, b, c = cue(5, 0), cue(5, 4), cue(5, 5)
slides.append(dict(c0=a, ghost="NO", gs=1300, top=220, eyebrow="The answer", acc=VIO, lines=[
    dict(t="NO.", size=480, c=a, slam=True), dict(t="YOUR", size=230, c=b), dict(t="*voice.*", size=300, c=c)]))
fx("whoosh", a, 0.22, -0.06); fx("stamp", a, 0.45); fx("snap", b, 0.3); fx("plink", c, 0.25)

# 6 Objection 2: I follow up myself
a, b = cue(6, 0), cue(6, 4)
slides.append(dict(c0=a, ghost="ME", gs=1500, top=600, eyebrow="Objection 2 of 3", lines=[
    dict(t="I already follow up", size=100, c=a, lc=True, color=GRAY), dict(t="MYSELF.", size=215, c=b, outline=True)]))
fx("whoosh", a, 0.22, -0.06); fx("plink", a, 0.22); fx("glitch", b, 0.22)

# 7 Answer: 2 AM, 21 days
a, b, c = cue(7, 3), cue(7, 9), cue(7, 11)
slides.append(dict(c0=a, ghost="DAYS", gs=1100, top=200, eyebrow="The answer", acc=VIO, lines=[
    dict(t="2 AM.", size=320, c=a, slam=True), dict(t="21", size=460, c=b, slam=True, color=VIO), dict(t="DAYS.", size=230, c=c)]))
fx("whoosh", a, 0.22, -0.06); fx("snap", a, 0.3); fx("snap", b, 0.35); fx("tap", c, 0.3)

# 8 Objection 3: not ready
a, b, c = cue(8, 0), cue(8, 4), cue(8, 5)
slides.append(dict(c0=a, ghost="READY", gs=1000, top=420, eyebrow="Objection 3 of 3", lines=[
    dict(t="What if they are", size=100, c=a, lc=True, color=GRAY), dict(t="NOT", size=420, c=b, outline=True), dict(t="READY?", size=250, c=c, outline=True)]))
fx("whoosh", a, 0.22, -0.06); fx("plink", a, 0.22); fx("glitch", b, 0.22); fx("glitch", c, 0.2)

# 9 Answer: content, monthly check in
l1, a, b, l2, c, d = cue(9, 2), cue(9, 4), cue(9, 5), cue(9, 6), cue(9, 12), cue(9, 13)
slides.append(dict(c0=l1, ghost="MONTH", gs=1000, top=250, eyebrow="The answer", acc=VIO, lines=[
    dict(t="NOT READY", size=60, c=l1, color=GRAY), dict(t="YOUR", size=230, c=a), dict(t="CONTENT.", size=170, c=b),
    dict(t="QUIET LEADS", size=60, c=l2, color=GRAY, gap=30), dict(t="EVERY", size=240, c=c), dict(t="*month.*", size=270, c=d)]))
fx("whoosh", l1, 0.22, -0.06); fx("tap", l1); fx("snap", a, 0.3); fx("tap", b); fx("tap", l2); fx("snap", c, 0.3); fx("plink", d, 0.25)

# 10 Cold calling chases. DUXIO answers.
a, b, s, c, lg = cue(10, 0), cue(10, 2), endcue(10, -0.1), cue(11, 0), cue(11, 0, 0.1)
slides.append(dict(c0=a, ghost="ANSWER", gs=900, top=420, acc=VIO, x="logo", xc=[lg], logo="assets/duxio-wordmark-white.svg", logoTop=1010, lines=[
    dict(t="COLD CALLING", size=96, c=a, color=GRAY), dict(t="CHASING", size=215, c=b, strike=s), dict(t="ANSWERING", size=156, c=c, color=VIO, gap=40)]))
fx("whoosh", a, 0.22, -0.06); fx("tap", a); fx("snap", b, 0.3); fx("drop", s, 0.35); fx("stamp", c, 0.35); fx("pluck", lg, 0.3)

# 11 Book a Strategy Call
a, b, c = cue(12, 0), cue(12, 2), cue(12, 3)
slides.append(dict(c0=a, ghost="CALL", gs=1100, top=560, acc=VIO, x="cta", xc=[a], lines=[
    dict(t="BOOK A", size=240, c=a, slam=True), dict(t="STRATEGY", size=188, c=b), dict(t="CALL.", size=290, c=c, slam=True, color=VIO)]))
fx("whoosh", a, 0.22, -0.06); fx("snap", a, 0.3); fx("tap", b); fx("stamp", c, 0.5); fx("send", a, 0.3, 0.12); fx("pulse", c, 0.3, 0.2)

reel = {
    "id": "cold-call-ai", "voice": {"script": "voice.vo.json"}, "music": {"track": "thugs", "seed": 7},
    "tail": 0.8, "hit": "hookhit", "capChunk": 3, "vars": {"--hl": "#B794FF"},
    "assets": ["brand/duxio/logo/svg/duxio-wordmark-white.svg"],
    "silence": {"from": {"p": 11, "dt": round(tm[11]["end"] - tm[11]["start"] + 0.02, 3)}, "to": {"p": 12, "dt": -0.04}},
    "beats": [{"at": 0, "scene": "slab", "bg": "dark", "props": {"slides": slides}, "cues": C, "sfx": SFX}],
}
json.dump(reel, open(os.path.join(H, "reel.json"), "w"), indent=1)
print("reel.json:", len(C), "cues,", len(SFX), "sfx")
