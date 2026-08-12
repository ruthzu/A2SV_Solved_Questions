from collections import defaultdict
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        max_len = 0
        s = []
        ma = defaultdict(int)
        i = 0
        for j in range(len(nums)):
            ma[nums[j]] += 1
            while ma[nums[j]] > k:
                ma[nums[i]] -= 1
                i += 1
            max_len = max(max_len,j-i+1)
        return max_len


            




            
