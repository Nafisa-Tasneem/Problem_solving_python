A = [4,2,5,7]
odd = []
even = []
result = []
for i in A:
    if int(i) % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
for i in range(len(odd)):
    result.append(even[i])
    result.append(odd[i])
print(result)
