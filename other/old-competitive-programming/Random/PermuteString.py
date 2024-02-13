"""
print all permutations of a string
backtracking algorithm
"""


def solve(string, choices, n, currs):
    if len(currs) == n:
        permutations.append(currs)
        return
    else:
        for i, c in enumerate(choices):
            solve(string, choices[:i] + choices[i + 1 :], n, currs + c)
            choices = choices[:i] + c + choices[i + 1 :]
    return


string = "abc"
n = len(string)
permutations = []
solve(string, string, n, "")
print(permutations)
