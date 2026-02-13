class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        arr=0
        for i in grid:
            for j in i:
                if j<0:
                    arr+=1
        return arr