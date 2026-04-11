from collections import deque

n,k=map(int,input().split())
x,a,b,c=map(int,input().split())

dq=deque()
res=0

for i in range(n):
    if i>0:
        x=(a*x+b)%c
    while dq and dq[-1][0]>=x:
        dq.pop()
    dq.append((x,i))
    while dq[0][1]<=i-k:
        dq.popleft()
    if i>=k-1:
        res^=dq[0][0]

print(res)