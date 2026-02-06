class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq={}
        answer=[]
        for i in strs:
            temp=str(sorted(i))
            if temp in freq:
                freq[temp].append(i)
            else:
                freq[temp]=[i]
        for value in freq.values():
            answer.append(value)
        return answer