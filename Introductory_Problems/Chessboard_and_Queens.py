board = [input() for _ in range(8)]
col_used = [False] * 8
diag1_used = [False] * 15
diag2_used = [False] * 15

ans = 0

def backtrack(row):
    global ans

    if row == 8:
        ans += 1
        return
    
    for col in range(8):
        if board[row][col] == "*":
            continue

        d1 = row - col + 7
        d2 = row + col

        if col_used[col] or diag1_used[d1] or diag2_used[d2]:
            continue

        col_used[col] = True
        diag1_used[d1] = True
        diag2_used[d2] = True

        backtrack(row+1)

        col_used[col] = False
        diag1_used[d1] = False
        diag2_used[d2] = False

backtrack(0)
print(ans)