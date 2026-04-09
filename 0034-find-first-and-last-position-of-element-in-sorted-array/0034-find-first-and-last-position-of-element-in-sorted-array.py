class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def loww(arr,target):
            low = 0 
            high = len(arr) -1
            while low <= high:
                mid = (low + high)//2
                if arr[mid] < target:
                    low = mid +1
                else:
                    high = mid -1
            if low < len(arr) and arr[low] == target:
                return low
            return -1
        
        def highh(arr,target):
            low = 0 
            high = len(arr) -1
            while low <= high:
                mid = (low + high)//2
                if arr[mid] <= target:
                    low = mid +1
                else:
                    high = mid -1
            if high > -1 and arr[high] == target:
                return high
            return -1
        return [loww(nums,target),highh(nums,target)]
        
