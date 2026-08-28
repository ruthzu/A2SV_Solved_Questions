from collections import Counter


class Solution:

    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cnt = Counter(s)

        # 1. Palindrome Check: At most one character can have an odd frequency
        odd_chars = [ch for ch, freq in cnt.items() if freq % 2 != 0]
        if len(odd_chars) > 1:
            return ""

        mid_char = odd_chars[0] if odd_chars else ""

        # Half frequency map for the first n // 2 characters
        half_cnt = {ch: freq // 2 for ch, freq in cnt.items()}
        m = n // 2

        def build_palindrome(first_half: str, remaining_cnt: dict) -> str:
            """Constructs the smallest full palindrome given a partial first half."""
            rest = "".join(
                ch * remaining_cnt[ch] for ch in sorted(remaining_cnt.keys())
            )
            full_first = first_half + rest
            return full_first + mid_char + full_first[::-1]

        def get_prefix_counts(length: int):
            """Tries to match target[:length] using available half_cnt."""
            prefix = []
            curr_cnt = half_cnt.copy()
            for ch in target[:length]:
                if curr_cnt.get(ch, 0) > 0:
                    curr_cnt[ch] -= 1
                    prefix.append(ch)
                else:
                    return None, None
            return "".join(prefix), curr_cnt

        candidates = []

        # 2. Case A: Match first half exact to target[:m]
        exact_prefix, remaining = get_prefix_counts(m)
        if exact_prefix is not None:
            cand = build_palindrome(exact_prefix, remaining)
            if cand > target:
                candidates.append(cand)

        # 3. Case B: Diverge at position i with a strictly larger character
        for i in range(m - 1, -1, -1):
            prefix, remaining = get_prefix_counts(i)
            if prefix is None:
                continue

            for ch in sorted(remaining.keys()):
                if ch > target[i] and remaining[ch] > 0:
                    next_remaining = remaining.copy()
                    next_remaining[ch] -= 1
                    cand = build_palindrome(prefix + ch, next_remaining)
                    if cand > target:
                        candidates.append(cand)
                        break  # Pick smallest valid character at index i

        return min(candidates) if candidates else ""