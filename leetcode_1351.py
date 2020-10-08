grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]

cnt = 0

for element in range(len(grid)):
    # print(grid[element])
    for number in range(len(grid[element])):
        if (grid[element][number]) < 0:
            cnt +=1
print(cnt)