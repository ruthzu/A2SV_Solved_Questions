t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))

    # arr.sort()
    ans = 0

    for k in range(n):
        i = 0
        j = k - 1
        while j > i:
            need = max(arr[k],(arr[n-1]-arr[k]))
            if arr[i] + arr[j] > need:
                ans += (j-i)
                j -= 1
            else:
                i += 1
    x = inf
    print(ans)
        
    
              