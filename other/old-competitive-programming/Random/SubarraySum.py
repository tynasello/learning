"""
given an array, find if there is a subarray which sums to a target.
*Using two pointers method
"""


def solve(arr, target):
    currSum = 0
    left = 0
    right = -1
    while True:
        if currSum == target:
            return arr[left : right + 1]
        elif right + 1 == len(arr):
            break
        elif currSum + arr[right + 1] <= target:
            right += 1
            currSum += arr[right]
        else:
            currSum -= arr[left]
            left += 1
    return "No solution"


if __name__ == "__main__":
    arr = [1, 3, 2, 5, 1, 1, 2, 3]
    target = 10
    print(solve(arr, target))
