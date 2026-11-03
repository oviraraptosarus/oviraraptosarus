import json,subprocess,html,os,numpy as np,soundfile as sf
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"/"; D=30.5
words=json.load(open(R+"words.json"))
T=dict(turn=.16,a1=.56,dmw=.72,into=1.12,a2=1.36,client=1.44,loading=2.16,dm=4.0,s15=6.08,reply=6.92,own=8.24,s35=8.96,three=9.76,quick=10.08,questions=10.32,want=11.12,where=11.84,soon=12.4,
 s50=13.2,pick=13.76,time=14.32,s70=14.88,reminders=15.52,day=16.48,two=17.28,ten=18.16,s85=19.36,they=20.08,actually=20.32,show=20.56,up=20.8,s100=21.28,now=22.24,its=22.48,just=22.72,a3=22.88,good=23.04,conv=23.2,kw=24.16)
json.dump(T,open(R+"T.json","w"))
def dur(f): return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",R+f]))
# ---- music bed: dark pad + soft pulse, 120 BPM ----
sr=44100;n=int(sr*D);t=np.arange(n)/sr
pad=sum(np.sin(2*np.pi*f*t+np.sin(2*np.pi*.1*t)) for f in (110,164.8,220,261.6))*.12
pad*= (0.6+0.4*np.sin(2*np.pi*t/7.5)**2)
beat=np.zeros(n)
for b in np.arange(0,D,.5):
    i=int(b*sr);L=int(.12*sr);k=np.arange(L)/sr;beat[i:i+L]+=np.sin(2*np.pi*(60+80*np.exp(-k*40))*k)*np.exp(-k*28)*.5 if i+L<n else 0
bed=np.stack([pad+beat*.8]*2,1);bed=bed/np.abs(bed).max()*.7
bed[:int(sr*.05)]*=np.linspace(0,1,int(sr*.05))[:,None];bed[-int(sr*1.2):]*=np.linspace(1,0,int(sr*1.2))[:,None]
os.makedirs(R+"assets/music",exist_ok=True);sf.write(R+"assets/music/bed.wav",bed.astype("float32"),sr)
tags=[f'<audio id="vo" src="assets/vo/vo.wav" data-start="0" data-duration="{dur("assets/vo/vo.wav"):.3f}" data-track-index="10" data-volume="1" data-audio-group="voiceover"></audio>']
def reel(t,d,n=8,v=.3): return [("tick",t+d*(1-(1-k/n)**(1/3)),v) for k in range(n)]
S=[("hookhit",0,.85),("whoosh",0,.25),("haptic",T["dm"]-.1,.4),("ping",T["dm"],.22)]
S+=[("card-slide-1",T["dm"]-.05,.25)]
for to,L in [(15,T["s15"]),(35,T["s35"]),(50,T["s50"]),(70,T["s70"]),(85,T["s85"]),(100,T["s100"])]:
    S+=reel(L-.7,.7)+[("tap1",L,.3)]
S+=[("whoosh",T["s15"]-.3,.25)]+reel(T["s15"]+.1,1.0,10,.26)+[("tap2",T["s15"]+1.12,.3),("send",T["reply"]+.05,.32),("tap3",T["reply"]+.9,.2)]
S+=[("whoosh",T["s35"]-.3,.25),("card-slide-2",T["three"]-.1,.22)]
S+=[("tap1",T["want"]+.1,.3),("tap2",T["where"]+.1,.3),("tap3",T["soon"]+.1,.3)]
S+=[("whoosh",T["s50"]-.3,.25),("card-slide-1",T["s50"]+.3,.28),("click3",T["time"]+.1,.28),("confirm2",T["time"]+.3,.3)]
S+=[("whoosh",T["s70"]-.3,.25),("card-slide-2",T["day"]-.3,.2),("tap1",T["day"],.3),("card-slide-2",T["two"]-.3,.2),("tap2",T["two"],.3),("card-slide-2",T["ten"]-.3,.2),("tap3",T["ten"],.3)]
S+=[("whoosh",T["s85"]-.3,.25),("card-slide-1",T["s85"]+.1,.25)]+[("keypress-001",T["s85"]+.4+k*.4,.06) for k in range(3)]+[("join",T["show"]+.15,.38)]
S+=[("swell",T["s100"]-1.4,.25),("hookhit",T["s100"],.42),("sub",T["s100"],.3)]
S+=[("tap4",T["now"],.25),("tap4",T["conv"],.25),("whoosh",T["kw"]-.2,.3),("hookhit",T["kw"],.5),("tap2",T["kw"]+.5,.2)]
for k,(f,t0,v) in enumerate(S):
    ext="ogg" if os.path.exists(R+f"assets/sfx/{f}.ogg") else "wav"; t0=max(0,t0); d=min(dur(f"assets/sfx/{f}.{ext}"),D-t0-.01)
    tags.append(f'<audio id="sfx{k}" src="assets/sfx/{f}.{ext}" data-start="{t0:.3f}" data-duration="{d:.3f}" data-track-index="{20+k}" data-volume="{v}" data-audio-group="sfx"></audio>')
tags.append(f'<audio id="music" src="assets/music/bed.wav" data-start="0" data-duration="{D}" data-track-index="5" data-volume="0.035" data-audio-group="music"></audio>')
q=lambda o: html.escape(json.dumps(o,separators=(",",":")),quote=True)
vchain={"version":1,"nodes":[{"type":"highpass","id":"v1","params":{"frequency":70,"q":0.707,"poles":"2"}},{"type":"compressor","id":"v3","params":{"threshold":-20,"ratio":2.5,"attack":10,"release":150,"makeup":2}},{"type":"peaking","id":"v4","params":{"frequency":3500,"gain":1.5,"q":0.9}},{"type":"limiter","id":"v5","params":{"limit":-1}}]}
schain={"version":1,"nodes":[{"type":"highpass","id":"s1","params":{"frequency":80,"q":0.707,"poles":"2"}},{"type":"lowpass","id":"s3","params":{"frequency":9000,"q":0.707,"poles":"2"}},{"type":"limiter","id":"s2","params":{"limit":-9}}]}
groups=f'<hf-audio-group id="voiceover" data-label="Voiceover" data-volume="1" data-fx-chain="{q(vchain)}"></hf-audio-group>\n<hf-audio-group id="sfx" data-label="SFX" data-volume="0.3" data-fx-chain="{q(schain)}"></hf-audio-group>'
s=open(R+"tools/template.html").read()
s=s.replace("__T__",json.dumps(T)).replace("__W__",json.dumps([{"w":w["w"],"s":round(w["s"],3)} for w in words],separators=(",",":"))).replace("__D__",str(D))
s=s.replace("<!--AUDIO-->",groups+"\n"+"\n".join(tags))
open(R+"index.html","w").write(s);print(len(tags),"audio tags")
