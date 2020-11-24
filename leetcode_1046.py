stones = [2,7,4,1,8,1,9]

sorted_stones = sorted(stones)

while (len(sorted_stones)>1):
    sorted_stones = sorted(sorted_stones)
    print((sorted_stones))
    x = sorted_stones.pop(len(sorted_stones)-1)
    y = sorted_stones.pop(len(sorted_stones)-1)
    new_weight = x-y
    if new_weight> 0 :
        sorted_stones.append(new_weight)
# print(sorted_stones)
result = 0
if len(sorted_stones) > 0 :
    result = sorted_stones[0]
print(result)