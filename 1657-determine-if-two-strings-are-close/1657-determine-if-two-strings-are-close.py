class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        

        if len(word1) != len(word2):
            return False
        count1=Counter(word1)
        count2=Counter(word2)
        
        key1=sorted([count1.keys()])
        value1=sorted([count1.values()])

        key2=sorted([count2.keys()])
        value2=sorted([count2.values()])

        if key1 == key2 or value1 == value2:
            return True
        else:
            return False

