from collections import Counter
A = ["bella","label","roller"]

c = A[0]
for i in range(1,len(A)):
    c = list((Counter(c) & Counter(A[i])).elements())
print(c)


