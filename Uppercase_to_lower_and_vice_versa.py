# code for turning uppercase to lower and lowercase to upper

string = input('Enter the string : ')
newstring = ''
for i in string:
    if i.islower()== True:
        newstring += i.upper()
    elif i.isupper() == True:
        newstring += i.lower()
    elif i.isspace() == True:
        newstring += i
    else:
        newstring += i

print('The output string is : ', newstring)

