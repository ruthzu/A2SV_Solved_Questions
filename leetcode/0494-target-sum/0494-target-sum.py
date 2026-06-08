from collections import defaultdict
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)

        if abs(target) > total:
            return 0
        if (target + total) % 2 != 0:
            return 0

        S = (target + total) // 2

        dp = defaultdict(int)
        dp[0] = 1

        for num in nums:
            next_dp = defaultdict(int)
            for curr_sum in dp:
                next_dp[curr_sum] += dp[curr_sum]
                next_dp[curr_sum + num] += dp[curr_sum]
            dp = next_dp

        return dp[S]