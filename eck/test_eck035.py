"""ECK-035 — four carrier sparse neural net, feed-forward and backprop regression."""
NAMES=("WEAK","MEDIUM","STRONG","FUSION")
GAINS=(.20,.25,.30,.25)
TRAIN=(0,1,3,4,5,7)
VALID=(2,6)
TEST=(8,)
EDGES=tuple((layer,src,dst,src==dst)
 for layer in range(2) for dst in range(9) for src in range(9)
 if abs(src//3-dst//3)+abs(src%3-dst%3)<=1)
def init():
    return [[(.65+.012*c if identity else .018+.004*c) for layer,src,dst,identity in EDGES] for c in range(4)]
def forward(seed,weights):
    a=[0.]*9;a[seed]=1.
    layers=[a];pre=[]
    for layer in range(2):
        z=[0.]*9
        for j,(depth,src,dst,_) in enumerate(EDGES):
            if depth!=layer:continue
            for c in range(4):z[dst]+=GAINS[c]*weights[c][j]*layers[layer][src]
        pre.append(z);layers.append([max(0.,v) for v in z])
    return layers,pre
def loss(seed,weights):
    out=forward(seed,weights)[0][-1]
    return sum((v-(1. if i==seed else 0.))**2 for i,v in enumerate(out))/9
def mean_loss(seeds,weights):
    return sum(loss(seed,weights) for seed in seeds)/len(seeds)
def epoch(weights,ceiling,rate=.24):
    before,validation=mean_loss(TRAIN,weights),mean_loss(VALID,weights)
    gradients=[[0.]*len(EDGES) for _ in range(4)]
    for seed in TRAIN:
        layers,pre=forward(seed,weights)
        d_out=[2*(v-(1. if i==seed else 0.))/9*(1. if pre[1][i]>0 else 0.) for i,v in enumerate(layers[-1])]
        d_hidden=[0.]*9
        for j,(layer,src,dst,_) in enumerate(EDGES):
            if layer==1:d_hidden[src]+=d_out[dst]*sum(GAINS[c]*weights[c][j] for c in range(4))
        d_hidden=[v*(1. if pre[0][i]>0 else 0.) for i,v in enumerate(d_hidden)]
        for j,(layer,src,dst,_) in enumerate(EDGES):
            d=d_hidden[dst] if layer==0 else d_out[dst]
            for c in range(4):gradients[c][j]+=GAINS[c]*d*layers[layer][src]/len(TRAIN)
    next_weights=[[max(-2.,min(2.,weights[c][j]-rate*gradients[c][j]))
        for j in range(len(EDGES))] for c in range(4)]
    if mean_loss(TRAIN,next_weights)<before-1e-12 and mean_loss(VALID,next_weights)<=ceiling+1e-12:
        return next_weights,True
    return weights,False
def test():
    checks=0
    def ck(v):
        nonlocal checks
        assert v
        checks+=1
    ck(len(EDGES)==66)
    ck(len(NAMES)==4)
    ck(set(TRAIN).isdisjoint(VALID) and set(TRAIN).isdisjoint(TEST) and set(VALID).isdisjoint(TEST))
    ck(len(set((e[0],e[1],e[2]) for e in EDGES))==66)
    weights=init();initial_train=mean_loss(TRAIN,weights)
    initial_validation=mean_loss(VALID,weights);ceiling=initial_validation+.001
    accepted=0
    for i in range(50):
        prev=mean_loss(TRAIN,weights)
        weights,did=epoch(weights,ceiling)
        accepted+=did
        ck(mean_loss(TRAIN,weights)<=prev+1e-12)
        ck(mean_loss(VALID,weights)<=ceiling+1e-12)
        ck(len(weights)==4 and all(len(w)==66 for w in weights))
    ck(accepted==50)
    ck(mean_loss(TRAIN,weights)<initial_train)
    ck(all(len(forward(i,weights)[0])==3 for i in range(9)))
    print(f"ECK-035: {checks} checks PASS, {accepted} accepted epochs, train MSE {initial_train:.8f} -> {mean_loss(TRAIN,weights):.8f}; validation {initial_validation:.8f} -> {mean_loss(VALID,weights):.8f}")
if __name__=="__main__":test()
