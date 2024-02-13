# 6/15 marks

import sys

if __name__ == "__main__":
    n = int(input())
    t = int(input())

    coordinates = []
    minLeft = sys.maxsize
    maxRight = -1
    minTop = sys.maxsize
    maxBottom = -1
    for _ in range(n):
        a, b, c, d, e = map(int, input().split())
        coordinates.append([a, b, c, d, e])
        minLeft = min(minLeft, a)
        maxRight = max(maxRight, c)
        minTop = min(minTop, b)
        maxBottom = max(maxBottom, d)
    vals = [[0 for _ in range(minLeft, maxRight)] for _ in range(minTop, maxBottom)]
    for coor in coordinates:
        a, b, c, d = coor[0], coor[1], coor[2], coor[3]
        tintFact = coor[4]
        for col in range(a - minLeft, c - minLeft):
            for row in range(b - minTop, d - minTop):
                vals[col][row] += tintFact
    ans = 0
    for row in vals:
        for val in row:
            if val >= t:
                ans += 1
    print(ans)
