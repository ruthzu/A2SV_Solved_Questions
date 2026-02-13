class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=[w for w in s.split()]
        if len(s)!=len(pattern):
            return False
        
        sp={}
        ps={}
        
        for p, w in zip(pattern, s):
            if p in ps and ps[p] != w:
                return False
            if w in sp and sp[w] != p:
                return False

            ps[p] = w
            sp[w] = p

        return True
