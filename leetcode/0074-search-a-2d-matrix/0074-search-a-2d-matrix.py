class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n,m = len(matrix),len(matrix[0])
        l,r = 0, n*m -1
        while l <= r:
            mi = (l + r) // 2
            if matrix[mi//m][mi % m] == target:
                return True
            elif matrix[mi//m][mi % m] > target:
                r = mi - 1
            else:
                l = mi + 1
        return False