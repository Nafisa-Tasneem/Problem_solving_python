def minimumDistances(a):

    op = []
    dist = 0
    for i in range(n):
        for j in range(n):
            if i != j and a[j] == a[i]:
                dist = abs(j-i)
                op.append(dist)

    if op == []:
        result = -1
    else:
        result = min(op)

    # print(result)
    return result


n = int(input())

a = list(map(int, input().rstrip().split()))

result = minimumDistances(a)
