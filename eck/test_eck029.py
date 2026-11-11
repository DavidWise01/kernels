"""ECK-029: deterministic weighted propagation through a 3x3x3 generational mesh."""
NODES=tuple((g,r,c) for g in range(3) for r in range(3) for c in range(3))
def idx(g,r,c): return g*9+r*3+c
def tick(old,inter=0.72,local=0.12):
    if len(old)!=27 or not 0<=inter<=1 or not 0<=local<=0.4:
        raise ValueError("invalid network state or weights")
    result=[0.0]*27
    for g,r,c in NODES:
        j=idx(g,r,c)
        v=0.35*old[j]
        for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
            rr,cc=r+dr,c+dc
            if 0<=rr<3 and 0<=cc<3:
                v+=local*old[idx(g,rr,cc)]
        if g>0:v+=inter*old[idx(g-1,r,c)]
        result[j]=min(1.0,max(0.0,v))
    return result
def approx(a,b):return abs(a-b)<1e-12
def test():
    assertions=0
    def ck(x):
        nonlocal assertions
        assert x
        assertions+=1
    initial=[0.0]*27;initial[idx(0,1,1)]=1.0
    first=tick(initial)
    second=tick(first)
    ck(approx(first[idx(0,1,1)],.35))
    ck(approx(first[idx(0,0,1)],.12))
    ck(approx(first[idx(1,1,1)],.72))
    ck(all(x==0 for x in first[18:]))
    ck(second[idx(2,1,1)]>0)
    ck(initial[idx(0,1,1)]==1)
    ck(tick([0.0]*27)==[0.0]*27)
    for lw in (0,.12,.4):
        for iw in (0,.72,1):
            state=initial[:]
            for _ in range(30):
                state=tick(state,iw,lw)
                ck(len(state)==27)
                ck(all(0<=x<=1 for x in state))
    ck(sum(first[:9])>0)
    ck(sum(first[9:18])>0)
    ck(sum(first[18:])==0)
    ck(sum(second[18:])>0)
    print(f"ECK-029: {assertions} assertions PASS, 3 generations and 27 nodes")
if __name__=="__main__":test()
