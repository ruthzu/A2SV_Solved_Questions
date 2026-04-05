t = int(input())
for _ in range(t):
    s = input()
    n = len(s)
    i = 0
    working = set()

    while i < n:
        j = i
        while j < n and s[j] == s[i]:
            j += 1
        
        length = j - i
        if length % 2 == 1:
            working.add(s[i])
        
        i = j

    print(''.join(sorted(working)))