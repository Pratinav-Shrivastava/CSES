def distinct_numbers(nums):
    nums.sort()

    distinct_count = 0
    prev = None
    for num in nums:
        if num != prev:
            distinct_count += 1
            prev = num
    return distinct_count

def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    print(distinct_numbers(nums))

if __name__ == "__main__":
    solve()