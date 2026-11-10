"""ECK-022 phase comparison and non-mutating replay, deterministic reference tests."""
from dataclasses import dataclass
ADDRESSES=("upperleftback","lowerleftback","centerback","centerupper","center","centerlower","upperrightfront","centerrightfront","lowerrightfront")
PYRAMID=(27,24,21,17.5,13,8,5,3,2,1,1)
ORIGIN="(0=-.)"
ROUTE=("0","1a","1b","2","3","5","8","13","17.5","21","24","27","0")
@dataclass(frozen=True)
class Phase:
    wheels:tuple
    fields:tuple
    address:str
    n:int
    addresses:tuple=ADDRESSES
    pyramid:tuple=PYRAMID
@dataclass(frozen=True)
class Snapshot:
    generation:int
    origin:str
    route:tuple
    phase:Phase
def compare(a,b):
    pa,pb=a.phase,b.phase
    return {
        "wheels":tuple(y-x for x,y in zip(pa.wheels,pb.wheels)),
        "fields":tuple(y-x for x,y in zip(pa.fields,pb.fields)),
        "total":sum(pb.fields)-sum(pa.fields),
        "address_changed":pa.address!=pb.address,
        "n_delta":pb.n-pa.n,
        "same_origin":a.origin==b.origin,
        "same_route":a.route==b.route,
        "same_addresses":pa.addresses==pb.addresses,
        "same_pyramid":pa.pyramid==pb.pyramid,
    }
def replay(snap):
    p=snap.phase
    if snap.origin!=ORIGIN or len(p.wheels)!=4 or len(p.fields)!=4:return None
    if p.addresses!=ADDRESSES or p.pyramid!=PYRAMID or p.address not in ADDRESSES or not 1<=p.n<=9:return None
    if any(not low<=v<=high for v,low,high in zip(p.wheels,(0,0,380,0),(359,359,750,999))):return None
    if any(not isinstance(v,int) or not 0<=v<=100 for v in p.fields):return None
    return {"wheels":list(p.wheels),"fields":list(p.fields),"address":p.address,"n":p.n}
def test():
    count=0
    def ck(b):
        nonlocal count
        assert b
        count+=1
    archive=[]
    for g in range(100):
        pa=Phase((180+g,28,590,250),(35+g%30,35,35,35),ADDRESSES[g%9],1+g%9)
        archive.append(Snapshot(g,ORIGIN,ROUTE,pa))
    original=tuple(archive)
    for i in range(100):
        a=archive[i]
        for j in range(100):
            b=archive[j]
            d=compare(a,b)
            ck(d["wheels"]==(j-i,0,0,0))
            ck(d["total"]==(j%30)-(i%30))
            ck(d["same_origin"] and d["same_route"] and d["same_addresses"] and d["same_pyramid"])
        state=replay(a)
        ck(state is not None and state["wheels"][0]==180+i)
        state["wheels"][0]=-1234
        ck(archive[i].phase.wheels[0]==180+i)
    ck(original==tuple(archive))
    ck(compare(archive[0],archive[0])["total"]==0)
    malformed=Snapshot(0,ORIGIN,ROUTE,Phase((180,28,590,250),(35,35,35,35),"unknown",2))
    ck(replay(malformed) is None)
    print(f"ECK-022: {count} checks passed; 100 generations, 10,000 pair comparisons")
if __name__=="__main__":test()
