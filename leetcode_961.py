from collections import Counter
A = [2,1,2,5,3,2]
cnt = Counter(A)
print(cnt)
# ans = int()
# for x,y in cnt.items():
#     # print(x,y)
#     if int(y)> 1:
#         print(int(x))

for j in cnt.keys():
    if cnt[j] > 1:
        print(j)