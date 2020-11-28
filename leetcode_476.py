num = 123
arr = []
while num != 0:
    arr.insert(0,(num%2))
    num = num //2
print(arr)
arr_complement = []
for i in arr:
    if i == 0:
        arr_complement.append(1)
    else:
        arr_complement.append(0)
print(arr_complement)
decimal = 0
index = len(arr_complement) -1
for i in arr_complement:
    # print(index)
    decimal +=  int(i) * pow(2,index)
    index -=1
print(decimal)
