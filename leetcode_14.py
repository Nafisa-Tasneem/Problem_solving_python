strs = []

ans = ''
if len(strs) != 0:
    mini = 201
    for i in strs:
        if len(i) < mini:
            mini = len(i)

    for i in range(0,mini):
        isequal = True
        character = strs[0][i]
        for element in strs:
            if element[i] != character:
                isequal = False
                break
        if isequal == True:
            ans += character
        else:
            break
print(ans)
