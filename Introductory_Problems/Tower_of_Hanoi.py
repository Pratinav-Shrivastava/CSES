def hanoi(n, start, end, moves):
    if n == 1:
        moves.append((start, end))
        return
    else:
        other = 6 - (start + end)
        hanoi(n-1, start, other, moves)
        moves.append((start, end))
        hanoi(n-1, other, end, moves)

def solve():
    n = int(input())
    moves = []
    hanoi(n, 1, 3, moves)

    print(len(moves))
    for move in moves:
        print(move[0], move[1])

if __name__ == "__main__":
    solve()