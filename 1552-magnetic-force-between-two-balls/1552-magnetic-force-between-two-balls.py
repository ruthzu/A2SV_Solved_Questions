class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        left = 1
        right = position[-1] - position[0]
        ans = 0

        while left <= right:
            mid = (left + right) // 2

            count = 1
            last_position = position[0]

            for p in position:
                if p - last_position >= mid:
                    count += 1
                    last_position = p

            if count >= m:
                ans = mid
                left = mid + 1   
            else:
                right = mid - 1  
        return ans