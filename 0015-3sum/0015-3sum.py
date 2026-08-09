class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        j = 0
        k = len(nums)
        ans = set()
        test = []


        for i in range(len(nums)):
            j = i + 1
            k = len(nums) -1
            while j < k:
                t = nums[i] +nums[j] + nums[k]
                if nums[i] +nums[j] + nums[k] == 0:
                    ans.add((nums[i],nums[j],nums[k]))
                    j += 1
                    k -= 1
                elif t > 0:
                    k-=1
                else:
                    j += 1
            
               
        return list(ans)
            

            

        #      if z in nums and nums.index(z)!= indx and nums.index(z)!= indy-indx:
        #             print(indx,indy-indx,nums.index(z),[x,y,z])
        #             ans.add((x, y, z))
        # print(test)

       