class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sc=Counter(s)
        tc=Counter(t)
        ans=0
        if sc==tc:
            return ans
        for key ,value in sc.items():
            if tc[key]<value:
                ans+=value-tc[value]
        return ans-1