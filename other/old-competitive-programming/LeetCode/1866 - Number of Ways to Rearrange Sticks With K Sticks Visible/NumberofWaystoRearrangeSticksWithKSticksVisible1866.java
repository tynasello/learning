import java.util.Arrays;

class NumberofWaystoRearrangeSticksWithKSticksVisible1866 {
    final static int mod = (int) 1e9 + 7;

    public static void main(String args[]) {
        System.out.println(rearrangeSticks(3, 2));
    }

    public static int rearrangeSticks(int n, int k) {
        long[][] dp = new long[n + 1][k + 1];
        for (int i = 0; i < dp.length; i++) {
            Arrays.fill(dp[i], -1);
        }
        return (int) dfs(n, k, dp);
    }

    public static long dfs(int n, int k, long[][] dp) {
        if (k == n) {
            return 1;
        }
        if (k == 0 || n == 0) {
            return 0;
        }
        if (dp[n][k] != -1) {
            return dp[n][k];
        }
        dp[n][k] = (dfs(n - 1, k - 1, dp) % mod + ((n - 1) * (dfs(n - 1, k, dp)) % mod)) % mod;
        return dp[n][k];
    }
};
