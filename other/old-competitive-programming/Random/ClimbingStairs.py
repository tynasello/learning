"""
You are climbing a staircase. It takes n steps to reach to the top. 
Each time you can either climb 1 or 2 steps. 
In how many distinct ways can you climb to the top? (n is always a positive integer).
Example
Input: 4
Ouptut: 5
Explanation: you can take the steps [1,1,1,1],[2,1,1],[1,2,1],[1,1,2], or [2,2]
"""


def solve(steps):
    if steps < 0:
        return 0
    if steps == 0:
        return 1
    elif dp[steps] != -1:
        return dp[steps]
    else:
        take1 = solve(steps - 1)
        take2 = solve(steps - 2)
        res = take1 + take2
    dp[steps] = res
    return res


totalSteps = 3
dp = [-1 for _ in range(totalSteps + 1)]
print(solve(totalSteps))