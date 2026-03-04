class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        n = len(nums)
        mini ,curr = 0,0
        for num in nums:
            curr +=num
            mini = min(curr,mini)
        return 1-mini