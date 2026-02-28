import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arrivals = []
    departures = []

    for _ in range(n):
        a, b = map(int, input().split())
        arrivals.append(a)
        departures.append(b)

    arrivals.sort()
    departures.sort()

    i = j = 0
    current = 0
    max_customers = 0

    while i < n:
        # if next arrival is before next departure
        if arrivals[i] < departures[j]:
            current += 1
            max_customers = max(max_customers, current)
            i += 1
        else:
            current -= 1
            j += 1

    print(max_customers)

if __name__ == "__main__":
    solve()