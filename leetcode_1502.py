arr = [1,2,3]
arr2 = sorted(arr)
print(arr2)
ans = True
for i in range(len(arr2)-2):
    if abs(int(arr2[i])- int(arr2[i+1])) != abs(int(arr2[i+1])- int(arr2[i+2])):
        ans = False
        print(ans)
        break


print(ans)