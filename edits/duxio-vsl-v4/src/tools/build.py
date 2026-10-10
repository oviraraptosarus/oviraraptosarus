import json,subprocess,re,os,html,math
R="/tmp/hf/v4/"; OFF=0.3; D=161.0
words=json.load(open(R+"words.json"))
norm=lambda s:re.sub(r"[^\w$%'-]","",s.replace("’","'")).lower()
def A(word,after):
    for w in words:
        if w["s"]>=after-0.05 and norm(w["w"])==norm(word): return round(w["s"]+OFF,3)
    raise SystemExit(f"no word {word} after {after}")
T=dict(
 notif=0.45, s2=A("someone",4.9), call=A("client",5), asleep=A("asleep",5),
 h3=A("three",8.5), gone=A("already",11), zoom=A("or",15), z45=A("45",15), end=A("end",15), fit=A("fit",20),
 post=A("post",22), ads=A("ads",22), spend=A("spend",22), glued=A("glued",22), old=A("old",31), employee=A("full-time",31),
 need=A("you",37.4), stop=A("stop",39.5), already=A("already",39.5),
 how=A("here",43), duxio=A("duxio",43), four=A("four",43),
 st1=A("step",47), reply=A("reply",49), sixty=A("60",49), spam=A("this",53.4), natural=A("natural",55), voice=A("voice",55), heard=A("heard",55),
 st2=A("step",62.5), three=A("three",64), questions=A("questions",64), situation=A("situation",64), goals=A("goals",64),
 notfit=A("people",71), directed=A("directed",71), serious=A("serious",74), pick=A("pick",74),
 st3=A("step",77), most=A("most",79.5), weeks=A("three",82), checkins=A("check",82), stories=A("stories",82), warm=A("warm",82),
 once=A("once",89), reminders=A("reminders",89), showup=A("show",89), business=A("business",89),
 st4=A("step",94.5), month=A("once",96.5), checkin=A("check-in",96.5), restarts=A("restarts",96.5), ready=A("ready",96.5),
 math=A("think",105), n80=A("80",107), rescues=A("rescues",107), thousands=A("thousands",107), profit=A("profit",107),
 noads=A("you",118.5), typing=A("typing",118.5),
 fit0=A("this",125), active=A("active",129), reach=A("reaching",129), capture=A("capture",129),
 below=A("below",137.5), fill=A("fill",140.5), strategy=A("strategy",141.5), inspect=A("inspect",145), leaking=A("leaking",145), runs=A("runs",145),
 endc=A("fill",152.5), talk=A("talk.",152.5), D=D, OFF=OFF)
json.dump(T,open(R+"T.json","w"),indent=0)
def dur(f): return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",R+f]))
s=open("/tmp/claude-0/v4/template.html").read()
parts=open(R+"assets/img/parts-white.svg").read().strip()
parts=re.sub(r'id="([a-z-]+)"',r'id="lg-\1"',parts).replace('<svg ','<svg id="lgsvg" ',1)
s=s.replace("<!--LOGO-->",parts)
s=s.replace("__T__",json.dumps(T)).replace("__W__",json.dumps([{"w":w["w"],"s":round(w["s"]+OFF,3)} for w in words],separators=(",",":")))
tags=[f'<audio id="vo" src="assets/vo/vo.wav" data-start="{OFF}" data-duration="{dur("assets/vo/vo.wav"):.3f}" data-track-index="10" data-volume="1" data-audio-group="voiceover"></audio>']
# ---- reel tick helper (power3.out deceleration) ----
def reel_ticks(t,d,n=12,v=.32):
    return [("rtick",t+d*(1-(1-k/n)**(1/3)),v) for k in range(n)]+[("land",t+d,.55)]
