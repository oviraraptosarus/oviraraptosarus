import subprocess,re,json,difflib,numpy as np,sherpa_onnx
R="/tmp/hf/ig/"
D="/tmp/claude-0/ed/model/sherpa-onnx-nemo-parakeet-tdt-0.6b-v2-int8/"
rec=sherpa_onnx.OfflineRecognizer.from_transducer(encoder=D+"encoder.int8.onnx",decoder=D+"decoder.int8.onnx",joiner=D+"joiner.int8.onnx",tokens=D+"tokens.txt",num_threads=4,sample_rate=16000,feature_dim=128,decoding_method="greedy_search",model_type="nemo_transducer")
lines=[l.split("|",1) for l in open(R+"lines.txt").read().strip().split("\n")]
norm=lambda w:re.sub(r"[^a-z0-9]","",w.lower().replace("’","'"))
out={}
for lid,text in lines:
    src=R+f"assets/vo/{lid}.wav"; dst=R+f"assets/vo/t/{lid}.wav"
    a=np.frombuffer(subprocess.check_output(["ffmpeg","-v","error","-i",src,"-ac","1","-ar","24000","-f","f32le","-"]),dtype=np.float32)
    env=np.convolve(np.abs(a),np.ones(240)/240,"same"); thr=10**(-45/20)
    idx=np.where(env>thr)[0]; s0=max(0,idx[0]-int(.03*24000)); s1=min(len(a),idx[-1]+int(.06*24000))
    subprocess.run(["ffmpeg","-y","-v","error","-i",src,"-af",f"atrim=start_sample={s0}:end_sample={s1},afade=t=in:d=0.01,areverse,afade=t=in:d=0.02,areverse","-ar","48000",dst],check=True)
    d=(s1-s0)/24000
    b=np.frombuffer(subprocess.check_output(["ffmpeg","-v","error","-i",dst,"-ac","1","-ar","16000","-f","f32le","-"]),dtype=np.float32)
    st=rec.create_stream(); st.accept_waveform(16000,b); rec.decode_stream(st); r=st.result
    # tokens -> words
    aw=[]
    for tok,t in zip(r.tokens,r.timestamps):
        if tok.startswith(" ") or tok.startswith("▁") or not aw: aw.append([tok.strip(" ▁"),t])
        else: aw[-1][0]+=tok
    words=text.split()
    A=[norm(w) for w in words]; Bn=[norm(w) for w,_ in aw]
    sm=difflib.SequenceMatcher(a=A,b=Bn,autojunk=False); st_=[None]*len(words)
    for blk in sm.get_matching_blocks():
        for k in range(blk.size): st_[blk.a+k]=aw[blk.b+k][1]
    # fill gaps by interpolation weighted by length
    known=[(i,t) for i,t in enumerate(st_) if t is not None]
    if not known: known=[(0,0.03)]
    if known[0][0]!=0: st_[0]=0.03; known=[(0,0.03)]+known
    for (i0,t0),(i1,t1) in zip(known,known[1:]):
        for k in range(i0+1,i1): st_[k]=t0+(t1-t0)*(k-i0)/(i1-i0)
    li,lt=known[-1]
    for k in range(li+1,len(words)): st_[k]=lt+(d-0.1-lt)*(k-li)/(len(words)-li)
    res=[{"w":w,"s":round(float(st_[i]),3),"e":round(float(st_[i+1]) if i+1<len(words) else d,3)} for i,w in enumerate(words)]
    miss=sum(1 for x in sm.get_opcodes() if x[0]!="equal")
    out[lid]={"d":round(d,3),"text":text,"words":res}
    print(lid,round(d,2),"| asr:",r.text,"| mism" if miss else "")
json.dump(out,open(R+"vo.json","w"),indent=0)
