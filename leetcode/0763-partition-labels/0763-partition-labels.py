class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = defaultdict(list)
        for i,ch in enumerate(s):
            if count[ch] == []:
                count[ch]= [i,i]
            else:
                count[ch][1]= i

        val = sorted(list(count.values()))

        ans=[]
        s,e= val[0][0],val[0][-1]
        for i in range(1,len(val)):
            if val[i][0] < e:
                e = max(e,val[i][-1])
            else:
                ans.append(e-s+1)
                s=val[i][0]
                e=val[i][-1]

        ans.append(e-s+1)
        return ans

