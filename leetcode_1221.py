# 1221. Split a String in Balanced Strings
s = "RLRRRLLRLL"

def balancedStringSplit(s):
    arr = list(s)
    r = 0
    l= 0
    cnt = 0
    for i in range(len(arr)):
        if arr[i] == 'R':
            r +=1
        else:
            l +=1

        if r == l and (r,l !=0):
            cnt +=1
            r = 0
            l = 0
    print(cnt)
    return cnt

balancedStringSplit(s)