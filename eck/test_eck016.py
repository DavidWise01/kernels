"""ECK-016: exact integer-field conservation model (standard library)."""
def transfer(a,i,target):
    b=a[:]; t=max(0,min(100,round(target))); d=t-b[i]; remaining=abs(d)
    if not remaining: return b
    if d>0:
        for j in [(i+k)%4 for k in (1,2,3)]:
            n=min(remaining,b[j]);b[j]-=n;remaining-=n
            if not remaining:break
        b[i]+=abs(d)-remaining
    else:
        for j in [(i+k)%4 for k in (1,2,3)]:
            n=min(remaining,100-b[j]);b[j]+=n;remaining-=n
            if not remaining:break
        b[i]-=abs(d)-remaining
    return b
def test():
    n=0
    def check(x):
        nonlocal n
        assert x
        n+=1
    original=[35]*4
    check(transfer(original,0,55)==[55,15,35,35])
    check(original==[35]*4)
    check(sum(transfer(original,0,100))==140)
    check(transfer([100,0,0,0],0,100)==[100,0,0,0])
    check(transfer([0]*4,0,100)==[0]*4)
    check(transfer([100]*4,0,0)==[100]*4)
    check(transfer([50]*4,0,0)==[0,100,50,50])
    check(sum(transfer(original,3,-20))==140)
    for start in ([0]*4,[100]*4,[35]*4,[100,20,0,70],[1,99,40,45]):
        for i in range(4):
            for target in range(-20,121):
                result=transfer(start,i,target)
                check(sum(result)==sum(start))
                check(all(0<=v<=100 for v in result))
    for total in range(401):
        q,r=divmod(total,4)
        balanced=[q+(i<r) for i in range(4)]
        check(sum(balanced)==total)
        check(max(balanced)-min(balanced)<=1)
    print("ECK-016:",n,"assertions PASS")
if __name__=="__main__":test()
