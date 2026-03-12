from collections import deque

n = int(input())
circle = deque(range(1, n + 1))
result = []

while circle:
    circle.rotate(-1)
    result.append(circle.popleft())

print(*result)