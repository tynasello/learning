class MaximalSquare221 {
    public static void main(String[] args) {
        char shape[][] = { { '1', '0', '1', '0', '0' }, { '1', '0', '1', '1', '1' }, { '1', '1', '1', '1', '1' },
                { '1', '0', '0', '1', '0' } };

        System.out.println(maximalSquare(shape));
    }

    public static int maximalSquare(char[][] matrix) {
        int numR = matrix.length;
        int numC = matrix[0].length;
        int maxSquareLen = 0;
        int[][] dp = new int[numR][numC];
        for (int i = 0; i < numR; i++) {
            for (int j = 0; j < numC; j++) {
                dp[i][j] = -1;
            }
        }

        solve(0, 0, dp, matrix, numR, numC);
        for (int i = 0; i < numR; i++) {
            for (int j = 0; j < numC; j++) {
                if (dp[i][j] > maxSquareLen) {
                    maxSquareLen = dp[i][j];
                }
            }
        }
        return maxSquareLen * maxSquareLen;
    }

    public static int solve(int row, int col, int[][] dp, char[][] matrix, int numR, int numC) {

        if (row >= numR || col >= numC) {
            return 0;
        }
        if (dp[row][col] != -1) {
            return dp[row][col];
        } else {
            int toRight = solve(row, col + 1, dp, matrix, numR, numC);
            int down = solve(row + 1, col, dp, matrix, numR, numC);
            int downRightDiagonal = solve(row + 1, col + 1, dp, matrix, numR, numC);
            if (matrix[row][col] == '1') {
                dp[row][col] = 1 + Math.min(Math.min(toRight, down), downRightDiagonal);
            } else {
                dp[row][col] = 0;
            }
        }
        return dp[row][col];

    }
}
