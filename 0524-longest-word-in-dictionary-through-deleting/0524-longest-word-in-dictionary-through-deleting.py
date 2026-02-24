class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort()
        dictionary.sort(key=len,reverse = True)

        for word in dictionary:
            i,j=0,0
            while i < len(word) and j <len(s):
                if word[i] == s[j]:
                    i+=1
                    j+=1
                else:
                    j+=1
            
            if i == len(word):
                return word
        return ""
            