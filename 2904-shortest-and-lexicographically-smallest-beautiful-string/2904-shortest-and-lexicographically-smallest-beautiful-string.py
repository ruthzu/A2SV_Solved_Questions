class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ones = [i for i, ch in enumerate(s) if ch == '1']

        best = ""

        for i in range(len(ones) - k + 1):
            left = ones[i]
            right = ones[i + k - 1]

            candidate = s[left:right + 1]

            if not best or len(candidate) < len(best):
                best = candidate
            elif len(candidate) == len(best) and candidate < best:
                best = candidate

        return best