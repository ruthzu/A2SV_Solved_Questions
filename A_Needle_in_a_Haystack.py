t = int(input())
for _ in range(t):
    s = list(map(str,input()))
    t = list(map(str,input()))
    t.sort()
    sort_s = sorted(s)
    i = 0
    j = len(t)-1
    k = 0
    ne = []
    new = []
    while i < len(s) and j > 1 :
        if sort_s[i] == t[j]:
            i+=1
            j-=1
        else:
            new.append(t[j])
            j-=1
    # while k < len(new):
    #     if new[k] == sort_s[0]:
    #         break
    #     ne.append(new[k])
    # ne.extend(s)
    # ne.extend(new[k:])

    # print(ne)