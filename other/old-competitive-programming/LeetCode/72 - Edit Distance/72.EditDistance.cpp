#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int minDistance(string word1, string word2);
int solve(int row, int col, vector<vector<int> > &dp, string word1, string word2);

int main()
{
    cout << minDistance("horse", "hor");
    return 0;
}

int minDistance(string word1, string word2)
{
    vector<vector<int> > dp(word2.length() + 1, vector<int>(word1.length() + 1, -1));
    return solve(word2.length(), word1.length(), dp, word1, word2);
}
int solve(int row, int col, vector<vector<int> > &dp, string word1, string word2)
{
    if (row == 0 && col == 0)
    {
        return 0;
    }
    else if (row == 0)
    {
        return col;
    }
    else if (col == 0)
    {
        return row;
    }
    else if (dp[row][col] != -1)
    {
        return dp[row][col];
    }
    else if (word1[col - 1] == word2[row - 1])
    {
        dp[row][col] = solve(row - 1, col - 1, dp, word1, word2);
    }
    else
    {
        int d = solve(row, col - 1, dp, word1, word2);
        int r = solve(row - 1, col - 1, dp, word1, word2);
        int i = solve(row - 1, col, dp, word1, word2);
        dp[row][col] = 1 + min(min(d, r), i);
    }
    return dp[row][col];
}
