class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l = 0
        r = len(citations) - 1
        ans = 0 
        while l <= r:
            mid = (l+r)//2
            if len(citations) - mid <= citations[mid]:
                ans = max(ans,len(citations) - mid)
                r = mid - 1
            else:
                l = mid + 1
        return ans

