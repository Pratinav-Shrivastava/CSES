MOD = 10**9 + 7
import sys
input = sys.stdin.read
data = input().split()
n = int(data[0])
queries = [(int(data[i]), int(data[i+1])) for i in range(1, len(data), 2)]

MAX = 10**6
fact = [1] * (MAX + 1)
for i in range(1, MAX + 1):
    fact[i] = fact[i-1] * i % MOD

inv = [1] * (MAX + 1)
inv[MAX] = pow(fact[MAX], MOD-2, MOD)
for i in range(MAX, 0, -1):
    inv[i-1] = inv[i] * i % MOD

for a, b in queries:
    res = fact[a] * inv[b] % MOD * inv[a-b] % MOD
    print(res)