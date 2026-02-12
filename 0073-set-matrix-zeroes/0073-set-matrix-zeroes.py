class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m,n=len(matrix) ,len(matrix[0])
        row,col = [], []

        for i in range(m):

            for j in range(n):

                if matrix[i][j] == 0: 
                    row.append(i)
                    col.append(j)
        print(row,col)
        
        for i in range(len(row)):
            for j in range(n):
                matrix[row[i]][j]=0

        for i in range(len(col)):
            for j in range(m):
                matrix[j][col[i]]=0

