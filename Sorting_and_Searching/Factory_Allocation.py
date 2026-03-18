n, t = map(int, input().split())
k = list(map(int, input().split()))

left, right = 1, t * min(k)
answer = right

while left <= right:
    mid = (left + right) // 2
    total = sum(mid // time for time in k)
    
    if total >= t:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)