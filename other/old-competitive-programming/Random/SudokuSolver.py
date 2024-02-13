"""
given a partially filled n*n sudoku board, solve the board and print a valid output
Input:
[
  ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
  ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
  ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
  ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
  ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
  ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
  ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
  ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
  ['.', '.', '.', '.', '8', '.', '.', '7', '9']
]

Output:
[
  ['5', '3', '4', '6', '7', '8', '9', '1', '2'],
  ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
  ['1', '9', '8', '3', '4', '2', '5', '6', '7'],
  ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
  ['4', '2', '6', '8', '5', '3', '7', '9', '1'],
  ['7', '1', '3', '9', '2', '4', '8', '5', '6'],
  ['9', '6', '1', '5', '3', '7', '2', '8', '4'],
  ['2', '8', '7', '4', '1', '9', '6', '3', '5'],
  ['3', '4', '5', '2', '8', '6', '1', '7', '9']
]
"""


def isValid(board, n, currRow, currCol, num):
    # check col
    for i in range(n):
        if board[i][currCol] == num:
            return False
    # check row
    for i in range(n):
        if board[currRow][i] == num:
            return False
    # check subgrid
    # subgrids are always 3*3
    # subgrid cols/rows are 0-2,3-5,6-9...
    rowStart = currRow
    colStart = currCol
    while rowStart % 3 != 0:
        rowStart -= 1
    while colStart % 3 != 0:
        colStart -= 1
    for _ in range(3):
        for _ in range(3):
            if board[rowStart][colStart] == num:
                return False
            colStart += 1
        rowStart += 1
        colStart -= 3
    return True


def solve(board, n, currRow, currCol):
    if currCol >= n:
        currRow += 1
        currCol = 0
        if currRow >= n:
            return True
    if board[currRow][currCol] != ".":
        return solve(board, n, currRow, currCol + 1)
    for num in range(1, n + 1):
        if isValid(board, n, currRow, currCol, str(num)):
            board[currRow][currCol] = str(num)
            if solve(board, n, currRow, currCol + 1):
                return True
            board[currRow][currCol] = "."
    return False


if __name__ == "__main__":
    board = [
        ["3", ".", "6", "5", ".", "8", "4", ".", "."],
        ["5", "2", ".", ".", ".", ".", ".", ".", "."],
        [".", "8", "7", ".", ".", ".", ".", "3", "1"],
        [".", ".", "3", ".", "1", ".", ".", "8", "."],
        ["9", ".", ".", "8", "6", "3", ".", ".", "5"],
        [".", "5", ".", ".", "9", ".", "6", ".", "."],
        ["1", "3", ".", ".", ".", ".", "2", "5", "."],
        [".", ".", ".", ".", ".", ".", ".", "7", "4"],
        [".", ".", "5", "2", ".", "6", "3", ".", "."],
    ]

    n = len(board[0])
    solve(board, n, 0, 0)
    for r in board:
        print(r)
