"""ECK-019: indexed mitochondrial Hamilton cycle and nesting semantic checks."""
from decimal import Decimal
IDS=("0","1a","1b","2","3","5","8","13","17.5","21","24","27")
VALUES=(Decimal("0"),Decimal("1"),Decimal("1"),Decimal("2"),Decimal("3"),Decimal("5"),Decimal("8"),Decimal("13"),Decimal("17.5"),Decimal("21"),Decimal("24"),Decimal("27"))
EDGES=set(frozenset((IDS[i],IDS[(i+1)%len(IDS)])) for i in range(len(IDS)))
GROUPS={
 "origin":("0",),
 "single-cell-mito":("1a","1b"),
 "mito-complete":("2","3","5","8"),
 "emergence":("13",),
 "division":("17.5",),
 "re-emergence-diatom":("21",),
 "hamilton-walk":("24",),
 "hamilton-complete":("27",)
}
def is_hamiltonian_cycle(route):
    return (len(route)==len(IDS)+1 and route[0]==route[-1]
      and set(route[:-1])==set(IDS) and len(set(route[:-1]))==len(IDS)
      and all(frozenset((a,b)) in EDGES for a,b in zip(route,route[1:])))
def test():
    cases=[]
    def check(condition,label):
        assert condition,label
        cases.append(label)
    walk=IDS+("0",)
    check(len(IDS)==12,"12 unique vertex IDs including origin")
    check(len(set(IDS))==12,"no duplicate identities")
    check(VALUES[1]==VALUES[2] and IDS[1]!=IDS[2],"two distinct one-cells")
    check(VALUES[7]+VALUES[6]==VALUES[9],"21=13+8")
    check(VALUES[8]==Decimal("17.5"),"fractional division")
    check(is_hamiltonian_cycle(walk),"full defined graph cycle")
    check(not is_hamiltonian_cycle(IDS),"open route rejected")
    check(not is_hamiltonian_cycle(IDS[:8]+("13",)+IDS[9:]+("0",)),"duplicate vertex rejected")
    check(not is_hamiltonian_cycle(("0","1b","1a")+IDS[3:]+("0",)),"wrong directed? undirected adjacency shortcut rejected")
    check(not is_hamiltonian_cycle(IDS[:-2]+("27","24","0")),"broken adjacency rejected")
    check(all(x in IDS for xs in GROUPS.values() for x in xs),"group coverage valid")
    check(set(x for xs in GROUPS.values() for x in xs)==set(IDS),"all groups cover each vertex")
    check(sum(len(xs) for xs in GROUPS.values())==12,"no macro-state overlap")
    check(walk.count("0")==2,"origin only start and return")
    print(f"ECK-019: {len(cases)} structural assertions PASS")
if __name__=="__main__":test()
