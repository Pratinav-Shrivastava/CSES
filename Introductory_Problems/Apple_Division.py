def apple_division(weights):
    total = sum(weights)
    ans = float("inf")

    def search(index, group1_sum):
        nonlocal ans
        
        if index == len(weights):
            diff = abs(total - 2*group1_sum)
            ans = min(ans, diff)
            return
    
        search(index + 1, group1_sum + weights[index])
        search(index + 1, group1_sum)

    search(0,0)
    return ans
    

def solve():
    n = int(input())
    weights = list(map(int, input().split()))
    print(apple_division(weights))

if __name__ == "__main__":
    solve()