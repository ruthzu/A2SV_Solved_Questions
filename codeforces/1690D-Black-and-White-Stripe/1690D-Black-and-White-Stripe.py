t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()
    
    whites = 0
    for i in range(k):
        if s[i] == 'W':
            whites += 1
    
    ans = whites
    
    for i in range(k, n):
        if s[i] == 'W':
            whites += 1
        if s[i - k] == 'W':
            whites -= 1
        ans = min(ans, whites)
    
    print(ans)