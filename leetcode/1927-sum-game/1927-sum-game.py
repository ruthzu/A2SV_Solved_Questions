class Solution:
    def sumGame(self, num: str) -> bool:
        ha1 = 0
        ha2 = 0
        ha1c = 0
        ha2c = 0

        for i in range(len(num)):
            if i < len(num) // 2:
                if num[i] == '?':
                    ha1c += 1
                else:
                    ha1 += int(num[i])
            else:
                if num[i] == '?':
                    ha2c += 1
                else:
                    ha2 += int(num[i])

        x = ha1 - ha2
        q = ha1c - ha2c

        return 2 * x != -9 * q