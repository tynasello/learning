public class CombinationSumIV377 {

    public static void main(String[] args) {
        int arr[] = { 1, 2, 3 };
        System.out.println(combinationSum4(arr, 4));
    }

    public static int combinationSum4(int[] nums, int target) {
        int[] dp = new int[target + 1];
        dp[0] = 1;

        for (int sumTo = 1; sumTo < target + 1; sumTo++) {
            for (int n : nums) {
                if (sumTo - n >= 0) {
                    dp[sumTo] = dp[sumTo] + dp[sumTo - n];
                }
            }
        }
        return dp[target];
    }

}
