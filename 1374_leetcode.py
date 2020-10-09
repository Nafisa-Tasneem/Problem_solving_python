#1374. Generate a String With Characters That Have Odd Counts

n = 3

s = ''

for i in range(n):
    if n% 2 == 1:
        s += 'a'
    else:
        if i == 0:
            s += 'a'
        else:
            s +='b'
print(s)
