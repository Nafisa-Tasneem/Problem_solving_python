nums = [555,901,482,1771]

def findNumbers(nums):
    ans = 0
    for i in nums:
        string = str(i)
        arr = list(string)
        cnt = len(arr)

        if cnt % 2 == 0 :
            ans +=1

    print(ans)
    return ans

result = findNumbers(nums)
