"""ECK-051: cohort-protected acceptance policy, weighted counterexample, source split.

Run: python eck/test_eck051.py
This suite does not open the 145 reserved test examples.
"""
def triple(i):return (i//81,(i%81)//9,i%9)
def partition(t):
 a,b,c=sorted(t)
 return (7*a+11*b+13*c)%5
def accept(before,after,dual):
 primary=(after["train"]<before["train"]-1e-13 and
          after["validation"]<=before["validation"]+1e-12)
 return primary and (not dual or (after["repeated"]<=before["repeated"]+1e-12 and
                                 after["distinct"]<=before["distinct"]+1e-12))
def test():
 checks=0
 def ck(x):
  nonlocal checks
  assert x
  checks+=1
 train=[i for i in range(729) if partition(triple(i))<3]
 val=[i for i in range(729) if partition(triple(i))==3]
 final=[i for i in range(729) if partition(triple(i))==4]
 rep=[i for i in val if len(set(triple(i)))<3]
 distinct=[i for i in val if len(set(triple(i)))==3]
 ck((len(train),len(val),len(final))==(438,146,145))
 ck((len(rep),len(distinct))==(44,102))
 ck(set(rep).isdisjoint(distinct))
 ck(set(val)==set(rep)|set(distinct))
 ck(not set(final).intersection(train+val))
 before={"train":.020,"validation":.010,"repeated":.010,"distinct":.010}
 after={"train":.019,"repeated":.005,"distinct":.011,"validation":(44*.005+102*.011)/146}
 ck(after["validation"]<before["validation"])
 ck(accept(before,after,False))
 ck(not accept(before,after,True))
 improved={"train":.018,"repeated":.008,"distinct":.009,"validation":(44*.008+102*.009)/146}
 ck(accept(before,improved,True))
 unchanged={"train":.019,"repeated":.010,"distinct":.010,"validation":.010}
 ck(accept(before,unchanged,True))
 worsening_train={"train":.021,"repeated":.008,"distinct":.008,"validation":.008}
 ck(not accept(before,worsening_train,True))
 for i in range(729):
  a,b,c=triple(i)
  ck(partition((a,b,c))==partition((c,b,a)))
 print(f"ECK-051: {checks} checks PASS / aggregate-only accepts adverse candidate / dual-cohort rejects / 145 final examples untouched")
if __name__=="__main__":test()
