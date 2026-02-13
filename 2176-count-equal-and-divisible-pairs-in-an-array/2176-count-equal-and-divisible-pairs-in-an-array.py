class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        ans=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (i<j and nums[i] == nums[j]):
                    if (i*(j)) % k == 0:
                        ans+=1
        return ans