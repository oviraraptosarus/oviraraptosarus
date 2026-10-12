import subprocess,re,json
lines=[l.split("|",1) for l in open("/tmp/hf/vsl/lines.txt").read().strip().split("\n")]
out={}
for lid,text in lines:
    f=f"/tmp/hf/vsl/assets/vo/{lid}.wav"
    d=float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f]))
    err=subprocess.run(["ffmpeg","-i",f,"-af","silencedetect=noise=-42dB:d=0.12","-f","null","-"],capture_output=True,text=True).stderr
    ss=[float(x) for x in re.findall(r"silence_start: ([\d.]+)",err)]; se=[float(x) for x in re.findall(r"silence_end: ([\d.]+)",err)]
    chunks=[];cur=0.0
    for a,b in zip(ss,se+[d]*(len(ss)-len(se))):
        if a-cur>0.08: chunks.append([cur,a])
        cur=b
    if d-cur>0.08: chunks.append([cur,d])
    words=text.split(); wts=[len(re.sub(r"\W","",w))+1.2 for w in words]; tot=sum(wts)
    sp=sum(b-a for a,b in chunks); pos=0; res=[]
    def at(x):
        for a,b in chunks:
            if x<=b-a: return a+x
            x-=b-a
        return chunks[-1][1]
    for w,wt in zip(words,wts):
        s=at(pos); pos+=sp*wt/tot; e=at(pos); res.append({"w":w,"s":round(s,3),"e":round(e,3)})
    out[lid]={"d":round(d,3),"text":text,"words":res}
json.dump(out,open("/tmp/hf/vsl/vo.json","w"))
scenes=[["h1","h2"],["p1","p2"],["p3"],["p4"],["p5"],["t1","t2"],["m0"],["m1"],["m2"],["m3"],["m4"],["n1","n2","n3"],["o1"],["o2","o3"],["f1"],["c1","c2"]]
t=0.45;starts={};sc=[]
for si,s in enumerate(scenes):
    s0=t
    for j,l in enumerate(s):
        starts[l]=round(t,3); t+=out[l]["d"]+(0.25 if j<len(s)-1 else 0)
    sc.append([round(s0-0.3 if si else 0,3),None]); t+=0.50
end=t-0.50
for i in range(len(sc)): sc[i][1]=sc[i+1][0] if i+1<len(sc) else 117.0
json.dump({"starts":starts,"scenes":sc,"voend":round(end,3)},open("/tmp/hf/vsl/plan.json","w"))
print("last VO ends",round(end,2),"hold",round(117-end,2)); print(sc)
