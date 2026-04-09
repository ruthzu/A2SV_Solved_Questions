# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 0
        r = n
        ans  =[]
        while r >= l:
            mid = (r +l)//2
            if isBadVersion(mid):
                ans.append(mid)
                r = mid - 1
            else:
                l = mid + 1
        ans.sort()
        return ans[0]
            


