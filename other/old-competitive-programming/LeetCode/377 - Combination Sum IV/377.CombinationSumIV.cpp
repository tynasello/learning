#include <vector>
#include <iostream>
using namespace std;

int combinationSum4(vector<int> &nums, int target)
{
    vector<unsigned int> dp(target + 1, 0);
    dp[0] = 1;

    for (int sumTo = 1; sumTo < target + 1; sumTo++)
    {
        for (int i = 0; i < sizeof(nums) ; i++)
        {
            int n = nums[i];
            if (sumTo - n >= 0)
            {
                dp[sumTo] = dp[sumTo] + dp[sumTo - n];
            }
        }
    }
    return dp[target];
}
int main()
{
    std::vector<int> vect;
    for (int i = 1; 1 < 4; i++)
    {
        vect.push_back(i);
    }
    cout << combinationSum4(vect, 4);
    return 0;
}
