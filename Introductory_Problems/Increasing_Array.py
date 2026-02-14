n = int(input())
nums = list(map(int, input().split()))

moves = 0
for i in range(1, n):
    if nums[i] < nums[i-1]:
        moves += nums[i-1] - nums[i]
        nums[i] = nums[i-1]

print(moves)