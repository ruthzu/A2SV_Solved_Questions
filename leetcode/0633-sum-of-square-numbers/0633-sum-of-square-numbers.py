class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        limit = math.floor(c**(1/2))
        a= 0 
        b = int(limit)

        while a<=b:
            d = (a**2) + (b**2)
            if d == c:
                return True
            elif d > c:
                b -= 1
            else:
                a +=1
        return False
