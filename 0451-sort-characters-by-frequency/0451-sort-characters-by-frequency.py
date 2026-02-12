class Solution:
    def frequencySort(self, s: str) -> str:
        freq=Counter(s)
        ans=[]
        order=dict(sorted(freq.items(),key=lambda item:item[1],reverse=True))
        for k,v in order.items():
            val=k*v
            ans.append(val)
        return "".join(ans)