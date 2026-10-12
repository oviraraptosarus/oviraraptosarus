import numpy as np, soundfile as sf, sys
SR=44100; out=sys.argv[1]; rng=np.random.default_rng(7)
t_=lambda d: np.arange(int(SR*d))/SR
def env(d,a=.005,dec=None):
    t=t_(d); e=np.minimum(t/a,1)
    return e*(np.exp(-t/dec) if dec else 1)
def sweep(f0,f1,d,curve="exp"):
    t=t_(d); f=f0*(f1/f0)**(t/d) if curve=="exp" else f0+(f1-f0)*t/d
    return np.sin(2*np.pi*np.cumsum(f)/SR)
def lp(x,a): # one-pole lowpass, a in (0,1)
    y=np.zeros_like(x); s=0
    for i,v in enumerate(x): s+=a*(v-s); y[i]=s
    return y
def bp_noise(d,lo,hi):
    n=rng.standard_normal(int(SR*d)); F=np.fft.rfft(n); fr=np.fft.rfftfreq(len(n),1/SR)
    F[(fr<lo)|(fr>hi)]=0; return np.fft.irfft(F,len(n))/3
def norm(x,p=.9): return x/np.max(np.abs(x)+1e-9)*p
def w(n,x,p=.9): sf.write(f"{out}/{n}.wav",norm(x,p).astype(np.float32),SR)

# kick / clap / hat (also for music)
kick=sweep(150,42,.35)*env(.35,.002,.09)
clap=sum(np.pad(bp_noise(.18,900,5000)*env(.18,.001,.04),(int(SR*o),int(SR*.2)))[:int(SR*.2)] for o in (0,.01,.022))
hat=bp_noise(.06,7000,15000)*env(.06,.001,.015)
w("kick",kick); w("clap",clap,.6); w("hat",hat,.4)

w("whoosh",bp_noise(.5,400,6000)*np.sin(np.pi*t_(.5)/.5)**2*(1+0*t_(.5)),.6)
# glitch: stuttered crushed noise + square blips
g=np.zeros(int(SR*.35))
for k in range(7):
    s=int(SR*k*.05); seg=np.sign(np.sin(2*np.pi*(300+k*170)*t_(.03)))*.5+bp_noise(.03,2000,9000)
    g[s:s+len(seg)]+=seg
w("glitch",np.round(g*6)/6,.6)
w("slam",sweep(110,40,.4)*env(.4,.001,.12)+bp_noise(.4,100,2500)*env(.4,.001,.03),.95)
# boing: pitch-wobble
t=t_(.5); f=330*(1+.25*np.sin(2*np.pi*14*t)*np.exp(-t/.25)); w("boing",np.sin(2*np.pi*np.cumsum(f)/SR)*env(.5,.003,.18),.7)
# slide whistle down with vibrato
t=t_(.9); f=1300*(280/1300)**(t/.9)*(1+.03*np.sin(2*np.pi*7*t)); w("slide",(np.sin(2*np.pi*np.cumsum(f)/SR)+.2*np.sin(4*np.pi*np.cumsum(f)/SR))*np.minimum(t/.03,1)*np.minimum((.9-t)/.1,1),.5)
w("bloop",sweep(900,250,.12)*env(.12,.002,.05),.6)
w("pop",sweep(400,1400,.06)*env(.06,.001,.025),.7)
w("blink",sweep(1800,2600,.04)*env(.04,.001,.012),.4)
# chomp: two crunchy bites
c=np.zeros(int(SR*.3))
for o in (0,.11):
    s=int(SR*o); b=bp_noise(.09,300,3500)*env(.09,.001,.03)+.8*sweep(180,60,.09)*env(.09,.001,.04); c[s:s+len(b)]+=b
w("chomp",c,.95)
w("tick",bp_noise(.03,2500,8000)*env(.03,.0005,.006),.5)
t=t_(1.2); w("ding",(np.sin(2*np.pi*1318*t)+.5*np.sin(2*np.pi*1976*t)+.25*np.sin(2*np.pi*2637*t))*env(1.2,.002,.35),.5)
t=t_(.7); w("riser",bp_noise(.7,200,12000)*(t/.7)**2+.3*sweep(200,1600,.7)*(t/.7)**2,.5)
w("stamp",sweep(90,45,.35)*env(.35,.001,.1)+bp_noise(.35,200,1500)*env(.35,.001,.05)+.5*bp_noise(.35,1500,6000)*env(.35,.001,.02),.95)
t=t_(.55); sc=bp_noise(.55,1500,7000)*(.5+.5*np.abs(np.sin(2*np.pi*9*t)))*np.minimum(t/.03,1)*np.minimum((.55-t)/.05,1); w("scribble",sc,.35)
# sparkle arpeggio
sp=np.zeros(int(SR*1.0))
for k,fq in enumerate([1568,2093,2637,3136,4186]):
    s=int(SR*k*.05); x=np.sin(2*np.pi*fq*t_(.5))*env(.5,.001,.12); sp[s:s+len(x)]+=x
w("sparkle",sp,.4)
