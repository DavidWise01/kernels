"""ECK-010: deterministic authenticated-prefix regression (standard library only).

This is a linear-size verifier; it is NOT an RFC6962 compact consistency proof.
"""
import hashlib, json, copy

def H(b): return hashlib.sha256(b).digest()
def canonical(r): return json.dumps(r,sort_keys=True,separators=(',',':')).encode()
def leaf(r): return H(b'\x00'+canonical(r))
def node(a,b): return H(b'\x01'+a+b)
def split(n):
    k=1
    while k*2<n:k*=2
    return k
def root(records):
    if not records:return H(b'').hex()
    def _tree(seq):
        if len(seq)==1:return leaf(seq[0])
        k=split(len(seq))
        return node(_tree(seq[:k]),_tree(seq[k:]))
    return _tree(records).hex()
def consistent(old_size,old_root,new_records):
    if old_size<0 or old_size>len(new_records):return False
    return root(new_records[:old_size])==old_root

def test():
    samples=[{'primitive':'observed-chrome-v1','position_deg':i*40,
              'hue_deg':i*55,'wavelength_nm':380+i*32,'chronos_ms':i*9}
             for i in range(1,7)]
    assert root([])==hashlib.sha256(b'').hexdigest()
    old=samples[:3];old_root=root(old)
    assert consistent(3,old_root,samples)
    assert consistent(3,old_root,old)
    assert not consistent(3,old_root,samples[:2])
    assert not consistent(3,old_root,samples[1:])
    mutated=copy.deepcopy(samples);mutated[1]['hue_deg']+=1
    assert not consistent(3,old_root,mutated)
    altered=copy.deepcopy(samples);altered[0],altered[1]=altered[1],altered[0]
    assert not consistent(3,old_root,altered)
    appended=copy.deepcopy(samples);appended.append({'primitive':'observed-chrome-v1','position_deg':0,'hue_deg':0,'wavelength_nm':750,'chronos_ms':0})
    assert consistent(3,old_root,appended)
    assert not consistent(4,old_root,samples)
    assert not consistent(-1,old_root,samples)
    assert root(samples)==root(copy.deepcopy(samples))
    print("ECK-010: 11/11 deterministic prefix checks PASS")
if __name__=='__main__':test()
