t = int(input())

for _ in range(t):
    n = int(input())
    p = list(map(int,input().split()))

    ans = []
    ans.append(p[0])
    for i in range(1,len(p)-1):
        if p[i] > p[i-1] and p[i] > p[i+1] or p[i] < p[i-1] and p[i] <p[i+1] :
            ans.append(p[i])
    ans.append(p[-1])
    print(len(ans))
    print(*ans)


