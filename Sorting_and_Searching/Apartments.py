def apartments(desired, sizes, k):
    desired.sort()
    sizes.sort()

    i, j = 0, 0
    given = 0
    while i < len(desired) and j < len(sizes):
        if abs(desired[i] - sizes[j]) <= k:
            given += 1
            i += 1
            j += 1
        else:
            if sizes[j] < desired[i]:
                j += 1
            else:
                i += 1
    return given

def solve():
    n, m, k = map(int, input().split())
    desired = list(map(int, input().split()))
    sizes = list(map(int, input().split()))
    print(apartments(desired, sizes, k))

if __name__ == "__main__":
    solve()