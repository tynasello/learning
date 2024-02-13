grid = [
    [3, 7, 9, 2, 7],
    [9, 8, 3, 5, 5],
    [1, 7, 9, 8, 5],
    [3, 8, 6, 4, 10],
    [6, 3, 9, 7, 8],
]
n = len(grid)
s = [[0 for i in range(n + 1)] for i in range(n + 1)]

for y in range(1, n + 1):
    for x in range(1, n + 1):
        s[y][x] = max(s[y][x - 1], s[y - 1][x]) + grid[y - 1][x - 1]
# for y in grid:
#     print (y)
# print()
# for y in s:
#     print (y)
print(s[n][n])
