class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p= [0]*len(nums)
        ans= [0]*len(nums)
        p[0] = nums[0]
        s= [0]*len(nums)
        s[-1] = nums[-1]

        for i in range(1,len(nums)):
            p[i] = p[i-1] * nums[i]
        for i in range(len(nums)-2,-1,-1):
            s[i] = s[i+1] * nums[i]
            
        ans[0]=s[1]
        ans[-1]= p[-2]
        for i in range(1,len(nums)-1):
            print(i)
            ans[i]= (p[i-1]*s[i+1])
        return ans

