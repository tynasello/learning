"""
You are given k eggs, and you have access to a building with n floors labeled from 1 to n.
Each egg is identical in function, and if an egg breaks, you cannot drop it again.
You know that there exists a floor f with 0 <= f <= n such that any egg dropped at a floor higher than f will break, 
and any egg dropped at or below floor f will not break.
Each move, you may take an egg (if you have an unbroken one) and drop it from any floor x (with 1 <= x <= n).
Your goal is to know with certainty what the value of f is.
Return the minimum number of moves that you need to know with certainty the value of f.

Input: k = 1, n = 2
Output: 2
Explanation: 
Drop the egg from floor 1. If it breaks, we know with certainty that f = 0.
Otherwise, drop the egg from floor 2. If it breaks, we know with certainty that f = 1.
If it did not break, then we know with certainty f = 2.
Hence, we needed 2 moves in the worst case to know what f is with certainty.
Example 2:
Input: k = 2, n = 6
Output: 3
Example 3:
Input: k = 3, n = 14
Output: 4
"""
import sys


def solve(egg, floor):
    # base cases
    if floor == 1 or floor == 0:
        dp[egg][floor] = floor
        return floor
    if egg == 1:
        dp[egg][floor] = floor
        return floor

    # check if we've already done this subproblem
    if dp[egg][floor] != -1:
        return dp[egg][floor]

    minRes = sys.maxsize

    for simfloor in range(1, floor + 1):
        breaks = solve(egg - 1, simfloor - 1)
        nobreak = solve(egg, floor - simfloor)
        res = max(breaks, nobreak)
        minRes = min(minRes, res)
        dp[egg][floor] = minRes + 1

    return dp[egg][floor]


totalFloors = 14
eggs = 3
dp = [[-1 for _ in range(totalFloors + 1)] for _ in range(eggs + 1)]

print(solve(eggs, totalFloors))
# print(dp)