def tower_of_hanoi(n, source, target, spare, moves):
    if n == 1:
        moves.append((source, target))
        return
    tower_of_hanoi(n-1, source, spare, target, moves)
    moves.append((source, target))
    tower_of_hanoi(n-1, spare, target, source, moves)

def solve():
    n = int(input())
    moves = []
    tower_of_hanoi(n, 1, 3, 2, moves)
    print(len(moves))
    for move in moves:
        print(move[0], move[1])

if __name__ == "__main__":
    solve()