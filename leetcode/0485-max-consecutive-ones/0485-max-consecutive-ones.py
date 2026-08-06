class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = []
        co = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                co +=1 
            else:
                ans.append(co)
                co = 0
                
        ans.append(co)
        print(ans)
        return max(ans)


