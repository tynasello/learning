"""
given two strings, return the length of the longest subsequence common to both
note: subsequence is not the same as substring
"""


def solve(s1, s2):
    if len(s1) == 0 or len(s2) == 0:
        res = 0
    elif s1[-1] == s2[-1]:
        res = 1 + solve(s1[:-1], s2[:-1])
    elif dp[len(s1)][len(s2)] != -1:
        res = dp[len(s1)][len(s2)]
    else:
        removeLeft = solve(s1[:-1], s2)
        removeRight = solve(s1, s2[:-1])
        res = max(removeLeft, removeRight)
    dp[len(s1)][len(s2)] = res
    return res


s1 = "abcd"
s2 = "abd"
dp = [[-1 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
print(solve(s1, s2))
