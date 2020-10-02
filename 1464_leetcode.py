# 1464. Maximum Product of Two Elements in an Array

nums = [3,4,5,2]
arr2 = []

for i in range(len(nums)):
    for j in range(len(nums)):
        if j!= i:
            arr2.append((nums[i]-1) * (nums[j]-1))

print(max(arr2))