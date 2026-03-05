from collections import defaultdict

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        p = 0
        count = 0
        freq = Counter()
        freq[0] = 1
 
        for num in nums:
            p += num        
            if p - goal in freq:
                count += freq[p - goal]         
            freq[p] += 1
        
        return count