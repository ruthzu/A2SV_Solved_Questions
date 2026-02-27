from collections import Counter
n =  int(input())
contests =[int(num) for num in input().split()]
contests.sort()
contests.reverse()
count = Counter(contests)
if contests[0] == 0:
    print(0)
else:
    print(len(count))