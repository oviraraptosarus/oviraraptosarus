import json,subprocess,re,os,html,random
R="/tmp/hf/vsl2/"; D=117.0
def dur(f): return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",R+f]))
vo=json.load(open(R+"vo.json")); pl=json.load(open(R+"plan.json")); ST=pl["starts"]
END=lambda i:ST[i]+vo[i]["d"]
norm=lambda s:re.sub(r"[^\w$%'-]","",s.replace("’","'")).lower()
def W(i,word,n=0):
    c=0
    for w in vo[i]["words"]:
        if norm(w["w"])==norm(word):
            if c==n: return ST[i]+w["s"]
            c+=1
    raise SystemExit(f"no word {i} {word}")
s=open("/tmp/claude-0/vslb/v2_template.html").read()
s=s.replace("__VO__",json.dumps(vo,separators=(",",":"))).replace("__PLAN__",json.dumps(pl,separators=(",",":")))
tags=[]
for k,i in enumerate(pl["order"]):
    tags.append(f'<audio id="vo_{i}" src="assets/vo/t/{i}.wav" data-start="{ST[i]:.3f}" data-duration="{vo[i]["d"]:.3f}" data-track-index="{10+k%2}" data-volume="1" data-audio-group="voiceover"></audio>')
# ---- key times (mirror the JS) ----
tOpen=ST["b1"]+.35; tTy0=W("b5","with"); tSend=W("b5","paragraphs")+.15
tN=W("b6","nothing"); lt0=tN+.75; lstep=(ST["b7"]+.1-lt0)/3
tOut=ST["b10"]-.25; breakT=W("c2","don't")
tRw=W("d0","rewind")+.1; tLand=ST["d1"]-.62; tB=W("d1","lands")-.2; tO2=W("d1","this")-.05
tE=ST["e1"]-.35; tEnd=ST["e3"]-.15
S=[("haptic",.28,.45),("ping",.32,.5)]
S+=[("click3",W("a1","coaching")+.12,.3),("click3",W("a1","people")+.12,.3),("select_008",W("a1","two-minute")-.1,.15)]
S+=[("whoosh",ST["a2"]-.32,.18),("select_008",W("a4","system")-.15,.16),("select_008",W("a4","memory")-.25,.16),("mouseclick1",END("a4")-.02,.55)]
S+=[("whoosh",ST["b1"]-.27,.18),("switch2",tOpen,.25),("drop_003",W("b2","dms")-.05,.3),("click3",W("b3","lead")-.25,.25)]
for t0,dd in [(W("b4","client")-.1,.5),(W("b4","dinner")-.15,.6),(W("b5","ten")-.2,.7)]:
    for k in range(6): S.append(("ctick",t0+k*dd/6,.16))
S+=[("card-place-1",W("b4","client")-.1,.22),("card-place-2",W("b4","dinner")-.15,.22),("whoosh",W("b5","ten")-.05,.12)]
random.seed(3); t=tTy0
while t<tSend-.08:
    S.append((f"keypress-00{random.randint(1,8)}",t,.2)); t+=random.uniform(.07,.11)
S+=[("send",tSend,.5)]
S+=[("tick",lt0+k*lstep,.4) for k in range(4)]
S+=[("card-place-3",W("b8","book")-.15,.25),("click_004",W("b8","never"),.35),("haptic",ST["b9"]-.17,.4),("ping",ST["b9"]-.15,.42)]
S+=[("whoosh",tOut,.22),("card-place-2",ST["b10"]+.05,.3),("whoosh",W("b10","silence")-.35,.12),("sub",W("b10","cost")-.06,.75)]
cd=END("b10")-W("b10","cost")-.05
S+=[("ctick",W("b10","cost")+k*.07,.13) for k in range(int(cd/.07*.7))]
S+=[("whoosh",ST["c1"]-.35,.15),("click3",W("c1","fine")-.05,.3),("click3",W("c1","fine",1)-.05,.3),("whoosh",W("c2","leak")-.15,.15)]
S+=[("card-place-1",W("c2","memory")-.15,.28)]
for tt in [W("c2","spreadsheet")-.1,W("c2","pile"),W("c2","pile")+.12,W("c2","tools"),W("c2","tools")+.12,W("c2","tools")+.24,W("c2","tools")+.36]: S.append(("select_008",tt,.12))
S+=[("snap",breakT+i*.07,.32) for i in range(7)]
# drops: sample of the falling dots
def dots(t0,t1,ev):
    out=[];t=t0
    while t<t1: out.append(t); t+=ev
    return out
