class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        from math import gcd
        n = len(coins)

        def lcm(a, b):
            return a // gcd(a, b) * b

        def count(x):
            ans = 0
            for mask in range(1, 1 << n):
                v = 1
                bits = 0
                ok = True

                for i in range(n):
                    if mask >> i & 1:
                        bits += 1
                        v = lcm(v, coins[i])
                        if v > x:
                            ok = False
                            break
                if not ok:
                    continue

                if bits % 2:
                    ans += x // v
                else:
                    ans -= x // v

            return ans
        lo = 1
        hi = min(coins) * k

        while lo < hi:
            mid = (lo + hi) // 2

            if count(mid) >= k:
                hi = mid
            else:
                lo = mid + 1

        return lo