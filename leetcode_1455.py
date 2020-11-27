sentence = 'i love loving lovq'
searchWord = 'love'
sentence_split = sentence.split(' ')
# print(sentence_split)
index = 1
isTrue = 0

for word in sentence_split:

    if len(word) < len(searchWord):
        index += 1
    else:
        for i in range(0, len(searchWord)):
            if word[i] != searchWord[i]:
                index += 1
                break
            else:
                equal = 1

                if word[i] == searchWord[i]:
                    isTrue = 1

    if isTrue == 1:
        break
    # print(index, word)

if isTrue == 0:
    index = -1
print(index)