class Solution:
    def minMoves(self, nums: List[int]) -> int:
        x = max(nums)
        ans = 0
        for i in nums:
            ans+=x-i
        return ans