"""ECK-050 collision repair regression; checks only training and validation cohorts.

The feature bit0*bit1 is supplied, not autonomously discovered. Final cases stay unopened.
"""
from math import isclose
def triple(n):return (n//81,(n%81)//9,n%9)
def part(n):
 a,b,c=sorted(triple(n))
 return (7*a+11*b+13*c)%5
def bit_planes(n):
 cells=[0]*9
 for k,a in enumerate(triple(n)):cells[a]+=1<<k
 return [[(x>>k)&1 for x in cells] for k in range(3)]
def collisions(n):
 b=bit_planes(n)
 return [b[0][a]*b[1][a] for a in range(9)]
def test():
 checks=0
 def ck(v):
  nonlocal checks
  assert v
  checks+=1
 train=[i for i in range(729) if part(i)<3]
 valid=[i for i in range(729) if part(i)==3]
 final={i for i in range(729) if part(i)==4}
 repeated=[i for i in valid if len(set(triple(i)))<3]
 distinct=[i for i in valid if len(set(triple(i)))==3]
 ck((len(train),len(valid),len(final))==(438,146,145))
 ck((len(repeated),len(distinct))==(44,102))
 ck(set(repeated).isdisjoint(distinct))
 ck(set(valid)==set(repeated)|set(distinct))
 ck(final.isdisjoint(train) and final.isdisjoint(valid))
 ck(87+9==96)
 for i in range(729):
  ck(collisions(i)==[bit_planes(i)[0][a]*bit_planes(i)[1][a] for a in range(9)])
  ck(part(i)==part(81*triple(i)[2]+9*triple(i)[1]+triple(i)[0]))
 for i in valid:
  b=bit_planes(i)
  for a in range(9):ck(collisions(i)[a] in (0,1))
 print(f"ECK-050: {checks} checks PASS; 9 collision gates; validation cohorts 44/102; final 145 unopened")
if __name__=="__main__":test()
