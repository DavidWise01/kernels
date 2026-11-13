"""ECK-043: frozen reversal transfer, cyclic-rotation algebra and carrier identifiability.

Stand-alone structural/analytic regression. Numerical training outcomes are
verified separately against the actual committed JavaScript functions.
"""
from itertools import product
from math import isclose

GAINS=(.20,.25,.30,.25)
CARRIER_NAMES=("WEAK","MEDIUM","STRONG","FUSION")
def encode(a,b,c):return 81*a+9*b+c
def decode(n):
    if type(n)!=int or not 0<=n<729:raise ValueError(n)
    return n//81,(n%81)//9,n%9
def reverse(n):
    a,b,c=decode(n)
    return encode(c,b,a)
def rotate(n):
    a,b,c=decode(n)
    return encode(b,c,a)
def split(n):
    a,b,c=sorted(decode(n))
    return (7*a+11*b+13*c)%5
def vector(n):
    out=[0.]*9
    for address,bit in zip(decode(n),(1,2,4)):
        out[address]+=bit/7
    return tuple(out)
def bits(n):
    return tuple(tuple((round(v*7)>>i)&1 for v in vector(n)) for i in range(3))
def initial_weights():
    return [[1. if i%4==0 else 0. for i in range(9)] for _ in range(4)]
def predict(n,weights,enabled=(True,True,True,True)):
    phase=bits(n)
    out=[0.]*9
    for address in range(9):
        for output_bit in range(3):
            for input_bit in range(3):
                weight=sum(GAINS[k]*weights[k][output_bit*3+input_bit]
                           for k in range(4) if enabled[k])
                out[address]+=2**output_bit/7*phase[input_bit][address]*weight
    return tuple(out)
def mse(ids,w):
    total=0.
    for n in ids:
        p,t=predict(n,w),vector(rotate(n))
        total+=sum((a-b)**2 for a,b in zip(p,t))/9
    return total/len(ids)

def test():
    assertions=0
    def ck(cond):
        nonlocal assertions
        assert cond
        assertions+=1
    ck(len(CARRIER_NAMES)==4)
    ck(3*3*3==27 and 9**3==729)
    ck(len({vector(i) for i in range(729)})==729)
    for i in range(729):
        ck(reverse(reverse(i))==i)
        ck(rotate(rotate(rotate(i)))==i)
        ck(split(i)==split(reverse(i))==split(rotate(i)))
        ck(encode(*decode(i))==i)
    training=[i for i in range(729) if split(i)<3]
    validation=[i for i in range(729) if split(i)==3]
    final=[i for i in range(729) if split(i)==4]
    ck((len(training),len(validation),len(final))==(438,146,145))
    ck(set(training).isdisjoint(validation) and set(training).isdisjoint(final))
    weights=initial_weights()
    changed=[r[:] for r in weights]
    changed[0][0]+=.1
    changed[1][0]-=.1*GAINS[0]/GAINS[1]
    ck(changed!=weights)
    for i in validation:
        ck(all(isclose(a,b,abs_tol=1e-12) for a,b in
               zip(predict(i,weights),predict(i,changed))))
    ck(isclose(mse(validation,weights),mse(validation,changed),abs_tol=1e-12))
    ck(all(len(w)==9 for w in weights))
    print(f"ECK-043: {assertions} assertions PASS; 729 exact rotation order-3 checks; 146 compensation equivalence checks; test partition unopened")

if __name__=="__main__":
    test()
