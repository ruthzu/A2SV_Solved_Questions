class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        ans = []
        for key,values in count.items():
            if values ==2:
                ans.append(key)
        return ans