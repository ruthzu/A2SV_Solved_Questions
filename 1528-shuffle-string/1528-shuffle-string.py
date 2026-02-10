class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        n = len(s)
        shuffled = [0] * n
        str_shuffled = ""

        for index,char in enumerate(s):
            indice = indices[index]
            shuffled[indice] = char
        
        for char in shuffled:
            str_shuffled=str_shuffled + char

        return str_shuffled