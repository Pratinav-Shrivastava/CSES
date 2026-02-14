n = int(input())

if n%4 not in (0, 3):
    print("NO")
else:
    print("YES")

    set1 = []
    set2 = []

    if n%4 == 0:
        for i in range(1, n//2+1, 2):
            set1.append(i)
            set1.append(n-i+1)
            set2.append(i+1)
            set2.append(n-i)

    else:
        set1.extend([1,2])
        set2.extend([3])

        for i in range(4, (n+1)//2 + 1, 2):
            set1.append(i)
            set1.append(n-i+4)
            set2.append(i+1)
            set2.append(n-i+3)
            
    print(len(set1))
    print(*set1)
    print(len(set2))
    print(*set2)