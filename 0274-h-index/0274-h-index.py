class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        citations.sort()
        for i in range(len(citations)):
            j = len(citations) - i
            if citations[i] >= j:
                return j
        return 0
