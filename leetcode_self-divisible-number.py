left = 1
right = 22
result = []
for i in range(left,right+1):
    ans = 0
    digits = str(i)
    for digit in digits:
        if int(digit) == 0:
            ans = 0
            break
        elif int(i) % int(digit) != 0:
            ans = 0
            break
        else:
            ans = 1

    if ans == 1:
        result.append(i)

print(result)
