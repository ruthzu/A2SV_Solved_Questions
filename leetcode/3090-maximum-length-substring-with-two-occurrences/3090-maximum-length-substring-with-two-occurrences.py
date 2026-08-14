class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        i = 0
        s = list(s)
        d = defaultdict(int)
        max_len = 0
        for j in range(len(s)):
            d[s[j]] += 1
            while d[s[j]] > 2:
                    d[s[i]] -= 1
                    i += 1
            max_len = max(max_len,j-i+1)
        return max_len
            