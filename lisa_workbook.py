def workbook(n, k, arr):
    chapter = 0
    problem = 1
    page = 1
    ans = 0

    while True :
        problem_pg = 0
        while problem_pg < k:
            if problem == page:
                ans +=1
            problem +=1
            if problem > arr[chapter]:
                chapter +=1
                problem = 1
                break
            problem_pg +=1
        if chapter == n:
            break
        page +=1

    print(ans)
    return ans


nk = input().split()

n = int(nk[0]) #number of chapters

k = int(nk[1]) #problems per page

arr = list(map(int, input().rstrip().split())) #problem per chapter

result = workbook(n, k, arr)