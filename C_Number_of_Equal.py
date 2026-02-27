from collections import Counter
n,m = map(int,input().split())
a= list(map(int,input().split()))
b= list(map(int,input().split()))
ans = 0
if n>m:
    count = Counter(a)
    for i in b:
        ans+=count[i]
else:
    count = Counter(b)
    for i in a:
        ans+=count[i]
print(ans)

