class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        count=Counter(nums)
        n=len(nums)
        sortedf=dict(sorted(count.items(),key=lambda x:x[1],reverse=True))
        x=next(iter(sortedf.items()))[0]
        for i in range(n):
            s1=nums[0:i]
            s2=nums[i:]
            if (s1.count(x)>(i/2) and s2.count(x)> ((n-i)/2)):
                return i-1
        return -1
            
        