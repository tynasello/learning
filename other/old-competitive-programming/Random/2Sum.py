"""
given an array of n numbers and a target sum x, 
find two array values such that their sum is x, 
or report that no such values exist.
*using two pointers method
"""


def solve(arr, target):
    l = 0
    r = len(arr) - 1
    arr.sort()
    while True:
        if l == r:
            return "No Solution"
        if arr[r] + arr[l] == target:
            return (arr[l], arr[r])
        elif arr[r] + arr[l] > target:
            r -= 1
        else:
            l += 1
    return "No Solution"


arr = [5, 1, -11, -1, 4, 5, 6, -3, 7, 9, 9, 10]
target = 9
print(solve(arr, target))
