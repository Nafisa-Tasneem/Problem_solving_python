cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
dictionary = {}
for i in cpdomains:
    cnt, domains = i.split(' ')
    # print(number)

    # print(domains)
    x = domains.split('.')
    current = ""
    for j in reversed(x):
        if (len(current)== 0):
            current = j
        else:
            current = j + '.'+ current
        if current in dictionary:
            dictionary[current] += int(cnt)
        else:
            dictionary[current] = int(cnt)
# print(dictionary)
result = []
for i,j in dictionary.items():
    result.append(str(j)+ ' ' + i)
print(result)




