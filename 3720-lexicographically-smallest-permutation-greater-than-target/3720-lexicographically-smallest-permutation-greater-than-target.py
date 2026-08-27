class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - 97] += 1

        ans = []

        for i, c in enumerate(target):
            x = ord(c) - 97

            if cnt[x]:
                cnt[x] -= 1
                ans.append(c)
                continue

            for y in range(x + 1, 26):
                if cnt[y]:
                    cnt[y] -= 1
                    return ''.join(ans) + chr(y + 97) + ''.join(
                        chr(j + 97) * cnt[j] for j in range(26)
                    )

            for k in range(i - 1, -1, -1):
                old = ord(ans[k]) - 97
                cnt[old] += 1
                ans.pop()

                for y in range(old + 1, 26):
                    if cnt[y]:
                        cnt[y] -= 1
                        return ''.join(ans) + chr(y + 97) + ''.join(
                            chr(j + 97) * cnt[j] for j in range(26)
                        )

            return ""

        for k in range(len(ans) - 1, -1, -1):
            old = ord(ans[k]) - 97
            cnt[old] += 1

            for y in range(old + 1, 26):
                if cnt[y]:
                    cnt[y] -= 1
                    return ''.join(ans[:k]) + chr(y + 97) + ''.join(
                        chr(j + 97) * cnt[j] for j in range(26)
                    )

        return ""