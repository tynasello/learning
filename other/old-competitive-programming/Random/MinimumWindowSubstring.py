"""
Given two strings s and t, return the minimum window in s which will contain all the characters in t. 
If there is no such window in s that covers all characters in t, return the empty string "".

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"

Example 2:
Input: s = "a", t = "a"
Output: "a"
"""

from collections import Counter


def solve(s, t):
    if not s or not t or len(t) > len(s):
        return ""
    l = 0
    r = 0
    minL = len(s) + 1
    tCount = Counter(t)
    currChars = Counter()
    matches = 0
    res = ""

    while l <= len(s) - len(t):
        # print(l, r, s[l:r])
        if matches < len(tCount):
            if r == len(s):
                return res
            currChars[s[r]] += 1
            if tCount[s[r]] > 0 and currChars[s[r]] == tCount[s[r]]:
                matches += 1
            r += 1
        else:
            currChars[s[l]] -= 1
            if tCount[s[l]] > 0 and currChars[s[l]] == tCount[s[l]] - 1:
                matches -= 1
            l += 1
        if matches == len(tCount):
            if len(s[l:r]) < minL:
                minL = len(s[l:r])
                res = s[l:r]
    return res


if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    print(solve(s, t))