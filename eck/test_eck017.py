"""ECK-017: Quantum Chrome nine-address plus singlet regression."""
ADDRESSES=(
 "upperleftback","lowerleftback","centerback","centerupper","center",
 "centerlower","upperrightfront","centerrightfront","lowerrightfront"
)
SINGLET="."
def expression(n):
    if type(n) is not int or not 1<=n<=9: raise ValueError("symbolic n must be integer 1..9")
    return "{{ "+", ".join(f"{name}{{{{{n}}}}}" for name in ADDRESSES)+" }}^{{"+str(n)+"}}^{{"+str(n)+"}} || repeat"
def test():
    checks=0
    assert len(ADDRESSES)==9;checks+=1
    assert len(set(ADDRESSES))==9;checks+=1
    assert SINGLET not in ADDRESSES;checks+=1
    assert len(ADDRESSES)+(1 if SINGLET else 0)==10;checks+=1
    for n in range(1,10):
        e=expression(n)
        assert e.count("{{"+str(n)+"}}")==11;checks+=1
        assert e.endswith("|| repeat");checks+=1
        for address in ADDRESSES:
            assert address+"{{"+str(n)+"}}" in e;checks+=1
    for bad in (0,10,-1,2.2,True,"2"):
        try:expression(bad)
        except ValueError:checks+=1
        else:raise AssertionError(f"accepted invalid n: {bad!r}")
    print(f"ECK-017: {checks} assertions PASS")
if __name__=="__main__":test()
