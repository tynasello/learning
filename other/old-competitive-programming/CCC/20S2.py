y = int(input())
x = int(input())
grid = []

# Can you reach end of grif


def isValid(currX, currY):
    if currX >= 0 and currY >= 0 and currX < x and currY < y:
        return True
    return False


def getFactors(num):
    factors = []
    if num == 1:
        return [(1, 1)]
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append((num // i - 1, i - 1))
    return factors


def solve(currX, currY, jumps):
    if currX == x - 1 and currY == y - 1:
        return True
    if jumps >= x * y:
        return False
    if isValid(currX, currY):
        factors = getFactors(grid[currY][currX])
        prevX = currX
        prevY = currY
        for pos in factors:
            if solve(pos[0], pos[1], jumps + 1):
                return True
        currX = prevX
        currY = prevY
        jumps -= 1
        return False
    return False


if __name__ == "__main__":
    for _ in range(y):
        grid.append(list(map(int, input().split())))
    if len(grid) != y or len(grid[0]) != x:
        print("no")
        quit()
    if solve(0, 0, 0):
        print("yes")
    else:
        print("no")

"""
5
5
3 10 8 14 5  
3 10 8 14 5
3 10 8 14 3
3 10 8 14 1
3 10 8 14 1


"""