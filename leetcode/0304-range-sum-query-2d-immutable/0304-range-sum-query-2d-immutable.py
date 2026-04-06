class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.p = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.p[i][j] = (
                    self.p[i - 1][j] +
                    self.p[i][j - 1] -
                    self.p[i - 1][j - 1] +
                    matrix[i - 1][j - 1]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1 = row1 + 1, col1 + 1
        r2, c2 = row2 + 1, col2 + 1
        return (
            self.p[r2][c2]
            - self.p[r1 - 1][c2]
            - self.p[r2][c1 - 1]
            + self.p[r1 - 1][c1 - 1])

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)