class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        string="".join(map(str,nums))
        answer=[int(num) for num in string]
        return answer