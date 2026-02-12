class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count=Counter(nums)
        arr=[]
        for k,v in count.items():
            if v == 2:
                arr.append(k)
        return arr