n = int(input())
points =[int(num) for num in input().split()]
points.sort()
if n % 2 == 0:
    print(points[len(points)//2-1])
else:
    print(points[len(points)//2])