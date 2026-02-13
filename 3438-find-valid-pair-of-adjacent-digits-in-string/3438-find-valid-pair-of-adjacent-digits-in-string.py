class Solution:
    def findValidPair(self, s: str) -> str:
        count=Counter(s)
        prev=0
        a=''
        for i in range(len(s)-1):
            curr=s[i]
            nextt=s[i+1]
            if curr != nextt:
                if int(curr) == count[curr] and int(nextt) == count[nextt] :
                    return s[i]+s[i+1]
        
        return ""