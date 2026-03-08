n = int(input())
songs = list(map(int, input().split()))

seen = set()
l = 0
ans = 0

for r in range(n):
    while songs[r] in seen:
        seen.remove(songs[l])
        l += 1
    
    seen.add(songs[r])
    ans = max(ans, r - l + 1)

print(ans)