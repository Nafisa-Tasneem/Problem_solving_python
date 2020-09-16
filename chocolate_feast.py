t = int(input())

def chocolateFeast(n, c, m):

    wrapper = (n // c)
    choco_no = (n // c)

    while wrapper >= m: # calculating wrapper for each test case
        choco_no = choco_no + (wrapper // m)
        wrapper = (wrapper // m) + (wrapper % m)

    # print(choco_no, wrapper)
    return choco_no

for t_itr in range(t):
    ncm = input().split()

    n = int(ncm[0])

    c = int(ncm[1])

    m = int(ncm[2])

    result = chocolateFeast(n, c, m)