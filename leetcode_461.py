x = 1
y = 4

def dec_to_bin(x):
    arr= []
    while x != 0:
        arr.insert(0,(x%2))
        x = x // 2
    return arr

arr1 = dec_to_bin(x)
arr2 = dec_to_bin(y)

# print(arr1,arr2)

diff = abs(len(arr1) - len(arr2))

for i in range(diff):
    if len(arr1) > len(arr2):
        arr2.insert(0,0)
    elif len(arr2) > len(arr1):
        arr1.insert(0, 0)

# print(arr1,arr2)
cnt = 0
for i in range (len(arr1)):
    if arr1[i] != arr2[i]:
        cnt +=1
print(cnt)



