from functools import lru_cache


class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        @lru_cache(maxsize=None)
        def dp(i, s1Prefix, s2Prefix, evilMatchesLength):

            if evilMatchesLength == len(evil):
                return 0
            if i == n:
                return 1

            if s1Prefix:
                start = ord(s1[i])
            else:
                start = ord("a")
            if s2Prefix:
                end = ord(s2[i])
            else:
                end = ord("z")

            res = 0

            for index in range(start, end + 1):
                currC = chr(index)

                tempMatches = evilMatchesLength
                while tempMatches > 0 and currC != evil[tempMatches]:
                    tempMatches = lps[tempMatches - 1]

                if currC == evil[tempMatches]:
                    tempMatches += 1

                res += dp(
                    i + 1,
                    s1Prefix and index == start,
                    s2Prefix and index == end,
                    tempMatches,
                )

            return res

        def buildLPS(string):
            l = len(string)
            lps = [0] * l
            i = 0
            for j in range(1, l):
                while i > 0 and string[i] != string[j]:
                    i = lps[i - 1]
                if string[i] == string[j]:
                    lps[j] = i + 1
                    i += 1

            return lps

        lps = buildLPS(evil)
        return dp(0, True, True, 0) % (10 ** 9 + 7)


test1 = Solution
print(
    test1.findGoodStrings(
        None,
        81,
        "ithrfztwiwvtkyzgufoxtofywlyhwwjdmpfbtyvpqtkitfhhoyhjrmoipdcaaksgfuzaersicuarqbyng",
        "uxmmpikhthamnhicxsseiqeeojmdgvchkdbzagbwxovdwdmpmfhosgwksgbzpmjmyeamvbmeojbbeidca",
        "uexivgvomkuiiuuhhbszsflntwruqblr",
    )
)
