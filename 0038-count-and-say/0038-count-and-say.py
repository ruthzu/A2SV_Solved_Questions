class Solution:
    def countAndSay(self, n: int) -> str:
        p = "1"

        for _ in range(n - 1):
            ans = ""
            count = 1

            for i in range(1, len(p)):
                if p[i] == p[i - 1]:
                    count += 1
                else:
                    ans += str(count) + p[i - 1]
                    count = 1

            ans += str(count) + p[-1]
            p = ans

        return p