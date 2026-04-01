MOD = 10**9 + 7

n = int(input())
p = input().strip()
m = len(p)

lps = [0]*m
j = 0
for i in range(1, m):
    while j > 0 and p[i] != p[j]:
        j = lps[j-1]
    if p[i] == p[j]:
        j += 1
    lps[i] = j

go = [[0]*26 for _ in range(m)]
for i in range(m):
    for c in range(26):
        ch = chr(ord('A') + c)
        j = i
        while j > 0 and p[j] != ch:
            j = lps[j-1]
        if p[j] == ch:
            j += 1
        go[i][c] = j

dp = [[0]*m for _ in range(n+1)]
dp[0][0] = 1

for i in range(n):
    for j in range(m):
        if dp[i][j] == 0:
            continue
        for c in range(26):
            nj = go[j][c]
            if nj < m:
                dp[i+1][nj] = (dp[i+1][nj] + dp[i][j]) % MOD

bad = sum(dp[n]) % MOD
total = pow(26, n, MOD)
print((total - bad) % MOD)