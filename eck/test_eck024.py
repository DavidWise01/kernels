"""ECK-024: 11 nested layers, lossless 9-address transport, distinct unit caps."""
from dataclasses import dataclass
from copy import deepcopy
NAMES=("upperleftback","lowerleftback","centerback","centerupper","center","centerlower","upperrightfront","centerrightfront","lowerrightfront")
LEVELS=(27,24,21,17.5,13,8,5,3,2,1,1)
FIELDS=("POSITION","CHROMA","WAVELENGTH","CHRONOS")
ORIGIN="(0=-.)"
def pack(n):
    assert 1<=n<=9
    return tuple(tuple((i,NAMES[i],n) for i in range(c,9,4)) for c in range(4))
def recover(packet):
    if len(packet)!=4:raise ValueError("channels")
    result=[None]*9
    for c,group in enumerate(packet):
        for i,name,n in group:
            if not (type(i) is int and 0<=i<9 and i%4==c and result[i] is None):
                raise ValueError("index")
            result[i]=(name,n)
    if any(v is None or v[0]!=NAMES[i] for i,v in enumerate(result)):
        raise ValueError("missing or altered")
    return tuple(result)
@dataclass(frozen=True)
class Layer:
    index:int
    size:float
    packet:tuple
def verify(history,n):
    if not history or len(history)>len(LEVELS):return False
    for k,layer in enumerate(history):
        if layer.index!=k or layer.size!=LEVELS[k]:return False
        try:entries=recover(layer.packet)
        except (ValueError,TypeError):return False
        if tuple(v[1] for v in entries)!=(n,)*9:return False
    return True
def test():
    assertions=0
    def ck(ok):
        nonlocal assertions
        assert ok
        assertions+=1
    for n in range(1,10):
        payload=pack(n);history=[]
        for k in range(11):
            history.append(Layer(k,LEVELS[k],deepcopy(payload)))
            ck(verify(history,n))
            ck(history[-1].size==LEVELS[k])
            ck(recover(history[-1].packet)==tuple((name,n) for name in NAMES))
        ck(history[9].size==history[10].size and history[9].index!=history[10].index)
        for k in range(10,0,-1):
            ck(history[k].packet==history[k-1].packet)
        broken=list(payload);broken[0]=broken[0][:-1]
        ck(not verify([Layer(0,27,tuple(broken))],n))
        shuffled=list(history);shuffled[3]=Layer(6,shuffled[3].size,shuffled[3].packet)
        ck(not verify(shuffled,n))
        ck(len(history)==11 and history[-1].index==10)
    print(f"ECK-024: {assertions}/{assertions} assertions PASS across 9 nesting settings")
if __name__=="__main__":test()
