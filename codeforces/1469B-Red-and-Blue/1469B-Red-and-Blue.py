t = int(input())
for _ in range(t):
    n= int(input())
    r = list(map(int,input().split()))

    m= int(input())
    b = list(map(int,input().split()))
    
    p_r ,max_r= 0,0
    p_b, max_b = 0,0

    for i in range(n):
        p_r += r[i]
        max_r = max(max_r,p_r)

    for i in range(m):
        p_b += b[i]
        max_b = max(max_b,p_b)
    
    print(max_b + max_r)