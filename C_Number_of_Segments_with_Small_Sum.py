n,s =map(int,input().split())
arr = list(map(int,input().split()))

curr_s = 0
ans = 0
left = 0
for right in range(len(arr)):
    curr_s+=arr[right]
    while  curr_s>s:
        curr_s -= arr[left]
        left += 1
    ans += (right - left + 1)
print(ans)
    