thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
print(thisdict)

aboutnafisa ={
    "name" : "Nafisa",
    "age" : 23,
    "district" : "Dhaka"
}
print(aboutnafisa["age"],thisdict["model"],aboutnafisa.get("name"))
aboutnafisa["district"] = "Khulna"
print(aboutnafisa)

for x in aboutnafisa:
    print(x)
for x in thisdict:
    print(thisdict[x])
for x in thisdict.values():
    print(x)
for x,y in thisdict.items():
    print(x)
if "name" in aboutnafisa:
    print("yes")
print(len(aboutnafisa))
# adding new item in dictionary

aboutnafisa["University"] = "KUET"
print(aboutnafisa)
aboutnafisa.pop("district")
print(aboutnafisa)
aboutnafisa.popitem()
print(aboutnafisa)
# del aboutnafisa
# print(aboutnafisa)
# aboutnafisa.clear()
print(aboutnafisa)
dict2 = aboutnafisa.copy()
print(dict2)
dict3 = dict(thisdict)
print(dict3)