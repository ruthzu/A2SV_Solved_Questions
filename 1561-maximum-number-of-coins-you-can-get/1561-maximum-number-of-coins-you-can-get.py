class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)
        i = n - 2
        s = 0
        k = n // 3
        while k > 0:
            s += piles[i]
            i -= 2
            k -= 1
        return s
