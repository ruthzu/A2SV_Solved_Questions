class Solution:
    def pancakeSort(self, arr: list[int]) -> list[int]:
        res = []
        n = len(arr)

        def flip(k):
            l, r = 0, k - 1
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1

        for s in range(n, 1, -1):
            m = max(arr[:s])
            i = arr.index(m)

            if i == s - 1:
                continue

            if i != 0:
                res.append(i + 1)
                flip(i + 1)

            res.append(s)
            flip(s)

        return res