s=input().strip()
n=len(s)
lps=[0]*n
j=0

for i in range(1, n):
    while j > 0 and s[i] != s[j]:
        j = lps[j-1]
    if s[i] == s[j]:
        j += 1
        lps[i] = j

borders = []
k = lps[n-1]
while k > 0:
    borders.append(k)
    k = lps[k-1]

borders.reverse()
print(" ".join(map(str, borders)))