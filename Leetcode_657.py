moves = "LDRRLRUULR"

cor = [0,0]
result = False
for i in moves:
    if i == 'R':
        cor[0] +=1
    elif i == 'L':
        cor[0] -=1
    elif i == 'U':
        cor[1] +=1
    elif i == 'D':
        cor[1] -=1
    else:
        print('Not valid')

if cor[0] == 0 and cor[1] == 0:
    result = True
print(result)