#1436. Destination City

paths = [["qMTSlfgZlC","ePvzZaqLXj"],["xKhZXfuBeC","TtnllZpKKg"],["ePvzZaqLXj","sxrvXFcqgG"],["sxrvXFcqgG","xKhZXfuBeC"],["TtnllZpKKg","OAxMijOZgW"]]

# making 2 one dimensional arrays from a two-dimensional array
c0 = [i[0] for i in paths] #keeping the first value of each set in array c0, using  inline loop (list comprehension)
c1 = [i[1] for i in paths]

for element in c1: # accessing each element of array c1
    if element not in c0:
        print(element)
