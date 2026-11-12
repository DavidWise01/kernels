"""ECK-033 — four ordered search strategies with disjoint seed/target holdouts."""
from itertools import permutations

STAGES=(1,.5,1/3,.25)
ORDERS=tuple(permutations(range(4)))
TRAIN=((1,1),(0,0))
HOLDOUT=((0,1),(2,2))
DIRECTIONS={
 0:((1,0),(-1,0),(0,1),(0,-1)),
 1:((1,1),(1,-1),(-1,1),(-1,-1)),
 2:((2,-1),(-2,1),(1,-2),(-1,2)),
 3:((1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)),
}
def idx(g,r,c):return 9*g+3*r+c
def tick(old,inter,local):
    out=[0.]*27
    for g in range(3):
        for r in range(3):
            for c in range(3):
                v=.35*old[idx(g,r,c)]
                for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                    rr,cc=r+dr,c+dc
                    if 0<=rr<3 and 0<=cc<3:v+=local*old[idx(g,rr,cc)]
                if g:v+=inter*old[idx(g-1,r,c)]
                out[idx(g,r,c)]=max(0.,min(1.,v))
    return out
def score_case(inter,local,r,c):
    a=[0.]*27;a[idx(0,r,c)]=1.
    a=tick(tick(a,inter,local),inter,local)
    target=a[idx(2,r,c)]
    return target-.02*(sum(a)-target)
def score(inter,local,cases):
    return sum(score_case(inter,local,r,c) for r,c in cases)/len(cases)
def quantized(i,l):
    return (round(max(0.,min(1.,i)),2),round(max(0.,min(.4,l)),2))
def improve(inter,local,order):
    assert len(order)==4 and len(set(order))==4
    btrain=score(inter,local,TRAIN);bhold=score(inter,local,HOLDOUT)
    best=(inter,local,btrain,bhold)
    checks=0
    for stage in order:
        step=max(.01,round(5*STAGES[stage])/100)
        winner=best
        for di,dl in DIRECTIONS[stage]:
            ci,cl=quantized(best[0]+step*di,best[1]+step*dl)
            train,hold=score(ci,cl,TRAIN),score(ci,cl,HOLDOUT)
            checks+=1
            if train>winner[2]+1e-10 and hold+1e-10>=bhold and hold+1e-10>=winner[3]:
                winner=(ci,cl,train,hold)
        best=winner
    accepted=best[2]>btrain+1e-10 and best[3]+1e-10>=bhold
    return (best if accepted else (inter,local,btrain,bhold)),accepted,checks
def test():
    assertions=0
    def ck(v):
        nonlocal assertions
        assert v
        assertions+=1
    ck(len(ORDERS)==24)
    ck(set(TRAIN).isdisjoint(HOLDOUT))
    ck(len(set(DIRECTIONS.keys()))==4)
    i,l=.72,.12
    first=(score(i,l,TRAIN),score(i,l,HOLDOUT))
    archive=[]
    total=0
    for iteration,order in enumerate(ORDERS):
        btrain,bhold=score(i,l,TRAIN),score(i,l,HOLDOUT)
        result,accepted,n=improve(i,l,order)
        i,l=result[:2]
        atrain,ahold=score(i,l,TRAIN),score(i,l,HOLDOUT)
        total+=n
        archive.append((iteration,order,accepted,btrain,bhold,atrain,ahold))
        ck(atrain+1e-10>=btrain)
        ck(ahold+1e-10>=bhold)
        ck(n==20)
        ck(len(archive)==iteration+1)
        ck(0<=i<=1 and 0<=l<=.4)
    ck(total==480)
    ck(sum(v[2] for v in archive)==3)
    ck(len(archive)==24)
    ck((i,l)==(1.,0.))
    ck(score(i,l,TRAIN)>first[0])
    ck(score(i,l,HOLDOUT)>first[1])
    print(f"ECK-033: {assertions} checks passed / 24 iterations / {total} candidates / 3 accepted")
if __name__=="__main__":test()
