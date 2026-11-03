import json,subprocess,re,os,html,random
R="/tmp/hf/ig/"; D=59.0
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
s=open("/tmp/claude-0/reel/reel_template.html").read()
s=s.replace("__VO__",json.dumps(vo,separators=(",",":"))).replace("__PLAN__",json.dumps(pl,separators=(",",":")))
tags=[]
for k,i in enumerate(pl["order"]):
    tags.append(f'<audio id="vo_{i}" src="assets/vo/t/{i}.wav" data-start="{ST[i]:.3f}" data-duration="{vo[i]["d"]:.3f}" data-track-index="{10+k%2}" data-volume="1" data-audio-group="voiceover"></audio>')
# ---- key times (mirror the JS) ----
tH2=ST["h2"]-.04; tLose=W("h2","lose")
t7=W("s1","seven"); tS2=ST["s2"]-.15
tGap=W("t1","gap"); tClose=W("t1","closes"); tMeet=tClose+.22; tLogo=tMeet+.32; tUp=ST["m1"]+.55
tR0=W("m2","reply")-.1; tR1=W("m2","minute")+.2
tS6=ST["m4"]-.2; tS7=ST["m6"]-.15; tS8=ST["m7"]-.15
tk0=W("m7","check-in")-.2; tk1=W("m7","days")+.25
tS9=ST["e1"]-.12; tS10=ST["c1"]-.2; tL=ST["c2"]+.3
S=[("haptic",.0,.5),("ping",.02,.55)]
S+=[("ctick",tH2+p*(tLose-tH2+.05),.35) for p in (.25,.45,.62,.78)]
S+=[("whoosh",tLose+.1,.22)]
# stat
S+=[("click3",W("s1","harvard")-.05,.3),("card-slide-1",W("s1","leads")-.1,.2),("card-place-1",W("s1","contacted"),.3),
    ("card-place-2",W("s1","within")-.05,.3),("select_008",W("s1","hour")-.12,.2),("sub",t7-.04,.7),("impactGeneric_light_002",t7-.04,.35)]
S+=[("ctick",t7-.05+k*.1,.22) for k in range(7)]
S+=[("click3",W("s1","likely")-.1,.25)]
# night
S+=[("whoosh",tS2-.22,.2),("drop_003",tS2+.1,.3),("card-slide-2",W("s2","that")-.1,.22),("drop_002",W("s2","night")+.05,.32)]
S+=[("card-place-3",W("s3","booked"),.32),("click_004",W("s3","else"),.4)]
S+=[("snap",W("s4","better")+.3,.32),("whoosh",W("s4","faster")-.05,.14)]
S+=[("card-slide-1",tGap-.05,.22),("riser",tClose-1.25,.3),("whoosh",tClose-.12,.2),("whoosh",tLogo-.1,.25),
    ("sub",tLogo+.02,.85),("impactGeneric_light_002",tLogo+.02,.45),("card-slide-2",tLogo+.28,.25)]
# build
S+=[("whoosh",tUp,.2),("card-slide-1",tUp+.3,.25)]+[("click3",tUp+.45+i*.13,.18) for i in range(5)]
S+=[("switch2",W("m1","inside")+i*.09,.2) for i in range(5)]+[("select_008",W("m1","own")-.05,.25)]
S+=[("tick",ST["m2"]-.3,.3)]
# reply
S+=[("select_008",ST["m2"],.18)]
n=int((tR1-tR0)/.12)
S+=[("ctick",tR0+k*.12,.16) for k in range(n)]+[("send",tR1-.05,.35)]
S+=[("drop_001",ST["m3"]-.1,.3),("send",W("m3","voice")-.1,.3),("card-place-1",W("m3","approved")-.25,.22),("switch2",W("m3","approved")+.15,.35),("haptic",W("m3","approved")+.15,.25)]
# qualify
S+=[("select_008",ST["m4"],.18)]+[("click3",tS6+.1+i*.08,.12) for i in range(0,9,2)]
S+=[(f"card-place-{1+i}",W("m4","questions")-.2+i*.15,.22) for i in range(3)]
S+=[("snap",W("m4","sort"),.22),("ping",W("m4","serious"),.22)]
S+=[("haptic",W("m5","text")-.15,.5),("ping",W("m5","text")-.12,.4)]
# book
S+=[("card-slide-1",tS7,.25),("select_008",W("m6","book")-.05,.18),("chime",W("m6","book")+.05,.42)]
S+=[("tick",W("m6",w)-.1,.32) for w in ("twenty-four","two","ten")]+[("select_008",W("m6","reminders"),.16)]
# quiet + report
S+=[("select_008",ST["m7"],.16)]
S+=[("drop_002",tk0+(tk1-tk0)*d/90-.05,.3) for d in (30,60,90)]
S+=[("card-slide-2",ST["m8"]-.1,.3)]+[("ctick",W("m8","report")-.25+i*.08,.18) for i in range(5)]
# easy
S+=[("whoosh",ST["e1"]-.38,.18)]+[("click3",tS9+.05+i*.08,.12) for i in range(0,6,2)]
S+=[("snap",W("e1","software")+.05,.4),("whoosh",W("e1","about")-.35,.18)]
S+=[("ctick",W("e1","thirty")-.05+k*.1,.16) for k in range(8)]
S+=[("card-slide-1",ST["e2"]-.12,.25),("join",W("e2","show")+.05,.45)]
# cta
S+=[("whoosh",tS10-.05,.2),("card-place-2",W("c1","book")-.2,.3),("mouseclick1",W("c1","call")-.08,.55),("haptic",W("c1","call")-.06,.3),("click3",W("c1","link")-.12,.3)]
# loop back to the hook frame
S+=[("whoosh",tL,.2),("haptic",W("c2","dms")-.25,.45),("ping",W("c2","dms")-.22,.5)]
for k,(f,t,v) in enumerate(S):
    ext="ogg" if os.path.exists(R+f"assets/sfx/{f}.ogg") else "wav"
    t=max(0,t); d=min(dur(f"assets/sfx/{f}.{ext}"),D-t-.01)
    tags.append(f'<audio id="sfx{k}" src="assets/sfx/{f}.{ext}" data-start="{t:.3f}" data-duration="{d:.3f}" data-track-index="{20+k}" data-volume="{v}" data-audio-group="sfx"></audio>')
q=lambda o: html.escape(json.dumps(o,separators=(",",":")),quote=True)
# music: full from frame 0; filtered and lower for the night scene; a dropout before "closes"; hit on the logo
M={"version":1,"lanes":[
 {"target":"volume","points":[{"t":0,"v":1},{"t":tS2-.3,"v":1},{"t":tS2+.3,"v":.8},{"t":tClose-.35,"v":.8},{"t":tClose-.1,"v":0},{"t":tLogo-.02,"v":0},{"t":tLogo+.02,"v":1.1},
   {"t":tUp+1.5,"v":1},{"t":D-.6,"v":1},{"t":D,"v":.0}]},
 {"target":"fx.lp.frequency","points":[{"t":0,"v":16000},{"t":tS2-.3,"v":16000},{"t":tS2+.4,"v":900},{"t":tClose-.2,"v":900},{"t":tLogo,"v":16000}]}]}
mchain={"version":1,"nodes":[{"type":"lowpass","id":"lp","label":"Night filter","params":{"frequency":16000,"q":0.7,"poles":"2"}}]}
tags.append(f'<audio id="music" src="assets/music/bed.mp3" data-start="0" data-duration="{D:.3f}" data-track-index="5" data-volume="0.34" data-audio-group="music" data-fx-chain="{q(mchain)}" data-automation="{q(M)}"></audio>')
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
