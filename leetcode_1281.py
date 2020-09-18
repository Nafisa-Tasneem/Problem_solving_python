# 1281. Subtract the Product and Sum of Digits of an Integer
n = 4421
def subtractProductAndSum(n):
    string = str(n)
    strlen = len(string)
    # print(strlen)
    arr = list(string)
    # print('arr is ',arr)

    product = 1
    sum = 0

    for i in range (strlen):
        product = product * int(arr[i])
        sum = sum + int(arr[i])

    diff = product - sum
    # print(diff)
    return diff



subtractProductAndSum(n)