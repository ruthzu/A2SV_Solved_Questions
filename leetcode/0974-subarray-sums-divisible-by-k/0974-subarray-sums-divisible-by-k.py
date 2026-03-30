class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d = {0: 1}
        s = 0
        c = 0
        
        for n in nums:
            s += n
            r = s % k
            if r in d:
                c += d[r]
                d[r] += 1
            else:
                d[r] = 1
                
        return c