nums = [6,6]

if len(nums)==1:
    print(nums)
elif len(nums)==2 and nums[0]==nums[1]:
    print(nums)
else:

    sorted_nums = sorted(nums,reverse=True)
    # print(sorted_nums)
    sum_result = 0
    arr2 = []
    copy = sorted_nums
    for i in range(len(sorted_nums)-1):
        sum_result+= sorted_nums[0]
        arr2.append(sorted_nums[0])
        copy.pop(0)
        x = sum(copy)
        print(sum_result,x)

        if sum_result >x :
            print(arr2)
            break
