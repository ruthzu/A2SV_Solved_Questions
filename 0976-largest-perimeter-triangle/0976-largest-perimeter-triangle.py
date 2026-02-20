class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        ans=0
        for i in range(len(nums)-1,-1,-1):
            fi = nums[i] < (nums[i-1] + nums[i-2])
            sec = nums[i-1] < (nums[i] + nums[i-2])
            tri = nums[i-2] < (nums[i-1] + nums[i])
            if fi and sec and tri:
                peri = nums[i] + nums[i-1] + nums[i-2]
                ans = max(ans,peri)
        return ans