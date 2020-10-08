s = "aaaabbbbcccc"

char_freq = {} #using dictionary
result = []

for element in s:
    if element in char_freq:
        char_freq[element] +=1
    else:
        char_freq[element] =1

print(char_freq )


smallest = True
while char_freq:
    keys = [key for key in char_freq]
    keys = sorted(keys) if smallest else sorted(keys, reverse=True)
    smallest = not smallest

    for i in keys:
        result.append(i)
        if char_freq[i] == 1:
            del char_freq[i]
        else:
            char_freq[i] -=1
print(''.join(result))


