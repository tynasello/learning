"""
In this challenge, you will be given an array B and must determine an array A. 
There is a special rule: For all i, A[i] <= B[i]. That is, A[i] can be any number you choose such that 1 <= A[i] <= B[i]. 
Your task is to select a series of A[i] given B[i] such that the sum of the absolute difference of consecutive pairs of A is maximized. 
Sample Input
1 - the number of test cases.
5 - the length of B
10 1 10 1 10 - B
Sample Output
36
Explanation
The maximum sum occurs when A[1]=A[3]=A[5]=10 and A[2]=A[4]=1. Sum = 36
"""


def solve(b, n):
    dp = [[0 for _ in range(100001)] for _ in range(2)]
    for i in range(n - 1):
        dp[0][i + 1] = max(dp[0][i], dp[1][i] + abs(b[i] - 1))
        dp[1][i + 1] = max(
            dp[0][i] + abs(1 - b[i + 1]), dp[1][i] + abs(b[i] - b[i + 1])
        )
    print(dp[0][0:5])
    print(dp[1][0:5])
    return max(dp[0][n - 1], dp[1][n - 1])


if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        b = list(map(int, input().split()))
        print(solve(b, n))
