import numpy as np, soundfile as sf
from scipy.signal import butter, sosfilt
SR=48000; R="/tmp/hf/v4/assets/"
def lp(x,f,o=4): return sosfilt(butter(o,f,'low',fs=SR,output='sos'),x)
def hp(x,f,o=2): return sosfilt(butter(o,f,'high',fs=SR,output='sos'),x)
def env(n,a,d): t=np.arange(n)/SR; return (1-np.exp(-t/max(a,1e-4)))*np.exp(-t/d)
def save(n,x,g=.8): x=x/ (np.max(np.abs(x))+1e-9)*g; sf.write(R+"sfx/"+n+".wav",np.stack([x,x],1).astype(np.float32),SR)
def note(f,dur,dec,harm=(1,.35,.12,.05)):
    n=int(SR*dur);t=np.arange(n)/SR
    return sum(a*np.sin(2*np.pi*f*(k+1)*t) for k,a in enumerate(harm))*env(n,.003,dec)
# pitch ladder chimes (soft bell, lowpassed)
for name,f in [("lad1",523.25),("lad2",659.25),("lad3",783.99),("lad4",1046.5)]:
    x=note(f,1.0,.32,(1,.0,.25,.0,.08))+.4*note(f*2.01,1.0,.12); save(name,lp(x,8000),.6)
# land thunk: short sub + body
n=int(SR*.35);t=np.arange(n)/SR
th=np.sin(2*np.pi*(110*np.exp(-t*18)+55)*t)*env(n,.002,.09)+.3*lp(np.random.default_rng(1).standard_normal(n),900)*env(n,.001,.02)
save("land",th,.85)
# dull thud (loss)
n=int(SR*.6);t=np.arange(n)/SR
d=np.sin(2*np.pi*(70*np.exp(-t*6)+38)*t)*env(n,.003,.22)+.2*lp(np.random.default_rng(2).standard_normal(n),400)*env(n,.002,.05)
save("thud",d,.9)
# soft tick for reels
n=int(SR*.05);t=np.arange(n)/SR
tk=np.sin(2*np.pi*2200*t)*env(n,.0005,.006)+.5*lp(np.random.default_rng(3).standard_normal(n),5000)*env(n,.0003,.003)
save("rtick",lp(tk,7000),.5)
# glass whoosh: filtered noise swell
n=int(SR*.7);t=np.arange(n)/SR;nz=np.random.default_rng(4).standard_normal(n)
sw=np.sin(np.pi*t/.7)**2
w=hp(lp(nz,2500),300)*sw; save("gwhoosh",w,.55)
# light swish (short, brighter but capped)
n=int(SR*.35);t=np.arange(n)/SR;nz=np.random.default_rng(5).standard_normal(n)
save("swish",hp(lp(nz,6000),900)*np.sin(np.pi*t/.35)**3,.45)
# riser 1.2s
n=int(SR*1.2);t=np.arange(n)/SR;nz=np.random.default_rng(6).standard_normal(n)
ri=lp(nz,1200)*(t/1.2)**2+.4*np.sin(2*np.pi*(200+500*(t/1.2)**2)*t)*(t/1.2)**2
save("vriser",lp(ri,6000),.5)
# big hit: sub drop + shimmer
n=int(SR*2.0);t=np.arange(n)/SR
hit=np.sin(2*np.pi*(90*np.exp(-t*3)+42)*t)*env(n,.002,.5)+.15*sum(np.sin(2*np.pi*f*t) for f in (1046.5,1318.5,1568))*env(n,.01,.6)
save("bighit",lp(hit,8000),.9)
# confirm chime (two notes)
c=np.concatenate([note(783.99,.12,.2),np.zeros(0)]);c2=note(1046.5,.9,.35)
x=np.zeros(int(SR*1.0));x[:len(c)]+=c;o=int(SR*.09);x[o:o+len(c2)]+=c2[:len(x)-o]
save("confirm",lp(x,8500),.6)
# ---- ambient bed (calm, 3 sections) ----
D=162.0;N=int(SR*D);t=np.arange(N)/SR
def pad(freqs,t0,t1,amp,cut):
    i0,i1=int(t0*SR),int(t1*SR);tt=np.arange(i1-i0)/SR;s=np.zeros(i1-i0)
    for f in freqs:
        for det in (-0.12,0,0.11):
            ph=np.random.default_rng(int(f*10)).uniform(0,6.28)
            s+=np.sign(np.sin(2*np.pi*(f*(1+det/100))*tt+ph))*.3+np.sin(2*np.pi*f*(1+det/100)*tt+ph)
    s=lp(s,cut,2);fade=np.minimum(1,np.minimum(tt/1.5,(tt[-1]-tt)/1.5));return i0,i1,s*fade*amp
