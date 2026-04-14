n,s = map(int,input().split())
arr = list(map(int,input().split()))

j = 0
cu = 0
ans = 0
for i in range(len(arr)):
    cu+= arr[i]
    while cu >= s:
        ans += len(arr) - i 
        cu -= arr[j]
        j += 1
print(ans)
