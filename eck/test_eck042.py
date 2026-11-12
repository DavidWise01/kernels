"""ECK-042: three temporally reused 3x3 bit planes; four trainable routing carriers."""
from itertools import product
GAINS=(.20,.25,.30,.25)
def decode(n):return n//81,(n%81)//9,n%9
def encode(t):return 81*t[0]+9*t[1]+t[2]
def partition(t):
 a,b,c=sorted(t)
 return (7*a+11*b+13*c)%5
def vec(t):
 out=[0.]*9
 for p,a in enumerate(t):out[a]+=(1<<p)/7
 return out
CASES=[(n,decode(n),vec(decode(n)),partition(decode(n))) for n in range(729)]
TRAIN=[c for c in CASES if c[3]<3]
VALID=[c for c in CASES if c[3]==3]
FINAL=[c for c in CASES if c[3]==4]
def planes(c):
 bits=[round(7*v) for v in c[2]]
 return [[(v>>p)&1 for v in bits] for p in range(3)]
def target(c):return vec(tuple(reversed(c[1])))
def init():return [[1. if j%4==0 else 0. for j in range(9)] for k in range(4)]
def predict(c,w):
 pl=planes(c);out=[0.]*9
 for a in range(9):
  for j in range(3):
   for i in range(3):
    total=sum(GAINS[k]*w[k][j*3+i] for k in range(4))
    out[a]+=(1<<j)/7*pl[i][a]*total
 return out
def loss(cases,w):
 total=0.
 for c in cases:
  p,t=predict(c,w),target(c)
  total+=sum((v-y)**2 for v,y in zip(p,t))
 return total/(len(cases)*9)
def audit(cases,w):
 correct=0
 for c in cases:
  p,t=predict(c,w),target(c)
  if all(round(max(0,min(7,v*7)))==round(y*7) for v,y in zip(p,t)):correct+=1
 return correct
def epoch(w,rate=10.):
 grad=[[0.]*9 for _ in range(4)]
 for c in TRAIN:
  pl=planes(c);pred=predict(c,w);t=target(c)
  for a in range(9):
   for j in range(3):
    for i in range(3):
     base=2*(pred[a]-t[a])/(9*len(TRAIN))*(1<<j)/7*pl[i][a]
     for k in range(4):grad[k][j*3+i]+=base*GAINS[k]
 next_w=[[max(-3,min(3,v-rate*grad[k][j])) for j,v in enumerate(row)] for k,row in enumerate(w)]
 old,old_val=loss(TRAIN,w),loss(VALID,w)
 if loss(TRAIN,next_w)<old-1e-15 and loss(VALID,next_w)<=old_val+1e-15:return next_w,True
 return w,False
def test():
 checks=0
 def ck(v):
  nonlocal checks
  assert v
  checks+=1
 ck(len(CASES)==729 and (len(TRAIN),len(VALID),len(FINAL))==(438,146,145))
 ck(len({tuple(round(v*7) for v in c[2]) for c in CASES})==729)
 for c in CASES:
  ck(encode(c[1])==c[0])
  ck(encode(tuple(reversed(tuple(reversed(c[1])))))==c[0])
  ck(partition(c[1])==partition(tuple(reversed(c[1]))))
 w=init();begin=loss(VALID,w)
 ck(audit(VALID,w)==16)
 accepted=0
 for i in range(400):
  w,ok=epoch(w)
  if not ok:break
  accepted+=1
 ck(accepted==63)
 ck(audit(VALID,w)==len(VALID))
 ck(loss(VALID,w)<1e-12)
 ck(sum(map(len,w))==36)
 print(f"ECK-042: {checks} checks PASS; {accepted} accepted; 146/146 validation; MSE {begin:.8f} -> {loss(VALID,w):.12f}; final test NOT evaluated")
if __name__=="__main__":test()