dl=dots(breakT+.4,ST["c3"],.32)+dots(ST["c3"],W("c3","lose")+.2,.13)+dots(W("c3","lose")+.2,END("c3")+.25,.07)
for k,tt in enumerate(dl):
    if k%3==0: S.append((f"drop_00{1+k%2}",tt+.47,.1))
S+=[("rewind",tRw,.55),("haptic",tLand-.02,.45),("ping",tLand,.5)]
S+=[("whoosh",tB,.2),("card-place-1",W("d1","lands")+.15,.32),("select_008",W("d1","accounts")-.05,.18),("switch2",tO2,.22)]
cnt_d=W("d2","seconds")-W("d2","reply")+.1
S+=[("ctick",W("d2","reply")+k*cnt_d/10,.12) for k in range(10)]
S+=[("card-slide-1",W("d2","reply"),.3),("send",W("d2","forty-one")-.1,.35)]
S+=[("whoosh",ST["d2b"]-.15,.13),("click_004",W("d2b","later")-.1,.3)]
S+=[("send",W("d3","questions")-.2,.25),("drop_003",W("d3","serious")-.35,.25),("select_008",W("d3","buyer")-.05,.22),("card-slide-2",W("d3","buyer")+.15,.28),
    ("card-place-3",ST["d3"]+.4,.2),("card-slide-1",W("d3","sorted")-.1,.25)]
S+=[("card-slide-2",W("d4","follow-up")-.1,.3)]+[("send",W("d4",w)-.25,.22) for w in ["story","result","invite"]]
S+=[("chime",W("d5","books")+.05,.42)]+[("tick",W("d5","reminders")+.05+i*.22,.28) for i in range(3)]
S+=[("whoosh",W("d6","check-in")-.4,.12)]+[("select_008",W("d6","check-in")-.3+k*.15,.1) for k in range(4)]+[("card-slide-1",W("d6","month")-.15,.3)]
S+=[("join",W("d7","call")-.25,.42)]+[("click3",W("d7",w)-.15,.22) for w in ["learn","write","build","run"]]
S+=[("whoosh",tE,.22),("click3",W("e1","offer")-.2,.25),("click3",W("e1","leads")-.15,.25),("card-slide-1",W("e1","request")-.25,.3),("click3",W("e1b","starting")-.2,.2)]
S+=[("ctick",W("e2","map")+i*.12,.15) for i in range(5)]+[("click_004",W("e2","quiet")-.15,.3),("select_008",W("e2","fix")-.15,.2)]
S+=[("riser",tEnd-1.35,.32),("sub",tEnd+.05,.4),("impactGeneric_light_002",tEnd+.05,.3)]
for k,(f,t,v) in enumerate(S):
    ext="ogg" if os.path.exists(R+f"assets/sfx/{f}.ogg") else "wav"
    d=min(dur(f"assets/sfx/{f}.{ext}"),D-t-.01)
    tags.append(f'<audio id="sfx{k}" src="assets/sfx/{f}.{ext}" data-start="{t:.3f}" data-duration="{d:.3f}" data-track-index="{20+k}" data-volume="{v}" data-audio-group="sfx"></audio>')
