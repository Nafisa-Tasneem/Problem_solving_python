n = 25
dictionary = {0 : 0}
counts = [0] * (36) # largest numbr is 9999, sum of which is 36
# print(counts)
for i in range(1,n+1):
    quotient, remainder = divmod(i,10) #dividing each number by 10
    dictionary[i] = remainder + dictionary[quotient]

    counts[dictionary[i]-1] += 1
print(dictionary)
print(counts)
max_count =  max(counts)

result = counts.count(max_count) # calculating max_count kotobar ache

print(result)