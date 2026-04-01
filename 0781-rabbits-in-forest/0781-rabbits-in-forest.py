class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        ans = 0
        print(count)
        for i,c in count.items():
            group = i + 1
            num_groups = (c + i) // group
            ans += num_groups * group
        return ans 