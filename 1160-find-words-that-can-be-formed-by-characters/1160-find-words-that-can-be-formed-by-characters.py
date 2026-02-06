class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        
        ans=0
        freq_chars=defaultdict(int)
        for c in chars:
            freq_chars[c]+=1
   
        def helper(word,freq_chars):

            count=0
            currcount=0
            freq_word=defaultdict(int)

            for c in word:
                freq_word[c]+=1
            # print(freq_word,freq_chars)
            
            for c in word:
                if freq_chars[c]<freq_word[c]:
                    print(c,freq_chars[c],freq_word[c])
                    currcount=0
                    break
                currcount+=1
            count+=currcount
            currcount=0
            print(count)
            return count
        for word in words:
            print(helper(word,freq_chars))
            ans+=helper(word,freq_chars)
        return ans
                