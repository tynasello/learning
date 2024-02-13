# This solution works for small test cases, however the backtracking method is enefficient to solve larger ones and exceeds time limits.
# I'm working on a faster solution
import sys

maximum = sys.maxsize
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


moves = [[-1, 0], [0, -1], [1, 0], [0, 1]]
conveyor = ["U", "D", "L", "R"]
conveyorMove = [[-1, 0], [1, 0], [0, -1], [0, 1]]

alreadyVisited = set()


def solve(grid, currRow, currCol, getTo, movesTaken, minimum):
    visitedCopy = visited
    if movesTaken > minimum:
        return minimum
    if isValidPos(grid, currRow, currCol):
        if currRow == getTo[0] and currCol == getTo[1]:
            minimum = min(minimum, movesTaken)
        if grid[currRow][currCol] in conveyor:
            for i, c in enumerate(conveyor):
                if grid[currRow][currCol] == c:
                    currRow += conveyorMove[i][0]
                    currCol += conveyorMove[i][1]
                    if (currRow, currCol) not in alreadyVisited:
                        alreadyVisited.add((currRow, currCol))
                        minimum = solve(
                            grid,
                            currRow,
                            currCol,
                            getTo,
                            movesTaken,
                            minimum,
                        )
                        alreadyVisited.remove((currRow, currCol))
                    currRow -= conveyorMove[i][0]
                    currCol -= conveyorMove[i][1]
        else:
            for move in range(4):
                currRow += moves[move][0]
                currCol += moves[move][1]
                movesTaken += 1

                if (currRow, currCol) not in alreadyVisited:
                    # cant go back otherwise we will run into maximum recursion depth as we continously move back and forth between same indexs
                    alreadyVisited.add((currRow, currCol))
                    minimum = solve(grid, currRow, currCol, getTo, movesTaken, minimum)
                    alreadyVisited.remove((currRow, currCol))
                currRow -= moves[move][0]
                currCol -= moves[move][1]
                movesTaken -= 1
    return minimum


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
                escapePos.append((rowi, coli))
            if grid[rowi][coli] == "S":
                currRow = rowi
                currCol = coli
    for pos in range(find):
        res = solve(grid, currRow, currCol, escapePos[pos], 0, maximum)
        if res == maximum:
            print(-1)
        else:
            print(res)
