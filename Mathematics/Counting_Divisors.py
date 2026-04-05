n=int(input())
a=[int(input()) for _ in range(n)]
m=max(a)

d=[0]*(m+1)
for i in range(1,m+1):
    for j in range(i,m+1,i):
        d[j]+=1

for x in a:
    print(d[x])