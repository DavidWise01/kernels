"""ECK-030 — bounded recursive self-improving 27-node iteration."""
from dataclasses import dataclass
NODES=tuple((g,r,c) for g in range(3) for r in range(3) for c in range(3))
def index(g,r,c):return g*9+r*3+c
def tick(old,inter,local):
    new=[0.0]*27
    for g,r,c in NODES:
        val=.35*old[index(g,r,c)]
        for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
            rr,cc=r+dr,c+dc
            if 0<=rr<3 and 0<=cc<3:val+=local*old[index(g,rr,cc)]
        if g>0:val+=inter*old[index(g-1,r,c)]
        new[index(g,r,c)]=min(1.0,max(0.0,val))
    return new
def evaluation(inter,local):
    data=[0.0]*27
    data[index(0,1,1)]=1
    for _ in range(2):data=tick(data,inter,local)
    target=data[index(2,1,1)]
    spill=sum(data)-target
    return target-.02*spill
def clipped(i,l):
    return (round(max(0,min(1,i)),2),round(max(0,min(.4,l)),2))
def iteration(i,l):
    previous=evaluation(i,l)
    best=(i,l,previous)
    for di,dl in ((.05,0),(-.05,0),(0,.05),(0,-.05),(.05,-.05),(-.05,.05)):
        ni,nl=clipped(i+di,l+dl)
        score=evaluation(ni,nl)
        if score>best[2]+1e-10:best=(ni,nl,score)
    return best,best[2]>previous+1e-10
def test():
    count=0
    def ck(condition):
        nonlocal count
        assert condition
        count+=1
    i,l=.72,.12
    baseline=evaluation(i,l)
    archive=[]
    accepted=0
    for attempt in range(30):
        prior=(i,l,evaluation(i,l))
        (i2,l2,score),did_accept=iteration(i,l)
        if did_accept:i,l=i2,l2;accepted+=1
        archive.append((attempt,prior,(i2,l2,score),did_accept))
        ck(score+1e-10>=prior[2])
        ck(0<=i<=1 and 0<=l<=.4)
        ck(evaluation(i,l)+1e-10>=prior[2])
        ck(archive[-1][0]==attempt)
    ck(len(archive)==30)
    ck(accepted>0)
    ck(evaluation(i,l)>baseline)
    ck(i==1 and l==0)
    ck(all(a[3] or a[1][2]==a[2][2] for a in archive))
    ck(archive[0][1][:2]==(.72,.12))
    print(f"ECK-030: {count} assertions passed; accepted {accepted}/30; score {baseline:.5f} -> {evaluation(i,l):.5f}")
if __name__=="__main__":test()
