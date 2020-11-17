S = "I speak Goat Latin"

ans = ''
ans_string = []
vowels = ['a','e','i','o','u','A','E','I','O','U']
S_split = S.split()
index = 1

for word in S_split :

    if word[0] in vowels:
        word += 'ma'

    else:
        first_letter = word[0]
        word = word[1:] + first_letter + 'ma'
    word += ('a'*index)
    ans_string.append(word)
    index +=1

print(' '.join(ans_string))
