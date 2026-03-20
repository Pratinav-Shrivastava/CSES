n = int(input())
t = list(map(int, input().split()))

total = sum(t)
mx = max(t)

print(max(total, 2*mx))