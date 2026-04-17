class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
       count = sorted(Counter(nums).items(),key = lambda x:x[1],reverse = True)
       return (count[0][0])