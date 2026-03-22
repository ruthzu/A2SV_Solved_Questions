class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        r = 0
        last = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] <= last:
                last = nums[i]
            else:
                k = (nums[i] + last - 1) // last
                r += k - 1
                last = nums[i] // k
        return r