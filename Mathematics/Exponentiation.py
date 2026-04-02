MOD = 10**9 + 7

def mod_pow(a, b):
    res = 1
    a %= MOD
    while b:
        if b & 1:
            res = res * a % MOD
        a = a * a % MOD
        b >>= 1
    return res

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(mod_pow(a, b))