from collections import defaultdict

n,k=map(int,input().split())
a=list(map(int,input().split()))

cnt=defaultdict(int)
l=0
res=0
distinct=0

for r in range(n):
    if cnt[a[r]]==0:
        distinct+=1
    cnt[a[r]]+=1
    
    while distinct>k:
        cnt[a[l]]-=1
        if cnt[a[l]]==0:
            distinct-=1
        l+=1
    
    res+=r-l+1

print(res)