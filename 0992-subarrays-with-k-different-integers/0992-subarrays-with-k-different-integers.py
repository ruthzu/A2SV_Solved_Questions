class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        def atMost(goal: int) -> int:
            if goal == 0:
                return 0
            count = Counter()
            left = 0
            res = 0
            for right in range(len(nums)):
                count[nums[right]] += 1
                while len(count) > goal:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        del count[nums[left]]
                    left += 1
                res += (right - left + 1)
            return res

        return atMost(k) - atMost(k - 1)