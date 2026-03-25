n = int(input())
a = list(map(int, input().split()))

count = [0] * n
count[0] = 1

prefix = 0
result = 0

for val in a:
    prefix += val
    mod = prefix % n
    result += count[mod]
    count[mod] += 1

print(result)