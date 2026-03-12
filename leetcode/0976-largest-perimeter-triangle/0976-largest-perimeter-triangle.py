class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for i in range(len(nums)-2):
            c = nums[i]
            a = nums[i+1]
            b = nums[i+2]
            if (b< a + c):
                print(c,a,b)
                ans = max(ans,a +b + c)
        return ans

