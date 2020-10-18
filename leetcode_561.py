nums = [1,4,3,2]

sorted_nums = sorted(nums)
# print(sorted_nums)
sum = 0
while len(sorted_nums) !=0 :

    x= sorted_nums.pop(0)
    # print(sorted_nums)
    y = sorted_nums.pop(0)
    sum += min(x, y)
    # print(sorted_nums,sum)

print(sum)
