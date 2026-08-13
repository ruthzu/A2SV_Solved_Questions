class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        tree = [None] * (4 * n)
        def merge(a, b):
            a_len, a_lc, a_ll, a_rc, a_rl, a_best = a
            b_len, b_lc, b_ll, b_rc, b_rl, b_best = b

            length = a_len + b_len
            best = max(a_best, b_best)
            if a_rc == b_lc:
                best = max(best, a_rl + b_ll)

            left_char, left_len = a_lc, a_ll
            if a_ll == a_len and a_lc == b_lc:
                left_len = a_len + b_ll

            right_char, right_len = b_rc, b_rl
            if b_rl == b_len and b_rc == a_rc:
                right_len = b_len + a_rl

            return (length, left_char, left_len, right_char, right_len, best)

        def build(node, lo, hi):
            if lo == hi:
                c = s[lo]
                tree[node] = (1, c, 1, c, 1, 1)
                return
            mid = (lo + hi) // 2
            build(2 * node, lo, mid)
            build(2 * node + 1, mid + 1, hi)
            tree[node] = merge(tree[2 * node], tree[2 * node + 1])

        def update(node, lo, hi, idx, ch):
            if lo == hi:
                tree[node] = (1, ch, 1, ch, 1, 1)
                return
            mid = (lo + hi) // 2
            if idx <= mid:
                update(2 * node, lo, mid, idx, ch)
            else:
                update(2 * node + 1, mid + 1, hi, idx, ch)
            tree[node] = merge(tree[2 * node], tree[2 * node + 1])

        build(1, 0, n - 1)

        result = []
        for ch, idx in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, idx, ch)
            result.append(tree[1][5])  
        return result








        # ans = []
        # def longest_sub(s):
        #     max_len = 1
        #     i = 0
        #     for j in range(1,len(s)):
        #         if s[i] == s[j]:
        #             max_len = max(max_len,j-i+1)
        #         else:
        #             i = j
        #     return max_len
        # s = list(s)
        # for i in range(len(queryIndices)):
        #     s[queryIndices[i]] = queryCharacters[i]
        #     ans.append(longest_sub(s))

        
        # # result = "".join(ans)
        # return ans
        













