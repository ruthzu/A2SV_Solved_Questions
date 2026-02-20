class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        points.reverse()
        arrow = len(points)
        temp=[]

        for i in range(len(points)-1):
            s = points[i][0] - points[i+1][0]
            e = points[i][1] - points[i+1][1]
            
            if s < e :
                print(s,e,arrow,"b")
                arrow =arrow  - 1
                print(arrow,"a")

            temp.append(points[i])
        
        for j in range(len(temp)-1):
            if temp[j][0] == temp[j+1][1] or temp[j][1] == temp[j+1][0]:
                arrow =arrow  - 1

        return arrow
