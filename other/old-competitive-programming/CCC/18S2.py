def rotate(grid):
    newGrid = []
    for col in range(len(grid[0])):
        add = []
        for row in range(len(grid) - 1, -1, -1):
            add.append(grid[row][col])
        newGrid.append(add)
    return newGrid


def possibleSolve(grid):
    for rowi in range(len(grid) - 1):
        gridRowCopy = sorted(grid[rowi])
        if grid[rowi] == gridRowCopy:
            for coli, col in enumerate(grid[rowi]):
                if col < grid[rowi + 1][coli]:
                    continue
                else:
                    return False
        else:
            return False
    return True


if __name__ == "__main__":
    n = int(input())
    grid = []
    for _ in range(n):
        row = list(map(int, input().split()))
        grid.append(row)

    for _ in range(4):
        rowZero = sorted(grid[0])
        if grid[0][0] < grid[1][0] and rowZero == grid[0]:

            if possibleSolve(grid):
                for row in grid:
                    print(*row)
                break

        else:
            grid = rotate(grid)
