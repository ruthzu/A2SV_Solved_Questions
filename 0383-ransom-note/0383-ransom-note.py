class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        countr=Counter(ransomNote)
        countm=Counter(magazine)

        if countr-countm != {}:
            return False
        else:
            return True
        
