def digit_query(n):
    i = 1
    count = 9
    start = 1

    while n > (i*count):
        n -= i*count
        i += 1
        count *= 10
        start *= 10

    number = start + (n-1)//i
    return int(str(number)[(n-1)%i])

def solve():
    q = int(input())
    for _ in range(q):
        k = int(input())
        print(digit_query(k))

if __name__ == "__main__":
    solve()