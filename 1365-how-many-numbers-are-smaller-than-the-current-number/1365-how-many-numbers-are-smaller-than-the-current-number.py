class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        ans=[]
        for num in nums:
            n = sorted_nums.index(num)
            ans.append(n)
        return ans
        