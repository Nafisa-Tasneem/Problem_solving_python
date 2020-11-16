nums = [1,1,2,2,2,3]

from collections import Counter
import collections
dictionary = collections.defaultdict(list)
dict_counter =(Counter((nums)))
print(dict_counter)
ans = []

for key,value in dict_counter.items():
    dictionary[value].append(key)
print(dictionary)
dict_check = dict(sorted(dictionary.items()))
print(dict_check)
for num, ele in dict_check.items():
    ans += sorted(ele*num, reverse=True)
print(ans)