from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0]*numCourses

        for u,v in prerequisites:
            graph[v].append(u)
            indegree[u] += 1
        
        queue = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                queue.append(n)
        count = 0 
        while queue:
            n = queue.popleft()
            count += 1
            if count == numCourses:
                return True
            
            for neighbor in graph[n]:
                indegree[neighbor] -= 1
                
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                
        return False

