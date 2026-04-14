class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left = 1
        right = max(candies)
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            count = 0
            for c in candies:
                if mid != 0:
                    count += c // mid
            if count >= k:
                ans = mid        
                left = mid + 1  
            else:
                right = mid - 1  
        return ans