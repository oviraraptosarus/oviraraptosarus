import json,subprocess,re,os,html,random
R="/tmp/hf/vsl3/"; D=111.0
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
s=open("/tmp/claude-0/vslb/v3_template.html").read()
s=s.replace("__VO__",json.dumps(vo,separators=(",",":"))).replace("__PLAN__",json.dumps(pl,separators=(",",":")))
tags=[f'<audio id="vo_main" src="assets/vo/el_main.wav" data-start="{pl["offset"]}" data-duration="{pl["dur"]:.3f}" data-track-index="10" data-volume="1" data-audio-group="voiceover"></audio>']
tOpen=W("s1","dms")-.15; tTy0=W("s1","with"); tSend=W("s1","paragraphs")+.2
tRw=W("s6","rewind")+.05; tB=W("s6","pipeline")-.1; tLand=W("s6","maya")-.25; tO2=W("s6","messages")+.45
tEnd=W("s11","click")-.3; tF=ST["s10"]-.35
S=[("haptic",.28,.45),("ping",.32,.5)]
S+=[("switch2",tOpen,.25),("drop_003",tOpen+.35,.3),("click3",W("s1","dms")+.5,.25)]
for t0,dd in [(W("s1","client")-.1,.5),(W("s1","dinner")-.15,.6),(W("s1","ten")-.2,.7)]:
    for k in range(6): S.append(("ctick",t0+k*dd/6,.16))
S+=[("card-place-1",W("s1","client")-.1,.22),("card-place-2",W("s1","dinner")-.15,.22),("whoosh",W("s1","ten")-.05,.12)]
random.seed(3); t=tTy0
while t<tSend-.08:
    S.append((f"keypress-00{random.randint(1,8)}",t,.2)); t+=random.uniform(.07,.11)
S+=[("send",tSend,.5),("tick",W("s1","reads"),.35),("click_004",W("s1","never"),.35)]
S+=[("click3",W("s1","booked")-.25,.25),("click3",W("s1","booked")-.05,.25),("snap",W("s1","two",1)-.2,.4),("sub",W("s1","two",1)-.15,.45)]
S+=[("select_008",W("s2","harvard")-.1,.2),("select_008",W("s2","respond")-.1,.18),("sub",W("s2","seven")-.1,.5),("whoosh",W("s2","took")-.2,.14),("click3",W("s2","took")+.25,.25),("whoosh",W("s2","eight")-.05,.12)]
S+=[("whoosh",ST["s3"]-.25,.2),("card-place-2",W("s3","sell")-.05,.3),("whoosh",W("s3","silent")-.4,.12),("sub",W("s3","cost")-.06,.7)]
cd=END("s3")-W("s3","cost")-.05
S+=[("ctick",W("s3","cost")+k*.07,.13) for k in range(int(cd/.07*.7))]
S+=[("card-place-1",W("s4","buy")-.15,.28),("click_004",W("s4","isn't")-.05,.35),("whoosh",W("s4","problem",1)-.3,.12)]
S+=[("card-place-3",W("s4","memory")-.2,.3),("card-place-2",W("s4","instagram")-.2,.3),("snap",W("s4","inbox")-.05,.4)]
for k in range(9):
    if k%3==0: S.append((f"drop_00{1+(k//3)%3}",W("s4","inbox")-.05+.2+k*.42+.45,.12))
S+=[("whoosh",ST["s5"]-.25,.15),("card-place-1",W("s5","don't")-.2,.25),("click_004",W("s5","ads")-.05,.3),("card-place-2",W("s5","install")-.1,.3)]
S+=[("select_008",W("s5","five-stage")+i*.22,.14) for i in range(5)]
S+=[("ctick",W("s5","dropping")-.2+k*.14+.4,.15) for k in range(7)]
S+=[("rewind",tRw,.55),("whoosh",tB,.2),("haptic",tLand-.02,.45),("ping",tLand,.5),("card-place-1",tLand+.25,.3),("switch2",tO2,.22)]
cnt_d=W("s6","later")-W("s6","exactly")+.3
S+=[("ctick",W("s6","exactly")+k*cnt_d/10,.12) for k in range(10)]
S+=[("send",W("s6","reply")-.05,.35),("card-slide-1",W("s6","reply"),.3)]
S+=[("send",W("s7","answers")-.1,.25),("select_008",W("s7","qualifies")+.1,.22),("card-slide-2",W("s7","qualifies")+.25,.28),("send",W("s7","booking")-.2,.25),
    ("chime",W("s7","books")-.05,.42),("card-slide-1",W("s7","books")-.2,.28),("tick",W("s7","forty-eight-hour")-.1,.3),("card-slide-2",W("s7","shows")-.1,.28)]
