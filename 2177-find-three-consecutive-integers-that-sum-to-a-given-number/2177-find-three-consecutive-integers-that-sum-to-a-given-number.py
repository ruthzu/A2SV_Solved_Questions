class Solution:
    def sumOfThree(self, num: int) -> List[int]:

        if (num-3) % 3 == 0:
            first=(num-3)/3
            return [int(first),int(first+1),int(first+2)]

        else:
            return []