salary = [8000,9000,2000,3000,6000,1000]

sorted_salary = sorted(salary)
sum = 0
for i in range(1,len(sorted_salary)-1):
    sum += sorted_salary[i]

print(sum/(len(sorted_salary)-2))