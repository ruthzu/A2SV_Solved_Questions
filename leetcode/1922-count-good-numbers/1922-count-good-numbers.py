class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        if n % 2 == 0:
            even = (n) // 2
            odd = (n) // 2
        else:
            even = (n+1) // 2
            odd = (n) // 2

        def pow(x, y):
            if y == 0:
                return 1
            
            if y % 2 == 0:
                half = pow(x, y//2)
                return (half * half) % MOD
            else:
                return (x * pow(x, y - 1)) % MOD

        return (pow(5, even) * pow(4, odd)) % MOD