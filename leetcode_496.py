nums1 = [2,4]
nums2 = [1,2,3,4]

maxi = max(nums2)
# print(maxi)
result_var = False
result = []

for i in range(len(nums1)):
    if nums1[i] == maxi:
        result.append(-1)
    else:
        for j in range(i,len(nums2)):
            if nums2[j] > nums1[i]:
                result.append(nums2[j])
                result_var = True
                break
        if result_var == False:
            result.append(-1)
print(result)
