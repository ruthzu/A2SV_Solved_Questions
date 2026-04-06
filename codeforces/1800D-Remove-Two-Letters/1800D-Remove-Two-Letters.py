t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    
    duplicates = 0
    
    for i in range(n - 2):
        if s[i] == s[i + 2]:
            duplicates += 1
    
    print((n - 1) - duplicates)