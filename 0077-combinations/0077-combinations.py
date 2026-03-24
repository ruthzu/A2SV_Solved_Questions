class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        def f(s, p):
            if len(p) == k:
                res.append(p[:])
                return
            for i in range(s, n + 1):
                p.append(i)
                f(i + 1, p)
                p.pop()
        
        f(1, [])
        return res