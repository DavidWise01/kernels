"""ECK-027: directed coupling coverage across all 10 pyramid transitions."""
from collections import Counter
NODES=tuple(range(9))
LEVELS=(27,24,21,17.5,13,8,5,3,2,1,1)
def pair(k):
    if type(k)!=int or not 1<=k<=10:raise ValueError("invalid transition")
    return (k-1)%9,k%9
def test():
    count=0
    def check(value):
        nonlocal count
        assert value
        count+=1
    edges=tuple(pair(k) for k in range(1,11))
    check(len(edges)==10)
    check(len(set(edges))==9)
    check(set(a for a,b in edges)==set(NODES))
    check(set(b for a,b in edges)==set(NODES))
    check(edges[0]==edges[-1]==(0,1))
    check(edges[8]==(8,0))
    check(len(LEVELS)==11 and LEVELS[9:]==(1,1))
    check(all(a!=b for a,b in edges))
    counts=Counter(edges)
    check(counts[(0,1)]==2)
    check(all(counts[(i,(i+1)%9)]==1 for i in range(1,9)))
    for k in range(1,11):
        a,b=pair(k)
        check(a in NODES and b in NODES)
        check(b==(a+1)%9)
    # Ring traversal: every node visited exactly once before returning.
    route=tuple(range(9))+(0,)
    check(len(set(route[:-1]))==9)
    check(all((a,b) in set(edges) for a,b in zip(route,route[1:])))
    print(f"ECK-027: {count} assertions PASS; 9/9 source and target coverage")
if __name__=="__main__":test()
