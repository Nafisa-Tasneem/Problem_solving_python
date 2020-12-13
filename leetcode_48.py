matrix = [[1,2],[3,4]]

n = len(matrix)

if n > 1:
    for col in range (n):
        for row in range(col, n):
            # print(row,col,op_row)
            # temp1 = matrix[row][col]
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

    for i in range(n):
        matrix[i].reverse()


print(matrix)