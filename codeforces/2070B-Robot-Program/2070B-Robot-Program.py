t = int(input())
for _ in range(t):
    n, x, k = map(int, input().split())
    s = input().strip()
    
    balance = 0
    first_zero = -1
    for i in range(n):
        if s[i] == 'L':
            balance -= 1
        else:
            balance += 1
        if x + balance == 0:
            first_zero = i + 1
            break
    
    if first_zero == -1 or first_zero > k:
        print(0)
        continue
    
    result = 1
    remaining_steps = k - first_zero
    
    balance = 0
    cycle_length = -1
    for i in range(n):
        if s[i] == 'L':
            balance -= 1
        else:
            balance += 1
        if balance == 0:
            cycle_length = i + 1
            break
    
    if cycle_length == -1:
        print(result)
    else:
        result += remaining_steps // cycle_length
        print(result)