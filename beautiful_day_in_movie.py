
def beautifulDays(i, j, k):
    count = 0
    for x in range (i,j+1):
        rev_num = 0
        num = x
        while num >0 :
            # a = num % 10
            rev_num = rev_num *10 + num % 10
            num = num//10 # a//b --> integer division, returns floored result of floating point division
            # print(rev_num)

        print(rev_num)
        if abs(x - rev_num) % k == 0:
            count += 1

    print(count)
    return count



ijk = input().split()

i = int(ijk[0])

j = int(ijk[1])

k = int(ijk[2])

result = beautifulDays(i, j, k)