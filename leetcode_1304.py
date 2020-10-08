n = 5

summation = 0

result = []
if n % 2 == 1:
    result.append(0)
positive = 1
negative = -1
while len(result) < n:
    if positive + negative == 0:
        result.append(negative)
        result.append(positive)
    positive +=1
    negative -=1
print(result)




