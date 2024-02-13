conveyor = ["U", "D", "L", "R"]
conveyorMove = [[-1, 0], [1, 0], [0, -1], [0, 1]]
cameraHelper = [[0, 1], [0, -1], [-1, 0], [1, 0]]


def isValidPos(grid, currRow, currCol):
    if currRow == 0 or currRow == len(grid):
        return False
    if currCol == 0 or currCol == len(grid[0]):
        return False
    if grid[currRow][currCol] == "W" or grid[currRow][currCol] == "C":
        return False
    if grid[currRow][currCol] in conveyor:
        return True
    else:
        # Check left right up and down for cameras
        # up and below
        for i in range(len(cameraHelper)):
            rowCopy = currRow
            colCopy = currCol
            while True:
                rowCopy += cameraHelper[i][0]
                colCopy += cameraHelper[i][1]
                if grid[rowCopy][colCopy] == "C":
                    return False
                elif grid[rowCopy][colCopy] == "W":
                    break
    return True


incrimentHelper = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def buildTree(grid, currRow, currCol, n, m):
    if isValidPos(grid, currRow, currCol):
        currLevel = [[currRow, currCol]]
    else:
        currLevel = []
    visited = set()
    visited.add((currRow, currCol))
    tree = {}
    nextLevel = [[currRow, currCol]]
    level = 1
    while len(nextLevel) != 0:
        nextLevel = []
        for pos in currLevel:
            # Check up down left and right
            for x in range(4):
                row = pos[0]
                col = pos[1]
                row += incrimentHelper[x][0]
                col += incrimentHelper[x][1]
                for i, letter in enumerate(conveyor):
                    if grid[row][col] == letter:
                        row += conveyorMove[i][0]
                        col += conveyorMove[i][1]
                if row <= n - 1 and row >= 0 and col <= m - 1 and col >= 0:
                    if (row, col) in visited:
                        continue
                    else:
                        visited.add((row, col))
                        if isValidPos(grid, row, col):
                            nextLevel.append([row, col])
        if nextLevel != []:
            tree[level] = nextLevel
        currLevel = nextLevel
        level += 1
    return tree


if __name__ == "__main__":
    visited = []
    grid = []
    row, col = map(int, input().split())
    find = 0
    escapePos = []
    for rowi in range(row):
        grid.append(list(input()))
        visited.append([0 for _ in range(col)])
        for coli in range(col):
            if grid[rowi][coli] == ".":
                find += 1
                escapePos.append([rowi, coli])
            if grid[rowi][coli] == "S":
                currRow = rowi
                currCol = coli
    tree = buildTree(grid, currRow, currCol, row, col)

    for end in escapePos:
        res = []
        for key, value in tree.items():
            if end in value:
                res.append(key)
        if len(res) == 0:
            print(-1)
        else:
            print(res[0])