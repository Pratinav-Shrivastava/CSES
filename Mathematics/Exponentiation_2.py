MOD = 10**9 + 7

def mod_pow(a, b, mod):
    res = 1
    a %= mod
    while b:
        if b & 1:
            res = res * a % mod
        a = a * a % mod
        b >>= 1
    return res

n = int(input())
for _ in range(n):
    a, b, c = map(int, input().split())
    
    exp = mod_pow(b, c, MOD-1)
    
    if a == 0:
        print(1 if exp == 0 else 0)
    else:
        print(mod_pow(a, exp, MOD))