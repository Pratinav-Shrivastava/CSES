def count_rounds(n, arr):
    pos = [0] * (n + 1)

    for i, v in enumerate(arr, start=1):
        pos[v] = i

    rounds = 1

    for i in range(2, n + 1):
        if pos[i] < pos[i - 1]:
            rounds += 1

    return rounds


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))

    print(count_rounds(n, arr))