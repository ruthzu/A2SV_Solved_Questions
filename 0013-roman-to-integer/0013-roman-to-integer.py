class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        num = 0
        prev = 0

        for i in reversed(s):
            char = roman[i]
            if char < prev:
                num -= char  
            else:
                num += char
            prev = char
        
        return num
