"""
CCC 2019 SENIOR PROBLEM 3
"""
import random


def findMissing(a, b, c):
    if a == "X":
        d = c - b
        return b - d
    elif b == "X":
        d = (c - a) // 2
        return a + d
    else:
        d = b - a
        return b + d


def fillMost(grid):

    # Start by filling all rows or cols that have two values
    for rowi, row in enumerate(grid):
        for vali, val in enumerate(row):
            if val == "X":
                # see if we can solve
                # LOOK IN ROW
                if vali == 0:
                    if grid[rowi][1] != "X" and grid[rowi][2] != "X":
                        grid[rowi][0] = findMissing(row[0], row[1], row[2])
                elif vali == 1:
                    if grid[rowi][0] != "X" and grid[rowi][2] != "X":
                        grid[rowi][1] = findMissing(row[0], row[1], row[2])
                elif vali == 2:
                    if grid[rowi][0] != "X" and grid[rowi][1] != "X":
                        grid[rowi][2] = findMissing(row[0], row[1], row[2])
                if grid[rowi][vali] == "X":
                    # LOOK IN COL
                    if rowi == 0:
                        if grid[1][vali] != "X" and grid[2][vali] != "X":
                            grid[0][vali] = findMissing(
                                grid[0][vali], grid[1][vali], grid[2][vali]
                            )
                    elif rowi == 1:
                        if grid[0][vali] != "X" and grid[2][vali] != "X":
                            grid[1][vali] = findMissing(
                                grid[0][vali], grid[1][vali], grid[2][vali]
                            )
                    else:
                        if grid[0][vali] != "X" and grid[1][vali] != "X":
                            grid[2][vali] = findMissing(
                                grid[0][vali], grid[1][vali], grid[2][vali]
                            )
            if grid[rowi][vali] != "X":
                # see if we can solve others
                # LOOK IN ROW
                if vali == 0:
                    if grid[rowi][1] != "X" and grid[rowi][2] == "X":
                        grid[rowi][2] = findMissing(row[0], row[1], row[2])
                    elif grid[rowi][1] == "X" and grid[rowi][2] != "X":
                        grid[rowi][1] = findMissing(row[0], row[1], row[2])

                elif vali == 1:
                    if grid[rowi][0] != "X" and grid[rowi][2] == "X":
                        grid[rowi][2] = findMissing(row[0], row[1], row[2])
                    elif grid[rowi][0] == "X" and grid[rowi][2] != "X":
                        grid[rowi][0] = findMissing(row[0], row[1], row[2])

                else:
                    if grid[rowi][0] != "X" and grid[rowi][1] == "X":
                        grid[rowi][1] = findMissing(row[0], row[1], row[2])
                    elif grid[rowi][0] == "X" and grid[rowi][1] != "X":
                        grid[rowi][0] = findMissing(row[0], row[1], row[2])
                # LOOK IN COL
                if rowi == 0:
                    if grid[1][vali] == "X" and grid[2][vali] != "X":
                        grid[1][vali] = findMissing(
                            grid[0][vali], grid[1][vali], grid[2][vali]
                        )
                    elif grid[1][vali] != "X" and grid[2][vali] == "X":
                        grid[2][vali] = findMissing(
                            grid[0][vali], grid[1][vali], grid[2][vali]
                        )

                elif rowi == 1:
                    if grid[0][vali] != "X" and grid[2][vali] == "X":
                        grid[2][vali] = findMissing(
                            grid[0][vali], grid[1][vali], grid[2][vali]
                        )
                    elif grid[0][vali] == "X" and grid[2][vali] != "X":
                        grid[0][vali] = findMissing(
                            grid[0][vali], grid[1][vali], grid[2][vali]
                        )

                else:
                    if grid[0][vali] != "X" and grid[1][vali] == "X":
                        grid[1][vali] = findMissing(
                            grid[0][vali], grid[1][vali], grid[2][vali]
                        )
                    if grid[0][vali] == "X" and grid[1][vali] != "X":
                        grid[0][vali] = findMissing(
                            grid[0][vali], grid[1][vali], grid[2][vali]
                        )

    return grid


def cross(grid):
    # print(grid)
    rowi = 0
    coli = 0
    for i, row in enumerate(grid):
        if "X" not in row:
            rowi = i

    for i in range(3):
        col = []
        for i2 in range(3):
            col.append(grid[i2][i])
        if "X" not in col:
            coli = i
    d = grid[1][coli] - grid[0][coli]
    if rowi == 0:
        grid[1][0] = grid[0][0] + d
        grid[2][0] = grid[0][0] + 2 * d
        grid[1][1] = grid[0][1] + d
        grid[2][1] = grid[0][1] + 2 * d
        grid[1][2] = grid[0][2] + d
        grid[2][2] = grid[0][2] + 2 * d

    elif rowi == 1:
        grid[0][0] = grid[1][0] - d
        grid[2][0] = grid[1][0] + d
        grid[0][1] = grid[1][1] - d
        grid[2][1] = grid[1][1] + d
        grid[0][2] = grid[1][2] - d
        grid[2][2] = grid[1][2] + d
    else:
        grid[0][0] = grid[2][0] - 2 * d
        grid[1][0] = grid[2][0] - d
        grid[0][1] = grid[2][1] - 2 * d
        grid[1][1] = grid[2][1] - d
        grid[0][2] = grid[2][2] - 2 * d
        grid[1][2] = grid[2][2] - d
    return grid


