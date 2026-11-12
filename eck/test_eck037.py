"""ECK-037 — 729 distinct ordered triples through 27-node four-carrier neural net.

Pure reference test, no live browser requirement. The test partition is never
used by the optimizer. All permutations of a multiset stay in one split.
"""
from itertools import product
from collections import defaultdict
GAINS=(.20,.25,.30,.25)
STAGES=(1.,.5,1/3,.25)
EDGES=tuple((layer,src,dst,src==dst)
 for layer in range(2) for dst in range(9) for src in range(9)
 if abs(src//3-dst//3)+abs(src%3-dst%3)<=1)

def encode(a,b,c):
    assert all(type(x)==int and 0<=x<9 for x in (a,b,c))
    return 81*a+9*b+c
def decode(n):
    assert type(n)==int and 0<=n<729
    return (n//81,(n%81)//9,n%9)
def input_code(triple):
    v=[0.]*9
    for address,weight in zip(triple,(1,2,4)):v[address]+=weight/7
    return tuple(v)
def partition(triple):
    a,b,c=sorted(triple)
    return (7*a+11*b+13*c)%5

CASES=tuple((n,decode(n),input_code(decode(n)),partition(decode(n))) for n in range(729))
TRAIN=tuple(c for c in CASES if c[3]<=2)
VALID=tuple(c for c in CASES if c[3]==3)
TEST=tuple(c for c in CASES if c[3]==4)

def weights_init():
    return [[(.65+.012*k) if same else (.018+.004*k) for _,_,_,same in EDGES] for k in range(4)]
def forward(x,weights):
    layers=[list(x)];pre=[]
    for layer in range(2):
        z=[0.]*9
        for j,(depth,src,dst,_) in enumerate(EDGES):
            if depth!=layer:continue
            w=sum(GAINS[k]*weights[k][j] for k in range(4))
            z[dst]+=w*layers[layer][src]
        pre.append(z)
        layers.append([max(0.,v) for v in z])
    return layers,pre
def mean_loss(cases,weights):
    errors=0.
    for _,_,target,_ in cases:
        result=forward(target,weights)[0][2]
        errors+=sum((y-t)**2 for y,t in zip(result,target))/9
    return errors/len(cases)
def train_epoch(weights,carrier,rate,ceiling):
    initial=mean_loss(TRAIN,weights)
    gradients=[[0.]*len(EDGES) for _ in range(4)]
    for _,_,target,_ in TRAIN:
        layers,pre=forward(target,weights)
        dout=[2/9*(y-t)*(pre[1][i]>0) for i,(y,t) in enumerate(zip(layers[2],target))]
        dh=[0.]*9
        for j,(layer,src,dst,_) in enumerate(EDGES):
            if layer==1:
                dh[src]+=dout[dst]*sum(GAINS[k]*weights[k][j] for k in range(4))
        dh=[v*(pre[0][i]>0) for i,v in enumerate(dh)]
        for j,(layer,src,dst,_) in enumerate(EDGES):
            delta=dh[dst] if layer==0 else dout[dst]
            if carrier is None:
                for k in range(4):
                    gradients[k][j]+=GAINS[k]*delta*layers[layer][src]/len(TRAIN)
            else:
                gradients[carrier][j]+=GAINS[carrier]*delta*layers[layer][src]/len(TRAIN)
    proposal=[[max(-2,min(2,v-rate*gradients[k][j])) for j,v in enumerate(row)] for k,row in enumerate(weights)]
    after=mean_loss(TRAIN,proposal)
    hold=mean_loss(VALID,proposal)
    return (proposal,True) if after<initial-1e-12 and hold<=ceiling+1e-12 else (weights,False)

def test():
    checks=0
    def ck(ok):
        nonlocal checks
        assert ok
        checks+=1
    ck(len(CASES)==729)
    ck(len(TRAIN)==438 and len(VALID)==146 and len(TEST)==145)
    ck(len(EDGES)==66)
    ck(len({tuple(round(x*7) for x in c[2]) for c in CASES})==729)
    fam=defaultdict(set)
    for n,triple,x,split in CASES:
        ck(encode(*decode(n))==n)
        ck(abs(sum(x)-1)<1e-12)
        fam[tuple(sorted(triple))].add(split)
    ck(len(fam)==165)
    ck(all(len(parts)==1 for parts in fam.values()))
    w=weights_init()
    start=mean_loss(TRAIN,w)
    initial_val=mean_loss(VALID,w)
    ceiling=initial_val+.002
    accepted=0
    # 24 symbolic slot permutations: each uses one chosen stage's carrier.
    from itertools import permutations
    for slot,order in enumerate(permutations(range(4))):
        carrier=order[slot%4]
        before=mean_loss(TRAIN,w)
        w,ok=train_epoch(w,carrier,.24*STAGES[carrier],ceiling)
        accepted+=ok
        ck(mean_loss(TRAIN,w)<=before+1e-12)
        ck(mean_loss(VALID,w)<=ceiling+1e-12)
    ck(accepted==24)
    ck(mean_loss(TRAIN,w)<start)
    ck(len(w)==4 and sum(map(len,w))==264)
    print(f"ECK-037: {checks} assertions PASS; 729 distinct ordered inputs; 24 accepted carrier iterations; train {start:.8f} -> {mean_loss(TRAIN,w):.8f}; validation {initial_val:.8f} -> {mean_loss(VALID,w):.8f}")

if __name__=="__main__":test()
