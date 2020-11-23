day = 15
month = 8
year = 1993

day_of_year = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

if month == 1 or month == 2 :
    month +=10
    year = year -1
else:
    month = month - 2

year_st = str(year)
C = year_st[0:2]
D = year_st[2:]
# print(C, D, month)
f = day + ((13* month -1)//5) + int(D) + (int(D)//4) + (int(C)//4) - 2* int(C)
# print(f, (13* month -1)//5)
result = int(f % 7)
print(day_of_year[result])