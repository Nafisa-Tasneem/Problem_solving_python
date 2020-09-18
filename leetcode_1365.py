# 1365. How Many Numbers Are Smaller Than the Current Number
nums = [8, 1, 2, 2, 3]
def smallerNumbersThanCurrent(nums):
    result = []
    for i in range(len(nums)):
        cnt = 0
        for j in range(len(nums)):
            if j!= i and nums[j] < nums[i]:
                cnt +=1
        result.append(cnt)
    # print('result is : ',result)
    return result

x= smallerNumbersThanCurrent(nums)
print(x)