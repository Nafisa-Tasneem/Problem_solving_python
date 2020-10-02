#804. Unique Morse Code Words
words =  ["gin", "zen", "gig", "msg"]
morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
# print(morse[2])
# arr = ''
arr2 = []
for word in words:
    arr = ''
    for i in word:
        diff = ord (i) - ord('a')
        arr += morse[diff]
    arr2.append(arr)

set1 = set(arr2)
print(len(set1))
