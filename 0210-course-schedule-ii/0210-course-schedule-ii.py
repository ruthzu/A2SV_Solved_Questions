from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for u,v in prerequisites:
            graph[v].append(u)
            indegree[u] += 1
        
        queue = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                queue.append(n)

        order = []
        # print(indegree)
        while queue:
            n = queue.popleft()
            order.append(n)

            for nei in graph[n]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    queue.append(nei)
        if len(order)!= numCourses:
            return []
        # order.reverse()        
        return order
