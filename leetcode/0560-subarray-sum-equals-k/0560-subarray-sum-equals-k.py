from collections import Counter

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = Counter()
        count[0] = 1  
        
        p = 0
        ans = 0
        
        for i in nums:
            p += i
            
            if (p - k) in count:
                ans += count[p - k]   
            
            count[p] += 1   
        
        return ans