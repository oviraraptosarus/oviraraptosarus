import json,numpy as np,subprocess,re
words=json.load(open("words.json")); words=[w for w in words if w["s"]<53.3]
fix={"curtain's":"Koenigsegg"}
for w in words: w["w"]=fix.get(w["w"],w["w"])
words=[w for i,w in enumerate(words) if not (w["w"].lower().startswith("egg") and words[i-1]["w"]=="Koenigsegg")]
for i,w in enumerate(words):
    if w["w"]=="Koenigsegg": w["w"]="Koenigsegg,"
# speech chunks from a finer silence map (-38dB, 0.09s gaps) so short pauses between words split chunks
out=subprocess.run(["ffmpeg","-i","/home/user/oviraraptosarus/input/small.mp4","-af","silencedetect=noise=-35dB:d=0.18","-f","null","-"],capture_output=True,text=True).stderr
ss=[float(x) for x in re.findall(r"silence_start: ([\d.]+)",out)]; se=[float(x) for x in re.findall(r"silence_end: ([\d.]+)",out)]
chunks=[];cur=0.0
for a,b in zip(ss,se):
    if a-cur>0.1: chunks.append([cur,a])
    cur=b
if 53.0-cur>0.07: chunks.append([cur,53.0])
chunks=[c for c in chunks if c[0]<53.0 and c[1]-c[0]>0.1]
N,M=len(words),len(chunks); print("words",N,"chunks",M)
t=np.array([w["s"] for w in words])
cost=np.zeros((N,M))
for j,(a,b) in enumerate(chunks):
    cost[:,j]=np.maximum(0,np.maximum(a-t,t-b))
# DP monotonic assignment, discourage >9 words in one chunk
INF=1e9; dp=np.full((N,M),INF); bp=np.zeros((N,M),int)
dp[0]=cost[0]
for i in range(1,N):
    best=np.minimum.accumulate(dp[i-1]); arg=np.zeros(M,int); mi=0
    run=INF;ai=0
    for j in range(M):
        if dp[i-1][j]<run: run=dp[i-1][j]; ai=j
        arg[j]=ai; best[j]=run
    dp[i]=best+cost[i]; bp[i]=arg
j=int(dp[-1].argmin()); assign=[0]*N; assign[-1]=j
for i in range(N-1,0,-1): j=bp[i][j]; assign[i-1]=j
groups={}
for i,j in enumerate(assign): groups.setdefault(j,[]).append(i)
for j,idx in groups.items():
    a,b=chunks[j]; wts=[len(re.sub(r"\W","",words[i]["w"]))+1.5 for i in idx]; tot=sum(wts); acc=a
    for i,wt in zip(idx,wts):
        d=(b-a)*wt/tot; words[i]["s"]=round(acc,3); words[i]["e"]=round(acc+d,3); acc+=d
json.dump(words,open("words_aligned.json","w"))
print(" ".join(f'{w["w"]}@{w["s"]:.2f}' for w in words))
