#include <iostream>
#include <vector>
using namespace std;

int solve(int i, int j, vector<vector<int> > &dp, string s, string t)
{
    if (j == t.length())
    {
        return 1;
    }
    if (i == s.length())
    {
        return 0;
    }
    if (dp[i][j] != -1)
    {
        return dp[i][j];
    }
    if (s[i] == t[j])
    {
        dp[i][j] = solve(i + 1, j + 1, dp, s, t) + solve(i + 1, j, dp, s, t);
    }
    else
    {
        dp[i][j] = solve(i + 1, j, dp, s, t);
    }

    return dp[i][j];
}
int numDistinct(string s, string t)
{
    vector<vector<int> > dp(s.length(), vector<int>(t.length(), -1));
    int res = solve(0, 0, dp, s, t);
    return res;
}
int main()
{
    cout << numDistinct("rabbbit", "rabbit");
    return 0;
}