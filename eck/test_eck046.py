"""ECK-046: trainable weak/medium/strong/fusion operator kernels.

This is a synthetic-task regression; the 145 final-test configurations are not read.
Run: python eck/test_eck046.py
"""
def cube(n):
    return (n//81,(n%81)//9,n%9)
def partition(n):
    a,b,c=sorted(cube(n))
    return (7*a+11*b+13*c)%5
def phases(n):
    coded=[0]*9
    for p,a in enumerate(cube(n)):coded[a]+=(1<<p)
    return [[(v>>p)&1 for v in coded] for p in range(3)]
EDGES=tuple((y*3+x,a) for a in range(9) for r,c in [divmod(a,3)]
            for y,x in ((r-1,c),(r+1,c),(r,c-1),(r,c+1))
            if 0<=y<3 and 0<=x<3)
BY_DEST=tuple(tuple(j for j,(_,dst) in enumerate(EDGES) if dst==a) for a in range(9))
TRAIN=tuple(i for i in range(729) if partition(i)<3)
VALID=tuple(i for i in range(729) if partition(i)==3)
FINAL=tuple(i for i in range(729) if partition(i)==4)
def signal(n):
    bits=phases(n)
    features=[[0.]*9 for _ in range(5)]
    for a in range(9):
        neighbor=[bits[0][EDGES[j][0]] for j in BY_DEST[a]]
        features[0][a]=sum(neighbor)/len(neighbor)
        features[1][a]=bits[1][a]
        features[2][a]=bits[2][a]
        features[3][a]=bits[0][a]*bits[2][a]
        features[4][a]=bits[0][a]*bits[1][a]
    return features
def target(n):
    f=signal(n)
    return [(.19+.035*(a//3-a%3))*f[0][a]+.22*f[1][a]
            +(.27-.035*(a//3-a%3))*f[2][a]+.23*f[3][a]+.09*f[4][a]
            for a in range(9)]
def initial():
    return {
        "weak":[.12/len(BY_DEST[dst]) for _,dst in EDGES],
        "medium":[v for _ in range(9) for v in (.025,.16)],
        "strong":[v for _ in range(9) for v in (.22,.025)],
        "fusion":[v for _ in range(9) for v in (.65,.16,.16)]
    }
def copy(w):return {k:v[:] for k,v in w.items()}
def predict(n,w):
    bits=phases(n)
    result=[0.]*9
    for j,(src,dst) in enumerate(EDGES):
        result[dst]+=w["weak"][j]*bits[0][src]
    for a in range(9):
        m,q=2*a,3*a
        near2=sum(bits[2][EDGES[j][0]] for j in BY_DEST[a])/len(BY_DEST[a])
        result[a]+=w["medium"][m]*bits[0][a]+w["medium"][m+1]*bits[1][a]
        result[a]+=w["strong"][m]*bits[2][a]+w["strong"][m+1]*near2
        result[a]+=(w["fusion"][q]*bits[0][a])*(w["fusion"][q+1]*bits[1][a]+w["fusion"][q+2]*bits[2][a])
    return result
def mse(ids,w):
    total=0.
    for n in ids:
        output,desired=predict(n,w),target(n)
        total+=sum((v-t)**2 for v,t in zip(output,desired))
    return total/(len(ids)*9)
def gradient(ids,w):
    g={k:[0.]*len(row) for k,row in w.items()}
    for n in ids:
        bits=phases(n)
        output,desired=predict(n,w),target(n)
        for a in range(9):
            d=2*(output[a]-desired[a])/(len(ids)*9)
            for j in BY_DEST[a]:
                g["weak"][j]+=d*bits[0][EDGES[j][0]]
            near2=sum(bits[2][EDGES[j][0]] for j in BY_DEST[a])/len(BY_DEST[a])
            m,q=2*a,3*a
            g["medium"][m]+=d*bits[0][a]
            g["medium"][m+1]+=d*bits[1][a]
            g["strong"][m]+=d*bits[2][a]
            g["strong"][m+1]+=d*near2
            b0,b1,b2=(bits[k][a] for k in range(3))
            g["fusion"][q]+=d*b0*(w["fusion"][q+1]*b1+w["fusion"][q+2]*b2)
            g["fusion"][q+1]+=d*w["fusion"][q]*b0*b1
            g["fusion"][q+2]+=d*w["fusion"][q]*b0*b2
    return g
def test():
    checks=0
    def ck(ok):
        nonlocal checks
        assert ok
        checks+=1
    ck(len(EDGES)==24)
    ck((len(TRAIN),len(VALID),len(FINAL))==(438,146,145))
    ck(len({cube(i) for i in range(729)})==729)
    w=initial()
    ck(sum(map(len,w.values()))==87)
    old=mse(TRAIN,w);hold=mse(VALID,w)
    g=gradient(TRAIN,w)
    for key,j in (("weak",0),("weak",23),("medium",8),("strong",17),("fusion",0),("fusion",14),("fusion",26)):
        plus=copy(w);minus=copy(w);epsilon=1e-5
        plus[key][j]+=epsilon;minus[key][j]-=epsilon
        numerical=(mse(TRAIN,plus)-mse(TRAIN,minus))/(2*epsilon)
        ck(abs(numerical-g[key][j])<1e-7)
    accepted=0
    for _ in range(50):
        grad=gradient(TRAIN,w)
        proposal={k:[max(-2,min(2,v-1.8*grad[k][j])) for j,v in enumerate(row)]
                  for k,row in w.items()}
        before=mse(TRAIN,w);val_before=mse(VALID,w)
        if mse(TRAIN,proposal)<before-1e-13 and mse(VALID,proposal)<=val_before+1e-12:
            w=proposal;accepted+=1
        ck(mse(VALID,w)<=val_before+1e-12)
    ck(accepted>0)
    ck(mse(TRAIN,w)<old and mse(VALID,w)<hold)
    print(f"ECK-046: {checks} checks PASS; {accepted} accepted epochs; validation MSE {hold:.8f} -> {mse(VALID,w):.8f}; final 145 withheld")
if __name__=="__main__":test()
