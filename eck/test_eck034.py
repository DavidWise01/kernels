"""ECK-034: bounded recursive topology pruning with preserved nine-address coverage."""
from dataclasses import dataclass
from math import isclose

COORDS=tuple((g,r,c) for g in range(3) for r in range(3) for c in range(3))
TRAIN=((1,1),(0,0))
VALID=((0,1),(2,2))
FINAL=((0,2),(1,0),(1,2),(2,0),(2,1))
SINGLET="(0=-.)"
PENALTY=.004

def idx(g,r,c):return 9*g+3*r+c
def edges():
    result=[]
    for g,r,c in COORDS:
        for dr,dc,dg in ((0,1,0),(1,0,0),(0,0,1)):
            rr,cc,gg=r+dr,c+dc,g+dg
            if rr<3 and cc<3 and gg<3:
                result.append((idx(g,r,c),idx(gg,rr,cc),bool(dg)))
    return tuple(result)

EDGES=edges()

def coverage(mask):
    for r in range(3):
        for c in range(3):
            for g in (0,1):
                a,b=idx(g,r,c),idx(g+1,r,c)
                if not any(on and x==a and y==b and across for on,(x,y,across) in zip(mask,EDGES)):
                    return False
    return True

def score(mask,weights,cases):
    inter,local=weights
    results=[]
    for r,c in cases:
        old=[0.]*27
        old[idx(0,r,c)]=1.
        for _ in range(2):
            new=[.35*v for v in old]
            for on,(a,b,across) in zip(mask,EDGES):
                if not on:continue
                w=inter if across else local
                new[b]+=w*old[a]
                if not across:new[a]+=w*old[b]
            old=[max(0.,min(1.,v)) for v in new]
        target=old[idx(2,r,c)]
        results.append(target-.02*(sum(old)-target))
    return sum(results)/len(results)

@dataclass(frozen=True)
class Version:
    number:int
    parent:int|None
    mask:tuple
    train:float
    validation:float
    fitness:float
    origin:str=SINGLET

def metrics(mask,weights):
    train=score(mask,weights,TRAIN)
    val=score(mask,weights,VALID)
    return (train,val,train-PENALTY*sum(mask))

def search_once(mask,weights):
    train,val,fitness=metrics(mask,weights)
    best=None
    inspected=0
    for i,on in enumerate(mask):
        if not on:continue
        alt=list(mask);alt[i]=False;alt=tuple(alt)
        if not coverage(alt):continue
        cand=metrics(alt,weights)
        inspected+=1
        if cand[2]>fitness+1e-10 and cand[1]+1e-10>=val and (best is None or cand[2]>best[2][2]+1e-10):
            best=(i,alt,cand)
    return best,inspected

def test():
    checks=0
    def ck(value):
        nonlocal checks
        assert value
        checks+=1
    ck(len(COORDS)==27 and len(set(COORDS))==27)
    ck(len(EDGES)==54)
    ck(sum(a!=b and across for a,b,across in EDGES)==18)
    ck(sum(not across for _,_,across in EDGES)==36)
    ck(set(TRAIN).isdisjoint(VALID))
    ck(set(TRAIN).isdisjoint(FINAL))
    ck(set(VALID).isdisjoint(FINAL))
    weights=(.72,.12)
    mask=(True,)*54
    ck(coverage(mask))
    beginning=metrics(mask,weights)
    versions=[Version(0,None,mask,*beginning)]
    attempts=[]
    for number in range(54):
        before=metrics(mask,weights)
        candidate,inspected=search_once(mask,weights)
        if candidate:
            _,mask,after=candidate
            versions.append(Version(len(versions),versions[-1].number,mask,*after))
        else:
            after=before
        attempts.append((number,candidate is not None,inspected))
        ck(coverage(mask))
        ck(after[2]+1e-10>=before[2])
        ck(after[1]+1e-10>=before[1])
        ck(versions[0].mask==(True,)*54)
        ck(versions[-1].origin==SINGLET)
    ck(len(versions)==37)
    ck(sum(x[1] for x in attempts)==36)
    ck(len(attempts)==54)
    ck(sum(mask)==18)
    ck(all(v.number==i for i,v in enumerate(versions)))
    ck(all(v.parent==i-1 for i,v in enumerate(versions[1:],1)))
    ck(versions[0].mask==(True,)*54)
    ck(metrics(mask,weights)[2]>beginning[2])
    original_test=score(versions[0].mask,weights,FINAL)
    evolved_test=score(mask,weights,FINAL)
    ck(evolved_test>original_test)
    ck(isclose(original_test,.4904428,abs_tol=1e-8))
    ck(isclose(evolved_test,.50587,abs_tol=1e-8))
    print(f"ECK-034: {checks} checks PASS / 54 iterations / 36 accepted / 18 links / final test {original_test:.7f} -> {evolved_test:.7f}")

if __name__=="__main__":
    test()
