class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        m=len(image)
        n=len(image[0])
        invert=[[0]*n for i in range(m)]
        for i in range(m):
            image[i].reverse()
            for j in range (n):
                if image[i][j] == 1:
                    invert[i][j] = 0
                else:
                    invert[i][j] = 1
        return invert
