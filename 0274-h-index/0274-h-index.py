class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        citations.sort()
        count = Counter(citations)
        for i in range(len(citations)):
            j = len(citations) - i
            if citations[i] == j:
                return j
        if len(citations) == 1 and citations[0] != 0:
            return 1
        if len(count) == 1:
            return citations[0]
        return 1
