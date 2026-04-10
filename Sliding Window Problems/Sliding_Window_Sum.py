n, k = map(int, input().split())
x, a, b, c = map(int, input().split())

window_sum = 0
xor_result = 0
arr = []

for i in range(n):
    if i == 0:
        xi = x
    else:
        xi = (a * xi + b) % c
    arr.append(xi)
    window_sum += xi
    if i >= k:
        window_sum -= arr[i - k]
    if i >= k - 1:
        xor_result ^= window_sum

print(xor_result)