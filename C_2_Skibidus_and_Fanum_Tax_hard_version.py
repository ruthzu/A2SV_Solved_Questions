t = int(input())
for _ in range(t):
    n, m_size = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b.sort()
    
    prev = float('-inf')
    flag = True
    
    for i in range(len(a)):
        l = 0
        r = len(b) - 1
        ans = float('inf')
        if a[i] >= prev:
            ans =min(a[i],ans)
        best = float('inf')
        while l <= r:
            mid = (l + r) // 2
            if b[mid] - a[i] >= prev:
                best = b[mid] - a[i]
                r = mid - 1 
            else:
                l = mid + 1
                
        ans = min(ans, best)
        
        if ans == float('inf'):
            flag = False
            break
        else:
            prev = ans
    
    if flag:
        print("YES")
    else:
        print("NO")