S+=[("whoosh",W("s8","ninety-day")-.4,.14),("card-place-2",W("s8","ninety-day")-.1,.26)]+[("select_008",W("s8","checks")-.1+k*.2,.12) for k in range(3)]+[("card-slide-1",W("s8","schedule")-.1,.3)]
S+=[("click3",W("s9",w)-.15,.22) for w in ["write","build","maintain"]]+[("click_004",W("s9","account")-.05,.2)]
S+=[("join",W("s9","take")-.3,.42),("select_008",W("s9","pre-qualified")-.1,.2)]
S+=[("whoosh",tF,.22),("click3",W("s10","above")-.2,.25),("click3",W("s10","twenty")-.2,.25),("click_004",W("s10","pre-revenue")-.15,.3)]
S+=[("card-slide-1",ST["s11"]-.15,.3),("select_008",W("s11","thirty")-.05,.2)]+[("click3",W("s11",w)-.25,.22) for w in ["setup","leaks","straight"]]
S+=[("riser",tEnd-1.3,.32),("sub",tEnd+.05,.4),("impactGeneric_light_002",tEnd+.05,.3),("card-place-3",tEnd+.7,.3)]
for k,(f,t,v) in enumerate(S):
    ext="ogg" if os.path.exists(R+f"assets/sfx/{f}.ogg") else "wav"
    d=min(dur(f"assets/sfx/{f}.{ext}"),D-t-.01)
    tags.append(f'<audio id="sfx{k}" src="assets/sfx/{f}.{ext}" data-start="{max(0,t):.3f}" data-duration="{d:.3f}" data-track-index="{20+k}" data-volume="{v}" data-audio-group="sfx"></audio>')
q=lambda o: html.escape(json.dumps(o,separators=(",",":")),quote=True)
a0=0.4; pa=lambda t:round(t-a0,3)
tDark=W("s1","ten")-.1; tNever=W("s1","never")
A={"version":1,"lanes":[
 {"target":"volume","points":[{"t":0,"v":0},{"t":pa(1.6),"v":.8},{"t":pa(tNever-.1),"v":.8},{"t":pa(tNever+.1),"v":0},{"t":pa(ST["s2"]-.1),"v":0},{"t":pa(ST["s2"]+.7),"v":.8},
   {"t":pa(tRw),"v":.85},{"t":pa(tRw+.35),"v":0}]},
 {"target":"fx.lp.frequency","points":[{"t":0,"v":2400},{"t":pa(tOpen-.2),"v":2400},{"t":pa(tOpen+.4),"v":1100},{"t":pa(tDark),"v":1100},{"t":pa(tDark+.7),"v":650},
   {"t":pa(ST["s4"]),"v":650},{"t":pa(ST["s4"]+.8),"v":1300},{"t":pa(ST["s5"]+3),"v":2600,"curve":0.3},{"t":pa(tRw),"v":2600},{"t":pa(tRw+.35),"v":500}]}]}
achain={"version":1,"nodes":[{"type":"lowpass","id":"lp","label":"Mood filter","params":{"frequency":2400,"q":0.8,"poles":"2"}}]}
tags.append(f'<audio id="musicA" src="assets/music/musicA.mp3" data-start="{a0}" data-duration="{tRw+.5-a0:.3f}" data-track-index="5" data-volume="0.42" data-audio-group="music" data-fx-chain="{q(achain)}" data-automation="{q(A)}"></audio>')
b0=tLand; pb=lambda t:round(t-b0,3); bd=D-b0
B={"version":1,"lanes":[{"target":"volume","points":[{"t":0,"v":1},{"t":pb(tF),"v":1},{"t":pb(tF+.5),"v":.85},{"t":pb(tEnd-1.4),"v":.85},{"t":pb(tEnd+.1),"v":1.25},{"t":pb(D-1.5),"v":1.25},{"t":round(bd,3),"v":0}]}]}
tags.append(f'<audio id="musicB" src="assets/music/musicB.mp3" data-start="{b0:.3f}" data-duration="{bd:.3f}" data-track-index="6" data-volume="0.38" data-audio-group="music" data-automation="{q(B)}"></audio>')
vchain={"version":1,"nodes":[{"type":"highpass","id":"v1","label":"Remove Rumble","params":{"frequency":75,"q":0.707,"poles":"2"}},
 {"type":"compressor","id":"v3","label":"Even Out Loudness","params":{"threshold":-20,"ratio":3,"attack":8,"release":140,"makeup":3}},
 {"type":"peaking","id":"v4","label":"Presence","params":{"frequency":3200,"gain":1.5,"q":0.9}},
 {"type":"limiter","id":"v5","label":"Peak Ceiling","params":{"limit":-1}}]}
schain={"version":1,"nodes":[{"type":"highpass","id":"s1","params":{"frequency":90,"q":0.707,"poles":"2"}},{"type":"limiter","id":"s2","params":{"limit":-4}}]}
groups=f"""<hf-audio-group id="voiceover" data-label="Voiceover" data-volume="1" data-fx-chain="{q(vchain)}"></hf-audio-group>
<hf-audio-group id="sfx" data-label="SFX" data-volume="0.8" data-fx-chain="{q(schain)}"></hf-audio-group>"""
s=s.replace("<!--AUDIO-->","<!--AUDIO-->\n"+groups+"\n"+"\n".join(tags))
open(R+"index.html","w").write(s); print(len(tags),"audio tags;",len(S),"sfx; tLand",round(tLand,2),"tEnd",round(tEnd,2))
