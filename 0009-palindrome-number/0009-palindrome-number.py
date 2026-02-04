class Solution:
    def isPalindrome(self, x: int) -> bool:
     x=str(x)
     p=x[::-1]
     if x==p:
        return True
     else:
            return False
    