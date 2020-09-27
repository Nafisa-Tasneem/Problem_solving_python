
num = 9669

numarr = list(str(num))
# print(numarr)
result =''

for i in range(len(numarr)):
    print(i)
    if numarr[i] == '6':
        numarr[i] = '9'
        # print(numarr)
        # result.append(str(numarr))
        break

print(int(result.join(numarr)))


