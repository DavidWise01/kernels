"""ECK-012 authenticated calibration-event ledger regression.

Local trust boundary: old root/count must be retained separately by verifier.
"""
import copy, hashlib, json

def canon(x):
    return json.dumps(x,separators=(",",":"),ensure_ascii=False).encode()
def digest(b):
    return hashlib.sha256(b).digest()
def leaf(x):
    return digest(bytes([0])+canon(x))
def node(a,b):
    return digest(bytes([1])+a+b)
def merkle(records):
    if not records:return digest(b"").hex()
    if len(records)==1:return leaf(records[0]).hex()
    k=1
    while (k<<1)<len(records):k<<=1
    return node(bytes.fromhex(merkle(records[:k])),bytes.fromhex(merkle(records[k:]))).hex()
def verify_prefix(records,count,old_root):
    return 0<=count<=len(records) and merkle(records[:count])==old_root
def make_cal(raw,i,wheel,offset):
    key={"POSITION":"position_deg","CHROMA":"hue_deg",
         "WAVELENGTH":"wavelength_nm","CHRONOS":"chronos_ms"}[wheel]
    return {"kind":"calibration","parent_index":i,"parent_leaf":leaf(raw).hex(),
            "wheel":wheel,"wheel_key":key,"offset":offset,
            "derived_value":raw[key]+offset,"source_value":raw[key]}
def test():
    count=0
    def check(value):
        nonlocal count
        assert value
        count+=1
    raw={"primitive":"observed-chrome-v1","position_deg":180,"hue_deg":28,
         "wavelength_nm":590,"chronos_ms":250}
    records=[{"kind":"observation","index":0,"raw_hash":leaf(raw).hex(),"raw":copy.deepcopy(raw)}]
    root0=merkle(records)
    check(verify_prefix(records,1,root0))
    for wheel,offset in [("POSITION",12),("CHROMA",-7),("WAVELENGTH",5),("CHRONOS",25)]:
        records.append(make_cal(raw,0,wheel,offset))
    root1=merkle(records)
    check(root0!=root1)
    check(verify_prefix(records,1,root0))
    check(verify_prefix(records,5,root1))
    check(raw["wavelength_nm"]==590 and raw["chronos_ms"]==250)
    for index in range(1,5):
        tampered=copy.deepcopy(records);tampered[index]["offset"]+=1
        check(not verify_prefix(tampered,5,root1))
    for index in range(1,5):
        missing=records[:index]+records[index+1:]
        check(not verify_prefix(missing,5,root1))
    for index in range(1,5):
        changed=copy.deepcopy(records);changed[index]["derived_value"]+=1
        check(not verify_prefix(changed,5,root1))
    changed=copy.deepcopy(records);changed[0]["raw"]["hue_deg"]+=1
    check(not verify_prefix(changed,5,root1))
    changed=copy.deepcopy(records);changed[2],changed[3]=changed[3],changed[2]
    check(not verify_prefix(changed,5,root1))
    check(not verify_prefix(records[:2],5,root1))
    check(verify_prefix(records+[make_cal(raw,0,"CHROMA",20)],5,root1))
    check(not verify_prefix(records,5,"0"*64))
    print(f"ECK-012: {count}/{count} assertions PASS")
if __name__=="__main__": test()
