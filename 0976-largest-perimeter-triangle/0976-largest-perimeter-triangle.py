class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        ans=0
        for i in range(len(nums)-2):
            a = nums[i] 
            b = nums[i+1] 
            c = nums[i+2] 
            if a +b > c:
                ans = max (ans , a+b+c)

        return ans