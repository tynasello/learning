"""
Given an array of integers and a target sum, determine the sum nearest to but not exceeding the target that can be created. 
To create the sum, use any element of your array zero or more times.

The first line contains an integer , the number of test cases.
Each of the next  pairs of lines are as follows: 
- The first line contains two integers  and , the length of  and the target sum. 
- The second line contains  space separated integers .

Sample Input
2
3 12
1 6 9
5 9
3 4 4 4 8
Sample Output
12
9
"""


def solve(arr, curr_sum, closest, target):
    if curr_sum > target:
        return closest
    if target - curr_sum < target - closest:
        closest = curr_sum
    for n in arr:
        closest = solve(arr, curr_sum + n, closest, target)
    return closest


res = []
samples = int(input())
for _ in range(samples):
    n, target = map(int, input().split())
    arr = list(map(int, input().split()))
    if 1 in arr:
        res.append(target)
        continue
    res.append(solve(arr, 0, 0, target))

for r in res:
    print(r)
