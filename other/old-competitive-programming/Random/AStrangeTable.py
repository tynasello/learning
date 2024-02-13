"""
A. Strange Table from CodeForces
"""


def solve(n, m, x):
    col = (x - 1) // n
    if x % n - 1 < 0:
        row = n - 1
    else:
        row = x % n - 1

    num = col + 1 + row * m
    return num


if __name__ == "__main__":
    c = int(input())
    cases = []
    for _ in range(c):
        n, m, x = map(int, input().split())
        cases.append([n, m, x])
    for case in cases:
        print(solve(case[0], case[1], case[2]))
"""
5
1 1 1
2 2 3
3 5 11
100 100 7312
1000000 1000000 1000000000000

"""