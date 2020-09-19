# 1389. Create Target Array in the Given Order

nums = [1]
index = [0]

def createTargetArray(nums,index):
    target = []
    for i in range(len(nums)):
        target.insert(index[i],nums[i])

    print(target)
    return target

createTargetArray(nums, index)