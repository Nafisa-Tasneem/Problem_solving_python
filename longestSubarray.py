n = int(input())
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)

# print(arr)

def longestSubarray(arr):
    count = 0
    brr = []
    for i in range (n-1):
        ref = arr[i]
        ref2 = arr[i+1]
        if abs(ref - ref2) <= 1:
            brr.append(ref)
            brr.append(ref2)
            count = count + 2
        if abs(ref2 - arr[i+2]) <= 1 and abs(ref - arr[i+1]) <=1:
            count += 1

    print(count)
    return count


longestSubarray(arr)


