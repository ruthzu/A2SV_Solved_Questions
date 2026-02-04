class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return "" 
            
        word = strs[0]
        prefix=""
        for i in range(len(word)):
            x=word[i]
            for j in strs:
                if i>=len(j) or j[i] != x:
                    return prefix
            prefix+=x

        return prefix