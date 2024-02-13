from functools import lru_cache


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @lru_cache(maxsize=None)
        def solve(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            ans = 0
            if s[i] == t[j]:
                ans += solve(i + 1, j + 1)
                ans += solve(i + 1, j)
            else:
                ans += solve(i + 1, j)
            return ans

        return solve(0, 0)
