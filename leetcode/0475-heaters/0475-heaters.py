class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        max_radius = 0
        def search(n,heaters):
            l = 0
            r = len(heaters)-1
            distance  = float('inf')
            while l <= r:
                mid = (l+r)//2
                distance = min(distance,abs(n - heaters[mid]))
                if heaters[mid] < n:
                    l = mid + 1
                else:
                    r = mid - 1
            return distance
        for i in houses:
            distance = search(i,heaters)
            max_radius = max(max_radius,distance)

        return max_radius