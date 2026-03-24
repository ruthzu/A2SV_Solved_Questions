from collections import Counter

def main():
    line = input()
    if not line:
        return
    t_cases = int(line)
    
    for _ in range(t_cases):
        s = input().strip()
        t = input().strip()
        
        c_t = Counter(t)
        c_s = Counter(s)
        
        possible = True
        for char in c_s:
            if c_t[char] < c_s[char]:
                possible = False
                break
        
        if not possible:
            print("Impossible")
            continue
            
        res = []
        rem_s = c_s
        
        for char_s in s:
            for i in range(ord('a'), ord(char_s)):
                char_low = chr(i)
                while c_t[char_low] > rem_s[char_low]:
                    res.append(char_low)
                    c_t[char_low] -= 1
            
            res.append(char_s)
            c_t[char_s] -= 1
            rem_s[char_s] -= 1
            
        for i in range(ord('a'), ord('z') + 1):
            char_rem = chr(i)
            while c_t[char_rem] > 0:
                res.append(char_rem)
                c_t[char_rem] -= 1
                
        print("".join(res))

main()