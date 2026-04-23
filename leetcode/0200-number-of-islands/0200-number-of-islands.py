class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        answer = 0
        def dfs(row,col):
            if row >= rows or row < 0 or col < 0 or col >= cols or grid[row][col] == "0":
                return 
            grid[row][col] = "0"
            for i , j in directions:
                newRow , newCol = row + i, col + j
                dfs(newRow,newCol)
            
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    answer += 1
                    dfs(i,j)
        return answer