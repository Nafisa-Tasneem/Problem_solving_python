def kaprekarNumbers(p, q):
    result = []
    for i in range(p,q+1):
        d = len(str(i))
        square = i*i
        # print(square)
        arr = []

        for k in str(square):
            arr.append(int(k))
        # print(arr)
        sqr_len = len(arr)
        r =[]
        l = []

        for x in range(0,d):
            num = arr.pop() #by default, pop removes the last item
            r.append(num)
        # print(r)

        r1 = []
        for x in range(len(r)):
            y = r.pop()
            r1.append(y)
        # print(r1)

        l = arr

        right_string = [str(j) for j in r1]
        a_string = "".join(right_string)
        right = int(a_string)
        # print(right)

        # making reverse of right_rev or right:
        # num = right_rev
        # right = 0
        # while num>0:
        #     right = right*10 + num% 10
        #     num = num// 10

        # print(right)
    #
        # for i in l:
        if i > 3:
            left_str = [str(j) for j in l]
            b_str = "".join(left_str)
            left = int(b_str)
        else:
            left = 0

        # print(left)
        if (left + right) == i:
            # print(i, end="0")
            result.append(i)

    if result == []:
        print("INVALID RANGE")
    else:
        for i in result:
            print(i,end=' ')

p = int(input())

q = int(input())

kaprekarNumbers(p, q)
