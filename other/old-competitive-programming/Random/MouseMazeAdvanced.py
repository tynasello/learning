# MULTIPLE JUMPS


def isValid(maze, x, y):
    if x < n and y < n and x >= 0 and y >= 0 and maze[x][y] != 0:
        return True
    return False


def solveMaze(maze, x, y, sol):
    if x == n - 1 and y == n - 1 and maze[x][y] != 0:
        sol[x][y] = 1
        return True
    if isValid(maze, x, y):
        sol[x][y] = 1
        for i in range(1, n):
            if i <= maze[x][y]:
                if solveMaze(maze, x + i, y, sol):
                    sol[x][y] = 1
                    return True
                if solveMaze(maze, x, y + i, sol):
                    return True
        sol[x][y] == 0
        return False
    return False


n = 4
maze = [[2, 1, 0, 0], [3, 0, 0, 1], [0, 1, 0, 1], [0, 0, 0, 1]]
sol = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
# Output { {1, 0, 0, 0},
#            {1, 0, 0, 1},
#            {0, 0, 0, 1},
#            {0, 0, 0, 1}
#          }
print(solveMaze(maze, 0, 0, sol))
print(sol)
