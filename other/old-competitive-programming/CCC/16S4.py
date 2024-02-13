"""
https://ccc.amorim.ca/docs/2016/s4/solution/ helped me a great deal in understanding and solving this problem
"""


def canCombine(start, end):
    if start == end:
        return True
    else:
        return dp[start][end] != -1


def combineTwo(firstStart, secondEnd):
    for firstEnd in range(firstStart, secondEnd):
        secondStart = firstEnd + 1

        if not canCombine(firstStart, firstEnd) or not canCombine(
            secondStart, secondEnd
        ):
            continue

        if firstStart == firstEnd:
            firstSum = balls[firstStart]
        else:
            firstSum = dp[firstStart][firstEnd]

        if secondStart == secondEnd:
            secondSum = balls[secondStart]
        else:
            secondSum = dp[secondStart][secondEnd]
        if secondSum == firstSum:
            dp[firstStart][secondEnd] = firstSum + secondSum
        else:
            continue
        return True
    return False


def combineThree(firstStart, secondEnd):
    for midStart in range(firstStart + 1, secondEnd):
        firstEnd = midStart - 1
        if not canCombine(firstStart, firstEnd):
            continue
        for midEnd in range(midStart, secondEnd):
            secondStart = midEnd + 1
            if not canCombine(midStart, midEnd) or not canCombine(
                secondStart, secondEnd
            ):
                continue
            if firstStart == firstEnd:
                firstSum = balls[firstStart]
            else:
                firstSum = dp[firstStart][firstEnd]

            if secondStart == secondEnd:
                secondSum = balls[secondStart]
            else:
                secondSum = dp[secondStart][secondEnd]
            if secondSum == firstSum:
                if midStart == midEnd:
                    midSum = balls[midStart]
                else:
                    midSum = dp[midStart][midEnd]
                dp[firstStart][secondEnd] = firstSum + midSum + secondSum
            else:
                continue
            return True
    return False


def solve():
    for length in range(2, n + 1):
        for firstStart in range(0, n - length + 1):
            secondEnd = firstStart + length - 1
            if combineTwo(firstStart, secondEnd):
                continue
            elif length > 2:
                combineThree(firstStart, secondEnd)


def searchForAnswer():
    res = -1
    for start in range(n):
        for end in range(start, n):
            if start == end:
                temp = balls[start]
            else:
                temp = dp[start][end]
            res = max(res, temp)
    return res


n = int(input())
balls = list(map(int, input().split()))
dp = [[-1 for _ in range(n)] for _ in range(n)]

if __name__ == "__main__":

    solve()
    print(searchForAnswer())
# 661557 109092 46588 186954 46588 280130 42555 23982 42555 665660
# 661557 109092 280130 280120 109092 655660
# 661557 109092 560260 109092 655660
