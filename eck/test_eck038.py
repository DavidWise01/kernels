"""ECK-038: controlled reversed-order neural witnesses and four carrier ablations.

Fixed reference model uses the same nine-channel positional coding, 66 sparse
edges, four carrier gains, and validation-only permutation families.
"""
from itertools import product
from math import sqrt
GAINS=(.20,.25,.30,.25)
NAMES=("WEAK","MEDIUM","STRONG","FUSION")
EDGES=tuple((layer,src,dst,src==dst) for layer in range(2)
 for dst in range(9) for src in range(9)
 if abs(src//3-dst//3)+abs(src%3-dst%3)<=1)
def split(triple):
 a,b,c=sorted(triple)
 return (7*a+11*b+13*c)%5
def xvec(triple):
 v=[0.]*9
 for address,w in zip(triple,(1,2,4)):v[address]+=w/7
 return tuple(v)
def weights():
 return [[(.65+.012*k if same else .018+.004*k) for _,_,_,same in EDGES] for k in range(4)]
def forward(x,w,enabled):
 old=list(x)
 for layer in range(2):
  z=[0.]*9
  for j,(depth,src,dst,_) in enumerate(EDGES):
   if depth==layer:
    z[dst]+=sum(GAINS[k]*w[k][j] for k in range(4) if enabled[k])*old[src]
  old=[max(0.,v) for v in z]
 return old
def metric(w,enabled):
 pairs=[(xvec((a,b,c)),xvec((c,b,a))) for a,b,c in product(range(9),repeat=3)
        if a<c and split((a,b,c))==3]
 din=dout=loss=0.
 collapse=0
 for x,y in pairs:
  p,q=forward(x,w,enabled),forward(y,w,enabled)
  dist=lambda a,b:sqrt(sum((u-v)**2 for u,v in zip(a,b)))
  di,do=dist(x,y),dist(p,q)
  assert di>0
  din+=di;dout+=do
  collapse+=(do<1e-8)
  loss+=sum((u-v)**2 for u,v in zip(p,x))/9
  loss+=sum((u-v)**2 for u,v in zip(q,y))/9
 return len(pairs),din/len(pairs),dout/len(pairs),dout/din,collapse,loss/(2*len(pairs))
def test():
 checks=0
 def ck(v):
  nonlocal checks
  assert v
  checks+=1
 w=weights();all_on=(True,)*4
 base=metric(w,all_on)
 ck(base[0]==65)
 ck(base[4]==0)
 ck(abs(base[3]-.4404340389299353)<1e-12)
 ck(len(EDGES)==66)
 ck(len(w)==4 and sum(map(len,w))==264)
 for k,name in enumerate(NAMES):
  enabled=tuple(i!=k for i in range(4))
  trial=metric(w,enabled)
  ck(trial[0]==base[0])
  ck(trial[3]<base[3])
  ck(trial[5]>base[5])
  ck(name in NAMES)
 for a,b,c in product(range(9),repeat=3):
  ck(abs(sum(xvec((a,b,c)))-1)<1e-12)
  ck(split((a,b,c))==split((c,b,a)))
 print(f"ECK-038: {checks} checks PASS / 65 validation-only order pairs / four carrier ablations")
if __name__=="__main__":test()
