

def countGoodTriplets (arr, a, b, c):
    cnt = 0
    # for i in range(len(arr)):
    #     for j in range(i+1,len(arr)):
    #         for k in range(j+1,len(arr)):
    #             if 0<=i <j < k:
    #                 if abs ( arr[i] - arr[j])<= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k])<= c):
    #                     cnt +=1

    for i in range (len(arr)):
        for j in range(i+1,len(arr)):
            for k in range(j+1,len(arr)):
                if 0 <= i < j < k:
                    if abs ( arr[i] - arr[j])<= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k])<= c):
                        cnt +=1


    print(cnt)
    return cnt


arr = [1,1,2,2,3]
a = 0
b = 0
c = 1

x= countGoodTriplets(arr, a,b,c)