"""
Given a string digits representing a phone number, return all possible character arrangements that can result from the number.
Input: "43"
Output: ["gd","ge","gf","hd","he","hf","id","ie","if"]
"""
map_ = {
    2: ["a", "b", "c"],
    3: ["d", "e", "f"],
    4: ["g", "h", "i"],
    5: ["j", "k", "l"],
    6: ["m", "n", "o"],
    7: ["p", "q", "r", "s"],
    8: ["t", "u", "v"],
    9: ["w", "x", "y", "z"],
}


def solve(s, i, currs):
    if i >= len(s):
        res.append(currs)
        return
    elif int(s[i]) == 7 or int(s[i]) == 9:
        for letter in range(4):
            currs += map_[int(s[i])][letter]
            solve(s, i + 1, currs)
            currs = currs[:-1]
    else:
        for letter in range(3):
            currs += map_[int(s[i])][letter]
            solve(s, i + 1, currs)
            currs = currs[:-1]
    return


if __name__ == "__main__":
    res = []
    s = "43"
    solve(s, 0, "")
    print(res)
