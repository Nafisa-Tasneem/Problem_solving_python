matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
mini = []
for row in range(len(matrix)):
    mini.append(min(matrix[row]))
# print(mini)

maxi = []

col= len(matrix[0])

for i in range(col):
    temp_arr = []
    for j in range(len(matrix)):
        temp_arr.append(matrix[j][i])
    # print(temp_arr)
    maxi.append(max(temp_arr))
# print(maxi)
result=[]
for i in mini:
    for j in maxi:
        if i== j:
            result.append(i)
print(result)



