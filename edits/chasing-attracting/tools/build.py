import json,subprocess,html,re,os
R="/tmp/hf/cut/"
words=json.load(open("/tmp/claude-0/ed/words_edit.json"))
def W(t,n=0):
    c=[w for w in words if re.sub(r"[^\w']","",w["w"]).lower()==t.lower()]; return round(c[n]["s"],3)
SPK=44.4; END=2.4; DUR=round(SPK+END,2)
B=dict(b1_in=.30,k1=W("Koenigsegg"),a1=W("afford",0),c2=W("chasing",1),k2=W("Pagani"),a2=W("afford",1),
 c3=W("chasing",2),k3=W("yacht"),a3=W("afford",2),c4=W("chasing",3),k4=W("mansion"),a4=W("afford",3),b1_out=9.35,
 b2_in=11.55,sick=W("sick"),antelope=W("antelope"),b2_out=13.15,
 b3_in=14.05,bmw1=W("BMW",0),always=W("always"),like=W("like"),sure=W("Sure"),b3_out=18.55,
 b4_in=19.8,attract=W("attract"),every=W("every"),park=W("park"),wouldnt=W("wouldn't"),bmw3=W("BMW",3),b4_out=23.55,
 b5_in=24.5,woman=W("woman"),dont=W("don't"),someone=W("someone"),only=W("only",1),b5_out=29.25,
 b6_in=30.35,fraction=W("fraction"),b6_out=33.2,b6b_in=35.4,attracting=W("attracting"),b6b_out=36.45,
 b7_in=37.45,two=W("two"),rabbits=W("rabbits"),canonly=W("only",2),one=W("one",1),b7_out=41.0,
 b8_in=42.3,destructive=W("destructive"),b8_out=44.4)
t=open("/tmp/claude-0/ed/template.html").read()
t=t.replace("__WORDS__",json.dumps([{"w":w["w"],"s":w["s"],"e":w["e"]} for w in words])).replace("__BEAT__",json.dumps(B)).replace("__DUR__",str(DUR)).replace("__SPK__",str(SPK))
def dur(f): return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",R+f]))
tags=[]
S=[]  # (file, time, vol)
def add(f,t,v): S.append((f,round(t,3),v))
for i,k in enumerate(["k1","k2","k3","k4"]):
    pass
ins=[B["b1_in"],B["c2"]-.06,B["c3"]-.06,B["c4"]-.06]; locks=[B["a1"]+.2,B["a2"]+.2,B["a3"]+.2,B["a4"]+.2]
for tt in ins: add("drop_001.ogg",tt+.02,.28)
for tt in locks: add("impactSoft_medium_001.ogg",tt,.5)
add("card-slide-1.ogg",B["b2_in"],.3); add("click_003.ogg",B["antelope"]+.0,.45); add("impactSoft_medium_001.ogg",B["antelope"]+.4,.35)
add("card-slide-1.ogg",B["b3_in"],.3); add("card-place-1.ogg",B["bmw1"],.45)
add("click2.ogg",B["always"]-.1,.35); add("click2.ogg",B["like"],.35); add("card-slide-3.ogg",B["sure"],.5); add("card-slide-3.ogg",B["sure"]+.12,.4)
add("card-slide-1.ogg",B["b4_in"],.3); add("dice-shake-1.ogg",B["attract"],.4)
for k in range(6): add("card-place-1.ogg",B["every"]-.1+k*.17,.22)
add("click_003.ogg",B["park"],.4); add("bong_001.ogg",B["wouldnt"]+.4,.4)
add("card-slide-1.ogg",B["b5_in"],.3); add("drop_002.ogg",B["woman"]-.1,.35); add("drop_002.ogg",B["someone"]-.1,.3); add("card-slide-3.ogg",B["only"]+.1,.4)
add("card-slide-1.ogg",B["b6_in"],.3); add("riser.wav",B["attracting"]-.5,.35); add("sparkle.wav",B["attracting"]+.55,.35)
add("card-slide-1.ogg",B["b7_in"],.3); add("pop.wav",B["two"]-.1,.35); add("pop.wav",B["two"]+.05,.35); add("click_003.ogg",B["canonly"]+.2,.4)
add("card-slide-1.ogg",B["b8_in"],.3); add("impactPlank_medium_000.ogg",B["destructive"]+.1,.55); add("glitch.wav",B["destructive"]+.25,.35)
add("impactBell_heavy_003.ogg",SPK+.15,.7); add("sparkle.wav",SPK+.3,.4)
for k,(f,tm,v) in enumerate(S):
    d=dur("assets/sfx/"+f)
    tags.append(f'<audio id="sfx{k}" src="assets/sfx/{f}" data-start="{tm}" data-duration="{min(d,DUR-tm):.3f}" data-track-index="{20+k}" data-volume="{v}" data-audio-group="sfx"></audio>')
q=lambda o: html.escape(json.dumps(o,separators=(",",":")),quote=True)
mchain={"version":1,"nodes":[{"type":"highpass","id":"mh","params":{"frequency":60,"q":0.707,"poles":"2"}}]}
mauto={"version":1,"lanes":[{"target":"volume","points":[{"t":0,"v":0.0},{"t":0.8,"v":0.85},{"t":SPK-0.2,"v":0.85},{"t":SPK+0.1,"v":1.0},{"t":DUR-0.4,"v":1.0},{"t":DUR,"v":0}]}]}
tags.append(f'<audio id="music" src="assets/music/bed.mp3" data-start="0" data-duration="{DUR}" data-track-index="5" data-volume="0.30" data-audio-group="music" data-fx-chain="{q(mchain)}" data-automation="{q(mauto)}"></audio>')
vchain={"version":1,"nodes":[{"type":"peaking","id":"v2","label":"Reduce Mud","params":{"frequency":250,"gain":-2.5,"q":1}},
 {"type":"peaking","id":"v4","label":"Add Clarity","params":{"frequency":3000,"gain":2,"q":1}},{"type":"limiter","id":"v5","label":"Peak Ceiling","params":{"limit":-1}}]}
schain={"version":1,"nodes":[{"type":"highpass","id":"s1","params":{"frequency":70,"q":0.707,"poles":"2"}},{"type":"limiter","id":"s2","params":{"limit":-3}}]}
groups=f"""<hf-audio-group id="voiceover" data-label="Voiceover" data-volume="1" data-fx-chain='{json.dumps(vchain)}'></hf-audio-group>
<hf-audio-group id="sfx" data-label="SFX" data-volume="0.7" data-fx-chain='{json.dumps(schain)}'></hf-audio-group>"""
t=t.replace("<!--AUDIO-->",groups+"\n"+"\n".join(tags))
open(R+"index.html","w").write(t)
print(len(tags),"audio tags; DUR",DUR)
print({k:v for k,v in B.items() if k in("k1","k2","k3","k4","sick","antelope","bmw1","sure","attract","wouldnt","woman","fraction","attracting","two","one","destructive")})
