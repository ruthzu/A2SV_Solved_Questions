class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        ans = 0
        n = len(nums1)
        if n % 2 == 0:
            ans = (nums1[int(n/2)] + nums1[int(n/2-1)]) / 2
        else:
            ans = nums1[int(n/2)]
        
        return ans