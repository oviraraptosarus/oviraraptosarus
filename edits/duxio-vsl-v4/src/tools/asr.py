import subprocess,json,numpy as np,sherpa_onnx,sys
D="/tmp/claude-0/ed/model/sherpa-onnx-nemo-parakeet-tdt-0.6b-v2-int8/"
rec=sherpa_onnx.OfflineRecognizer.from_transducer(encoder=D+"encoder.int8.onnx",decoder=D+"decoder.int8.onnx",joiner=D+"joiner.int8.onnx",tokens=D+"tokens.txt",num_threads=4,sample_rate=16000,feature_dim=128,decoding_method="greedy_search",model_type="nemo_transducer")
a=np.frombuffer(subprocess.check_output(["ffmpeg","-v","error","-i",sys.argv[1],"-ac","1","-ar","16000","-f","f32le","-"]),dtype=np.float32)
# split at quietest points near every 20s
env=np.convolve(np.abs(a),np.ones(1600)/1600,"same")
cuts=[0];t=20*16000
while t<len(a)-8*16000:
    w=env[t-3*16000:t+3*16000];k=t-3*16000+int(np.argmin(w));cuts.append(k);t=k+20*16000
cuts.append(len(a))
words=[]
for s,e in zip(cuts,cuts[1:]):
    st=rec.create_stream();st.accept_waveform(16000,a[s:e]);rec.decode_stream(st);r=st.result
    cur=None
    for tok,tt in zip(r.tokens,r.timestamps):
        if tok.startswith(" ") or tok.startswith("▁") or cur is None:
            cur=[tok.strip(" ▁"),s/16000+tt];words.append(cur)
        else: cur[0]+=tok
json.dump([{"w":w,"s":round(t,3)} for w,t in words],open(sys.argv[2],"w"))
print(" ".join(w for w,_ in words))
