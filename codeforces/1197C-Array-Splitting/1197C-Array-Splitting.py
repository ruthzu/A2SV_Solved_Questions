n, k = map(int, input().split())
a = list(map(int, input().split()))

if k == 1:
    print(a[n-1] - a[0])
else:
    cost = a[n-1] - a[0]
    gaps = []
    
    for i in range(n - 1):
        gaps.append(a[i+1] - a[i])
    
    gaps.sort(reverse=True)
    
    for i in range(k - 1):
        cost -= gaps[i]
        
    print(cost)