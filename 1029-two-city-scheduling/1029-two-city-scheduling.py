class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        a = []
        ans = 0
        n = len(costs)

        for cost in costs:
            a.append([cost[0], cost[1], cost[0] - cost[1]])

        aa = sorted(a, key=lambda x: x[2])

        i = 0
        while i < len(aa):
            if i < n // 2:
                ans += aa[i][0]
            else:
                ans += aa[i][1]
            i += 1

        return ans