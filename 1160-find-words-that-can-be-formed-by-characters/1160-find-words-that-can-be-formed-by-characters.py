class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        
        ans=0
        def helper(word,chars):

            count=0
            currcount=0
            for c in word:
                if word.count(c)>chars.count(c):
                    currcount=0
                    break
                currcount+=1
            count+=currcount
            currcount=0
            return count
        for word in words:
            ans+=helper(word,chars)
        return ans
                