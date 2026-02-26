from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        n = len(s)
        ans = 0
        left = 0
        count = Counter()
        most_common = 0
        
        for right in range(n):

            count[s[right]] += 1
            most_common = max(most_common, count[s[right]])

            while right - left +1 - most_common > k:
                count[s[left]] -= 1
                left += 1

            ans = max(ans, right - left +1 )
           
        return ans