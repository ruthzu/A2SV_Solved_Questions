class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        def rangeSum(a, b):
            return prefix[b + 1] - prefix[a]

        dp = [[0] * n for _ in range(n)]

        leftPtr = [i - 1 for i in range(n)]
        leftBest = [float('-inf')] * n

        rightPtr = [j for j in range(n)]
        rightBest = [float('-inf')] * n

        for length in range(2, n + 1):
            for i in range(0, n - length + 1):
                j = i + length - 1

                while leftPtr[i] + 1 <= j - 1 and rangeSum(i, leftPtr[i] + 1) <= rangeSum(leftPtr[i] + 2, j):
                    leftPtr[i] += 1
                    k = leftPtr[i]
                    val = rangeSum(i, k) + dp[i][k]
                    if val > leftBest[i]:
                        leftBest[i] = val

                while rightPtr[j] - 1 >= i and rangeSum(rightPtr[j], j) <= rangeSum(i, rightPtr[j] - 1):
                    rightPtr[j] -= 1
                    k = rightPtr[j]
                    val = rangeSum(k + 1, j) + dp[k + 1][j]
                    if val > rightBest[j]:
                        rightBest[j] = val

                best = 0
                if leftBest[i] > float('-inf'):
                    best = max(best, leftBest[i])
                if rightBest[j] > float('-inf'):
                    best = max(best, rightBest[j])
                dp[i][j] = best

        return dp[0][n - 1]