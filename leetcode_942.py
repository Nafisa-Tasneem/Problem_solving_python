S = "IDID"
#idea is to put smallest element when it is 'I' and put the largest element when 'D'
low, hi = 0, len(S)
# print(A)
result = []

for i in S:
    if i == 'I':
        result.append(low)
        low +=1
    else:
        result.append(hi)
        hi -=1

print(result+ [low])

