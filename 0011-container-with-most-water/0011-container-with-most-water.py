class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_volume = 0
        left ,right = 0 , len(height)-1

        while left < right :
            curr_width = right - left
            curr_height = min(height[left],height[right])
            max_volume = max(max_volume,curr_width*curr_height)
            
            if height[left] > height[right]:
                    right-=1
            else:
                left+=1
        
        return max_volume