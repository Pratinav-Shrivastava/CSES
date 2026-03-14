I = lambda : map(int, input().split())

n, x = I()
coins = sorted(I())

sol = [0] + [10 ** 9] * x

f = [0] * (x + 1)

for c in coins:
    for i in range(c, x + 1):
        if sol[i - c] + 1 < sol[i]: 
            sol[i] = sol[i - c] + 1
            f[i] = c

if sol[x] == 10 ** 9: print("-1")
else: 
    print(sol[x])