"""
using sparse table
goal is to solve range minimum queries in O(1) time
"""
from math import log2
from math import floor


arr = [4, 2, 3, 7, 4, 5, 3, 3, 9, 6, 7, -1, 4]
p = floor(log2(len(arr)))
lookup = [["#" for _ in range(len(arr))] for _ in range(p + 1)]
for i, n in enumerate(arr):
    lookup[0][i] = n


def fillLookup():
    for row in range(1, p + 1):
        for col in range(len(arr)):
            if col + 2 ** (row - 1) > len(arr) - 1:
                break
            elif lookup[row - 1][col + 2 ** (row - 1)] == "#":
                break
            lookup[row][col] = min(
                lookup[row - 1][col], lookup[row - 1][col + 2 ** (row - 1)]
            )


def minimum(l, r):
    length = r - l + 1
    p = floor(log2(length))
    k = 2 ** p
    res = min(lookup[p][l], lookup[p][r - k + 1])
    return res


fillLookup()


subArrays = [[4, 9], [1, 3], [0, len(arr) - 1]]
print("Array:", arr)
for s in subArrays:
    print("minimum value in", s, "=", minimum(s[0], s[1]))
