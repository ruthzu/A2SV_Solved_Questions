class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_max = nums[0]
        ans =  nums[0]
        for i in range(1,len(nums)):
            curr_max = max(nums[i],curr_max + nums[i])
            ans = max(ans,curr_max)
        return ans