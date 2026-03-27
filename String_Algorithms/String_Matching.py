s=input().strip()
p=input().strip()

n=len(s)
m=len(p)

lps=[0]*m
j=0

for i in range(1,m):
    while j>0 and p[i]!=p[j]:
        j=lps[j-1]
    if p[i]==p[j]:
        j+=1
        lps[i]=j

j=0
res=0

for i in range(n):
    while j>0 and s[i]!=p[j]:
        j=lps[j-1]
    if s[i]==p[j]:
        j+=1
    if j==m:
        res+=1
        j=lps[j-1]

print(res)