class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        temp=[rows[:] for rows in matrix]

        for j in range(n):
            for i in range(n):
                matrix[i][j]=temp[n-j-1][i]
                
