def movies(times):
    times.sort(key = lambda x : x[1])

    count = 0
    current_end = 0

    for start, end in times:
        if start >= current_end:
            count += 1
            current_end = end
    return count

def solve():
    t = int(input())
    times = []

    for _ in range(t):
        x, y = map(int, input().split())
        times.append((x, y))
    print(movies(times))

if __name__ == "__main__":
    solve()