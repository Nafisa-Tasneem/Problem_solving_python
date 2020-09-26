#1252. Cells with Odd Values in a Matrix

n = 2
m = 3 #dimension of matrix
indices = [[0,1],[1,1]]
cnt = 0
# matrix = [[0]*m]*n
# 2d matrix can be thought of 2 1d arrays
x,y = [0]*n , [0]*m #assigning values to x and y as 2 1d list
for i in indices:
    x[i[0]] +=1 #acessing each element in indices, i[0] and i[1]
    y[i[1]] +=1

for j in y:
    for i in x:
        if (j+i)%2 ==1:
            cnt +=1
print(cnt)
# print(matrix)
# for i in range(len(indices)): # 0
#     row = indices[i][0] # 0
#     col = indices[i][1] # 1
#     for mcol in range (m): # 0
#         matrix[row][mcol] +=1 #
#         print(matrix)
#         # print(matrix[row][mcol])
#     for nrow in range(n):
#         matrix[nrow][col]+=1
#         print(matrix)
# print(matrix)

