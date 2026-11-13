"""ECK-049 — deterministic seed/cohort robustness checks (no final-test evaluation)."""
from math import sin, cos
def decode(n):return n//81,(n%81)//9,n%9
def partition(n):
 a,b,c=sorted(decode(n))
 return (a*7+b*11+c*13)%5
def code(n):
 x=[0.]*9
 for a,w in zip(decode(n),(1,2,4)):x[a]+=w/7
 return x
def cohorts():
 valid=[i for i in range(729) if partition(i)==3]
 repeated=[i for i in valid if len(set(decode(i)))<3]
 distinct=[i for i in valid if len(set(decode(i)))==3]
 return valid,repeated,distinct
def starting_forge(seed):
 sizes=(24,18,18,27)
 baseline=[[.12/(2 if j%9 in (0,2,6,8) else 3) for j in range(24)],
           [v for _ in range(9) for v in (.025,.16)],
           [v for _ in range(9) for v in (.22,.025)],
           [v for _ in range(9) for v in (.65,.16,.16)]]
 count=0
 for row in baseline:
  for i in range(len(row)):
   count+=1
   row[i]+=.018*sin((seed+1)*37+count*17)
 assert tuple(map(len,baseline))==sizes
 return baseline
def starting_mlp(seed):
 weights=[[.035*sin((h+1)*17+(i+2)*11) for i in range(5)] for h in range(12)]
 biases=[.01*cos(3*h+1) for h in range(12)]
 out=[.04*sin(7*h+3) for h in range(12)]
 count=0
 for row in weights:
  for i in range(len(row)):
   count+=1
   row[i]+=.018*sin((seed+1)*31+count*19)
 for i in range(12):
  count+=1
  out[i]+=.018*cos((seed+1)*23+count*13)
 return weights,biases,out,0.
def test():
 checks=0
 def ck(v):
  nonlocal checks
  assert v
  checks+=1
 valid,rep,distinct=cohorts()
 ck(len(valid)==146)
 ck(len(rep)==44 and len(distinct)==102)
 ck(set(rep).isdisjoint(distinct))
 ck(set(valid)==set(rep)|set(distinct))
 final={i for i in range(729) if partition(i)==4}
 ck(len(final)==145 and final.isdisjoint(valid))
 ck(len({tuple(round(7*v) for v in code(i)) for i in range(729)})==729)
 for seed in range(3):
  forge=starting_forge(seed);mlp=starting_mlp(seed)
  ck(forge==starting_forge(seed))
  ck(mlp==starting_mlp(seed))
  ck(sum(map(len,forge))==87)
  ck(sum(map(len,mlp[0]))+len(mlp[1])+len(mlp[2])+1==85)
 ck(starting_forge(0)!=starting_forge(1))
 ck(starting_mlp(0)!=starting_mlp(1))
 for i in range(729):
  a,b,c=decode(i)
  ck(partition(i)==partition(81*c+9*b+a))
 print(f"ECK-049: {checks} checks PASS; 3 reproducible seeded starts; validation 44 repeated + 102 distinct; final-test 145 withheld")
if __name__=="__main__":test()
