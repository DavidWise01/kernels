"""ECK-018 — nested Quantum Chrome hierarchy invariants."""
from decimal import Decimal
LAYERS = tuple(map(Decimal, ("27","24","21","17.5","13","8","5","3","2","1","1")))
LABELS=("upperleftback","lowerleftback","centerback","centerupper","center","centerlower","upperrightfront","centerrightfront","lowerrightfront")
def indexed_frame():
    return tuple((i+1, value) for i,value in enumerate(LAYERS))
def test():
    n=0
    def check(v):
        nonlocal n
        assert v
        n+=1
    check(len(LAYERS)==11)
    check(len(LABELS)==9)
    check(len(set(LABELS))==9)
    check(LAYERS[0]==Decimal("27"))
    check(LAYERS[3]==Decimal("17.5"))
    check(LAYERS[8]==Decimal("2"))
    check(LAYERS[9:]==(Decimal("1"),Decimal("1")))
    check(all(a>=b for a,b in zip(LAYERS,LAYERS[1:])))
    check(sum(v==Decimal("1") for v in LAYERS)==2)
    check(indexed_frame()[9]!=indexed_frame()[10])
    for i,(index,value) in enumerate(indexed_frame()):
        check(index==i+1)
        check(value==LAYERS[i])
    print(f"ECK-018: {n} structural assertions PASS")
if __name__=="__main__":test()
