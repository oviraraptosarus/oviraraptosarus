import json
sil=json.load(open("/tmp/claude-0/ed/sil.json"))
sil=[(a,b) for a,b in sil if b<=63.0]
END=53.12            # end of "general."
START=0.12
# dramatic pauses keep this much (seconds); other gaps >0.45 compress to 0.30
KEEP={(14.85,16.38):0.70,(20.46,21.55):0.45,(32.22,34.21):0.50,(41.58,43.75):0.50,(46.03,47.87):0.45,(12.58,12.86):None}
spans=[];cur=START
for a,b in sil:
    if b<=START or a>=END: continue
    if a<=cur: cur=max(cur,b); continue
    gap=b-a
    spans.append([cur,a]); cur=b
if END-cur>0.3: spans.append([cur,END])
# re-expand: insert the retained part of each silence at the boundaries
out=[]
for i,(s,e) in enumerate(spans):
    out.append([s,e])
final=[]
for i,(s,e) in enumerate(out):
    if i<len(out)-1:
        gs,ge=e,out[i+1][0]; g=ge-gs
        keep=None
        for (ka,kb),v in KEEP.items():
            if abs(ka-gs)<0.08: keep=v
        if keep is None: keep=g if g<=0.45 else 0.30
        keep=min(keep,g)
        final.append([s,e+keep/2]); out[i+1][0]=ge-keep/2
    else: final.append([s,e+0.25])
# merge adjacent contiguous
m=[]
for s,e in final:
    if m and abs(m[-1][1]-s)<1e-3: m[-1][1]=e
    else: m.append([round(s,3),round(e,3)])
json.dump(m,open("/tmp/claude-0/ed/edl.json","w"))
t=0
for s,e in m: print(f"src {s:6.2f}-{e:6.2f}  len {e-s:5.2f}  -> edit {t:6.2f}"); t+=e-s
print("TOTAL",round(t,2))
