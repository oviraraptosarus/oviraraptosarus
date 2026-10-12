import numpy as np, soundfile as sf
SR=44100; D=15.0; N=int(SR*D); B=60/143; BAR=4*B
rd=lambda n: sf.read(f"/tmp/hf/reel/audio/{n}.wav")[0]
kick,clap,hat=rd("kick"),rd("clap"),rd("hat")
mix=np.zeros(N); drums=np.zeros(N); kicks=[]
def put(buf,x,t,g=1):
    s=int(t*SR); e=min(N,s+len(x));
    if s<N: buf[s:e]+=g*x[:e-s]
def tone(f,d,dec,harm=((1,1),(4,.25)),a=.003):
    t=np.arange(int(SR*d))/SR; x=sum(g*np.sin(2*np.pi*f*h*t) for h,g in harm)
    return x*np.minimum(t/a,1)*np.exp(-t/dec)
chords=[(220,261.6,329.6,55),(174.6,220,261.6,43.65),(261.6,329.6,392,65.4),(196,246.9,293.7,49)]
dark=(9.15,10.85)
def indark(t): return dark[0]<=t<dark[1]
t=0.0; i=0
while t<14.1:
    bar=int(t//BAR); ch=chords[bar%4]; pos=round((t%BAR)/(B/2))  # 8th index 0..7
    if not indark(t):
        if pos in (0,3,4): put(drums,kick,t,.9); kicks.append(t)
        if pos in (2,6): put(drums,clap,t,.5)
        put(drums,hat,t,.25 if pos%2 else .15)
        # bass: root on 0, octave on 3, root 4, fifth 6
        bf={0:1,3:2,4:1,6:1.5}.get(pos)
        if bf: put(mix,tone(ch[3]*bf,.35,.12,harm=((1,1),(2,.5),(3,.3),(4,.15))),t,.55)
        # marimba stabs on offbeats
        if pos in (1,3,5,7) and pos!=3:
            for k,f in enumerate(ch[:3]): put(mix,tone(f*2,.4,.11),t+k*.008,.18)
        # top melody blips every 2 bars
        if pos==7 and bar%2==1: put(mix,tone(ch[2]*4,.25,.07),t,.12)
    t+=B/2
# dark pad for midnight
tt=np.arange(int(SR*(dark[1]-dark[0]+.3)))/SR
pad=sum(np.sin(2*np.pi*f*tt)*(1+.1*np.sin(2*np.pi*.5*tt)) for f in (110,164.8,220,261.6))
pad*=np.minimum(tt/.2,1)*np.minimum((tt[-1]-tt)/.3,1)
put(mix,pad,dark[0],.08)
# final hit
put(drums,kick,14.1,1.0); kicks.append(14.1)
for f in (261.6,329.6,392,523.2): put(mix,tone(f,1.0,.4),14.1,.2)
put(mix,tone(65.4,1.0,.35,harm=((1,1),(2,.5))),14.1,.5)
# sidechain
sc=np.ones(N); ts=np.arange(N)/SR
for k in kicks:
    m=(ts>=k)&(ts<k+.25); sc[m]=np.minimum(sc[m],1-.55*np.exp(-(ts[m]-k)/.08))
out=drums+mix*sc
out*=np.minimum(ts/.05,1)*np.clip((15-ts)/.4,0,1)
out=np.tanh(out*1.4)/np.tanh(1.4)
sf.write("/tmp/hf/reel/audio/bed.wav",(out/np.max(np.abs(out))*.9).astype(np.float32),SR)
print("ok")
