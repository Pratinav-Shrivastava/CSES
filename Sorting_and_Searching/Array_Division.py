n, k = map(int, input().split())
a = list(map(int, input().split()))

def can_divide(max_sum):
    count = 1
    current = 0
    for val in a:
        if current + val <= max_sum:
            current += val
        else:
            count += 1
            current = val
    return count <= k

low, high = max(a), sum(a)

while low < high:
    mid = (low + high) // 2
    if can_divide(mid):
        high = mid
    else:
        low = mid + 1

print(low)