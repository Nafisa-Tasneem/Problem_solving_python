arr = [10,100,1000,10000]
import collections

memo = collections.defaultdict(list) # creating dictionary with list type

for i in arr:
    ones = str(bin(i)).count('1')
    memo[ones].append(i)

print(memo)
arr2 = []
for key, value in sorted(memo.items()):

    result = sorted(value)
    for i in result:
        arr2.append(i)
print(arr2)