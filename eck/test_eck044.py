"""ECK-044: functional, noninterchangeable carrier features + retrained fusion-off comparator.

Diagnostic task explicitly contains nonlinear x0*x2 coincidence. No claim of
independently learned real-world physical-force specialization.
"""
from itertools import product
def decode(n):return n//81,(n%81)//9,n%9
def split(triple):
    a,b,c=sorted(triple)
    return (7*a+11*b+13*c)%5
def case(n):
    t=decode(n)
    raw=[0]*9
    for pos,a in enumerate(t):raw[a]+=1<<pos
    bits=[[((v>>p)&1) for v in raw] for p in range(3)]
    return bits
CASES=[(n,split(decode(n))) for n in range(729)]
TRAIN=[n for n,s in CASES if s<3]
VALID=[n for n,s in CASES if s==3]
FINAL=[n for n,s in CASES if s==4]
TRUTH=(.2,.2,.2,.4)
def features(n):
    bits=case(n);f=[[0.]*9 for _ in range(4)]
    for a in range(9):
        r,c=divmod(a,3)
        adj=[bits[0][3*rr+cc] for rr,cc in ((r+1,c),(r-1,c),(r,c+1),(r,c-1))
             if 0<=rr<3 and 0<=cc<3]
        f[0][a]=sum(adj)/len(adj)
        f[1][a]=bits[1][a]
        f[2][a]=bits[2][a]
        f[3][a]=bits[0][a]*bits[2][a]
    return f
def loss(ids,coef):
    total=0.
    for n in ids:
        f=features(n)
        for a in range(9):
            p=sum(coef[k]*f[k][a] for k in range(4))
            t=sum(TRUTH[k]*f[k][a] for k in range(4))
            total+=(p-t)**2
    return total/(len(ids)*9)
def epoch(ids,valid,coef,allow_fusion,rate=.85):
    train_before=loss(ids,coef);valid_before=loss(valid,coef)
    grad=[0.]*4
    for n in ids:
        f=features(n)
        for a in range(9):
            err=sum((coef[k]-TRUTH[k])*f[k][a] for k in range(4))
            for k in range(4):
                if k<3 or allow_fusion:grad[k]+=2*err*f[k][a]/(len(ids)*9)
    next_coef=[max(-2,min(2,coef[k]-rate*grad[k])) if (k<3 or allow_fusion) else 0. for k in range(4)]
    if loss(ids,next_coef)<train_before-1e-13 and loss(valid,next_coef)<=valid_before+1e-12:
        return next_coef,True
    return coef,False
def test():
    checks=0
    def ck(v):
        nonlocal checks
        assert v
        checks+=1
    ck((len(TRAIN),len(VALID),len(FINAL))==(438,146,145))
    ck(len({decode(i) for i in range(729)})==729)
    for n in range(729):
        ck(split(decode(n))==split(tuple(reversed(decode(n)))))
    runs=[[0.]*4,[0.]*4]
    accepted=[0,0]
    for i in range(600):
        flags=[]
        for k in range(2):
            old=loss(VALID,runs[k])
            runs[k],ok=epoch(TRAIN,VALID,runs[k],allow_fusion=(k==0))
            accepted[k]+=ok
            ck(loss(VALID,runs[k])<=old+1e-12)
            flags.append(ok)
        if not any(flags):break
    ck(accepted[0]>accepted[1])
    ck(loss(VALID,runs[0])<1e-9)
    ck(loss(VALID,runs[1])>1e-3)
    ck(runs[1][3]==0)
    ck(all(abs(runs[0][k]-TRUTH[k])<.001 for k in range(4)))
    print(f"ECK-044: {checks} checks PASS; full val={loss(VALID,runs[0]):.12g}; fusion-off val={loss(VALID,runs[1]):.8f}; final test unopened")
if __name__=="__main__":test()
