def solve(n, k):
    if n == 1:
        return 1
    if k <= n // 2:
        return 2 * k
    if n % 2 == 0:
        return 2 * solve(n // 2, k - n // 2) - 1
    x = solve((n + 1) // 2, k - n // 2)
    if x == 1:
        return n
    return 2 * x - 3

q = int(input())
for _ in range(q):
    n, k = map(int, input().split())
    print(solve(n, k))