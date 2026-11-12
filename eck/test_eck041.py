"""ECK-041 — exact boomerang teacher vs dense four-carrier student.

Regression emphasizes that a perfect symbolic involution is NOT a trained
neural model. Only validation cases are audited; final-test families remain
untouched.
"""
from itertools import product
GAINS=(.20,.25,.30,.25)
SYNAPSES=tuple((layer,src,dst) for layer in range(2) for dst in range(9) for src in range(9))
def decode(i):return i//81,(i%81)//9,i%9
def encode(a,b,c):return 81*a+9*b+c
def reverse(i):
 a,b,c=decode(i)
 return encode(c,b,a)
def code(triple):
 x=[0.]*9
 for addr,w in zip(triple,(1,2,4)):x[addr]+=w/7
 return x
def partition(triple):
 a,b,c=sorted(triple)
 return (7*a+11*b+13*c)%5
CASES=tuple((i,decode(i),code(decode(i)),partition(decode(i))) for i in range(729))
TRAIN=tuple(c for c in CASES if c[3]<3)
VALID=tuple(c for c in CASES if c[3]==3)
FINAL=tuple(c for c in CASES if c[3]==4)
def initial_weights():
 return [[.65+.012*k if src==dst else .012+.002*k for layer,src,dst in SYNAPSES] for k in range(4)]
def forward(x,weights,bias):
 layers=[list(x)];pre=[]
 for layer in range(2):
  z=bias[layer*9:layer*9+9]
  for j,(depth,src,dst) in enumerate(SYNAPSES):
   if depth==layer:
    z[dst]+=sum(GAINS[k]*weights[k][j] for k in range(4))*layers[layer][src]
  pre.append(z);layers.append([max(0.,v) for v in z])
 return layers,pre
def target(case):return code(decode(reverse(case[0])))
def mse(cases,weights,bias):
 total=0.
 for case in cases:
  y=forward(case[2],weights,bias)[0][-1]
  total+=sum((v-t)**2 for v,t in zip(y,target(case)))/9
 return total/len(cases)
def epoch(weights,bias,rate=.7):
 btrain=mse(TRAIN,weights,bias);bval=mse(VALID,weights,bias)
 grad=[[0.]*162 for _ in range(4)];gb=[0.]*18
 for c in TRAIN:
  layers,pre=forward(c[2],weights,bias);desired=target(c)
  dout=[2*(v-desired[i])/9*(pre[1][i]>0) for i,v in enumerate(layers[-1])]
  dh=[0.]*9
  for j,(layer,src,dst) in enumerate(SYNAPSES):
   if layer==1:dh[src]+=sum(GAINS[k]*weights[k][j] for k in range(4))*dout[dst]
  dh=[v*(pre[0][i]>0) for i,v in enumerate(dh)]
  for i in range(9):gb[i]+=dh[i]/len(TRAIN);gb[i+9]+=dout[i]/len(TRAIN)
  for j,(layer,src,dst) in enumerate(SYNAPSES):
   d=dh[dst] if layer==0 else dout[dst]
   for k in range(4):grad[k][j]+=GAINS[k]*d*layers[layer][src]/len(TRAIN)
 proposed=[[max(-2,min(2,v-rate*grad[k][j])) for j,v in enumerate(row)] for k,row in enumerate(weights)]
 newbias=[max(-.5,min(.5,v-rate*gb[i])) for i,v in enumerate(bias)]
 if mse(TRAIN,proposed,newbias)<btrain-1e-12 and mse(VALID,proposed,newbias)<=bval+1e-12:
  return proposed,newbias,True
 return weights,bias,False
def test():
 checked=0
 def ck(v):
  nonlocal checked
  assert v
  checked+=1
 ck(len(SYNAPSES)==162)
 ck(len(CASES)==729)
 ck((len(TRAIN),len(VALID),len(FINAL))==(438,146,145))
 ck(len({tuple(round(v*7) for v in c[2]) for c in CASES})==729)
 for case in CASES:
  i=case[0]
  ck(reverse(reverse(i))==i)
  ck(partition(decode(reverse(i)))==case[3])
 weights,bias=initial_weights(),[.025]*18
 initial=(mse(TRAIN,weights,bias),mse(VALID,weights,bias))
 archive=[(0,None,initial)]
 accepted=0
 for i in range(50):
  oldtrain,oldvalid=mse(TRAIN,weights,bias),mse(VALID,weights,bias)
  weights,bias,ok=epoch(weights,bias)
  accepted+=ok
  ck(mse(TRAIN,weights,bias)<=oldtrain+1e-12)
  ck(mse(VALID,weights,bias)<=oldvalid+1e-12)
  if ok:archive.append((len(archive),len(archive)-1,(mse(TRAIN,weights,bias),mse(VALID,weights,bias))))
 ck(accepted==50)
 ck(len(archive)==51)
 ck(sum(map(len,weights))==648)
 ck(mse(TRAIN,weights,bias)<initial[0])
 ck(mse(VALID,weights,bias)<initial[1])
 print(f"ECK-041: {checked} checks PASS, {accepted} accepted epochs; train {initial[0]:.8f} -> {mse(TRAIN,weights,bias):.8f}; validation {initial[1]:.8f} -> {mse(VALID,weights,bias):.8f}")
if __name__=="__main__":test()
