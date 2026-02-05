from collections import Counter

class Solution:
    def isSubset(self, a, b):
        ca = Counter(a)
        cb = Counter(b)

        for x in cb:
            if ca[x] < cb[x]:
                return False
        return True
