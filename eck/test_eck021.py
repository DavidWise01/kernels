"""ECK-021 — immutable phase snapshot reference test."""
from dataclasses import dataclass
IDS=('0','1a','1b','2','3','5','8','13','17.5','21','24','27')
ADDRESSES=('upperleftback','lowerleftback','centerback','centerupper','center','centerlower','upperrightfront','centerrightfront','lowerrightfront')
LEVELS=(27,24,21,17.5,13,8,5,3,2,1,1)
@dataclass(frozen=True)
class Phase:
    wheels:tuple
    lobes:tuple
    addresses:tuple
    selected:str
    n:int
    pyramid:tuple
    total:int
def snapshot(wheels,lobes,index,n):
    assert 0<=index<9 and 1<=n<=9
    return Phase(tuple(wheels),tuple(lobes),ADDRESSES,ADDRESSES[index],n,LEVELS,sum(lobes))
def test():
    checks=0
    def ck(condition):
        nonlocal checks
        assert condition
        checks+=1
    wheels=[180,28,590,250];lobes=[35,35,35,35];archive=[]
    for generation in range(100):
        if generation: wheels[0]=(wheels[0]+1)%360;lobes[0]+=1
        p=snapshot(wheels,lobes,generation%9,generation%9+1)
        archive.append((generation,'(0=-.)',IDS+('0',),p))
        ck(archive[-1][0]==generation)
        ck(archive[-1][1]=='(0=-.)')
        ck(archive[-1][2][0]==archive[-1][2][-1]=='0')
        ck(len(set(archive[-1][2][:-1]))==12)
        ck(len(p.addresses)==9)
        ck(len(p.pyramid)==11)
        ck(p.total==sum(p.lobes))
    ck(archive[0][-1].wheels==(180,28,590,250))
    ck(archive[0][-1].lobes==(35,35,35,35))
    ck(archive[-1][-1].wheels[0]==279)
    ck(all(record[-1].selected in ADDRESSES for record in archive))
    ck(len(set(r[0] for r in archive))==100)
    ck(archive[0][-1].total==140)
    print(f"ECK-021: {checks}/{checks} checks PASS, 100 generations")
if __name__=='__main__':test()
