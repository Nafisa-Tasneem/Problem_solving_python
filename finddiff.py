def missingNumbers(arr, brr):
    a = sorted(arr)
    b = sorted(brr)
    j= 0
    new_list = []
    for i in range(0,m):
        # print(i, '', j)
        if j >= n:
            new_list.append(b[i])
        elif b[i] != a[j] :
            new_list.append(b[i])
            # j +=1
            # print(new_list)

        else:
            j +=1

    unique_set = set(new_list)
    x = list(unique_set)
    y = sorted(x)
    print(y)
    return y

n = int(input())

arr = list(map(int, input().rstrip().split()))

m = int(input())

brr = list(map(int, input().rstrip().split()))

result = missingNumbers(arr, brr)