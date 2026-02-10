from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]):

        n=len(nums)
        limit = n//2
        count = Counter(nums)
 
        for key, value in Counter(nums).items():
               if value > limit: return key  
       

       