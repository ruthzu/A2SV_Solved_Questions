from typing import List

class Solution:
    def checkSubarraySum(self, a: List[int], k: int) -> bool:
        if k == 0:
            for i in range(len(a) - 1):
                if a[i] == 0 and a[i + 1] == 0:
                    return True
            return False
        
        s = 0
        d = {0: -1}
        
        for i in range(len(a)):
            s += a[i]
            r = s % k
            
            if r in d:
                if i - d[r] > 1:
                    return True
            else:
                d[r] = i
        
        return False