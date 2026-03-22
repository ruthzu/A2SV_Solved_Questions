class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        A=[]
        A = list(range(1, n + 1))
        curr=0   
        while len(A)>1:
            curr=(curr+k-1)%len(A)
            A.pop(curr)
            #continue
        return A[0]        