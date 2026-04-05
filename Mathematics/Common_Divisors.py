def max_gcd():
    n=int(input())
    a=list(map(int,input().split()))
    m=max(a)
    cnt=[0]*(m+1)
    for x in a:
        cnt[x]+=1
    for i in range(m,0,-1):
        s=0
        for j in range(i,m+1,i):
            s+=cnt[j]
            if s>=2:
                print(i)
                return

max_gcd()