def max_subarray_sum(nums):
    curr_sum, best_sum = nums[0], nums[0]
    for i in range(1, len(nums)):
        curr_sum = max(nums[i], curr_sum+nums[i])
        best_sum = max(curr_sum, best_sum)
    return best_sum

def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    print(max_subarray_sum(nums))

if __name__ == "__main__":
    solve()