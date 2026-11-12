"""ECK-032: four symbolic spinor resolutions, all 4! orders, double-turn and recursive iterations."""
import itertools
import math

STAGES=(1.0,0.5,1/3,0.25)
SCHEDULE=(-1,-1,-1,1,1,1,1,1,1,-1,-1,-1)
ORDERS=tuple(itertools.permutations(range(4)))
SINGLET="(0=-.)"

def spinor_phase(slot):
    if type(slot) is not int or not 0<=slot<=24: raise ValueError("slot outside bounds")
    theta=4*math.pi*slot/24
    return math.cos(theta/2), math.sin(theta/2)

def index(g,r,c): return 9*g+3*r+c

def activation_tick(old,inter,local_weight):
    out=[0.0]*27
    for g in range(3):
        for r in range(3):
            for c in range(3):
                j=index(g,r,c)
                value=.35*old[j]
                for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                    rr,cc=r+dr,c+dc
                    if 0<=rr<3 and 0<=cc<3:
                        value+=local_weight*old[index(g,rr,cc)]
                if g>0: value+=inter*old[index(g-1,r,c)]
                out[j]=min(1.0,max(0.0,value))
    return out

def evaluate(inter,local_weight):
    activations=[0.0]*27
    activations[index(0,1,1)]=1.0
    for _ in range(2):
        activations=activation_tick(activations,inter,local_weight)
    target=activations[index(2,1,1)]
    return target-.02*(sum(activations)-target)

def clip(inter,local_weight):
    return (round(max(0,min(1,inter)),2),round(max(0,min(.4,local_weight)),2))

def try_iteration(inter,local_weight,step):
    baseline=evaluate(inter,local_weight)
    best=(inter,local_weight,baseline)
    for di,dl in ((1,0),(-1,0),(0,1),(0,-1),(1,-1),(-1,1)):
        ci,cl=clip(inter+step*di,local_weight+step*dl)
        score=evaluate(ci,cl)
        if score>best[2]+1e-10:
            best=(ci,cl,score)
    return best,best[2]>baseline+1e-10

def test():
    assertions=0
    def ck(x):
        nonlocal assertions
        assert x
        assertions+=1
    ck(len(ORDERS)==24)
    ck(len(set(ORDERS))==24)
    ck(all(len(set(p))==4 for p in ORDERS))
    for k in range(4):
        ck(sum(p[0]==k for p in ORDERS)==6)
    ck(SCHEDULE[:6]==tuple(reversed(SCHEDULE[6:])))
    ck(sum(SCHEDULE)==0)
    for slot,expect in ((0,1),(12,-1),(24,1)):
        real,imag=spinor_phase(slot)
        ck(abs(real-expect)<1e-12)
        ck(abs(imag)<1e-12)
    inter,local_weight=.72,.12
    baseline=evaluate(inter,local_weight)
    history=[]
    for slot,order in enumerate(ORDERS):
        stage=order[0]
        resolution=STAGES[stage]
        step=max(.01,round(5*resolution)/100)
        before=evaluate(inter,local_weight)
        proposal,accepted=try_iteration(inter,local_weight,step)
        if accepted:
            inter,local_weight=proposal[:2]
        after=evaluate(inter,local_weight)
        history.append((slot,stage,order,resolution,accepted,before,after,SINGLET))
        ck(after+1e-10>=before)
        ck(0<=inter<=1 and 0<=local_weight<=.4)
        ck(history[-1][-1]==SINGLET)
    ck(len(history)==24)
    ck(all(history[i][5]+1e-10<=history[i][6] for i in range(24)))
    ck(evaluate(inter,local_weight)>baseline)
    ck(sum(row[4] for row in history)==6)
    ck((inter,local_weight)==(1.0,0.0))
    print(f"ECK-032: {assertions} checks PASS; 24 recursive iterations, 6 accepted, {baseline:.5f} -> {evaluate(inter,local_weight):.5f}")

if __name__=="__main__":
    test()
