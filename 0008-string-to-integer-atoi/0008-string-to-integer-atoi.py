class Solution:
    def myAtoi(self, s: str) -> int:
        signflag = True
        ans = []
        num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        started = False

        for i in s:
            if not started and i == " ":
                continue

            elif not started and i == "-":
                signflag = False
                started = True

            elif not started and i == "+":
                started = True

            elif i in num:
                ans.append(i)
                started = True

            else:
                break

        if len(ans) == 0:
            return 0

        result = 0
        for i in ans:
            result = result * 10 + (ord(i) - ord('0'))

        if not signflag:
            result = -result

        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX

        return result