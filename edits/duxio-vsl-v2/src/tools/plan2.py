import json
R="/tmp/hf/vsl2/"; vo=json.load(open(R+"vo.json"))
order=[l.split("|")[0] for l in open(R+"lines.txt").read().strip().split("\n")]
gap={"a1":0.95,"a2":0.3,"a3":0.12,"a4":0.18,"b1":0.4,"b2":0.18,"b3":0.22,"b4":0.22,"b5":0.2,"b6":0.85,"b7":1.75,"b8":0.45,"b9":0.3,"b10":0.4,
"c1":0.95,"c2":0.15,"c3":0.25,"d0":0.6,"d1":1.85,"d2":0.25,"d2b":0.1,"d3":0.3,"d4":0.25,"d5":0.25,"d6":0.25,"d7":0.3,"e1":0.45,"e1b":0.2,"e2":0.25,"e3":0.25}
fixed={"a1","b6","b7","c1","d0","d1"}  # deliberate beats keep their length
HOLD=3.2
speech=sum(vo[k]["d"] for k in order); g=sum(gap.values()); gf=sum(gap[k] for k in fixed)
k=(117-HOLD-speech-gf)/(g-gf)
t=0;st={}
for i in order:
    t+=gap[i]*(1 if i in fixed else k); st[i]=round(t,3); t+=vo[i]["d"]
print("speech",round(speech,2),"gap scale",round(k,3),"voend",round(t,3))
json.dump({"starts":st,"voend":round(t,3),"order":order},open(R+"plan.json","w"))
for i in order: print(i,st[i],round(st[i]+vo[i]["d"],2))
