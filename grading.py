def gradingStudents(grades):
    results = []
    for i in range (grades_count):
        grd = grades[i]
        # print('the grade is :', grades[i])
        if grd >= 38 :
            if grd % 5 != 0:
                mod = grd % 5
                if mod == 3 :
                    grd = grd + 2
                elif mod == 4:
                    grd = grd + 1
                else:
                    grd = grd
        print(grd)
        results.append(grd)
    print(results)
    return results
            # results.append(grd)





grades_count = int(input().strip())

grades = []
for _ in range(grades_count):
    grades_item = int(input().strip())
    grades.append(grades_item)

result = gradingStudents(grades)