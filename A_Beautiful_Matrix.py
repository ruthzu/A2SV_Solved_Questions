grid=[]
for _ in range(5):
    r=[int(num) for num in input().split()]
    grid.append(r)
ans=0
for i in range(5):
    for j in range(5):
        if grid[i][j]==1:
            n=2-i
            m=2-j
            ans=abs(m)+abs(n)
print(ans)
