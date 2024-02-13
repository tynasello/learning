class DistinctSubsequences115 {
    public static void main(String[] args) {
        System.out.println(numDistinct("Rabbbit", "Rabbit"));
    }

    public static int numDistinct(String s, String t) {

        int[][] dp = new int[s.length()][t.length()];
        for (int i = 0; i < s.length(); i++) {
            for (int j = 0; j < t.length(); j++) {
                dp[i][j] = -1;
            }
        }
        return solve(0, 0, dp, s, t);

    }

    public static int solve(int i, int j, int[][] dp, String s, String t) {
        if (j == t.length()) {
            return 1;
        }
        if (i == s.length()) {
            return 0;
        }
        if (dp[i][j] != -1) {
            return dp[i][j];
        }

        if (s.charAt(i) == t.charAt(j)) {
            dp[i][j] = solve(i + 1, j + 1, dp, s, t) + solve(i + 1, j, dp, s, t);
        } else {
            dp[i][j] = solve(i + 1, j, dp, s, t);
        }

        return dp[i][j];

    }
}
