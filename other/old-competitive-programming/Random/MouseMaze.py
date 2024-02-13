def isValid(maze, x, y):
    if x < n and y < n and x >= 0 and y >= 0 and maze[x][y] == 1:
        return True
    return False


def solveMaze(maze, x, y, sol):
    if x == n - 1 and y == n - 1 and maze[x][y] == 1:
        sol[x][y] = 1
        return True
    if isValid(maze, x, y):
        sol[x][y] = 1
        if solveMaze(maze, x + 1, y, sol):
            return True
        if solveMaze(maze, x, y + 1, sol):
            return True
        sol[x][y] = 0
        return False


n = 4
maze = [[1, 0, 0, 0], [1, 1, 0, 1], [0, 1, 0, 0], [1, 1, 1, 1]]
sol = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
if solveMaze(maze, 0, 0, sol):
    print(sol)
else:
    print(False)
