class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        # max_b = math.floor(math.sqrt(c))
        i=0
        j = math.isqrt(c)
        while i <=j:
            if i*i + j*j == c:
                return True
            elif i*i + j*j > c:
                j-=1
            else:
                i+=1
        return False