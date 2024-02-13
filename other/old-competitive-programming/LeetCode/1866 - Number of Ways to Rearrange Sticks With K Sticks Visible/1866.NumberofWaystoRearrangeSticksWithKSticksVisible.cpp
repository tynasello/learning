#include <iostream>
#include <vector>
using namespace std;
const static int mod = (int)1e9 + 7;

long dfs(int n, int k, vector<vector<long> > &dp)
{
    if (k == n)
    {
        return 1;
    }
    if (k == 0 || n == 0)
    {
        return 0;
    }
    if (dp[n][k] != -1)
    {
        return dp[n][k];
    }
    dp[n][k] = (dfs(n - 1, k - 1, dp) % mod + ((n - 1) * (dfs(n - 1, k, dp)) % mod)) % mod;
    return dp[n][k];
}
long rearrangeSticks(int n, int k)
{
    vector<vector<long> > dp(n + 1, vector<long>(k + 1, -1));
    return dfs(n, k, dp);
}
int main()
{
    cout << rearrangeSticks(4, 3);
    return 0;
}