q=lambda o: html.escape(json.dumps(o,separators=(",",":")),quote=True)
# music A: dark, filtered; cut to silence on "nothing"; back for the no-show; out on the rewind
a0=0.6
pa=lambda t:round(t-a0,3)
A={"version":1,"lanes":[
 {"target":"volume","points":[{"t":0,"v":0},{"t":pa(1.4),"v":.8},{"t":pa(ST["b1"]),"v":.8},{"t":pa(tN-.12),"v":.8},{"t":pa(tN-.02),"v":0},{"t":pa(ST["b8"]-.2),"v":0},{"t":pa(ST["b8"]+.8),"v":.75},
   {"t":pa(ST["c3"]),"v":.85},{"t":pa(tRw+.05),"v":.85},{"t":pa(tRw+.35),"v":0}]},
 {"target":"fx.lp.frequency","points":[{"t":0,"v":2400},{"t":pa(ST["b1"]-.3),"v":2400},{"t":pa(ST["b1"]+.4),"v":1100},{"t":pa(tDark:=W("b5","ten")-.05),"v":1100},{"t":pa(tDark+.7),"v":650},
   {"t":pa(ST["c1"]-.4),"v":650},{"t":pa(ST["c1"]+.4),"v":1300},{"t":pa(ST["c3"]),"v":1300},{"t":pa(END("c3")),"v":2600,"curve":0.3},{"t":pa(tRw),"v":2600},{"t":pa(tRw+.35),"v":500}]}]}
achain={"version":1,"nodes":[{"type":"lowpass","id":"lp","label":"Mood filter","params":{"frequency":2400,"q":0.8,"poles":"2"}}]}
tags.append(f'<audio id="musicA" src="assets/music/musicA.mp3" data-start="{a0}" data-duration="{tRw+.5-a0:.3f}" data-track-index="5" data-volume="0.42" data-audio-group="music" data-fx-chain="{q(achain)}" data-automation="{q(A)}"></audio>')
# music B: bright, lands on the downbeat with the notification after the rewind
b0=tLand; pb=lambda t:round(t-b0,3); bd=D-b0
B={"version":1,"lanes":[{"target":"volume","points":[{"t":0,"v":1},{"t":pb(ST["e1"]-.4),"v":1},{"t":pb(ST["e1"]),"v":.8},{"t":pb(tEnd-1.4),"v":.8},{"t":pb(tEnd+.1),"v":1.25},{"t":pb(115.4),"v":1.25},{"t":round(bd,3),"v":0}]}]}
tags.append(f'<audio id="musicB" src="assets/music/musicB.mp3" data-start="{b0:.3f}" data-duration="{bd:.3f}" data-track-index="6" data-volume="0.38" data-audio-group="music" data-automation="{q(B)}"></audio>')
vchain={"version":1,"nodes":[{"type":"highpass","id":"v1","label":"Remove Rumble","params":{"frequency":75,"q":0.707,"poles":"2"}},
 {"type":"peaking","id":"v2","label":"Reduce Mud","params":{"frequency":260,"gain":-2.5,"q":1}},
 {"type":"compressor","id":"v3","label":"Even Out Loudness","params":{"threshold":-20,"ratio":3,"attack":8,"release":140,"makeup":3}},
 {"type":"peaking","id":"v4","label":"Presence","params":{"frequency":3200,"gain":2.5,"q":0.9}},
 {"type":"highshelf","id":"v6","label":"Air","params":{"frequency":9000,"gain":1.5}},
 {"type":"limiter","id":"v5","label":"Peak Ceiling","params":{"limit":-1}}]}
schain={"version":1,"nodes":[{"type":"highpass","id":"s1","params":{"frequency":90,"q":0.707,"poles":"2"}},{"type":"limiter","id":"s2","params":{"limit":-4}}]}
groups=f"""<hf-audio-group id="voiceover" data-label="Voiceover" data-volume="1" data-fx-chain="{q(vchain)}"></hf-audio-group>
<hf-audio-group id="sfx" data-label="SFX" data-volume="0.85" data-fx-chain="{q(schain)}"></hf-audio-group>"""
s=s.replace("<!--AUDIO-->","<!--AUDIO-->\n"+groups+"\n"+"\n".join(tags))
open(R+"index.html","w").write(s); print(len(tags),"audio tags", len(S),"sfx")
