from collections import Counter
arr = [-5,5,5]
n = Counter(arr)

f1 = True
arr2 = sorted(list(n.values()))
print(arr2)
for i in range(len(arr2)-1):
    if arr2[i+1] == arr2[i]:
        f1 = False
        break
if f1 == 1:
    result = False
else:
    result = True
print(f1)