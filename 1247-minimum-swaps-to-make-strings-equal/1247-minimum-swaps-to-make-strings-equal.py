class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        if len(s1) != len(s2):
            return -1
        count= defaultdict(int)
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                case=s1[i] + s2[i]
                count[case]+=1
        print(count)
        if count['xy'] % 2 == 0 and count['yx'] % 2 == 0:
            return int(count['xy']/2 + count['yx']/2)
        if count['xy'] == count['yx']:
            return count['xy']*2
        return -1
        
