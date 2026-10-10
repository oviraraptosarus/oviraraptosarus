import json,subprocess,re,os,html
R="/tmp/hf/vsl/"; D=117.0
def dur(f): return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",R+f]))
vo=json.load(open(R+"vo.json")); pl=json.load(open(R+"plan.json")); ST=pl["starts"]; SC=pl["scenes"]
def W(id,word,n=0):
    norm=lambda s:re.sub(r"[^\w$%'-]","",s.replace("’","'")).lower()
    c=0
    for w in vo[id]["words"]:
        if norm(w["w"])==norm(word):
            if c==n: return ST[id]+w["s"]
            c+=1
    return ST[id]
s=open("/tmp/claude-0/vsl_template.html").read()
s=s.replace("__VO__",json.dumps(vo,separators=(",",":"))).replace("__PLAN__",json.dumps(pl,separators=(",",":")))
tags=[]
for k,id in enumerate(ST):
    d=dur(f"assets/vo/{id}.wav")
    tags.append(f'<audio id="vo_{id}" src="assets/vo/{id}.wav" data-start="{ST[id]:.3f}" data-duration="{d:.3f}" data-track-index="{10+k%2}" data-volume="1" data-audio-group="voiceover"></audio>')
S=[]
for i,(a,b) in enumerate(SC[1:],1):
    S.append(("whoosh",max(0,a-.05),.22))
S+=[("drop_001",W("h2","losing")+.3,.3),("pop",W("p1","dm"),.35),("click_003",W("p2","reply"),.35),("drop_002",W("p2","moved"),.3),
("drop_001",W("p3","slip"),.3),("click2",W("p4","forget"),.3),("tick",W("p5","forty-five"),.3),("impactSoft_medium_001",W("p5","I"),.35),
("impactSoft_medium_001",W("t2","build")-.2,.3),("impactBell_heavy_000",W("t2","DUXIO")+.55,.3),
("card-place-1",W("m1","answer"),.3),("pop",W("m1","minute"),.3),("rollover2",W("m2","sort"),.3),("click2",W("m2","text"),.35),
("card-slide-1",W("m3","story"),.3),("card-slide-1",W("m3","result"),.3),("card-slide-1",W("m3","book"),.3),("tick",W("m3","reminders"),.3),
("pop",W("m4","every"),.3),("click_003",W("n1","three"),.3),("click_003",W("n1","eighty"),.3),("chips-stack-1",W("n2","one"),.35),
("impactBell_heavy_000",W("n3","about"),.3),("click2",W("o1","own"),.25),("impactSoft_medium_001",W("o2","three"),.35),
("pop",W("o3","exact"),.3),("click2",W("f1","reach"),.25),("click2",W("f1","sign"),.25),
("impactBell_heavy_000",SC[15][0]+.15,.35),("bong_001",W("c1","book"),.25)]
for k,(f,t,v) in enumerate(S):
    ext="ogg" if os.path.exists(R+f"assets/sfx/{f}.ogg") else "wav"
    d=min(dur(f"assets/sfx/{f}.{ext}"),D-t)
    tags.append(f'<audio id="sfx{k}" src="assets/sfx/{f}.{ext}" data-start="{t:.3f}" data-duration="{d:.3f}" data-track-index="{20+k}" data-volume="{v}" data-audio-group="sfx"></audio>')
q=lambda o: html.escape(json.dumps(o,separators=(",",":")),quote=True)
md=dur("assets/music/bed.mp3")
mauto={"version":1,"lanes":[{"target":"volume","points":[{"t":0,"v":0},{"t":1.2,"v":1},{"t":113.4,"v":1},{"t":114.2,"v":1.6},{"t":116.0,"v":1.6},{"t":117.0,"v":0}]}]}
tags.append(f'<audio id="music" src="assets/music/bed.mp3" data-start="0" data-duration="{D:.3f}" data-track-index="5" data-volume="0.26" data-audio-group="music" data-automation="{q(mauto)}"></audio>')
vchain={"version":1,"nodes":[{"type":"highpass","id":"v1","label":"Remove Rumble","params":{"frequency":80,"q":0.707,"poles":"2"}},
 {"type":"peaking","id":"v2","label":"Reduce Mud","params":{"frequency":250,"gain":-3,"q":1}},
 {"type":"compressor","id":"v3","label":"Even Out Loudness","params":{"threshold":-20,"ratio":3,"attack":10,"release":150,"makeup":3}},
 {"type":"peaking","id":"v4","label":"Add Clarity","params":{"frequency":3000,"gain":2.5,"q":1}},
 {"type":"limiter","id":"v5","label":"Peak Ceiling","params":{"limit":-1}}]}
schain={"version":1,"nodes":[{"type":"highpass","id":"s1","params":{"frequency":120,"q":0.707,"poles":"2"}},{"type":"limiter","id":"s2","params":{"limit":-3}}]}
groups=f"""<hf-audio-group id="voiceover" data-label="Voiceover" data-volume="1" data-fx-chain="{q(vchain)}"></hf-audio-group>
<hf-audio-group id="sfx" data-label="SFX" data-volume="0.8" data-fx-chain="{q(schain)}"></hf-audio-group>"""
s=s.replace("<!--AUDIO-->","<!--AUDIO-->\n"+groups+"\n"+"\n".join(tags))
open(R+"index.html","w").write(s); print(len(tags),"audio tags; music",md)
