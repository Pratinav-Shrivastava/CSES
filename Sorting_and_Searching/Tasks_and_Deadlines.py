n = int(input())
tasks = [tuple(map(int, input().split())) for _ in range(n)]
tasks.sort(key=lambda x: x[0])

current_time = 0
total_reward = 0

for a, d in tasks:
    current_time += a
    total_reward += d - current_time

print(total_reward)