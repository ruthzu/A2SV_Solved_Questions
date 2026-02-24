class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skills=sorted(skill)
        result, i, j = 0, 0, len(skill)-1
        target=skills[0]+skills[len(skill)-1]
        while i<j:
            if target==skills[i]+skills[j]:
                  result+=skills[i]*skills[j]
                  i+=1
                  j-=1
            else:
                return -1      
        return result    

             
