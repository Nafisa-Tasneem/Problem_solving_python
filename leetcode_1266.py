# 1266. Minimum Time Visiting All Points

points = [[1,1],[3,4],[-1,0]]
n =len(points)
cnt = 0
for i in range (0,n-1): #excluding the last point
    # for j in range (0,2):
    tempi = points[i][0]
    tempj = points[i][1]
    print('initial temp : ',tempi,tempj)
    # print(tempj)
    # while abs (tempi-points[i+1][0]) > 0 and abs(tempj- points[i+1][1]) >0:
    while tempi != points[i+1][0] or tempj != points[i+1][1]:
        if tempi < points[i+1][0] and tempj < points[i+1][1]:
            # if abs (tempi-points[i+1][0]) < 0 and abs(tempj- points[i+1][1]) < 0 :
            tempi += 1
            tempj +=1
            cnt +=1
        elif tempi > points[i+1][0] and tempj < points[i+1][1]:
            tempi -=1
            tempj +=1
            cnt +=1
        elif tempi > points[i+1][0] and tempj > points[i+1][1]: # abs (tempi-points[i+1][0]) == 0 and abs(tempj- points[i+1][1]) > 0 :
            tempi -=1
            tempj -=1
            cnt +=1
        elif tempi < points[i+1][0] and tempj > points[i+1][1]:
            tempi += 1
            tempj -= 1
            cnt += 1
        elif tempi == points[i+1][0] and tempj != points[i+1][1]: #straight condition
            if tempj < points[i+1][1]:
                tempj +=1
            else:
                tempj -=1
            cnt +=1
        elif tempi != points[i + 1][0] and tempj == points[i + 1][1]:  # straight condition
            if tempi < points[i + 1][0]:
                tempi += 1
            else:
                tempi -= 1
            cnt += 1
        else:
            break
        print(tempi, tempj)
        print(cnt)


    # while tempi != points[i+1][0] and tempj != points[i+1][1]:
    #     if tempi < points[i+1][0] and tempj < points[i+1][1]:
    #         tempi +=1
    #         tempj +=1
    #         cnt +=1
    #
    #     elif tempi < points[i+1][0] and tempj == points[i+1][1]:
    #         tempi +=1
    #         cnt +=1
    #     elif tempi == points[i+1][0] and tempj < points[i+1][1]:
    #         tempj +=1
    #         cnt +=1
    #     else:
    #         break

print('final count ',cnt)


