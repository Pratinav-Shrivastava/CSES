I = lambda : map(int, input().split())
n, x = I()
a = [(idx + 1, i) for idx, i in enumerate(list(I()))]
a = sorted(a, key = lambda elem : elem[1]) 

found = False
for idx, (_, val_1) in enumerate(a):
    l, r = idx + 1, n - 1
    while True:
        if l >= r: break

        f = a[l][1] + a[r][1]

        if f < x - val_1: l += 1
        if f > x - val_1: r -= 1

        if f == x - val_1:
            print(a[l][0], a[r][0], _)
            found = True; break
    
    if found: break

if found == False: print("IMPOSSIBLE")