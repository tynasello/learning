class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        dp = {}

        def dfs(si, pi):
            if (si, pi) in dp:
                return dp[(si, pi)]

            if pi >= len(p):
                if si >= len(s):
                    return True
                return False

            sipiCharsMatch = si < len(s) and (s[si] == p[pi] or p[pi] == ".")

            if pi + 1 < len(p) and p[pi + 1] == "*":
                dp[(si, pi)] = (sipiCharsMatch and dfs(
                    si + 1, pi)) or dfs(si, pi + 2)
                return dp[(si, pi)]

            if sipiCharsMatch:
                dp[(si, pi)] = dfs(si + 1, pi + 1)
                return dp[(si, pi)]

            dp[(si, pi)] = False
            return False

        return dfs(0, 0)
