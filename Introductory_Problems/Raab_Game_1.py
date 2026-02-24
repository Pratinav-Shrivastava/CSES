def raab_game(n, a, b):
    if a == 0 and b == 0:
        print("YES")
        for i in range(n):
            print(i + 1, end=" ")
        print()
        for i in range(n):
            print(i + 1, end=" ")
        print()
        return

    if a == 0 or b == 0 or a + b > n:
        print("NO")
        return

    print("YES")
    offset = n - a - b

    for i in range(n):
        print(i + 1, end=" ")
    print()

    for i in range(offset):
        print(i + 1, end=" ")
    for i in range(offset + a, n):
        print(i + 1, end=" ")
    for i in range(offset, offset + a):
        print(i + 1, end=" ")
    print()


def solve():
    t = int(input())
    for _ in range(t):
        n, a, b = map(int, input().split())
        raab_game(n, a, b)


if __name__ == "__main__":
    solve()

# def raab_game(n, a, b):
#     if a + b > n:
#         return "NO"
    
#     p1 = list(range(1, n+1))
#     p2 = []
#     p2.extend(range(1, n-b+1))
#     p2.extend(range(n, n-b, -1))

#     result = "YES\n"
#     result += "".join(map(str, p1)) + "\n"
#     result += "".join(map(str, p2))
#     return result
    

# def solve():
#     t = int(input())
#     for _ in range(t):
#         n, a, b = map(int, input().split())
#         print(raab_game(n, a, b))

# if __name__ == "__main__":
#     solve()