S=[]
S+=[("haptic",T["notif"]-.02,.5),("ping",T["notif"],.42)]
S+=[("swish",T["s2"]-.15,.25),("select_008",T["call"],.18),("select_008",T["asleep"],.18)]
S+=reel_ticks(T["h3"]-.05,1.5)
S+=[("thud",T["gone"]-.03,.6)]
S+=[("gwhoosh",T["zoom"]-.25,.4)]+reel_ticks(T["z45"]-.2,1.8,14,.28)
S+=[("thud",T["fit"]-.02,.65),("land",T["fit"]-.02,.4)]
S+=[("card-slide-1",T["post"]-.12,.3),("lad1",T["post"]-.05,.18),("card-slide-2",T["ads"]-.12,.3),("lad2",T["ads"]-.05,.18),("card-slide-1",T["spend"]-.05,.3),("lad3",T["spend"]+.02,.18)]
S+=[("gwhoosh",T["old"]-.3,.35)]+[("rtick",T["old"]+.1+k*.11,.25) for k in range(10)]
S+=[("keypress-00%d"%(1+k%4),T["old"]+.4+k*.13,.1) for k in range(14)]
S+=[("switch2",T["employee"],.35)]
S+=[("thud",T["need"]-.05,.35),("swish",T["stop"]-.1,.3),("confirm",T["stop"]+1.4,.4)]
S+=[("vriser",T["duxio"]-1.1,.3),("bighit",T["duxio"]+.1,.45)]+[(f"lad{i+1}",T["four"]+.35+i*.14,.22) for i in range(4)]
for k in ("st1","st2","st3","st4"): S+=[("gwhoosh",T[k]-.45,.35),("select_008",T[k]+.1,.2)]
S+=[("drop_003",T["reply"]-.6,.3)]+reel_ticks(T["reply"]-.1,1.3,10,.26)+[("send",T["sixty"]+.35,.35),("lad4",T["sixty"]+.6,.18)]
S+=[("drop_002",T["spam"]-.2,.25),("swish",T["spam"]+.9,.3),("thud",T["spam"]+.9,.25)]
S+=[("keypress-001",T["voice"]-.4+k*.12,.08) for k in range(4)]+[("drop_003",T["heard"]-.1,.3),("lad3",T["heard"],.15)]
S+=[("card-slide-2",T["st2"]+.3,.25),("lad1",T["questions"]+.05,.25),("lad2",T["situation"]+.05,.25),("lad3",T["goals"]+.05,.25)]
S+=[("swish",T["directed"]-.1,.22),("swish",T["serious"]+.1,.22),("click3",T["pick"]-.05,.3),("confirm",T["pick"]+.15,.4)]
S+=[("swish",T["st3"]+.35,.2),("thud",T["most"]+.2,.2)]
for i,k in enumerate([0,1,2,3]): S+=[("ping",T["checkins"]-.3+i*.75,.18),(f"lad{i+1}",T["checkins"]-.28+i*.75,.12)]
S+=[("card-slide-1",T["once"],.3),("chime",T["once"]+.25,.35)]+[(f"lad{i+1}",T["reminders"]+.4+i*.45,.22) for i in range(3)]+[("join",T["showup"],.4)]
S+=[("card-slide-2",T["st4"]+.3,.25),("send",T["checkin"]-.1,.35),("confirm",T["restarts"],.45),("drop_003",T["ready"]+.35,.3)]
S+=[("gwhoosh",T["math"]-.35,.3)]+reel_ticks(T["n80"]-.05,1.4,12,.3)+[("vriser",T["thousands"]-1.4,.35),("swish",T["rescues"],.25),("bighit",T["thousands"]-.08,.6)]
S+=[("lad3",T["noads"]+.1,.25),("lad4",T["typing"]-.2,.25)]
S+=[("thud",T["fit0"]+.1,.3),("lad1",T["active"],.25),("lad2",T["reach"],.25),("lad3",T["capture"],.25)]
S+=[("gwhoosh",T["below"]-.3,.45)]+[("keypress-00%d"%(1+k%4),T["fill"]+.05+k*.085,.12) for k in range(12)]
S+=[("mouseclick1",T["fill"]+1.25,.4)]+[("click3",T["fill"]+1.55+i*.28,.25) for i in range(3)]
S+=[("mouseclick1",T["strategy"]-.05,.55),("haptic",T["strategy"]-.03,.4)]
S+=[("lad1",T["inspect"],.25),("lad2",T["leaking"],.25),("lad3",T["runs"],.25)]
S+=[("gwhoosh",T["endc"]-.35,.35),("bighit",T["endc"]+.05,.45)]
for k,(f,t,v) in enumerate(S):
    ext="ogg" if os.path.exists(R+f"assets/sfx/{f}.ogg") else "wav"
    t=max(0,t); d=min(dur(f"assets/sfx/{f}.{ext}"),D-t-.01)
    tags.append(f'<audio id="sfx{k}" src="assets/sfx/{f}.{ext}" data-start="{t:.3f}" data-duration="{d:.3f}" data-track-index="{20+k}" data-volume="{v}" data-audio-group="sfx"></audio>')
q=lambda o: html.escape(json.dumps(o,separators=(",",":")),quote=True)
M={"version":1,"lanes":[{"target":"volume","points":[{"t":0,"v":1},{"t":T["need"]-.2,"v":1},{"t":T["need"],"v":.45},{"t":T["stop"]+.5,"v":1},
   {"t":T["math"]-.2,"v":1},{"t":T["math"]+.2,"v":.5},{"t":T["thousands"]-.1,"v":.5},{"t":T["thousands"]+.1,"v":2.0},{"t":T["noads"]+1,"v":1},{"t":T["talk"]+.8,"v":1},{"t":T["talk"]+1.6,"v":5.0},{"t":D-1.5,"v":5.0},{"t":D,"v":0}]}]}
for _p in M['lanes'][0]['points']: _p['v']=round(_p['v']*0.06,4)
tags.append(f'<audio id="music" src="assets/music/bed.wav" data-start="0" data-duration="{D:.3f}" data-track-index="5" data-volume="0.028" data-audio-group="music" data-automation="{q(M)}"></audio>')
vchain={"version":1,"nodes":[{"type":"highpass","id":"v1","params":{"frequency":70,"q":0.707,"poles":"2"}},
 {"type":"peaking","id":"v2","params":{"frequency":250,"gain":-2,"q":1}},
 {"type":"compressor","id":"v3","params":{"threshold":-20,"ratio":2.5,"attack":10,"release":150,"makeup":2}},
 {"type":"peaking","id":"v4","params":{"frequency":3500,"gain":1.5,"q":0.9}},
 {"type":"limiter","id":"v5","params":{"limit":-1}}]}
schain={"version":1,"nodes":[{"type":"highpass","id":"s1","params":{"frequency":80,"q":0.707,"poles":"2"}},{"type":"lowpass","id":"s3","params":{"frequency":9000,"q":0.707,"poles":"2"}},{"type":"limiter","id":"s2","params":{"limit":-6}}]}
groups=f"""<hf-audio-group id="voiceover" data-label="Voiceover" data-volume="1" data-fx-chain="{q(vchain)}"></hf-audio-group>
<hf-audio-group id="sfx" data-label="SFX" data-volume="0.8" data-fx-chain="{q(schain)}"></hf-audio-group>"""
s=s.replace("<!--AUDIO-->","<!--AUDIO-->\n"+groups+"\n"+"\n".join(tags))
open(R+"index.html","w").write(s); print(len(tags),"audio tags")
