"""
data structure that supports two operations: processing a range query and updating an array value.
both operations work in O(log n) time.
Segment trees can support sum queries, minimum and maximum queries and many other queries.
The two segment trees here are designed for maximum and maximum queries
"""
from math import floor
import sys


def buildMaxSegmentTree(arr):
    n = len(arr)
    newTree = ["#" for _ in range(n)]
    newTree += arr
    for i in range(n - 1, 0, -1):
        newTree[i] = max(newTree[i * 2], newTree[i * 2 + 1])
    return newTree


def buildMinSegmentTree(arr):
    n = len(arr)
    newTree = ["#" for _ in range(n)]
    newTree += arr
    for i in range(n - 1, 0, -1):
        newTree[i] = min(newTree[i * 2], newTree[i * 2 + 1])
    return newTree


def updateMinValue(i, num, tree):
    i += n
    newTree = tree
    newTree[i] = num
    while i > 1:
        i = floor(i / 2)
        res = min(newTree[i * 2], newTree[i * 2 + 1])
        if tree[i] == res:
            return newTree
        else:
            tree[i] = res
    return newTree


def updateMaxValue(i, num, tree):
    i += n
    newTree = tree
    newTree[i] = num
    while i > 1:
        i = floor(i / 2)
        res = max(newTree[i * 2], newTree[i * 2 + 1])
        if tree[i] == res:
            return newTree
        else:
            tree[i] = res
    return newTree


def maximum(l, r, tree):
    l += n
    r += n
    res = -sys.maxsize
    while l < r:
        if r % 2 != 0:
            r -= 1
            res = max(res, tree[r])
        if l % 2 != 0:
            res = max(res, tree[l])
            l += 1
        l = floor(l / 2)
        r = floor(r / 2)
    return res


def minimum(l, r, tree):
    l += n
    r += n
    res = sys.maxsize
    while l < r:
        if r % 2 != 0:
            r -= 1
            res = min(res, tree[r])
        if l % 2 != 0:
            res = min(res, tree[l])
            l += 1
        l = floor(l / 2)
        r = floor(r / 2)
    return res


if __name__ == "__main__":
    arr = [5, 1, 3, 2, 7, 6, 8, 12]
    n = len(arr)
    maxTree = buildMaxSegmentTree(arr)
    minTree = buildMinSegmentTree(arr)
    qs = [[0, 3], [0, len(arr) - 1]]
    for q in qs:
        print("Array:", arr)
        print("maximum value in", q, "=", maximum(q[0], q[1] + 1, maxTree))
        print("minimum value in", q, "=", minimum(q[0], q[1] + 1, minTree))
        print("-----------------------------")

        arr[0] = 16
        arr[5] = 0
        maxTree = updateMaxValue(0, 16, maxTree)
        maxTree = updateMaxValue(5, 0, maxTree)
        minTree = updateMinValue(0, 16, minTree)
        minTree = updateMinValue(5, 0, minTree)
