class Solution:
    def isHappy(self, n: int) -> bool:
        
        temp=[]
        def recursion(n):
            s=0
            for i in str(n):
                s+=int(i)*int(i)
                
            if s==1:
                return True
            else:
                if s in temp:
                    return False
                else:
                    temp.append(s)
                    return recursion(s)
        return(recursion(n))