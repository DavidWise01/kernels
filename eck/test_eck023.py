"""ECK-023 — lossless nine-to-four Quantum Chrome packet transport."""
from dataclasses import dataclass
from copy import deepcopy
NAMES=("upperleftback","lowerleftback","centerback","centerupper","center","centerlower","upperrightfront","centerrightfront","lowerrightfront")
FIELDS=("POSITION","CHROMA","WAVELENGTH","CHRONOS")
SINGLET="(0=-.)"

def pack(addresses,n):
    if not isinstance(n,int) or isinstance(n,bool) or not 1<=n<=9:raise ValueError("n")
    if len(addresses)!=9 or len(set(addresses))!=9:raise ValueError("addresses")
    return {"schema":"eck023-transport-v1","singlet":SINGLET,"n":n,
      "channels":[{"field":f,"packets":[{"index":i,"name":name,"n":n}
          for i,name in enumerate(addresses) if i%4==c]} for c,f in enumerate(FIELDS)]}

def unpack(env):
    if env["schema"]!="eck023-transport-v1" or env["singlet"]!=SINGLET or len(env["channels"])!=4:raise ValueError("envelope")
    values=[None]*9
    for c,channel in enumerate(env["channels"]):
        if channel["field"]!=FIELDS[c]:raise ValueError("channel")
        for p in channel["packets"]:
            i=p["index"]
            if type(i)!=int or not 0<=i<9 or i%4!=c or values[i] is not None or p["n"]!=env["n"]:
                raise ValueError("packet")
            values[i]=p["name"]
    if tuple(values)!=NAMES:raise ValueError("missing or corrupt")
    return (env["singlet"],env["n"],tuple(values))

def test():
    count=0
    def ck(v):
        nonlocal count
        assert v
        count+=1
    for n in range(1,10):
        env=pack(NAMES,n)
        ck([len(x["packets"]) for x in env["channels"]]==[3,2,2,2])
        ck(unpack(env)==(SINGLET,n,NAMES))
        for c in range(4):
            for packet_i in range(len(env["channels"][c]["packets"])):
                broken=deepcopy(env);broken["channels"][c]["packets"].pop(packet_i)
                try:unpack(broken)
                except ValueError:ck(True)
                else:raise AssertionError("dropped packet accepted")
        for c in range(4):
            broken=deepcopy(env);broken["channels"][c]["packets"][0]["name"]="altered"
            try:unpack(broken)
            except ValueError:ck(True)
            else:raise AssertionError("altered packet accepted")
    ck(len(set(NAMES))==9)
    ck(SINGLET not in NAMES)
    print(f"ECK-023: {count} assertions PASS")
if __name__=="__main__":test()
