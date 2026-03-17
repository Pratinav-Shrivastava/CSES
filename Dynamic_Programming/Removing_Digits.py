n = int(input())
dp = [0] + [float('inf')] * n
for i in range(1, n + 1):
    for d in str(i):
        dp[i] = min(dp[i], dp[i - int(d)] + 1)
print(dp[n])