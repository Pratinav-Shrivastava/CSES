def contributes(a, b, pos):
    if a < 1 or b < 1 or a >= len(pos) or b >= len(pos):
        return 0
    return 1 if pos[a] > pos[b] else 0

def solve():
    n, m = map(int, input().split())
    arr = [0] + list(map(int, input().split()))

    pos = [0] * (n + 1)

    for i in range(1, n + 1):
        pos[arr[i]] = i

    rounds = 1
    for i in range(1, n):
        if pos[i] > pos[i + 1]:
            rounds += 1

    for _ in range(m):
        a, b = map(int, input().split())

        x = arr[a]
        y = arr[b]

        pairs = {
            (x - 1, x),
            (x, x + 1),
            (y - 1, y),
            (y, y + 1)
        }

        for u, v in pairs:
            if 1 <= u <= n and 1 <= v <= n:
                rounds -= contributes(u, v, pos)

        arr[a], arr[b] = arr[b], arr[a]
        pos[x], pos[y] = pos[y], pos[x]

        for u, v in pairs:
            if 1 <= u <= n and 1 <= v <= n:
                rounds += contributes(u, v, pos)

        print(rounds)

if __name__ == "__main__":
    solve()
    