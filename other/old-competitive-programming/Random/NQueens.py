def isValid(board, row, col):
    # left
    for i in range(col):
        if board[row][i] == 1:
            return False
    # left up
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    # right up
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


# board = [     [1, 2,  3,  4],
#               [5, 6,  7,  8],
#               [9, 10 ,11 ,12 ], 11 r = 2 c = 2
#               [13,14, 15, 16] ]
def chess(board, col):
    if col >= n:
        count.append(1)
        return True
    for i in range(n):
        if isValid(board, i, col):
            board[i][col] = 1
            chess(board, col + 1)
            board[i][col] = 0
    return


n = 4
board = []

for i2 in range(n):
    temp = []
    for i in range(n):
        temp.append(0)
    board.append(temp)
count = []
chess(board, 0)

res = 0
for i in count:
    res += 1
print(res)