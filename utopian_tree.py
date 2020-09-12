def utopianTree(n):
    for i in range(n+1):
        if (i==0):
            h = 1
        elif (i==1):
            h = h*2
        elif (i%2)==0:
            h = h+1
        else:
            h = h*2

    # print(h)
    return h


t = int(input())

for t_itr in range(t):
    n = int(input())

    result = utopianTree(n)
