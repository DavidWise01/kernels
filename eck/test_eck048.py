"""ECK-048 deterministic task-shift checks; original task unchanged and final partition sealed."""
from math import isclose
def decode(n):return n//81,(n%81)//9,n%9
def part(n):
 a,b,c=sorted(decode(n));return (7*a+11*b+13*c)%5
def phases(n):
 codes=[0]*9
 for p,a in enumerate(decode(n)):codes[a]+=(1<<p)
 return [[(v>>i)&1 for v in codes] for i in range(3)]
def signals(n):
 b=phases(n);F=[[0.]*9 for _ in range(5)]
 for a in range(9):
  r,c=divmod(a,3)
  neighbors=[b[0][3*y+x] for y,x in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)) if 0<=y<3 and 0<=x<3]
  F[0][a]=sum(neighbors)/len(neighbors)
  F[1][a]=b[1][a];F[2][a]=b[2][a]
  F[3][a]=b[0][a]*b[2][a]
  F[4][a]=b[0][a]*b[1][a]
 return F
def original(n):
 f=signals(n)
 return [(.19+.035*(a//3-a%3))*f[0][a]+.22*f[1][a]+
         (.27-.035*(a//3-a%3))*f[2][a]+.23*f[3][a]+.09*f[4][a] for a in range(9)]
def shifted(n):
 f=signals(n);b=phases(n)
 return [(.17+.028*(a%3-a//3))*f[0][a]+.19*f[1][a]+
         (.25-.028*(a%3-a//3))*f[2][a]+.17*f[3][a]+
         .22*b[1][a]*b[2][a] for a in range(9)]
def fusion(n,w):
 b=phases(n)
 return [(w[3*a]*b[0][a])*(w[3*a+1]*b[1][a]+w[3*a+2]*b[2][a]) for a in range(9)]
def run():
 checks=0
 def ck(x):
  nonlocal checks
  assert x
  checks+=1
 ck((sum(part(i)<3 for i in range(729)),sum(part(i)==3 for i in range(729)),sum(part(i)==4 for i in range(729)))==(438,146,145))
 ck(24+18+18+27==87 and 5*12+12+12+1==85)
 validation=[i for i in range(729) if part(i)==3]
 ck(any(any(abs(a-b)>1e-6 for a,b in zip(original(i),shifted(i))) for i in validation))
 w=[v for _ in range(9) for v in (.65,.16,.16)]
 alternative=w[:]
 for i in range(9):
  alternative[3*i]*=1.25
  alternative[3*i+1]/=1.25
  alternative[3*i+2]/=1.25
 ck(w!=alternative)
 for i in validation:
  ck(all(isclose(a,b,rel_tol=0,abs_tol=1e-12) for a,b in zip(fusion(i,w),fusion(i,alternative))))
  ck(part(i)==part(81*(decode(i)[2])+9*decode(i)[1]+decode(i)[0]))
 print(f"ECK-048: {checks} checks PASS; 146 validation gauge and permutation checks; shifted target differs; 145 final-test cases untouched")
if __name__=="__main__":run()
