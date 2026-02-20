class Solution:
    def smallestPalindrome(self, s: str) -> str:
        s=list(s)
        smallestP = []
        size = len(s)

        half = sorted(s[:size//2])

        flip = half[:]
        flip.reverse()

        smallestP.extend(half)

        if size % 2 != 0:
            smallestP.append(s[size//2])
            
        smallestP.extend(flip)

        return "".join(smallestP)
