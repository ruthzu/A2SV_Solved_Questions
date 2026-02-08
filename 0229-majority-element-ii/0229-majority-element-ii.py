from math import floor
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans=[]
        count=Counter(nums)
        n=floor(len(nums)/3)
        for key , value in count.items():
            if value > n:
                ans.append(key)
        return ans 