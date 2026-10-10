import sherpa_onnx, soundfile as sf, json
D="/tmp/claude-0/ed/model/sherpa-onnx-nemo-parakeet-tdt-0.6b-v2-int8/"
rec=sherpa_onnx.OfflineRecognizer.from_transducer(encoder=D+"encoder.int8.onnx",decoder=D+"decoder.int8.onnx",joiner=D+"joiner.int8.onnx",tokens=D+"tokens.txt",num_threads=4,sample_rate=16000,feature_dim=128,decoding_method="greedy_search",model_type="nemo_transducer")
a,sr=sf.read("/tmp/claude-0/ed/a16.wav",dtype="float32")
out=[]
step=25*16000  # windows < 30s w/ no cut mid-speech issue: use overlap-free 25s windows split at lowest-energy point
import numpy as np
i=0
while i<len(a):
    j=min(len(a),i+step)
    if j<len(a):
        # move split to quietest 0.2s within last 4 s
        seg=np.abs(a[j-4*16000:j]); k=np.convolve(seg,np.ones(3200)/3200,"valid").argmin()+j-4*16000+1600; j=k
    r=rec.create_stream(); r.accept_waveform(16000,a[i:j]); rec.decode_stream(r); res=r.result
    toks=list(zip(res.tokens,[round(t+i/16000,3) for t in res.timestamps]))
    out.append({"offset":i/16000,"text":res.text,"tokens":toks})
    print(f"[{i/16000:.1f}-{j/16000:.1f}]",res.text)
    i=j
json.dump(out,open("/tmp/claude-0/ed/pk.json","w"))
