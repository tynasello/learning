class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        nr = len(matrix)
        nc = len(matrix[0])
        self.sums = [[0] * nc for _ in range(nr)]

        for i in range(nr):
            for j in range(nc):
                self.sums[i][j] += self.matrix[i][j]
                if i > 0:
                    self.sums[i][j] += self.sums[i - 1][j]
                if j > 0:
                    self.sums[i][j] += self.sums[i][j - 1]
                if i > 0 and j > 0:
                    self.sums[i][j] -= self.sums[i - 1][j - 1]

        print(self.sums)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = self.sums[row2][col2]

        if col1 > 0:
            sum -= self.sums[row2][col1 - 1]
        if row1 > 0:
            sum -= self.sums[row1 - 1][col2]
        if row1 > 0 and col1 > 0:
            sum += self.sums[row1 - 1][col1 - 1]

        return sum
