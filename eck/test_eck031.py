"""ECK-031: twelve-step reflected boomerang spin and three-generation route."""
SCHEDULE=(-1,-1,-1,1,1,1,1,1,1,-1,-1,-1)
GENERATION_LEGS=(0,1,2,1)
ORIGIN="(0=-.)"
def spin_position(step):
    if type(step)!=int or step<0 or step>12:raise ValueError("step")
    return sum(SCHEDULE[:step])
def validate():
    assert SCHEDULE[:6]==tuple(reversed(SCHEDULE[6:]))
    assert spin_position(12)==0
    assert GENERATION_LEGS==(0,1,2,1)
    assert all(v in (-1,1) for v in SCHEDULE)
    assert len(SCHEDULE)==12
def test():
    validate()
    count=0
    def ck(ok):
        nonlocal count
        assert ok
        count+=1
    expected=(0,-1,-2,-3,-2,-1,0,1,2,3,2,1,0)
    ck(tuple(spin_position(i) for i in range(13))==expected)
    ck(max(expected)==3 and min(expected)==-3)
    ck(SCHEDULE[:3]==(-1,)*3)
    ck(SCHEDULE[3:6]==(1,)*3)
    ck(SCHEDULE[6:9]==(1,)*3)
    ck(SCHEDULE[9:]==(-1,)*3)
    ck(sum(SCHEDULE)==0)
    ck(len(GENERATION_LEGS)==4)
    ck(len(set(GENERATION_LEGS))==3)
    ck(ORIGIN not in GENERATION_LEGS)
    for k in range(13):
        ck(spin_position(k)==spin_position(12-k))
        ck(-3<=spin_position(k)<=3)
    for k in range(12):
        ck(spin_position(k+1)-spin_position(k)==SCHEDULE[k])
    archive=[]
    for generation in range(100):
        if spin_position(12)==0: archive.append((generation,tuple(SCHEDULE),ORIGIN))
        ck(len(archive)==generation+1)
        ck(archive[0][1]==SCHEDULE)
    ck(len(archive)==100)
    print(f"ECK-031: {count} assertions passed / 100 complete boomerang cycles")
if __name__=="__main__":test()
