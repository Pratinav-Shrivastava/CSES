n = int(input())
arr = list(map(int, input().split()))

seen = set()
l = 0
ans = 0

for r in range(n):
    while arr[r] in seen:
        seen.remove(arr[l])
        l += 1
    seen.add(arr[r])
    ans += r - l + 1

print(ans)