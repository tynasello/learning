#include <vector>
#include <iostream>
using namespace std;
class Solution
{
public:
    int maximalSquare(vector<vector<char> > &matrix)
    {
        int numR = matrix.size();
        int numC = matrix[0].size();
        int maxSquareLen = 0;
        vector<vector<int> > dp(numR, vector<int>(numC, -1));

        solve(0, 0, dp, matrix, numR, numC);
        for (int i = 0; i < numR; i++)
        {
            for (int j = 0; j < numC; j++)
            {
                if (dp[i][j] > maxSquareLen)
                {
                    maxSquareLen = dp[i][j];
                }
            }
        }
        return maxSquareLen * maxSquareLen;
    }

    int solve(int row, int col, vector<vector<int> > &dp, vector<vector<char> > &matrix, int numR, int numC)
    {

        if (row >= numR || col >= numC)
        {
            return 0;
        }
        if (dp[row][col] != -1)
        {
            return dp[row][col];
        }
        else
        {
            int toRight = solve(row, col + 1, dp, matrix, numR, numC);
            int down = solve(row + 1, col, dp, matrix, numR, numC);
            int downRightDiagonal = solve(row + 1, col + 1, dp, matrix, numR, numC);
            if (matrix[row][col] == '1')
            {
                dp[row][col] = 1 + min(min(toRight, down), downRightDiagonal);
            }
            else
            {
                dp[row][col] = 0;
            }
        }
        return dp[row][col];
    }
};
int main()
{
    Solution test1;
    char square[4][5] = {{'1', '0', '1', '0', '0'}, {'1', '0', '1', '1', '1'}, {'1', '1', '1', '1', '1'}, {'1', '0', '0', '1', '0'}};
    vector<vector<char> > v;
    for (int r = 0; r < 4; r++)
    {
        vector<char> row;
        for (int c = 0; c < 5; c++)
        {
            row.push_back(square[r][c]);
        }
        v.push_back(row);
    }

    cout << test1.maximalSquare(v);
    return 0;
}