def workbook(n, k, arr):
    cnt = 0
    page = 0

    for i in range(n): # loop for number of chapter
        no_of_problem = arr[i]
        while (no_of_problem >0):
            page = page + no_of_problem//k + no_of_problem % k
            no_of_problem = arr[i] - k
            if page <= arr[i]:
                cnt +=1
                break

    print(cnt)
    return(cnt)

nk = input().split()

n = int(nk[0]) #number of chapters

k = int(nk[1]) #problems per page

arr = list(map(int, input().rstrip().split())) #problem per chapter

result = workbook(n, k, arr)