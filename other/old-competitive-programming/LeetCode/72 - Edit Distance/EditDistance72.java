class EditDistance72 {
    public static void main(String args[]) {
        System.out.println(minDistance("horse", "hor"));
    }

    public static int minDistance(String word1, String word2) {
        int[][] dp = new int[word2.length() + 1][word1.length() + 1];
        for (int i = 0; i < word2.length() + 1; i++) {
            for (int j = 0; j < word1.length() + 1; j++) {
                dp[i][j] = -1;
            }
        }
        return solve(word2.length(), word1.length(), dp, word1, word2);

    }

    public static int solve(int row, int col, int[][] dp, String word1, String word2) {

        if (row == 0 && col == 0) {
            return 0;
        } else if (row == 0) {
            return col;
        } else if (col == 0) {
            return row;
        } else if (dp[row][col] != -1) {
            return dp[row][col];
        } else if (word1.charAt(col - 1) == word2.charAt(row - 1)) {
            dp[row][col] = solve(row - 1, col - 1, dp, word1, word2);
        } else {
            int d = solve(row, col - 1, dp, word1, word2);
            int r = solve(row - 1, col - 1, dp, word1, word2);
            int i = solve(row - 1, col, dp, word1, word2);
            dp[row][col] = 1 + Math.min(Math.min(d, r), i);
        }
        return dp[row][col];
    }
};