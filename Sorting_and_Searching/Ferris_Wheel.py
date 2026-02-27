def min_gandola(n, x, weights):
    weights.sort()

    seats = 0
    l, r = 0, n-1
    while l <= r:
        if weights[l] + weights[r] <= x:
            l += 1
        r -= 1
        seats += 1

    return seats

def solve():
    n, x = map(int, input().split())
    weights = list(map(int, input().split()))
    print(min_gandola(n, x, weights))

if __name__ == "__main__":
    solve()