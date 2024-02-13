if __name__ == "__main__":
    l = int(input())
    w = int(input())
    n = int(input())
    rowBrush = set()
    colBrush = set()
    for i in range(n):
        direction, index = input().split()
        if direction == "C":
            if index not in colBrush:
                colBrush.add(index)

            else:
                colBrush.remove(index)

        else:
            if index not in rowBrush:
                rowBrush.add(index)

            else:
                rowBrush.remove(index)

    cs = len(colBrush)
    rs = len(rowBrush)
    res = cs * l + rs * w - rs * cs * 2
    print(res)


"""
4
5
7
R 3
C 1
C 2
R 2
R 2
C 1
R 4
"""