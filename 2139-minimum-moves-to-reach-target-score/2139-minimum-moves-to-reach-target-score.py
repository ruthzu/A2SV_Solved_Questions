class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ans = 0
        x = target
        while x > 1:
            if maxDoubles <= 0:
                print(target,x,ans,x-1)
                ans += x -1
                break
            if x % 2 == 0 and maxDoubles > 0:
                x = x // 2
                maxDoubles -= 1
            else:
                x = x - 1
            ans += 1
        return ans
