import json,re,difflib,subprocess,numpy as np,sherpa_onnx,soundfile as sf
R="/tmp/hf/vsl3/"
D="/tmp/claude-0/ed/model/sherpa-onnx-nemo-parakeet-tdt-0.6b-v2-int8/"
subprocess.run(["ffmpeg","-y","-v","error","-i",R+"assets/vo/el_main.wav","-ac","1","-ar","16000","/tmp/claude-0/el/cut16.wav"],check=True)
rec=sherpa_onnx.OfflineRecognizer.from_transducer(encoder=D+"encoder.int8.onnx",decoder=D+"decoder.int8.onnx",joiner=D+"joiner.int8.onnx",tokens=D+"tokens.txt",num_threads=4,sample_rate=16000,feature_dim=128,decoding_method="greedy_search",model_type="nemo_transducer")
a,sr=sf.read("/tmp/claude-0/el/cut16.wav",dtype="float32")
DUR=len(a)/16000
step=25*16000;i=0;asr=[]
while i<len(a):
    j=min(len(a),i+step)
    if j<len(a):
        seg=np.abs(a[j-4*16000:j]);k=np.convolve(seg,np.ones(3200)/3200,"valid").argmin()+j-4*16000+1600;j=k
    r=rec.create_stream();r.accept_waveform(16000,a[i:j]);rec.decode_stream(r);res=r.result
    cur=None
    for tok,t in zip(res.tokens,res.timestamps):
        t=round(t+i/16000,3)
        if tok.startswith(" ") or cur is None:
            if cur: asr.append(cur)
            cur=[tok.strip(),t]
        else: cur[0]+=tok
    if cur: asr.append(cur)
    i=j
lines=[l.split("|",1) for l in open(R+"lines.txt").read().strip().split("\n")]
words=[];seg_of=[]
for sid,t in lines:
    for w in t.split(): words.append(w); seg_of.append(sid)
def norm(w):
    w=w.lower().replace("’","'")
    w=re.sub(r"[^a-z0-9]","",w)
    return w
NUM={"214":"twofourteen","247":"twoftyseven"}
A=[norm(w) for w in words]; B=[norm(w) for w,_ in asr]
# digit/word equivalences handled by interpolation
sm=difflib.SequenceMatcher(a=A,b=B,autojunk=False);ts=[None]*len(words)
for blk in sm.get_matching_blocks():
    for k in range(blk.size): ts[blk.a+k]=asr[blk.b+k][1]
known=[(i,t) for i,t in enumerate(ts) if t is not None]
if known[0][0]!=0: ts[0]=asr[0][1]; known=[(0,ts[0])]+known
for (i0,t0),(i1,t1) in zip(known,known[1:]):
    for k in range(i0+1,i1): ts[k]=t0+(t1-t0)*(k-i0)/(i1-i0)
li,lt=known[-1]
for k in range(li+1,len(words)): ts[k]=lt+(DUR-0.2-lt)*(k-li)/(len(words)-li)
miss=sum(1 for x in ts if x is None)
out={};order=[];idx=0
OFFSET=2.0
starts={}
for sid,t in lines:
    n=len(t.split()); sw=[(words[idx+k],ts[idx+k]) for k in range(n)]
    st=sw[0][1]-0.03
    nxt=ts[idx+n] if idx+n<len(ts) else DUR
    ws=[]
    for k,(w,tt) in enumerate(sw):
        e=sw[k+1][1] if k+1<n else min(nxt,tt+0.7)
        ws.append({"w":w,"s":round(tt-st,3),"e":round(e-st,3)})
    out[sid]={"d":round(ws[-1]["e"],3),"text":t,"words":ws}
    starts[sid]=round(OFFSET+st,3);order.append(sid);idx+=n
json.dump(out,open(R+"vo.json","w"))
END=OFFSET+DUR
json.dump({"starts":starts,"voend":round(END,3),"order":order,"offset":OFFSET,"dur":round(DUR,3)},open(R+"plan.json","w"))
print("audio dur",round(DUR,2),"voend",round(END,2),"unmatched interp",sum(1 for x in range(len(words)) if x not in [i for i,_ in known]))
for sid in order: print(sid,starts[sid],round(starts[sid]+out[sid]["d"],2))
