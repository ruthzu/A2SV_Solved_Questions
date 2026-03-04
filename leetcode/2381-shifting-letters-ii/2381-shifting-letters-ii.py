class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        p = [0] * (n + 1)

        for l, r, k in shifts:
            v = 1 if k == 1 else -1
            p[l] += v
            p[r + 1] -= v

        for i in range(1, n):
            p[i] += p[i - 1]

        ans = []

        for i in range(n):
            a = ord(s[i]) - ord('a')
            a = (a + p[i]) % 26
            ans.append(chr(a + ord('a')))

        return "".join(ans)