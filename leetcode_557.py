s = "xyz"
s2= s.split(' ')
reverse_s2= ''
for i in s2:
    for j in reversed(range(len(i))):
        reverse_s2 += i[j]
    reverse_s2 += ' '

print(reverse_s2.rstrip())



