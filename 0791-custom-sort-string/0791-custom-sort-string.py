class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
        
        result = []
        
        for c in order:
            if c in count:
                result.append(c * count[c])
                del count[c]
        
        for c in count:
            result.append(c * count[c])
        
        return "".join(result)