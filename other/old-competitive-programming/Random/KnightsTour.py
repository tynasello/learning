def isValid(board, x, y):
    if x >= 0 and y >= 0 and x < n and y < n and board[x][y] == -1:
        return True
    return False


def printSolution(board):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()


def main(n):
    board = []
    for _ in range(n):
        temp = []
        for _ in range(n):
            temp.append(-1)
        board.append(temp)
    pos = 1
    board[0][0] = 0
    xMoves = [2, 1, -1, -2, -2, -1, 1, 2]
    yMoves = [1, 2, 2, 1, -1, -2, -2, -1]

    if solveChess(board, 0, 0, xMoves, yMoves, pos):
        printSolution(board)


def solveChess(board, xCurrent, yCurrent, xMoves, yMoves, pos):
    if pos == n ** 2:
        return True
    for i in range(n):
        newX = xCurrent + xMoves[i]
        newY = yCurrent + yMoves[i]
        if isValid(board, newX, newY):
            board[newX][newY] = pos
            if solveChess(board, newX, newY, xMoves, yMoves, pos + 1):
                return True
            board[newX][newY] = -1
    return False


if __name__ == "__main__":
    global n
    n = 8
    main(n)
