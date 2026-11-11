"""ECK-026: invertible cross-address modular shears at all ten level boundaries."""
from copy import deepcopy
NAMES=("upperleftback","lowerleftback","centerback","centerupper","center","centerlower","upperrightfront","centerrightfront","lowerrightfront")
LEVELS=(27,24,21,17.5,13,8,5,3,2,1,1)
def initial(n):return tuple((name,n,i) for i,name in enumerate(NAMES))
def pair(k):
    if type(k)!=int or not 1<=k<=10:raise ValueError("invalid layer")
    return ((k-1)%9,k%9)
def apply(data,k,reverse=False):
    a,b=pair(k)
    out=[(name,n,p) for name,n,p in data]
    if reverse:
        name,n,p=out[b];out[b]=(name,n,(p-out[a][2])%9)
        out=[(name,n,(p-k)%9) for name,n,p in out]
    else:
        out=[(name,n,(p+k)%9) for name,n,p in out]
        name,n,p=out[b];out[b]=(name,n,(p+out[a][2])%9)
    return tuple(out)
def valid_route(route,n):
    if not 1<=len(route)<=11:return False
    for i,record in enumerate(route):
        if record[0]!=i or record[1]!=LEVELS[i]:return False
        if any((row[0],row[1])!=(NAMES[j],n) or not 0<=row[2]<9 for j,row in enumerate(record[2])):return False
        if i==0 and record[2]!=initial(n):return False
        if i and record[2]!=apply(route[i-1][2],i):return False
    return True
def test():
    checks=0
    def ck(ok):
        nonlocal checks
        assert ok
        checks+=1
    for n in range(1,10):
        beginning=initial(n);state=beginning;route=[(0,27,beginning)]
        for k in range(1,11):
            previous=state
            state=apply(state,k)
            ck(apply(state,k,True)==previous)
            route.append((k,LEVELS[k],state))
            ck(valid_route(route,n))
            ck(pair(k)[0]!=pair(k)[1])
        for k in range(10,0,-1):
            state=apply(state,k,True)
        ck(state==beginning)
        ck(route[9][1]==route[10][1] and route[9][0]!=route[10][0])
        altered=deepcopy(route)
        i,value,payload=altered[4]
        payload=list(payload)
        name,nv,phase=payload[0]
        payload[0]=(name,nv,(phase+1)%9)
        altered[4]=(i,value,tuple(payload))
        ck(not valid_route(altered,n))
    print(f"ECK-026: {checks}/{checks} assertions passed")
if __name__=="__main__":test()
