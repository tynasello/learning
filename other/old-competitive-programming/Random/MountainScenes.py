"""
An artist begins with a roll of ribbon, one inch wide. 
She clips it into pieces of various integral lengths, then aligns them with the bottom of a frame, rising vertically in columns, to form a mountain scene. 
A mountain scene must be uneven; if all columns are the same height, it’s a plain scene, not a mountain scene! 
It is possible that she may not use all of the ribbon.
Given the length of the ribbon and the width and height of the frame, all in inches, how many different mountain scenes can she create? 
Two scenes are different if the regions covered by ribbon are different. There’s no point in putting more than one piece of ribbon in any column.
The input will consist of a single line with three space-separated integers:
𝑛, 𝑤 and ℎ, where 𝑛 (0≤𝑛≤10000) is the length of the ribbon in inches, 𝑤 (1≤𝑤≤100) is the width and ℎ (1≤ℎ≤100) is the height of the frame, both in inches.
Output a single integer, indicating the total number of mountain scenes our artist could possibly make, modulo 109+7.
Sample Input 1	Sample Output 1
25 5 5          7770
Sample Input 2	Sample Output 2
15 5 5          6050
"""


def solve(currn, currw):
    if currn < 0:
        return 0
    if currw > w:
        return 1
    if dp[currw][currn] != None:
        return dp[currw][currn]
    res = 0
    for l in range(h + 1):
        res += solve(currn - l, currw + 1)
    dp[currw][currn] = res % modNum
    return dp[currw][currn]


modNum = 10 ** 9 + 7
n, w, h = map(int, input().split())
squares = min(h * w, n)
plains = int(squares / w + 1)
dp = [[None for _ in range(n + 1)] for _ in range(w + 1)]
res = ((solve(n, 1) - plains) + modNum) % modNum
print(res)
