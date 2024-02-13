"""
given a 2-D array, find the sub-rectangle which yeilds the greatest sum
"""


def maxContiguousSubarray(rowSums, i, dp):
    if i == 0:
        res = rowSums[0]
    elif dp[i] != "#":
        return dp[i]
    else:
        take = rowSums[i]
        dontTake = maxContiguousSubarray(rowSums, i - 1, dp) + rowSums[i]
        res = max(take, dontTake)
    dp[i] = res
    return res


def maxHelper(rowSums):
    dp = ["#" for _ in range(len(rowSums))]
    maxContiguousSubarray(rowSums, len(rowSums) - 1, dp)
    return max(dp)


def solve():
    maxSum = 0
    rowSums = [0 for i in range(len(arr))]
    for l in range(len(arr[0])):
        for r in range(len(arr[0]) - l):
            for row in range(len(rowSums)):
                if l == l + r:
                    rowSums[row] = arr[row][l]
                else:
                    rowSums[row] += arr[row][l + r]
            maxSum = max(maxSum, maxHelper(rowSums))
    return maxSum


if __name__ == "__main__":
    arr = [
        [1, 2, -1, -4, -20],
        [-8, -3, 4, 2, 1],
        [3, 8, 10, 1, 3],
        [-4, -1, 1, 7, -6],
    ]
    print(solve())
