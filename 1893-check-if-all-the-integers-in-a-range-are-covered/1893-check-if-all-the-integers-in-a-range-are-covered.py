class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        integers={i for i in range(left,right+1)}
        interval={i for List in ranges for i in List}
        if integers - interval == set():
         return True
        else:
         return False 
        