class Solution:
    def checkDivisibility(self, n: int) -> bool:
        x = list(str(n))
        add ,mul = 0,1
        for i in range(len(x)):
            add+=int(x[i])
            mul*=int(x[i])
        if n % (add+mul) == 0:
            return True
        return False