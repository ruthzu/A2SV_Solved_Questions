class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        r=[]
        s=float('inf')
        for indx,  i in enumerate (list1):
            for indx2,  j in enumerate (list2):
                if i == j:
                    d = indx + indx2
                    if d < s:
                        s = d
                        r = [i]
                    elif d == s:
                        r.append(i)
                else:
                    continue
        return r                
