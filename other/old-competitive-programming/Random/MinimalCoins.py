"""
minimal ammount of coins needed to sum to n
"""

import sys


def solve(x):
    if x < 0:
        return sys.maxsize
    if x == 0:
        return 0
    if ready[x]:
        return value[x]
    res = sys.maxsize
    for c in coins:
        res = min(res, solve(x - c) + 1)
    ready[x] = True
    value[x] = res
    return res


n = 40
ready = [0] * (n + 1)
value = [0] * (n + 1)
coins = [1, 5, 10, 25]
print(solve(n))
