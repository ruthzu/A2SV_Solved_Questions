from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        left = 0
        freq = 0
        maxi = 0
        for right in range(len(s)):
            count[s[right]] += 1
            freq = max(freq, count[s[right]])
            if (right - left + 1) - freq > k:
                count[s[left]] -= 1
                left += 1
            maxi = max(maxi, right - left + 1)
        return maxi
