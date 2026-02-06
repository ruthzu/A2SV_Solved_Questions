from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums)
        freq = dict(sorted(freq.items(),key = lambda item:item[1],reverse=True))
        key = list(freq.keys())
        return key[:k]
         