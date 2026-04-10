class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can(capacity):
            day=1
            weight=0
            for i in weights:
                if i+ weight >capacity:
                    day+=1
                    weight=0
                weight+=i
            return day<=days      
        low,high=max(weights) ,sum(weights)
        while high>low:
            mid=(low+high)//2
            if can(mid):
                high=mid
            else:
                low=mid+1
        return low
                