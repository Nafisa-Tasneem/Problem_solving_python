M = [[1,1,1],
 [1,0,1],
 [1,1,1]]

row = len(M)
col = len(M[0])
# print(row, col )
ans = [[0]*col for element in M] # making col of 3 0's for each row in M

for r in range(row):
    for c in range(col):
        count_of_elements = 0
        for nr in (r-1, r, r+1):
            for nc in (c-1, c, c+1):
                if 0 <= nr < row and 0 <= nc < col:
                    ans [r][c] += M[nr][nc]
                    count_of_elements +=1
        ans[r][c] = ans[r][c] // count_of_elements
print(ans)