"""
goal is to calculate sum queries of arrays in either one or two dimensions in O(1) time
"""


def build1DLookup(arr):

    lookup = [0]
    for n in arr:
        lookup.append(lookup[-1] + n)

    print("1-D Array =", arr)
    return lookup


def build2DLookup(arr):
    lookup = [["#" for _ in range(len(twoDArr[0]))] for _ in range(len(twoDArr))]
    lookup[0][0] = arr[0][0]

    for i in range(1, len(arr[0])):
        lookup[0][i] = lookup[0][i - 1] + arr[0][i]
    for row in range(1, len(arr)):
        for col in range(0, len(arr[0])):
            if col == 0:
                lookup[row][0] = arr[row][0] + lookup[row - 1][0]
            else:
                toLeft = 0
                for leftCol in range(col):
                    toLeft += arr[row][leftCol]
                lookup[row][col] = arr[row][col] + toLeft + lookup[row - 1][col]
    return lookup


def twoDSum(lookup, tl, br):
    tr = [tl[0], br[1]]
    bl = [br[0], tl[1]]
    if tl[0] == 0 and tl[1] == 0:
        res = lookup[br[0]][br[1]]
    elif tl[0] == 0:
        res = lookup[br[0]][br[1]] - lookup[bl[0]][bl[1] - 1]
    elif tl[1] == 0:
        res = lookup[br[0]][br[1]] - lookup[tr[0] - 1][tr[1]]
    else:
        res = (
            lookup[br[0]][br[1]]
            - lookup[bl[0]][bl[1] - 1]
            - lookup[tr[0] - 1][tr[1]]
            + lookup[tl[0] - 1][tl[1] - 1]
        )
    return res


if __name__ == "__main__":
    oneDArr = [1, 3, 4, 8, 6, 1, 4, 2]
    oneDLookup = build1DLookup(oneDArr)
    oneDQ = [[2, 5], [1, 3], [0, len(oneDArr) - 1]]
    for q in oneDQ:
        print("Sum from", q, "=", oneDLookup[q[1] + 1] - oneDLookup[q[0]])

    twoDArr = [[1, 3, 7, 2], [3, 7, 4, 6], [9, 10, 4, 6], [12, 5, 2, 11]]
    twoDLookup = build2DLookup(twoDArr)
    twoDQ = [[1, 1], [3, 2]]
    print("----------------------------")
    print("2-D Array:")
    for r in twoDArr:
        print(r)
    print(
        "Sum from",
        twoDQ[0],
        "to",
        twoDQ[1],
        "=",
        twoDSum(twoDLookup, twoDQ[0], twoDQ[1]),
    )
