"""ECK-025: invertible modulo-nine transformations along eleven indexed layers."""
from copy import deepcopy
NAMES=("upperleftback","lowerleftback","centerback","centerupper","center","centerlower","upperrightfront","centerrightfront","lowerrightfront")
LEVELS=(27,24,21,17.5,13,8,5,3,2,1,1)
FIELDS=("POSITION","CHROMA","WAVELENGTH","CHRONOS")
ORIGIN="(0=-.)"
def pack(n):
    return tuple(tuple((i,NAMES[i],n,i) for i in range(c,9,4)) for c in range(4))
def transform(channels,k,inverse=False):
    if not 1<=k<=10: raise ValueError("layer")
    shift=-k if inverse else k
    return tuple(tuple((i,name,n,(phase+shift)%9) for i,name,n,phase in group) for group in channels)
def validate(channels,n):
    if len(channels)!=4: raise ValueError("channels")
    observed=[None]*9
    for c,group in enumerate(channels):
        for i,name,number,phase in group:
            if type(i)!=int or not 0<=i<9 or i%4!=c or observed[i] is not None or not 0<=phase<9:
                raise ValueError("packet")
            observed[i]=(name,number,phase)
    if any(v is None or v[0]!=NAMES[i] or v[1]!=n for i,v in enumerate(observed)):
        raise ValueError("address identity")
    return True
def check_chain(history,n):
    if not 1<=len(history)<=11:return False
    try:
        for i,(level,value,channels) in enumerate(history):
            if level!=i or value!=LEVELS[i] or not validate(channels,n):return False
            if i==0 and channels!=pack(n):return False
            if i and channels!=transform(history[i-1][2],i):return False
        return True
    except (ValueError,TypeError,IndexError):return False
def test():
    assertions=0
    def ck(v):
        nonlocal assertions
        assert v
        assertions+=1
    for n in range(1,10):
        initial=pack(n);current=initial;history=[(0,LEVELS[0],initial)]
        for k in range(1,11):
            following=transform(current,k)
            ck(transform(following,k,True)==current)
            history.append((k,LEVELS[k],following))
            ck(check_chain(history,n))
            current=following
        ck(LEVELS[9]==LEVELS[10] and history[9][0]!=history[10][0])
        for k in range(10,0,-1):current=transform(current,k,True)
        ck(current==initial)
        altered=deepcopy(history)
        j,v,channels=altered[-1]
        groups=[list(g) for g in channels]
        i,name,num,phase=groups[0][0]
        groups[0][0]=(i,name,num,(phase+1)%9)
        altered[-1]=(j,v,tuple(tuple(g) for g in groups))
        ck(not check_chain(altered,n))
        skipped=history[:3]+history[4:]
        ck(not check_chain(skipped,n))
    print(f"ECK-025: {assertions} assertions PASS / nine n-settings / full forward-backward levels")
if __name__=="__main__":test()
