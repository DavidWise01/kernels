"""ECK-020: return-fold and ancestry test, local reference model."""
from dataclasses import dataclass
IDS=('0','1a','1b','2','3','5','8','13','17.5','21','24','27')
ORIGIN='(0=-.)'
@dataclass(frozen=True)
class Round:
    generation:int
    origin:str
    route:tuple
    fold:str='}{'
class Cycle:
    def __init__(self):
        self.step=0
        self.generation=0
        self.archive=[]
    def advance(self):
        self.step=min(self.step+1,len(IDS))
    def fold(self):
        if self.step!=len(IDS):return False
        if len(set(IDS))!=len(IDS) or IDS[0]!='0' or IDS[-1]!='27':return False
        rec=Round(self.generation,ORIGIN,IDS+('0',))
        self.archive.append(rec)
        self.generation+=1
        self.step=0
        return True

def test():
    c=Cycle();n=0
    def check(ok):
        nonlocal n
        assert ok
        n+=1
    check(not c.fold())
    check(not c.archive)
    for generation in range(100):
        for _ in range(len(IDS)-1):c.advance()
        check(not c.fold())
        c.advance()
        check(c.fold())
        check(c.step==0)
        check(c.generation==generation+1)
        check(len(c.archive)==generation+1)
        check(c.archive[-1].generation==generation)
        check(c.archive[-1].origin==ORIGIN)
        check(c.archive[-1].route==IDS+('0',))
        check(c.archive[-1].fold=='}{')
        check(len(set(c.archive[-1].route[:-1]))==12)
    check(len(set(x.generation for x in c.archive))==100)
    check(all(x.origin==ORIGIN for x in c.archive))
    check(c.archive[0].route==c.archive[-1].route)
    print(f'ECK-020: {n}/{n} assertions PASS, {len(c.archive)} complete rounds')
if __name__=='__main__':test()
