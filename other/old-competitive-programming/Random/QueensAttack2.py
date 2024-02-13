"""
You will be given a square chess board with one queen and a number of obstacles placed on it. Determine how many squares the queen can attack.
A queen is standing on an n x n chessboard. The chess board's rows are numbered from 1 to n, going from bottom to top. 
Its columns are numbered from 1 to n, going from left to right. 
Each square is referenced by a tuple, (r,c), describing the row, r, and column, c, where the square is located.

Sample Input 1
5 3
4 3
5 5
4 2
2 3
Sample Output 1
10
"""


def solve(row, col, n, obstacles):
    total = 0
    operations = [[0, 1], [0, -1], [-1, 0], [1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]]
    for o in operations:
        currR = row + o[0]
        currC = col + o[1]
        while currC != 0 and currC != n + 1 and currR != 0 and currR != n + 1:
            if (currR, currC) in obstacles:
                break
            total += 1
            currR += o[0]
            currC += o[1]
    return total


if __name__ == "__main__":
    n, o = map(int, input().split())
    row, col = map(int, input().split())
    obstacles = []
    if o != 0:
        for _ in range(o):
            obstacles.append(tuple(map(int, input().split())))
    print(solve(row, col, n, obstacles))


"""
5 3
4 3
5 5
4 2
2 3
"""