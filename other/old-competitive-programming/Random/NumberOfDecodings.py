"""
Given a string s that represents a special encoding, return the total ways that s can be decoded.
1 -> "a", 2 -> "b" ... 26 -> "z"

Input: "123"
Output: 3
["1", "2", "3"] =>["a", "b", "c"]
["12", "3"] => ["l", "c"]
["1", "23"] => ["a", "w"]
"""

map_ = {
    1: "a",
    2: "b",
    3: "c",
    4: "d",
    5: "e",
    6: "f",
    7: "g",
    8: "h",
    9: "i",
    10: "j",
    11: "k",
    12: "l",
    13: "m",
    14: "n",
    15: "o",
    16: "p",
    17: "q",
    18: "r",
    19: "s",
    20: "t",
    21: "u",
    22: "v",
    23: "w",
    24: "x",
    25: "y",
    26: "y",
}


def solve(code, i):
    if i > len(code) - 1:
        return 1
    if dp[i] != -1:
        return dp[i]
    res = 0
    for i2 in range(1, 3):
        if i + i2 <= len(code):
            if int(code[i : i + i2]) in range(1, 27):
                res += solve(code, i + i2)
    dp[i] = res
    return dp[i]


if __name__ == "__main__":
    code = "1122"
    dp = [-1] * len(code)
    print(solve(code, 0))