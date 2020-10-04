# 832. Flipping an Image
A = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
result = []
for element in range(len(A)):
    reverse = []
    inverse = []

    for i in range(len(A[element])):
        reverse.insert(0, A[element][i])
    for j in range(len(reverse)):
        if reverse[j] == 0:
            inverse.append(1)
        else:
            inverse.append(0)
    result.append(inverse)
print(result)
