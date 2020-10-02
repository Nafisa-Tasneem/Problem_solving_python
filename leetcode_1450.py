#1450. Number of Students Doing Homework at a Given Time

startTime = [1,1,1,1]
endTime = [1,3,2,4]
queryTime = 7
cnt = 0
for i in range(len(startTime)):
    if queryTime in range(startTime[i],(endTime[i]+1)):
        cnt +=1
print(cnt)