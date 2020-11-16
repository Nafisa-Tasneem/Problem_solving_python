A = [1,3,6]
K = 3

ans = 0

if len(A) > 1 :
    maxi = max(A)
    mini = min(A)
    ans = maxi - mini - 2*K
    if ans < 0:
        ans = 0
print(ans)