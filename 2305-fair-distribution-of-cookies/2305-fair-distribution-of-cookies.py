class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        res = float('inf')
        dist = [0] * k
        
        def backtrack(i):
            nonlocal res
            if i == len(cookies):
                res = min(res, max(dist))
                return
            
            if max(dist) >= res:
                return
            
            for j in range(k):
                dist[j] += cookies[i]
                backtrack(i + 1)
                dist[j] -= cookies[i]
                
                if dist[j] == 0:
                    break
        
        backtrack(0)
        return res