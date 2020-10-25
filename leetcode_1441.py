target = [2,3,4]
n = 4
result = []
ele = 0
for i in range(1,n+1):
    # for ele in target:
    print(i,target[ele])
    if i == target[ele]:
        result.append('Push')
        ele+=1
        if ele == len(target):
            break
    else:
        result.append('Push')
        result.append('Pop')

print(result)
