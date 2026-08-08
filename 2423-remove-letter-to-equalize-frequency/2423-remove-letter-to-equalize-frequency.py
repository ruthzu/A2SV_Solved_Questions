class Solution:
    def equalFrequency(self, word: str) -> bool:
        count = Counter(word)

        for v, i in list(count.items()):
            count[v] -= 1

            if count[v] == 0:
                del count[v]

            c = [i for v, i in count.items()]

            if len(set(c)) == 1:
                return True

            count = Counter(word)

        return False