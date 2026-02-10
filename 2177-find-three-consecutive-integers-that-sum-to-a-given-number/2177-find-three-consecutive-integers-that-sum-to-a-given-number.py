class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        numbers=[]

        if (num-3) % 3 == 0:
            first=(num-3)/3
            numbers.append(int(first))
            numbers.append(int(first+1))
            numbers.append(int(first+2))
            return numbers

        else:
            return []