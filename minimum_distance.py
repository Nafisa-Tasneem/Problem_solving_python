points = [[1,1],[3,4],[-1,0]]
n =len(points)
cnt = 0
for i in range (0,n-1): #excluding the last point
    x0 = points[i][0]
    y0 = points[i][1]
    # print('initial temp : ',tempi,tempj)

    dx = abs(x0 - points[i+1][0])
    dy = abs(y0 - points[i+1][1])
    distance = max(dx,dy)
    cnt = cnt + distance
    # print(tempj)

print(cnt)

print('final count ',cnt)
