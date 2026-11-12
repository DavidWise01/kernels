"""ECK-040: separate 729-triple neural boomerang reversal, strict validation gate."""
from itertools import permutations
GAINS=(.20,.25,.30,.25)
STAGES=(1.,.5,1/3,.25)
EDGES=tuple((layer,src,dst,src==dst) for layer in range(2) for dst in range(9)
 for src in range(9) if abs(src//3-dst//3)+abs(src%3-dst%3)<=1)
def decode(n):return n//81,(n%81)//9,n%9
def encode(a,b,c):return 81*a+9*b+c
def vector(t):
 out=[0.]*9
 for x,w in zip(t,(1,2,4)):out[x]+=w/7
 return tuple(out)
def split(t):
 a,b,c=sorted(t)
 return (a*7+b*11+c*13)%5
CASES=tuple((n,decode(n),vector(decode(n)),split(decode(n))) for n in range(729))
TRAIN=tuple(c for c in CASES if c[3]<=2)
VALID=tuple(c for c in CASES if c[3]==3)
TEST=tuple(c for c in CASES if c[3]==4)
def weights():
 return [[(.65+.012*k if same else .018+.004*k) for _,_,_,same in EDGES] for k in range(4)]
def forward(x,w):
 layers=[list(x)];pre=[]
 for layer in range(2):
  z=[0.]*9
  for j,(depth,src,dst,_) in enumerate(EDGES):
   if depth!=layer:continue
   z[dst]+=sum(GAINS[k]*w[k][j] for k in range(4))*layers[layer][src]
  pre.append(z);layers.append([max(0.,v) for v in z])
 return layers,pre
def target(c):
 a,b,d=c[1]
 return vector((d,b,a))
def mean(cases,w):
 total=0.
 for c in cases:
  y=forward(c[2],w)[0][-1]
  total+=sum((p-t)**2 for p,t in zip(y,target(c)))/9
 return total/len(cases)
def epoch(w,rate,carrier):
 prev=mean(TRAIN,w);old_val=mean(VALID,w)
 grads=[[0.]*len(EDGES) for _ in range(4)]
 for c in TRAIN:
  layers,pre=forward(c[2],w);t=target(c)
  dout=[(2/9)*(y-t[i])*(pre[1][i]>0) for i,y in enumerate(layers[-1])]
  dh=[0.]*9
  for j,(layer,src,dst,_) in enumerate(EDGES):
   if layer==1:dh[src]+=dout[dst]*sum(GAINS[k]*w[k][j] for k in range(4))
  dh=[v*(pre[0][i]>0) for i,v in enumerate(dh)]
  for j,(layer,src,dst,_) in enumerate(EDGES):
   d=dh[dst] if layer==0 else dout[dst]
   grads[carrier][j]+=GAINS[carrier]*d*layers[layer][src]/len(TRAIN)
 proposal=[[max(-2.,min(2.,v-rate*grads[k][j])) for j,v in enumerate(row)] for k,row in enumerate(w)]
 if mean(TRAIN,proposal)<prev-1e-12 and mean(VALID,proposal)<=old_val+1e-12:return proposal,True
 return w,False
def test():
 count=0
 def check(cond):
  nonlocal count
  assert cond
  count+=1
 check(len(EDGES)==66)
 check(len(CASES)==729)
 check((len(TRAIN),len(VALID),len(TEST))==(438,146,145))
 check(len({vector(c[1]) for c in CASES})==729)
 for c in CASES:
  t=c[1]
  check(decode(encode(*t))==t)
  check(decode(encode(*reversed(t)))==tuple(reversed(t)))
  check(split(t)==split(tuple(reversed(t))))
 w=weights();base_train=mean(TRAIN,w);base_val=mean(VALID,w)
 archive=[(0,None,tuple(tuple(v) for v in w),base_train,base_val)]
 accepted=0
 for slot,order in enumerate(permutations(range(4))):
  stage=order[slot%4]
  oldtrain,oldval=mean(TRAIN,w),mean(VALID,w)
  w,ok=epoch(w,.24*STAGES[stage],stage)
  accepted+=ok
  if ok:archive.append((len(archive),len(archive)-1,tuple(tuple(v) for v in w),mean(TRAIN,w),mean(VALID,w)))
  check(mean(TRAIN,w)<=oldtrain+1e-12)
  check(mean(VALID,w)<=oldval+1e-12)
 check(accepted==24)
 check(len(archive)==25)
 check(all(row[1]==idx-1 for idx,row in enumerate(archive) if idx>0))
 check(mean(TRAIN,w)<base_train and mean(VALID,w)<base_val)
 check(archive[0][2]!=archive[-1][2])
 print(f"ECK-040: {count} checks PASS; {accepted} accepted; reversal train {base_train:.8f} -> {mean(TRAIN,w):.8f}; validation {base_val:.8f} -> {mean(VALID,w):.8f}; final test withheld")
if __name__=="__main__":test()
