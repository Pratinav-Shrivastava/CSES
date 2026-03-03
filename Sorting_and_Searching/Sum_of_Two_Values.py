def sum_of_two_values(nums, x):
    c = [(nums[i], i + 1) for i in range(len(nums))]
    c.sort()
    
    i, j = 0, len(nums) - 1
    
    while i < j:
        s = c[i][0] + c[j][0]
        
        if s == x:
            return c[i][1], c[j][1]
        elif s < x:
            i += 1
        else:
            j -= 1
    
    return None


def solve():
    n, x = map(int, input().split())
    nums = list(map(int, input().split()))
    
    result = sum_of_two_values(nums, x)
    
    if result is None:
        print("IMPOSSIBLE")
    else:
        print(*result)

if __name__ == "__main__":
    solve()