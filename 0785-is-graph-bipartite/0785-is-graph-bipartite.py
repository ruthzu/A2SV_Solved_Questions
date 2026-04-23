class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n

        def dfs(node):
            for neighbour in graph[node]:
                if color[neighbour] == -1:
                    color[neighbour] = 1 - color[node]
                    if not dfs(neighbour):
                        return False
                elif color[neighbour] == color[node]:
                    return False
            return True

        for node in range(n):
            if color[node] == -1:
                color[node] = 0
                if not dfs(node):
                    return False

        return True