class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        co = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                co +=1 
            else:
                ans= max(ans,co)
                co = 0
        ans= max(ans,co)
        return ans


