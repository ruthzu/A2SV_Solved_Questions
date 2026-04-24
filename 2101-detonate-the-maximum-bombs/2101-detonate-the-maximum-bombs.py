from collections import defaultdict
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = defaultdict(list)
        for i in range(n):
            for j in range(i+1,n):
                x1 ,y1,r1 = bombs[i][0] ,bombs[i][1] ,bombs[i][2]
                x2 ,y2, r2 = bombs[j][0] ,bombs[j][1], bombs[j][2]
                d = (((x1 - x2)**2) + ((y1 - y2)**2))   
                if d <= r1**2:
                    graph[i].append(j)
                if d <= r2**2:
                    graph[j].append(i)

        # visited = set(')
        def dfs(node,visited):
            visited.add(node)
            count = 1
            for nei in graph[node]:
                if nei not in visited:
                    count += dfs(nei,visited)
            return count
        
        res = 0
        for i in range(n):
            visited = set()
            res = max(res,dfs(i,visited))

        return res

