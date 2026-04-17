class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = sorted(Counter(nums).items(),key = lambda x:x[1],reverse = True)
        print(count)
        n = len(nums)
        x = int((n * (n + 1)) / 2 - (sum(nums) - count[0][0]))
        return [count[0][0],x]