bed=np.zeros(N)
# chords (Hz): Am9 / Fmaj7 / Cmaj7 / G6  ; 8s each
CH=[[110,164.81,196,261.63,246.94],[87.31,130.81,174.61,220,329.63],[130.81,196,246.94,329.63],[98,146.83,196,246.94,329.63]]
k=0;tt0=0.0
while tt0<D-0.1:
    seg=8.0;t1=min(D,tt0+seg+1.5)
    cut=900 if tt0<43 else (1600 if tt0<105 else 2200)
    i0,i1,s=pad(CH[k%4],tt0,t1,1.0,cut);bed[i0:i1]+=s;tt0+=seg;k+=1
# arpeggio in steps (43.8 - 105.8) and lighter after 125
def arp(t0,t1,step=.25,amp=.25):
    out=np.zeros(N);tt=t0;j=0
    while tt<t1:
        chord=CH[int(tt//8)%4];f=chord[j%len(chord)]*2
        n=note(f,.6,.18,(1,.2,.05));i=int(tt*SR);m=min(len(n),N-i);out[i:i+m]+=n[:m]*amp;tt+=step;j+=1
    return lp(out,5000)
bed+=arp(43.8,105.4)+arp(125.0,153.0,.5,.18)
# sub pulse (very soft) on beats at 90bpm during steps
bed=bed/np.max(np.abs(bed))*.5
# fade in/out
bed*=np.minimum(1,t/1.0)*np.minimum(1,(D-t)/2.0)
sf.write(R+"music/bed.wav",np.stack([bed,np.roll(bed,int(.012*SR))],1).astype(np.float32),SR)
print("ok")

# ---------- v4.1 additions: hook impacts, soft plucks (replace bells), coin counter, cash land ----------
rng=np.random.default_rng(11)
# cinematic hook hit: sub boom + body thump + short air burst, long tail
n=int(SR*2.6);t=np.arange(n)/SR
boom=np.sin(2*np.pi*(62*np.exp(-t*2.2)+34)*t)*env(n,.004,.9)
body=np.sin(2*np.pi*(140*np.exp(-t*14)+70)*t)*env(n,.002,.12)
air=lp(hp(rng.standard_normal(n),200),3000)*env(n,.003,.25)*.35
save("hookhit",lp(boom+.6*body+air,7000),.95)
# tension swell (reverse-style) 1.4s
n=int(SR*1.4);t=np.arange(n)/SR;x=t/1.4
sw=(lp(rng.standard_normal(n),900)*(1-x)+lp(rng.standard_normal(n),2600)*x)*x**3+.5*np.sin(2*np.pi*(55+40*x)*t)*x**2
save("swell",sw,.7)
# heartbeat-like low pulse (two thumps)
def thump(f,d):
    n=int(SR*d);t=np.arange(n)/SR;return np.sin(2*np.pi*(f*np.exp(-t*10)+f*.5)*t)*env(n,.002,.07)
hb=np.zeros(int(SR*.6));a=thump(90,.25);hb[:len(a)]+=a;o=int(SR*.2);b=thump(80,.3);hb[o:o+len(b)]+=b*.7
save("pulse",lp(hb,600),.8)
# soft wooden plucks (low, short) for ladders: C4 E4 G4 C5
for name,f in [("tap1",261.63),("tap2",329.63),("tap3",392.0),("tap4",523.25)]:
    n=int(SR*.35);t=np.arange(n)/SR
    x=(np.sin(2*np.pi*f*t)+.25*np.sin(2*np.pi*f*4*t)*np.exp(-t*60))*env(n,.002,.07)
    save(name,lp(x,4500),.55)
# low confirm: warm whoomp + soft pluck
n=int(SR*.8);t=np.arange(n)/SR
cf=np.sin(2*np.pi*(180*np.exp(-t*8)+110)*t)*env(n,.004,.15)
p=np.zeros(n);pl=np.sin(2*np.pi*392*t[:int(SR*.3)])*env(int(SR*.3),.002,.06);o=int(SR*.06);p[o:o+len(pl)]=pl
save("confirm2",lp(cf+.5*p,5000),.7)
# coin tick (metallic but rolled off) and cash land
n=int(SR*.09);t=np.arange(n)/SR
coin=(np.sin(2*np.pi*2350*t)+.6*np.sin(2*np.pi*3170*t)+.3*np.sin(2*np.pi*4420*t))*env(n,.0005,.018)
save("coin",lp(coin,7000),.5)
n=int(SR*1.6);t=np.arange(n)/SR
bell=(np.sin(2*np.pi*1318.5*t)+.5*np.sin(2*np.pi*1975.5*t)+.3*np.sin(2*np.pi*2637*t))*env(n,.002,.35)
drawer=lp(rng.standard_normal(n),1200)*env(n,.002,.04)+np.sin(2*np.pi*(120*np.exp(-t*20)+60)*t)*env(n,.002,.12)
cash=np.zeros(n);cash+=drawer*.9;o=int(SR*.05);cash[o:]+=bell[:n-o]*.55
save("cash",lp(cash,7000),.85)
print("v41 ok")
