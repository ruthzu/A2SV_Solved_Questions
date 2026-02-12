class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hashh={}
        ans=[]
        for i in nums:
            if i not in hashh:
                hashh[i]=1
            else:
                hashh[i]+=1
        for key,values in hashh.items():
            if values ==2:
                ans.append(key)
        return ans