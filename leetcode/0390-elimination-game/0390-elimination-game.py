class Solution:
    def lastRemaining(self, n: int) -> int:
        def remain(n: int, lr: bool) -> int:
            if n == 1:
                return 1    
            if lr or n % 2 == 1:
                return 2 * remain(n // 2, not lr)
            else:
                return 2 * remain(n // 2, not lr) - 1
        return remain(n, True)


