# 1572. Matrix Diagonal Sum

mat = [[5]]
sum = 0
for i in range(len(mat)):
        for j in range (len(mat)):
                if i == j or (i + j ==(len(mat) - 1) and i != j):
                        sum = sum + mat [i][j]
print(sum)

# print (len(mat))
