"""ECK-028: 3x3x3 indexed generational neural-style mesh."""
from collections import Counter
NAMES=("upperleftback","lowerleftback","centerback","centerupper","center","centerlower","upperrightfront","centerrightfront","lowerrightfront")
NODES=tuple((g,r,c) for g in range(3) for r in range(3) for c in range(3))
def edges():
    for g,r,c in NODES:
        for dg,dr,dc in ((0,0,1),(0,1,0),(1,0,0)):
            if g+dg<3 and r+dr<3 and c+dc<3:
                yield ((g,r,c),(g+dg,r+dr,c+dc))
def test():
    tests=0
    def ck(x):
        nonlocal tests
        assert x
        tests+=1
    ed=tuple(edges())
    ck(len(NODES)==27)
    ck(len(set(NODES))==27)
    ck(len(NAMES)==9 and len(set(NAMES))==9)
    ck(Counter(g for g,r,c in NODES)==Counter({0:9,1:9,2:9}))
    ck(len(ed)==54)
    ck(len(set(tuple(sorted(e)) for e in ed))==54)
    ck(sum(a[0]!=b[0] for a,b in ed)==18)
    ck(sum(a[0]==b[0] for a,b in ed)==36)
    ck(all(a in NODES and b in NODES for a,b in ed))
    ck(all(sum(abs(x-y) for x,y in zip(a,b))==1 for a,b in ed))
    ck(all((g,r,c) != "(0=-.)" for g,r,c in NODES))
    for g in range(3):
        ck(len([n for n in NODES if n[0]==g])==9)
        for r in range(3):
            for c in range(3):
                ck(NODES[g*9+r*3+c]==(g,r,c))
                ck(NAMES[r*3+c] in NAMES)
    ck(len({(g,NAMES[r*3+c]) for g,r,c in NODES})==27)
    print(f"ECK-028: {tests} structural assertions PASS")
if __name__=="__main__":test()
