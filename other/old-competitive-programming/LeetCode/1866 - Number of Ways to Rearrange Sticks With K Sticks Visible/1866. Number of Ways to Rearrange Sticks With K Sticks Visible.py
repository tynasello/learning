class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        vector<unsigned int> dp(target+1, 0);
        dp[0]=1;
        
        for (int sumTo=1;sumTo<target+1;sumTo++){
            for (int n:nums){
                if (sumTo-n>=0){
                    dp[sumTo] = dp[sumTo]+dp[sumTo-n];
                }
            }
        }
        return dp[target];
    }
};
