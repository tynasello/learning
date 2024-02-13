"""
find the contiguous subarray which yeilds the greatest sum
"""


def maxContiguousSubarray(i):
    if i == 0:
        res = arr[0]
    elif dp[i] != "#":
        return dp[i]
    else:
        take = arr[i]
        dontTake = maxContiguousSubarray(i - 1) + arr[i]
        res = max(take, dontTake)
    dp[i] = res
    return res


arr = [2, 2, -3, 5, 1, -3]
dp = ["#" for _ in range(len(arr))]
maxContiguousSubarray(len(arr) - 1)
print(max(dp))
