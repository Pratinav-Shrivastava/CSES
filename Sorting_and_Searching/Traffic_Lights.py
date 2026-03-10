import heapq

def traffic_lights(x, arr):
    n = len(arr)

    lights = [0] + arr + [x]
    lights.sort()

    seg = []
    for i in range(1, len(lights)):
        seg.append(lights[i] - lights[i-1])

    max_heap = []
    for s in seg:
        heapq.heappush(max_heap, -s)

    res = [0]*n
    res[-1] = -max_heap[0]

    pos_index = {v:i for i,v in enumerate(lights)}

    left = [i-1 for i in range(len(lights))]
    right = [i+1 for i in range(len(lights))]

    import collections
    count = collections.Counter(seg)

    for i in range(n-1,0,-1):
        p = arr[i]
        idx = pos_index[p]

        l = left[idx]
        r = right[idx]

        a = lights[idx] - lights[l]
        b = lights[r] - lights[idx]
        c = lights[r] - lights[l]

        count[a] -= 1
        count[b] -= 1
        count[c] += 1

        heapq.heappush(max_heap,-c)

        right[l] = r
        left[r] = l

        while count[-max_heap[0]] == 0:
            heapq.heappop(max_heap)

        res[i-1] = -max_heap[0]

    return res


def solve():
    x, n = map(int, input().split())
    arr = list(map(int, input().split()))

    ans = traffic_lights(x, arr)
    print(*ans)


if __name__ == "__main__":
    solve()