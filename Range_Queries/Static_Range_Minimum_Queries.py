n, q = map(int, input().split())
arr = list(map(int, input().split()))

size = 1
while size < n:
    size *= 2
tree = [float('inf')] * (2 * size)

for i in range(n):
    tree[size + i] = arr[i]
for i in range(size - 1, 0, -1):
    tree[i] = min(tree[2 * i], tree[2 * i + 1])

def query(l, r):
    l += size - 1
    r += size - 1
    res = float('inf')
    while l <= r:
        if l % 2 == 1:
            res = min(res, tree[l])
            l += 1
        if r % 2 == 0:
            res = min(res, tree[r])
            r -= 1
        l //= 2
        r //= 2
    return res

for _ in range(q):
    a, b = map(int, input().split())
    print(query(a, b))