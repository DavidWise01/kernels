"""ECK-045 — adaptive 3×3 carrier coefficients, comparison models, gradient check.

Run: python eck/test_eck045.py
The final-test partition is intentionally never evaluated.
"""
from itertools import product
def decode(n):return n//81,(n%81)//9,n%9
def split(t):
    a,b,c=sorted(t)
    return (7*a+11*b+13*c)%5
def features(n):
    t=decode(n)
    raw=[0]*9
    for phase,address in enumerate(t):raw[address]+=1<<phase
    bits=[[((v>>p)&1) for v in raw] for p in range(3)]
    out=[[0.]*9 for _ in range(5)]
    for a in range(9):
        r,c=divmod(a,3)
        neighbors=[bits[0][3*y+x] for y,x in ((r-1,c),(r+1,c),(r,c-1),(r,c+1))
                   if 0<=y<3 and 0<=x<3]
        out[0][a]=sum(neighbors)/len(neighbors)
        out[1][a]=bits[1][a]
        out[2][a]=bits[2][a]
        out[3][a]=bits[0][a]*bits[2][a]
        out[4][a]=bits[0][a]*bits[1][a]
    return out
def target(f):
    return [(.19+.035*(a//3-a%3))*f[0][a]+.22*f[1][a]
            +(.27-.035*(a//3-a%3))*f[2][a]+.23*f[3][a]+.09*f[4][a]
            for a in range(9)]
DATA=tuple((i,features(i),split(decode(i))) for i in range(729))
TRAIN=tuple((f,target(f)) for i,f,s in DATA if s<3)
VALID=tuple((f,target(f)) for i,f,s in DATA if s==3)
def loss(cases,weights,per_address):
    total=0.
    for f,t in cases:
        for a in range(9):
            p=sum(weights[k][a if per_address else 0]*f[k][a] for k in range(len(weights)))
            total+=(p-t[a])**2
    return total/(len(cases)*9)
def gradient(cases,weights,per_address):
    g=[[0.]*len(row) for row in weights]
    for f,t in cases:
        for a in range(9):
            p=sum(weights[k][a if per_address else 0]*f[k][a] for k in range(len(weights)))
            for k in range(len(weights)):
                g[k][a if per_address else 0]+=2*(p-t[a])*f[k][a]/(len(cases)*9)
    return g
def train(k,per_address,epochs=500,rate=1.1):
    w=[[0.]*(9 if per_address else 1) for _ in range(k)]
    initial=loss(VALID,w,per_address)
    accepted=0
    for _ in range(epochs):
        g=gradient(TRAIN,w,per_address)
        prop=[[max(-2,min(2,v-rate*g[i][j])) for j,v in enumerate(row)]
              for i,row in enumerate(w)]
        if loss(TRAIN,prop,per_address)<loss(TRAIN,w,per_address)-1e-13 and loss(VALID,prop,per_address)<=loss(VALID,w,per_address)+1e-12:
            w=prop
            accepted+=1
    return w,initial,accepted
def test():
    checks=0
    def ck(value):
        nonlocal checks
        assert value
        checks+=1
    ck(len(DATA)==729)
    ck(len(TRAIN)==438 and len(VALID)==146)
    ck(len({decode(i) for i,_,_ in DATA})==729)
    ck(all(split(decode(i))==split(tuple(reversed(decode(i)))) for i,_,_ in DATA))
    w0=[[0.]*9 for _ in range(4)]
    g=gradient(TRAIN,w0,True)
    h=1e-5
    for k,a in ((0,0),(1,4),(2,8),(3,2),(3,7)):
        positive=[row[:] for row in w0]
        negative=[row[:] for row in w0]
        positive[k][a]+=h;negative[k][a]-=h
        finite=(loss(TRAIN,positive,True)-loss(TRAIN,negative,True))/(2*h)
        ck(abs(finite-g[k][a])<1e-8)
    runs=[train(4,True),train(4,False),train(5,False)]
    scores=[loss(VALID,runs[i][0],i==0) for i in range(3)]
    ck(scores[0]<scores[1])
    ck(scores[0]<scores[2])
    ck(all(score<.001 for score in scores))
    ck(len(runs[0][0])==4 and sum(map(len,runs[0][0]))==36)
    print(f"ECK-045: {checks} checks PASS; adaptive {scores[0]:.9f}, shared {scores[1]:.9f}, nonlinear reference {scores[2]:.9f}; final test withheld")
if __name__=="__main__":test()
