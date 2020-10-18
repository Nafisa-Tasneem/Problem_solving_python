target = [1,2,3,4]
arr = [2,9,1,3]

sorted_target = sorted(target)
sorted_arr = sorted(arr)

for i in range(len(arr)):
    if sorted_target[i] == sorted_arr[i]:
        ans = True
    else:
        ans = False
        break

print(ans)