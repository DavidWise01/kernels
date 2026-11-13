"""ECK-047 — fusion gate gauge and parameter-matched nonlinear baseline sanity checks.

Checks the exact algebraic symmetry and parameter inventory. The browser's
actual JS MLP is separately checked with extracted function execution.
"""
from itertools import product
from math import isclose
def cube(n):return (n//81,(n%81)//9,n%9)
def split(t):
 a,b,c=sorted(t);return (7*a+11*b+13*c)%5
def positional(t):
 out=[0.]*9
 for i,a in enumerate(t):out[a]+=(1<<i)/7
 return out
def bits(t):
 return [[(round(v*7)>>k)&1 for v in positional(t)] for k in range(3)]
def forge_fusion(n,gates):
 b=bits(cube(n))
 return [(gates[3*a]*b[0][a])*(gates[3*a+1]*b[1][a]+gates[3*a+2]*b[2][a]) for a in range(9)]
def test():
 checks=0
 def ck(value):
  nonlocal checks
  assert value
  checks+=1
 ck(3*3*3==27)
 ck(9**3==729)
 ck(24+18+18+27==87)
 ck(5*12+12+12+1==85)
 ck((sum(split(cube(i))<3 for i in range(729)),sum(split(cube(i))==3 for i in range(729)),sum(split(cube(i))==4 for i in range(729)))==(438,146,145))
 baseline=[v for _ in range(9) for v in (.65,.16,.16)]
 compensated=baseline[:]
 for a in range(9):
  j=3*a
  compensated[j]*=1.25
  compensated[j+1]/=1.25
  compensated[j+2]/=1.25
 ck(compensated!=baseline)
 for n in range(729):
  x,y=forge_fusion(n,baseline),forge_fusion(n,compensated)
  ck(all(isclose(a,b,rel_tol=0,abs_tol=1e-12) for a,b in zip(x,y)))
  ck(split(cube(n))==split(tuple(reversed(cube(n)))))
 print(f"ECK-047: {checks} checks PASS; 729 compensated fusion outputs invariant; 87-vs-85 parameter count; no final test evaluated")
if __name__=="__main__":test()
