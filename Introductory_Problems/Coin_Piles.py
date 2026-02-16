t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    total = a + b
    if total % 3 == 0 and max(a,b) <= 2 * min(a,b):
        print("YES")
    else:
        print("NO")