def solve(grid):

    # case where we only have diagonal values once
    if grid[1][1] != "X":
        if (
            grid[0][1] == "X"
            and grid[1][0] == "X"
            and grid[1][2] == "X"
            and grid[2][1] == "X"
        ):
            if (
                grid[0][2] == "X"
                and grid[2][0] == "X"
                and grid[0][0] != "X"
                and grid[2][2] != "X"
            ):
                grid[0][1] = grid[1][1]
                grid[2][1] = grid[1][1]
            elif (
                grid[0][2] != "X"
                and grid[2][0] != "X"
                and grid[0][0] == "X"
                and grid[2][2] == "X"
            ):
                grid[0][1] = grid[1][1]
                grid[2][1] = findMissing(grid[0][1], grid[1][1], grid[2][1])
    # case where we have a grid like this
    # 14 X X
    # X X 18
    # X 16 X
    # make middle value equal to one of the two adjacent values
    else:
        cornerXCount = 0
        cornerI = (0, 0)
        numCount = 0
        for row in (0, 2):
            for val in (0, 2):
                if grid[row][val] == "X":
                    cornerXCount += 1
                else:
                    cornerI = (row, val)
        for row in grid:
            for val in row:
                if val != "X":
                    numCount += 1
        if cornerXCount == 3 and numCount == 3:
            if cornerI == (0, 0):
                grid[1][1] = grid[2][1]
                grid[0][1] = grid[2][1]
            elif cornerI == (0, 2):
                grid[1][1] = grid[2][1]
                grid[0][1] = grid[2][1]
            elif cornerI == (2, 0):
                grid[1][1] = grid[0][1]
                grid[2][1] = grid[2][1]
            else:
                grid[1][1] = grid[0][1]
                grid[0][1] = grid[2][1]
    # Only have two values not in same row or col
    nCount = 0
    pos = []
    for i, row in enumerate(grid):
        for i2, val in enumerate(row):
            if val != "X":
                nCount += 1
                pos.append((i, i2))

    if nCount == 2 and pos[0][1] != pos[1][1] and pos[0][0] != pos[1][0]:
        r1 = pos[0][0]
        r2 = pos[1][0]
        c1 = pos[0][1]
        c2 = pos[1][1]
        if r1 == 0 and r2 == 1:
            missing = findMissing(grid[r1][c1], grid[r2][c2], "X")
            grid[2][c2] = missing
        elif r1 == 0 and r2 == 2:
            missing = findMissing(grid[r1][c1], "X", grid[r2][c2])
            grid[1][c2] = missing
        else:
            missing = findMissing("X", grid[r1][c1], grid[r1][c1])
            grid[0][c2] = missing
    # Fill all rows or cols that already have 2 values

    grid = fillMost(grid)

    # If we only have one num
    numCount = 0
    num = 0
    for row in grid:
        for val in row:
            if val != "X":
                numCount += 1
                num = val
    if numCount == 1:
        for x in range(3):
            grid[x] = [num, num, num]
        return grid
    # If we have only one row or col
    # ROW
    rowxCount = 0
    loneRow = 0
    for i, row in enumerate(grid):
        if "X" not in row:
            loneRow = i
        elif row == ["X", "X", "X"]:
            rowxCount += 1
    if rowxCount == 2:
        if loneRow == 0:
            grid[1] = grid[0]
            grid[2] = grid[0]
        elif loneRow == 1:
            grid[0] = grid[1]
            grid[2] = grid[1]
        else:
            grid[0] = grid[2]
            grid[1] = grid[2]
        return grid
    # COL
    cols = []
    for i in range(3):
        col = []
        for i2 in range(3):
            col.append(grid[i2][i])
        cols.append(col)
    colxCount = 0
    loneCol = 0

    for i, col in enumerate(cols):
        if "X" not in col:
            loneCol = i
        elif col == ["X", "X", "X"]:
            colxCount += 1
    if colxCount == 2:
        if loneCol == 0:
            for x in range(3):
                grid[x][1] = cols[0][x]
                grid[x][2] = cols[0][x]
        elif loneCol == 1:
            for x in range(3):
                grid[x][0] = cols[1][x]
                grid[x][2] = cols[1][x]
        else:
            for x in range(3):
                grid[x][0] = cols[2][x]
                grid[x][1] = cols[2][x]
        return grid

    # Last case is if we have a filled cross of any kind with no other values in grid
    grid = fillMost(grid)
    for col in grid:
        if "X" in col:
            grid = cross(grid)
            break
    return grid


def isRight(grid):
    for col in grid:
        d = col[1] - col[0]
        if col[0] + d == col[1] == col[2] - d:
            continue
        else:
            return False
    cols = []
    for col in grid:
        add = []
        for val in col:
            add.append(val)
        cols.append(add)
    for col in cols:
        d = col[1] - col[0]
        if col[0] + d == col[1] == col[2] - d:
            continue
        else:
            return False
    return True


if __name__ == "__main__":
    # while True:
    choices = [-6 - 4, -2, 0, 2, 4, 6, "X", "X", "X", "X", "X", "X"]
    grid = []

    for row in range(3):
        add = []
        inp = input().split()
        for col in inp:
            if col != "X":
                add.append(int(col))
            else:
                add.append(col)
        grid.append(add)

    xcount = 0
    for col in grid:
        for val in col:
            if val == "X":
                xcount += 1
    if xcount == 9:
        grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    else:
        grid = solve(grid)
    for col in grid:
        for val in col:
            print(val, end=" ")
        print()
