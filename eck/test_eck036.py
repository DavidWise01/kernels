"""ECK-036: cube algebra, four force-carrier ablation and recursive 24-slot training."""
from itertools import permutations
NAMES=("WEAK","MEDIUM","STRONG","FUSION")
GAINS=(.20,.25,.30,.25)
TRAIN=(0,1,3,4,5,7)
VALID=(2,6)
STAGES=(1.,.5,1/3,.25)
ORDERS=tuple(permutations(range(4)))
EDGES=tuple((layer,src,dst,src==dst)
 for layer in range(2) for dst in range(9) for src in range(9)
 if abs(src//3-dst//3)+abs(src%3-dst%3)<=1)
def triple(a,b,c):
    assert all(type(v)==int and 0<=v<9 for v in (a,b,c))
    return a*81+b*9+c
def decode(v):
    assert type(v)==int and 0<=v<729
    return v//81,(v%81)//9,v%9
def init():
    return [[.65+.012*c if same else .018+.004*c for layer,src,dst,same in EDGES] for c in range(4)]
def forward(seed,weights,enabled=(True,)*4):
    first=[0.]*9;first[seed]=1
    layers=[first];pre=[]
    for layer in range(2):
        z=[0.]*9
        for j,(depth,src,dst,_) in enumerate(EDGES):
            if depth!=layer:continue
            for c in range(4):
                if enabled[c]:z[dst]+=GAINS[c]*weights[c][j]*layers[layer][src]
        pre.append(z);layers.append([max(0.,v) for v in z])
    return layers,pre
def loss(seed,weights,enabled=(True,)*4):
    output=forward(seed,weights,enabled)[0][-1]
    return sum((y-(1. if i==seed else 0.))**2 for i,y in enumerate(output))/9
def average(seeds,weights,enabled=(True,)*4):
    return sum(loss(seed,weights,enabled) for seed in seeds)/len(seeds)
def epoch(weights,c,rate,limit):
    before=average(TRAIN,weights)
    grad=[[0.]*len(EDGES) for _ in range(4)]
    for seed in TRAIN:
        layers,pre=forward(seed,weights)
        dout=[2*(y-(1. if i==seed else 0.))/9*(pre[1][i]>0) for i,y in enumerate(layers[2])]
        dh=[0.]*9
        for j,(layer,src,dst,_) in enumerate(EDGES):
            if layer==1:dh[src]+=dout[dst]*sum(GAINS[c]*weights[c][j] for c in range(4))
        dh=[v*(pre[0][i]>0) for i,v in enumerate(dh)]
        for j,(layer,src,dst,_) in enumerate(EDGES):
            d=dh[dst] if layer==0 else dout[dst]
            for k in range(4):grad[k][j]+=GAINS[k]*d*layers[layer][src]/len(TRAIN)
    proposed=[[max(-2,min(2,w-rate*grad[k][j])) if k==c else w for j,w in enumerate(row)] for k,row in enumerate(weights)]
    if average(TRAIN,proposed)<before-1e-12 and average(VALID,proposed)<=limit+1e-12:return proposed,True
    return weights,False
def test():
    tests=0
    def ck(ok):
        nonlocal tests
        assert ok
        tests+=1
    ck(3*3*3==27)
    ck((3*3)**3==729)
    ck(len({triple(a,b,c) for a in range(9) for b in range(9) for c in range(9)})==729)
    for n in range(729):ck(triple(*decode(n))==n)
    ck(len(ORDERS)==24)
    ck(len(EDGES)==66)
    weights=init();ck(sum(len(w) for w in weights)==264)
    baseline=average(TRAIN,weights)
    ceiling=average(VALID,weights)+.001
    ablation0=[average(VALID,weights,tuple(k!=c for k in range(4))) for c in range(4)]
    accepted=0
    for order in ORDERS:
        for c in order:
            before=average(TRAIN,weights)
            new,ok=epoch(weights,c,.24*STAGES[c],ceiling)
            if ok:weights=new;accepted+=1
            ck(average(TRAIN,weights)<=before+1e-12)
            ck(average(VALID,weights)<=ceiling+1e-12)
    ck(accepted==96)
    ck(average(TRAIN,weights)<baseline)
    ck(all(x>0 for x in ablation0))
    ck(all(len(w)==66 for w in weights))
    print(f"ECK-036: {tests} assertions PASS; 27 nodes / 729 address triples / 264 carrier weights; 24 slots, {accepted} accepted carrier updates")
if __name__=="__main__":test()
